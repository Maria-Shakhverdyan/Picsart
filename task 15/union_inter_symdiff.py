st1 = {13, 2, 4, 243, 101, 0}
st2 = {22, 65, 90, 101, 0}

miavorum = set()
hatum = set()
tarb = set()

#miavorum
for i in st1:
    miavorum.add(i)

for j in st2:
    miavorum.add(j)

#hatum
for i in st1:
    for j in st2:
        if i == j:
            hatum.add(i)

#simetrik tarberutyun
for i in st1:
    if i not in st2:
        tarb.add(i)

for i in st2:
    if i not in st1:
        tarb.add(i)

#print
print(miavorum)
print(hatum)
print(tarb)
