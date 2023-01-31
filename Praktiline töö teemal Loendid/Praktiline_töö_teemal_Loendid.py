#31.1.23
while True:
    try:
        index=int(input("Anna index: "))
        if index<999999 and index>10000:
            break
    except:
        print("Anna õige index!")

#4
def sort_list(lst, order):
    return sorted(lst, key=lambda x: abs(x), reverse=order)

lst = [int(x) for x in input("Sisestage tühikutega eraldatud numbrite loend: ").split()]
order = input("Kas sortida kasvavas või kahanevas järjekorras (kasvav/kahanev)? ") == 'desc'

print("Sorteeritud loend:", sort_list(lst, order))

#2
n = int(input("Sisestage vahetatavate elementide arv: "))
lst = [int(i) for i in input("Sisestage tühikuga eraldatud elementide loend: ").split()]

for i in range(n // 2):
    lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]

print("Uus nimekiri:", lst)



#1.
index=""
maakond=["Tln","Narva", "K-Järve","Ida-Virumaa","Tartu","Viljandi", "Pärnumaa", "Saarama"]
while True:
     try:
         index=int(intput("Anna index:"))
         break
     except:
         print("Anna õige index!")
i=index//10000
print(F"{index} on {maakonnad[i-1]}")
if i in [1 2,3]:
     print()
else:
     print()


#1
maakonnad=["Tln","Narva", "K-Järve","Ida-Virumaa","Tartu","Viljandi", "Pärnumaa", "Saarama"]
osa1=[]
osa2=[]
print(maakonnad)
if len(maakonnad)%2==00 and len (maakonnad)>=2:
    n=len(len(maakonnad))
    for i in range(1,n+1):
        osa1.append(maakonnad[i-1])
    for j in range(n+1, len(maakonnad)+1):
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:   
    print("väga")
 
#3
arvus=[]
kogus=int(input("kogus:"))
for i in range(kogus):
    arvus.append(randint(-100,100))
print(arvus)
max_arv=max(arvus)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=max_arv/kogus
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvus)

















































