# Create a dictonary for country names in alphabetically order

cuntries = {
    'A':['America','Alaska','Argentina'],
    'B':['Bhutan','Brazil','Bahrain'],
    'C':['Chaina','Chandan','Cuba']
}


Countries = {}
for i in range(4):
     name = input("Enter the Name of Country:")
     if name[0].upper() not in Countries:
         Countries[name[0].upper()] = [name]
     else:
          Countries[name[0].upper()].append(name)

print(Countries)
          
        
        
          


