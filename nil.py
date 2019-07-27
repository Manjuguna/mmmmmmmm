g1,v1=map(str,input().split())
y=0
if len(g1)>len(v1):
  g1,v1=v1,g1
p2=0
while p2<len(g1):
  y+=(ord(v1[p2])-ord(g1[p2]))
  p2+=1
for p2 in range(p2,len(v1)):
  y+=ord(v1[p2])-ord('a')+1
print(y)
