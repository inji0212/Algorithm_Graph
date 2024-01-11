"""
DFS(Depth-First Search)
"""

def my_dfs(graph,list, start_node):
    visited = [] # 방문한 노드를 담을 배열
    stack = [] # 정점과 인접한 방문 예정인 노드를 담을 배열

    stack.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.

  
    while list: # 더 이상 방문할 노드가 없을 때까지.
        node = stack.pop() # 방문할 노드를 앞에서 부터 하나싹 꺼내기.

        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node) # visited 배열에 추가
            # stack.extend(graph[node]) # 해당 노드의 자식 노드로 추가
            for i in range(0,len(list)):
              if list[i]==node:
                if i< m:
                  node=list[i][0] # visited 배열에 추가
                  
                  break


    print("dfs - ", visited)
    return visited

# 함수 실행

n, m,start_node = map(int, input().split()) 
Graph = []
List=[]
for _ in range(m): # 리스트A 선언
    Graph.append(list(map(int, list(input().split()))))
Graph.sort(key=lambda x:x[1])
for i in range(0,m):
  List[i]=Graph[i][0]
for i in range(0,m):
  List[i+m]=Graph[i][1]
my_dfs(List, start_node)