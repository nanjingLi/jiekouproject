import openpyxl
# class CaseData(object):
#     def __init__(self,zip_obj):
#         for i in zip_obj:
#             setattr(self,i[0],i[1])

class CaseData(object):
    def __init__(self,*args,**kwargs):
        for i in args:
            setattr(self, i[0], i[1])
class readExcel(object):
    def  __init__(self,workbook_name,sheet_name):
        self.workbook_name=workbook_name
        self.sheet_name=sheet_name
        super().__init__()
    def open(self):
        """
        打开工作铺
        :return:
        """
        #打开工作铺
        self.wb=openpyxl.load_workbook(self.workbook_name)
        #打开表单
        self.sh=self.wb[self.sheet_name]
    def read_data(self):
        """
        读取excel表格数据
        :return:
        """
        self.open()
        #一整行的读取表格数据，存为对象，
        # 在通过list转换为列表[【‘1’，‘（python21,1234567,1234567）,{"code":1,"msg":"注册成功"}】,[],......]
        rows=list(self.sh.rows)
        cases=[]
        #遍历表格第一行
        titles=[row.value for row in rows[0]]
        #遍历表格第二行到结束,遍历出来的还是列表组合，所以还得继续遍历列表内容
        for row in rows[1:]:
            datas=[r.value for r in row]
            case=dict(zip(titles,datas))
            cases.append(case)
        return  cases
    def read_data_obj(self):
        """
        读取excel表格数据
        :return:
        """
        self.open()
        # 一整行的读取表格数据，存为对象，
        # 在通过list转换为列表[【‘1’，‘（python21,1234567,1234567）,{"code":1,"msg":"注册成功"}】,[],......]
        rows = list(self.sh.rows)
        cases = []
        # 遍历表格第一行
        titles = [row.value for row in rows[0]]
        # 遍历表格第二行到结束,遍历出来的还是列表组合，所以还得继续遍历列表内容
        for row in rows[1:]:
            datas = [r.value for r in row]
            zip_obj= zip(titles, datas)
            case_data=CaseData(*zip_obj)
            cases.append(case_data)
        return cases
    def write(self,row,column,value):
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.workbook_name)


if __name__=='__main__':
    cases=readExcel('cases.xlsx','Sheet1').read_data()
    print(cases)
    cases2 = readExcel('cases.xlsx', 'Sheet1').read_data_obj()
    print(cases2)


