'''l=[]
for i in range(10):
    x=int(input('Vnesete broj\n'))
    l.append(x)
suma=(sum(l))
print('Sumata na vnesenite broevi e', suma)'''

'''l=[]
while True:
    p=input('Dali sakate da vnesete broj?da/ne\n')
    if p=='da':
        x=int(input('Vnesete broj\n'))
        l.append(x)
    else:
        break
l.sort()
golem=(l[-1])
print('Od broevite sto gi vnesovte najgolem e brojot', golem)'''

'''l=[]
while True:
    p=input('Dali sakate da vnesete broj? da/ne\n')
    if p=='da':
        x=int(input('Vnesete broj\n'))
        l.append(x)
    else:
        break
print(l)
r=int(input('Koj broj sakate da go izbrisete\n'))
l.remove(r)
print(l)'''

'''l=[]
b=[]
while True:
    i=input('Vnesete ime\n')
    k=len(i)
    b.append(k)
    print('Imeto sto go vnesovte ima', k, 'karakteri')
    p=input('Dali sakate da prodolzite? da/ne\n')
    l.append(i)
    if p=='da':
        pass
    else:
        break
print(l)
b.sort()
golem=b[-1]
print('Najdolgoto ime sto go vnesovte ima ', golem, 'karakteri')'''

'''l=[]
while True:
    p=input('Dali sakate da vnesete broj?da/ne\n')
    if p=='da':
        x=int(input('Vnesete broj\n'))
        l.append(x)
    else:
        break
l.sort()
golem=(l[-2])
print('Od broevite sto gi vnesovte vtor najgolem e brojot', golem)'''

'''p=[]
c=[]
zbir_y=0
while True:
    x=input('Vnesete go produktot\n')
    y=int(input('Vnesete ja cenata na produktot\n'))
    zbir_y+=y
    p.append(x)
    c.append(y)
    h=input('Dali sakate da platite? da/ne\n')
    if h=="ne":
        pass
    else:
        break
z=list(zip(p,c))
print(z)
print('Vkunpo za naplata imate', zbir_y, 'denari')
pari=int(input('Kolku pari ke dadete?\n'))
final=pari-zbir_y
print('Treba da vratite', final, 'denari')'''

