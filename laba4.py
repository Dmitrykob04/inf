
list = [2,4,5,6,7,8]
res = []
for i in range(len(list)):
  if i % 2 == 0:
    res.append(list[i])
print(res)



list = [2,-1,5,6,7,8]
res = []
for i in range(len(list)):
  if list[i-1]<list[i]:
    res.append(list[i])
print(res)


list = [2,-1,5,12,7,8]
i = list.index(max(list))
l = list.index(min(list))
list[l],list[i]=list[i],list[l]
print(list)


s = {1: 'sus', 2: 'susus', 3: 'amogus'}
k = int(input())
def sks(dictionary):
  sk = dictionary.get(k)
  print(sk)
sks(s)