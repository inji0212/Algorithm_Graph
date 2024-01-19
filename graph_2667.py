#단지이름붙이기


# 단지를 1번 찾아서+
# 계속 dfs 돌수있게

def dfs(x,y):
    # 단지찾기  
    
    global chk
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and visited[nx][ny]==0:
           chk+=1
           dfs(nx,ny)
    return chk
       


dx=[-1,1,0,0]
dy=[0,0,-1,1]    

n=int(input())

graph=[]
for _ in range(n):
  graph.append(list(map(int,input())))

count=[]
visited=[[0]*n for _ in range(n)]
# 1인곳을 dfs돌리면 한단지는 모두 방문
# 그다음 단지가 좌표로 들어간다.
# 체크 리스트 만들어서 단지사람 넣고 단지수는 길이
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            chk=1
            count.append(dfs(i,j))
            
            
            
print(len(count))
count.sort()
for i in count:
    print(i)