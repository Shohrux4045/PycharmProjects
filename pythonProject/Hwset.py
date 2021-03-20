 # Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
 # 75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету. Сколько семей живёт в доме N?


gazeta = set(range(1, 76))
jurnal = set(range(77, 104))
vmeste = (gazeta | jurnal)
gandj = set(range(1, 14))
s = vmeste-gandj
print(f'семей живёт в доме: {len( s)}')



# # Из 52 школьников 23 собирают значки, 35 - марки, 16 - и значки, и марки. Сколько школьников не увлекаются коллекционированием?
s = 52
zn = set(range(1,24))
m =  set(range(25,60))
znm = set(range(1,17))
sbr = len((zn|m)-znm)
nesbr = s-sbr
print(f'не увлекаются коллекционированием: {nesbr}')


garri = set(range(1,5))
larri = set (range(5,12))
gandl = (len(garri | larri))-1
a = gandl-len(garri)
b = gandl- len(larri)
print(a,b,sep="\n")