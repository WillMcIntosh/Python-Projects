import datetime

filename = datetime.datetime.now()

#Creates an empty file
def create_file():
    """This function creates an empty file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("") #writing empty string

create_file()
