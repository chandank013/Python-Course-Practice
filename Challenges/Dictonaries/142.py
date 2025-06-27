# Find longest and smallest meaning in dictonary

dict3 = {
    'piece':'portion of an object or of material,oroduced by cutting',
    'patch':'a piece of a cloth or other material use to mend or strenghen a torn or a week point',
    'area':'a region or a part of a town,or a world',
    'visit':'go to see and spent some time with (someone)',
    'with':'having a possessing',
    'small':'less than normal'}

keys = list(dict3.keys())
values = list(dict3.values())
lens = [len(x) for x in values]

max_lens = max(lens)
min_lens = min(lens)

max_index = lens.index(max_lens)
min_index = lens.index(min_lens)
# print(min_index)

print('max',keys[max_index],values[max_index])

    