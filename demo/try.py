try:
    f=open("file.txt","r")
    try:
        f.write("Hello, World!")
    finally:
        f.close()
        print("File closed successfully.")
except:
    print("error")
