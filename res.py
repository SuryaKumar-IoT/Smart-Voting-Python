import xlrd
import time
# Give the location of the file 
loc = ("result.xlsx") 
# To open Workbook
def readres():
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)  
    ysrcp=sheet.cell_value(1, 0)
    tdp=sheet.cell_value(1, 1)
    jsp=sheet.cell_value(1, 2)
    bjp=sheet.cell_value(1, 3)
    return(ysrcp,tdp,jsp,bjp)

