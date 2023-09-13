
"""
a part of code from ved(Virtual Excel-based Database
may helpful in future
"""
class Row:
    def __init__(self,
                 value:list,
                 is_header:bool = False,
                 data_type: str = "str",
                 header_mapping:dict=None
                 ):
        self.values = value
        self.__type = data_type
        self.__is_header = is_header  # header or data
        if is_header:
            self.__header_mapping = self.__set_field_map(header_mapping)
    def __set_field_map(self,mapping:dict):
        idx = 0
        mapping_values = [item for item in mapping.values()]
        mapping_keys = [item for item in mapping.keys()]
        ret = self.__t_check_list_duplication(mapping_values)
        if ret:
            raise Exception(f'mapped field {ret} has duplicated, construct failed')
        mapping_count = len(mapping.items())
        alias_idx = {}
        if self.__is_header:
            for val in self.values:
                try:
                    alias = mapping[val]
                    alias_idx.update({alias: idx})
                    mapping_keys.remove(val)
                    idx += 1
                    mapping_count -= 1
                except KeyError as e:
                    raise KeyError(f'Build mapping failed, key {e} do not have a valid map, build process terminated')
        else:
            raise TypeError(f'This row is not head row.')
        if mapping_count != 0:
            not_found_dict = {}
            for key in mapping_keys:
                not_found_dict.update({key:mapping[key]})
            print("Warning:no corresponding mapping has been found for the following elements:",not_found_dict)
        print("header build complete")
        return alias_idx
    def get_alias_idx(self,alias):
        val = self.__header_mapping[alias]
        return val
    def __t_check_list_duplication(self,target_list:list):
        tool_dict = {}
        idx = 0
        duplications = []
        for item in target_list:
            try:
                idx = tool_dict[item]
                duplications.append(item)
            except KeyError:
                tool_dict.update({item: idx})
                idx += 1
        if len(duplications) == 0:
            return None
        return duplications
    def __getitem__(self, item):
        return self.values[item]

class Table:
    def __init__(self,name):
        self.table_name = name
        self.__row_list=[]
        self.__count = 0
    def push(self,row:Row):
        self.__count += 1
        self.__row_list.append(row)
    def __getitem__(self, item):
        return self.__row_list[item]
    def get_max_row(self):
        return self.__count
