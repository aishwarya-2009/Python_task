source_file=input("Enter the source file name:")
destination_file=input("Enter the detination file name:")
with open(source_file,"r")as src:
    with open(destination_file,"w")as dest:
        content=src.read()
        dest.write(content)
