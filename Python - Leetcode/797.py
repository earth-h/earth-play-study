'''
797. All Paths From Source to Target
DAG(Directed Acyclic Graph)

n개의 노드가 0 ~ n-1 index를 가지고 있고, 0번 index에서 n-1 index에 도달할 수 있는 모든 경로 도출

2 <= n <= 15이기 때문에, bruce force로 구해도 된다.

path 자체에 append를 하게 되면, ansPath가 path 변경되면 모든 값이 변경된다.
따라서, path가 매번 새로운 메모리를 받도록 path + [nodexIdx]와 같은 형식으로 사용해야 한다.
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(nodeIdx: int, graph: List[List[int]], path: List[int], ansPath: List[List[int]]) -> List[List[int]]:
            if graph[nodeIdx] == [] and nodeIdx != len(graph) -1:
                return ansPath
            if nodeIdx == len(graph) - 1:
                ansPath.append(path + [nodeIdx])
            else:
                for i in range(len(graph[nodeIdx])):
                    dfs(graph[nodeIdx][i], graph, path + [nodeIdx], ansPath)
            return ansPath
        
        ansList= []
        ansList = dfs(0, graph, [], ansList)
            
        return ansList