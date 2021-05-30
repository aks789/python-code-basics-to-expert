import os
import shutil



f = open('practice.txt','w+')
f.write('this is a test string')
f.close()

print(os.getcwd())
print(os.listdir())
print(os.listdir('E:\\'))

#shutil.move('practice.txt','E:\\python')

#os.unlink()
#os.rmdir()

# Cannot be recovered
#shutil.rmtree()

for folder,sub_folder,files in os.walk('E:\\python\\Complete-Python-3-Bootcamp-master\\Complete-Python-3-Bootcamp-master\\13-Advanced Python Modules'):
    print(f"Currently looking at folder {folder}")
    print('\n')
    print('The sub folders are')
    for sub_fold in sub_folder:
        print(f"\t Currently looking at sub folder {sub_fold}")
    print('\n')
    print('The files are: ')
    for file in files:
        print(f"\tCurrently looking at file {file}")


