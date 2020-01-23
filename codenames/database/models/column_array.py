from collections.abc import MutableSequence


class ColumnArrayProxy(MutableSequence):
    def __init__(self, master: "ColumnArray", obj) -> None:
        self.master = master
        self.obj = obj

    def __len__(self) -> int:
        return getattr(self.obj, self.master.len_column_name) or 0

    def _set_length(self, new_length: int) -> None:
        setattr(self.obj, self.master.len_column_name, new_length)

    def _check_and_shift_index(self, index: int) -> int:
        length = len(self)

        if index < 0:
            index = index + length

        if index not in range(length):
            raise IndexError

        return index

    def clear(self) -> None:
        self._set_length(0)

    def __getitem__(self, index: int):
        index = self._check_and_shift_index(index)
        return getattr(self.obj, self.master.elem_column_template.format(index))

    def __setitem__(self, index: int, value) -> None:
        index = self._check_and_shift_index(index)
        setattr(self.obj, self.master.elem_column_template.format(index), value)

    def __delitem__(self, index: int) -> None:
        index = self._check_and_shift_index(index)
        new_length = len(self) - 1

        for i in range(index, new_length):
            self[i] = self[i + 1]

        self._set_length(new_length)

    def insert(self, index: int, value) -> None:
        old_length = len(self)
        if index != old_length:
            index = self._check_and_shift_index(index)

        new_length = old_length + 1
        if new_length > self.master.max_length:
            raise IndexError

        self._set_length(new_length)

        for i in range(new_length - 1, index, -1):
            self[i] = self[i - 1]

        self[index] = value


class ColumnArray:
    def __init__(self, prefix: str, max_length: int, column_type) -> None:
        digit_count = 1
        while (10 ** digit_count) < max_length:
            digit_count += 1

        self.elem_column_template = prefix + f"_{{:0{digit_count}}}"
        self.len_column_name = prefix + "_len"
        self.max_length = max_length
        self.column_type = column_type

    def __get__(self, obj, objtype=None) -> ColumnArrayProxy:
        if obj is not None:
            return ColumnArrayProxy(self, obj)

        return self
