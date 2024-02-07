#15971실패
#두로봇
#n개 방이 n-1개 통로로 연결되어 있따.
#두방 사이 이동 가능하며 같은 통로를 한번만 지나감
#로봇두대를 통신하려면 같은 통로에 있어야한다.
#통로 숫자는 길이
#ex)n=1,9이면 2,5로 이동해 통신가능=>14
#통신을 하기 위한 최소거리

#이동하는 거리 함수
#에서 가장 긴통로를 뺀게 현재루트의 최소값
#DFS#
# n번째의 1번째 수를 찾아 DFS함수를 VisitB함수가 1일 떄까지 반복

def DFS(N):
  print(N, end = " ")
  for i in data[N]:
    if visited[i]==0 and k2 in data[i]:
      visited[i]=1
     
      DFS(i)

    
n,k1,k2=map(int,input().split())
#통로 양끝의 방번호, 통로 길이 받기
# 양방향 통로라서 a,b의 경우 두번다 넣어주기
data=[[] for i in range(n+1)]
list=[]*(n+1)
for _ in range(n-1):
  a,b,l=map(int,input().split())
  data[a].append(b)
  data[b].append(a)
  list.append(l)
  data[a].sort()
  data[b].sort()
visited= [0] * (n+1)
visited[k1]=1
DFS(k1)

