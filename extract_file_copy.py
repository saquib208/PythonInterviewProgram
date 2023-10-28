import os
import shutil


def find_files(path):
    d=[]
    directory1="E:\Testing\Text"
    directory2 = "E:\Testing\zar"

    for folder, subfolders, files in os.walk(path):
        for file in files:
            #size = os.stat(os.path.join(folder, file)).st_size
            #print("File {}-->subfolder--> {} folders -->{}".format(os.path.join(folder, file),subfolders,folder))
            key = os.path.join(folder, file)
            value = file.split(".")[-1]
            d.append((key, file, value))


    return d



def create_folders(path,p1):
    #print(find_files(path))
    d=find_files(path)
    print(d)
    for path, file, ext in d:
        dir1 = '{}\{}'.format(p1,ext)
        print(dir1)
        try:
            os.makedirs(dir1, exist_ok=True)
            dir=os.listdir(p1)
        except Exception as e:
            print(e)
            continue
        for i in dir:
            if ext == i:
                #os.path.join(src, filename), os.path.join(dst, filename)
                try :
                    shutil.copy(path,dir1)
                except Exception as e:
                    print(e)
    return ("File Copied Succesfully")

def copy_files(path,p1):
    create_folders(path)
    print(os.listdir(p1))




path=r'C:\Users\SAQUIB\Downloads'
p1=r'C:\Users\SAQUIB\Downloads'
#path="E:\Testing\Files"
#p1="E:\Testing"
#print(find_files(path))

#print(copy_files(path,p1))
print(create_folders(path,p1))