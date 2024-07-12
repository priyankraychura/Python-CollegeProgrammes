class noName(Exception):
    pass

try:
    name = input("Enter name: ")
    if(name == ""):
        raise noName
    else:
        print("Your name is: ",name)
except:
    print("Name field cannot be empty")