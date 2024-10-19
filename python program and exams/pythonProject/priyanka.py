
file_path =open("D:\\aaa.txt")
try:
     with open("D:\\aaa.txt", 'r') as file:
         content = file.read()
         print(content)
except FileNotFoundError:
    print("the file was not found", file_path ,"please check again")

