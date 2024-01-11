n= int(input())
m=int( input() )
# Graph배열을 먼저 0~n까지의 빈 자리를 만들어주고  (n은 정점의 갯수라서)
# 간선은 양방향이기에 a,b 모두 Graph 배열에 넣고  순서대로 정리(앞순서부터 나가야해서)

Graph= [[] for i in range(m+1)]
for i in range(m):
  a, b = map(int, input().split())
  Graph[a].append(b)

VisitB = [0] * (n+1)
VisitB[1]=1

list=[]
list.append(1)
while list:

  chk=list.pop(0)
  for i in Graph[chk]:
    if VisitB[i]==0:
      VisitB[i]=1
      list.append(i)

print(list)


count=0
for i in (2,n+1):
  if VisitB[i]==1:
    count+=1
