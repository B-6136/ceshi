import xlrd
import pymysql
conn = pymysql.connect(host='localhost', user="root", password='root', database='everymonthdata', charset='utf8')
cursor = conn.cursor()

file = xlrd.open_workbook("E:\python1\day7\每月销售情况.xlsx")
sheet = file.sheet_by_index(0)
row_number = sheet.nrows

for i in range(1,row_number):
    row_content = sheet.row_values(i)
    sql1="insert into clothesdata values(%s,%s,%s,%s,%s)"
    list = []
    for j in row_content:
        list.append(j)
    cursor.execute(sql1,list)
    conn.commit()

cursor.close()
conn.close()



