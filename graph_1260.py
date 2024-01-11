#DFS#
# n번째의 1번째 수를 찾아 DFS함수를 VisitB함수가 1일 떄까지 반복

def DFS(N):
  print(N, end = " ")
  for i in Graph[N]:
    if VisitD[i]==0:
      VisitD[i]=1
      DFS(i)
  
#BFS#
# start번쨰의 배열을 전부 나열 후 그다음...
# list에 현재 노드를 pop, 현재 숫자를 visit에 넣고 print,숫자들은 다시 list in
# visit한 숫자면 pop만 되어서 모든 숫자가 visit하면 list에 숫자가 없어서 끝남


def BFS(N):
  VisitB = [0] * (n+1)
  VisitB[N]=1

  list=[]
  list.append(N)
  print(N, end = " ")

  while list:
    
    chk=list.pop(0)
    for i in Graph[chk]:
      if VisitB[i]==0:
        VisitB[i]=1
        list.append(i)
        print(i, end = " ")




  
n, m, Start = map(int, input().split())

# Graph배열을 먼저 0~n까지의 빈 자리를 만들어주고  (n은 정점의 갯수라서)
# 간선은 양방향이기에 a,b 모두 Graph 배열에 넣고  순서대로 정리(앞순서부터 나가야해서)

Graph= [[] for i in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  Graph[a].append(b)
  Graph[b].append(a)
  Graph[a].sort()
  Graph[b].sort()

VisitD = [0] * (n+1)
VisitD[Start]=1
DFS(Start)
print()
BFS(Start)

