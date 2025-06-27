
from zipfile import *

f = ZipFile('image.zip', 'r')
f.extractall()
f.close()