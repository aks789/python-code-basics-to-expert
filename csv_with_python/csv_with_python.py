import csv
import PyPDF2
import re

# open the file
data = open('E:\\python\\python_bootcamp\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\example.csv',encoding='utf-8')

# call csv.reader on it
csv_data = csv.reader(data)

# reformat into a python object list of lists

dat_lines = list(csv_data)

print(dat_lines)

for line in dat_lines[:5]:
    print(line[2])

full_names = []
for line in dat_lines[1:]:
    full_names.append(line[1] + ' ' + line[2])

file_to_output = open('to_save_names.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()

################ CSV/DDF Puzzle

f = open('E:\\python\\python_bootcamp\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\Exercise_Files\\find_the_link.csv',encoding='utf-8')

csv_data = csv.reader(f)

data_lines = list(csv_data)

print(data_lines)

print(data_lines[0])

file_size = len(data_lines)
s = ''
for n in range(file_size):
    s +=str(data_lines[n][n])
print(s)

link = ''
for row_num,data in enumerate(data_lines):
    link +=data[row_num]
print(link)


file = open('E:\\python\\python_bootcamp\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\Exercise_Files\\Find_the_Phone_Number.pdf','rb')

pdf_file_object = PyPDF2.PdfFileReader(file)

print(pdf_file_object.numPages)

pattern = r'\d{3}'

all_text=''
for num in range(pdf_file_object.numPages):
    file_page = pdf_file_object.getPage(num)
    file_page_text = file_page.extractText()
    all_text = all_text + ' ' + file_page_text

for match in re.finditer(pattern,all_text):
    print(match)

print(all_text[41808:41808+12])