with open("demo.txt", "w+") as f:
    f.write("content")
    f.seek(0)  # Reset file pointer to the beginning
    print(f.read())