import openpyxl
from openpyxl import workbook
import docx
from docx import Document
from docx2pdf import convert
import os

doc = docx.Document(r'C:\Users\konhotom\Desktop\convoc.docx')
wb = openpyxl.load_workbook(r"C:\Users\konhotom\Desktop\convoc.xlsx")
pg1 = wb['pg1']
pg1 =wb.active

date = pg1['A1'].value
#"print(date)

'''
for r in doc.paragraphs:
    if 'DATE' in r.text:
        inline = r.runs

        for i in range(len(inline)):
            if 'DATE' in inline[i].text:
                text = inline[i].text.replace('DATE', date)
                inline[i].text = text
        print (r.text)
'''

row = pg1.max_row
column = pg1.max_column

for z in range(10):
    for i in range(2, 3):
        for j in range(1,column+1):
            print(pg1.cell(i,j).value)
            salle = pg1.cell(i,j).value
            for t in doc.paragraphs:
                if 'SALLE' in t.text:
                    inline = t.runs

                    for x in range(len(inline)):
                        if 'SALLE' in inline[x].text:
                            text = inline[x].text.replace('SALLE',salle )
                            inline[x].text = text
                    print (t.text)
                doc.save(f'Desktop\\test\\convoc_{z}.docx')




#convert(r"C:\Users\konhotom\Desktop\convoc.docx", r"C:\Users\konhotom\Desktop\convoc.pdf")