# -*- coding:utf-8 -*-
import xlwt

STYLE_TITLE = xlwt.easyxf("font: bold on; align: horiz center")
TITLES = [u'序号', u'域名', u'流量']
COL_WIDTHS = [2000, 6400, 3000] # 列宽度，单位不明。。。

def generate_excel():
    print 'start'
    book = xlwt.Workbook(encoding='utf8')
    sheet = book.add_sheet('First Sheet', cell_overwrite_ok=True)
    fill_excel_title(sheet)
    fill_excel_content(sheet)
    book.save('/temp/test.xls')
    print 'done'

def fill_excel_title(sheet):
    """为Excel填充标题行
    """
    for i in range(len(TITLES)):
        sheet.write(0, i, TITLES[i], STYLE_TITLE)
        sheet.col(i).width = COL_WIDTHS[i]

def fill_excel_content(sheet):
    """为Excel填充内容
    """
    items = [
        {
            'domain': 'abc.com',
            'flux': 123
        },
        {
            'domain': 'def.com',
            'flux': 456
        },
        {
            'domain': 'xyz.com',
            'flux': 789
        }
    ]
    
    for i in range(len(items)):
        item = items[i]
        values = [
            i+1, 
            item['domain'], 
            item['flux']
        ]
        for j in range(len(values)):
            sheet.write(i+1, j, values[j])

if __name__ == '__main__':
    generate_excel()