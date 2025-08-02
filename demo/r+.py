# Open the file in read and write mode
with open("demo.txt", "r+") as f:
    print(f.read())
    f.seek(0)  # Reset file pointer to the beginning
    f.write("kiet women's") # Read again to show the content is still there