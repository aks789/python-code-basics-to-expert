import PyPDF2

f = open('E:\\python\\python_bootcamp\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\Working_Business_Proposal.pdf','rb')

pdf_reader_file = PyPDF2.PdfFileReader(f)

print(pdf_reader_file.numPages)


page_one = pdf_reader_file.getPage(0)

print(type(page_one))
pdf_file_pages = []

for num in range(pdf_reader_file.numPages):
    pdf_file_pages.append(pdf_reader_file.getPage(num))

print(len(pdf_file_pages))
pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(page_one)

pdf_output = open('Some_new_pdf_file','wb')

pdf_writer.write(pdf_output)

pdf_output.close()

page_one_text = page_one.extractText()

f.close()

print(page_one_text)