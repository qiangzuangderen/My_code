#coding=UTF-8

brithdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}

while True:
    print('please enter a name:(blank to quite)')
    name = input()
    if name == '':
        break

    if name in brithdays:
        print(brithdays[name] + ' is the brithday of ' + name)
        
    else:
        print('I don\'t have the brithday information for' + name)
        print('what\'s their brithday?')
        bday = input()
        brithdays[name] = bday
        print('Brithdays database updated.')
        print(brithdays)
        break
        
