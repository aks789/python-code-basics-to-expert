myfile = open('G:/2020/python/Complete-Python-3-Bootcamp-master/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt');

print(myfile.read());

myfile.seek(0);

print(myfile.read())

myfile.seek(0);

print(myfile.readlines())


with open('G:/2020/python/Complete-Python-3-Bootcamp-master/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test.txt') as my_file1:
    contents = my_file1.read();

with open('G:/2020/python/Complete-Python-3-Bootcamp-master/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test1.txt',mode='a') as my_file2:
    my_file2.write("Third Line!!");

with open('G:/2020/python/Complete-Python-3-Bootcamp-master/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test1.txt',mode='r') as my_file2:
    print(my_file2.read());

with open('G:/2020/python/Complete-Python-3-Bootcamp-master/Complete-Python-3-Bootcamp-master/00-Python Object and Data Structure Basics/test3.txt',mode='w') as my_file3:
    print(my_file3.write("First Line"));







