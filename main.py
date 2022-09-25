import sklearn.metrics as metrics
# try:
# 	print(10//0)
# except:
# 	print ("An exception")
# 	raise # To determine whether the exception was raised or not
# finally:
#   print("Finally")

# print("Out")

# C = 1000
# assert C < 1000, "Variable a smaller/different than variable b"

#I/O - input/output

# f = open("Testy.txt",'r')
# text = f.read()
# print(text)
# text1 = f.read()#what is the content of text1?
# print(text1)
# f.close()

# f = open("Testy.txt",'r')
# text = f.readline()
# print(text)
# text = f.readline()
# print(text)
# f.close()

# f = open("Testy.txt",'r')
# #f1 = open("Testy.txt",'w')#Error
# line = f.readline()

# while(line != ""):
#   print(line)
#   line = f.readline()

# f.close()

newF = open("NewFile.txt","w")
text = '''abra
cadabra, 
here's a magic trick
!'''
newF.write(text)
newF.close()

f = open("NewFile.txt",'r')
text = f.read()
print(text)
f.close()
###############################
newF = open("NewFile.txt","w")
text = '''dawnoidn'''
newF.write(text)
newF.close()

f = open("NewFile.txt",'r')
text = f.read()
print(text)
f.close()

#Task - read the Books file , create a new file - Catalogue.txt , Catalogue.txt should contain the Books file contents line by line(only one book title per line) in the format - first letter of title + title symbol count. EX: Harry Potter -> H12