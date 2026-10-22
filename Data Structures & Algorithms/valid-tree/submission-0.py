class Solution:
    def validTree(self, num_nodes: int, edges: List[List[int]]) -> bool:
        if len(edges) > (num_nodes - 1):
            return False

        adjacency_list = [[] for _ in range(num_nodes)]
        for node_u, node_v in edges:
            adjacency_list[node_u].append(node_v)
            adjacency_list[node_v].append(node_u)

        visited = set()
        def dfs(current_node, parent):
            if current_node in visited:
                return False

            visited.add(current_node)
            for neighbor in adjacency_list[current_node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, current_node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == num_nodes