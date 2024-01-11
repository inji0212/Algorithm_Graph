# x,y사이즈 만큼 빈 그래프만들고 
# 입력받은 좌표로 배추 1로 만들어줌 (갯수만큼 반복)

# 영역문제라서 

# visited배열 만들어서 1이면 true로 변경 
# 반복해서 값이 1(배추 있다)이고 인접하며
# visited이 false이면
# 카운트 없이 visited만 true로 변경 

# queue배열에 해당 좌표 넣어서 while()
# visited배열이 false일 때만 if문 실행되어
# 인접한 부분들이 전부 visit되면 def함수 끝

# 함수는 visit하지 않았고 1일떄(배추 있을떄)실행
#위를 케이스만큼 반복

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] ==1:
        visited[nx][ny] = True
        queue.append((nx, ny))

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
      a,b=map(int,input().split())
      graph[b][a]=1
        #좌표에 배추 1 심기

    visited = [[False for _ in range(m)] for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] ==1 and not visited[i][j]:
        #배추가 심어져 있고 방문하지 않은 좌표면 
                #bfs함수 실행
                bfs(i, j)
                count += 1

    print(count)