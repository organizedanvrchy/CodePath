# Clone Graph using DFS

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else[]
    
class Solution: 
    def graphCloner(self, node: 'Node') -> 'Node':
        # Check for empty graph
        if not node:
            return None
        
        # Create a dict to store original node and its clone
        originalToCloneMap = {}

        # Use DFS to clone graph
        def dfs(node):
            # If node already cloned, return its clone
            if node in originalToCloneMap:
                return originalToCloneMap[node]
            
            # If not, then clone node
            clone = Node(node.val)
            originalToCloneMap[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)

