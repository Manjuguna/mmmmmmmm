g1,v1=map(str,input().split())
yast=0
if len(g1)>len(v1):
  g1,v1=v1,g1
p2=0
while p2<len(g1):
  yast+=(ord(v1[p2])-ord(g1[p2]))
  pt1+=1
for pt1 in range(p2,len(v1)):
  yast+=ord(v1[p2])-ord('a')+1
print(yast)
