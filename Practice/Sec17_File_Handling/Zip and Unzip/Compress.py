
from zipfile import *

f = ZipFile('image.zip', 'w',ZIP_DEFLATED)

f.write('C++.png')
f.write('Creative.jpg')
f.write('java.png')
f.write('jawascript.png')
f.write('Python.jpg')

f.close()

