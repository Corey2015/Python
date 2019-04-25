# -*- coding: utf-8 -*-
import openpyxl


#生成一个实例化的workbook对象 注意Workbook中首字母大写
wb = openpyxl.Workbook()
#获取当前工作表 sheet
ws = wb.active
#修改工作表的名称
ws.title = "tmp_sheet"
#向单个单元格传入数据
ws['A1'] = 'name'
ws['B1'] = 'age'
data = {
    '老王':50,
    '老李':21,
    '老张':32,
    }
data_excel = []
#将字典中的每对数据（键，值）以列表形式传入data_excel列表
#[['老李', 21], ['老王', 50], ['老张', 32]]
for each in data:
    data_excel.append([each, data[each]])

#将列表里的数据写入数据表中
for each in data_excel:
    ws.append(each)

#使用 Workbook.create_sheet() 创建新的worksheets
ws1=wb.create_sheet('Mysheetfirst',0)

ws1['A1'] = "test"
#保存文件
wb.save("./test.xlsx")

def main():
    pass


if __name__ == "__main__":
    main()