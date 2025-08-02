with open("demo.txt","a+") as f:
    f.write("append plus mode")
    f.seek(0)
    print(f.read())