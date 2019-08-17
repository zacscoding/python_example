import shutil
import os


def delete_file(name):
    if os.path.exists(name):
        os.remove(name)


src_name = 'shutil_example.txt'
delete_file(src_name)

data = 'new text'
f = open(src_name, 'w')
f.write(data)
f.close()

dest_name = 'shutil_example_copy.txt'
shutil.copy(src_name, dest_name)

f = open(dest_name, 'r')
read_data = f.read()
print(">> data == read_data : ", (data == read_data))
f.close()

delete_file(src_name)
delete_file(dest_name)
