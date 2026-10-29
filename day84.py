#SHUTIL MODULE IN PYTHON
import os
# print(os.getcwd())
os.chdir(r"C:\Users\dell\Desktop\cpp by code with harry\python by the code with harry")
import shutil
print(os.getcwd())
shutil.copy("methode_with_import.py","methode_with_import2.py")#copy the file not the folder
shutil.copy2()# it is same as the copy but additionaly provide the meta data of the old file like when the file is created and all that stuff
shutil.copytree("python by the code with harry","yash")# it is used to copy the folder along with all present directories
shutil.move("python by the code with harry/yash","yash")# python by the code with harry se yash folder as yash bahar kar do
#move is also use to rename alog with moving the file
shutil.move("d.cpp","ram.cpp")# also used to rename the file
shutil.rmtree("yash")# we can delate the folder but not the file by shutil 
os.remove("file naem") # os module can delate the file also
shutil.copy("day87.py","day871.py")

