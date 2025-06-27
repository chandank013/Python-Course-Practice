

f = open('Python1.jpg','rb')
data = f.read()

copy = open('Python2.jpg','wb')

copy.write(data)
f.close()
copy.close()