from openpyxl import Workbook,load_workbook
from client.StudentInfo import StudentSchema
from client.MoralScore import MoralRecordSchema
from client.InfoText import TextSchema
schemas = {
    "Student":StudentSchema,
    "Moral":MoralRecordSchema,
    "Text":TextSchema
}
class ExcelModel:
    def __init__(self,filename):
        # load excel workbook
        wb:Workbook = load_workbook(filename)
        # confirm a prime data sheet and a mapping sheet
        self.__obj_cls :object.__class__
        self.__mapping_sheet = None  # sheet with mapping
        self.__data_sheet = None
        self.__mapping = {}
        # by mark position
        mark_pos = 'A1'
        for i in wb.worksheets:
            mark_point:str = i[mark_pos].value
            if mark_point.startswith("#"):
                self.obj_cls:object.__class__ = schemas.get(mark_point[1:])
                self.__mapping_sheet = i
                break
        for i in self.__mapping_sheet.iter_rows():
            field_name = i[1].value
            class_attr = i[0].value
            self.__mapping.update({class_attr:field_name})
        # ------- Auto Load ----------
        for i in schemas.items():
            cls_obj:object.__class__ = i[1]
            for j in vars(cls_obj).get('__fields__').items():
                obj_attr = j[0]
                print(obj_attr)
            print("next obj")


        pass
    def set_mapping(self,map_dict):
        self.__mapping.update(map_dict)
    def load_excel(self,filename):
        pass
    def load_mapping(self,mapping_dict):
        pass
    def auto_load_schema(self):
        pass
    def export_standard_excel_by_schema(self,schema):
        pass
ExcelModel("text.xlsx")