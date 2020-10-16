class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


mapping_obj = Mapping([1, 2, 3])
print('mapping_obj.items_list:', mapping_obj.items_list)
mapping_obj.update([4, 5, 6])
print('mapping_obj.items_list:', mapping_obj.items_list)
print()

mappingSub_obj = MappingSubclass([1, 2, 3])
print('mappingSub_obj.items_list:', mappingSub_obj.items_list)

# execute update() from MappingSubclass
mappingSub_obj.update([4, 5, 6], [7, 8, 9])
print('mappingSub_obj.items_list:', mappingSub_obj.items_list)


# Note that the mangling rules are designed mostly to avoid accidents;
# it still is possible to access or modify a variable that is considered private.

# execute update() from Mapping for 'mappingSub_obj'
Mapping.update(mappingSub_obj, [10, 11, 12])
print('\nmappingSub_obj.items_list:', mappingSub_obj.items_list)

