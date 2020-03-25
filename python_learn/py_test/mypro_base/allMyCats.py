#coding=UTF-8

catNames = []
while True:
    print('Enter the name of cat' + str(len(catNames) + 1) + '(Or enter nothing to stop.):')
    name = input()
    if name == '':       
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in range(len(catNames)):
    #print(' ' + name)
    print('Index ' + str(name) + ' in catNames is:' + catNames[name])

print('please input a pet name:')
petName = input()
if petName not in catNames:
    print('I do not have the pet ' + petName)
else:
    print(petName + ' is my pet')
    catNames.append('picker')
    catNames.insert(5,'john')
    print(catNames)
