import shutil
import zipfile
import re
import os

f = open('fileone.txt','w+')
f.write('ONE FILE 123-456-7892')
f.close()

f = open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)

comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('extracted_content')

dir_to_zip = 'E:\\python\\UdemyCourse\\advanced_concepts\\extracted_content'
output_filename = 'example'

shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive('example.zip','final_unzip','zip')

with open('fileone.txt') as f:
    content = f.read()
    print(content)


def search(file,pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file,'r')
    text = f.read()

    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''

results = []
for folder,sub_folder,files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        full_path = folder + '\\' + f
        print('full path ' + full_path)
        results.append(search(full_path))

for res in results:
    if res != '':
        print(res.group())
