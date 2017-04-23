import os

file_list = os.listdir(r"C:\udacitya\python-course\prank")
print file_list
os.chdir(r"C:\udacitya\python-course\prank")
for file_cur in file_list:
    new_name = file_cur.translate(None, "0123456789")
    print new_name
    os.rename(file_cur, new_name)
