#r=read
# f=open("demo.txt","r")
# print(f.read())
# f.close()#error 



f=open("demo.txt","r")
with open("demo.txt","r") as f:
  print(f.read())




