contries = {'th':'Thailand' , 'jp':'Japan' , 'kr':'korea'}

for key in contries.keys():
    print(contries[key])


value = contries.values()
for v in value:
    print(v, ' ',end='')


    
print()
for (k , v) in contries.items():
    print(f'{k} : {v}')