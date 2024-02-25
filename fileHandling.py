#Reading files
#read mode
#ABsolute and relative path
#file.read read the entire file
#file.readline read the first line from a file
#readlines-
with open("test.txt",mode='r') as file:
    data = file.readlines()

for x in data:
    print(x)
#Creating new files
   #w = write mode 
    #a= append add more lines
    #Adding a squre brackets will write a list
try:
    with open("newfile.txt",mode='w') as file:
        file.writelines(["\nthis is a new file created","\nThis is another line"])
except Exception as e:
    print(e)
                
