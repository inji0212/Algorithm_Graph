#조합 함수
import copy

n,m = map(int,input().split())
nx=[-1,1,0,0]
ny=[0,0,-1,1]

graph=[]
for _ in range(n):
  graph.append(list(input().split()))

area=[]
virus=[]
for i in range(n):
  for j in range (m):
    if graph[i][j] == '0':
      area.append([i,j])
    elif graph[i][j]== '2':
      virus.append((i,j))

chk=[[0]*m for _ in range (n)] 
chk=copy.deepcopy(graph)

chk[0][0]=5
print  (graph)
#Combi_Wall=combinations(empty,3)

#test=[[]*m *n]
#chk=[[]*m *n]

#def func():
#  if len.area==3:
#    print(test)
#  else :
#    for i in range(n):
#      for j in range (m):
#        if 

