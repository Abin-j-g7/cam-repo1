file_path="C:/Users/abinj/OneDrive/Desktop/output.txt"

content=file_path.read()
print(content)
with open(file_path,"r") as file:
    content=file.read()
    print(content)
 
# with open(file_path,"w") as file:
#     file.write("hai boss")
    
