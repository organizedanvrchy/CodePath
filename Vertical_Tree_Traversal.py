# LINK to Question: https://www.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
from collections import defaultdict

class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        # Check for empty tree
        if not root:
            return
        
        # Create map to store vertical order
        vertMap = defaultdict(list)
        horDist = 0
        
        # Create queue for BFS (level-order traversal)
        # and store node with their horizontal distance
        queue = deque([(root, horDist)])
        
        while queue:
            # Pop front of queue
            node, horDist = queue.popleft()
            
            if node:
                # Insert each node data into vertMap list
                vertMap[horDist].append(node.data)
                # Add left child with horizontal distance - 1
                queue.append((node.left, horDist - 1))
                # Add right child with horizontal distance + 1
                queue.append((node.right, horDist + 1))
                
        # Traverse map in sorted order of horizontal distances
        res = []
        for key in sorted(vertMap.keys()):
            # res.append(vertMap[key])
            res.extend(vertMap[key])    # Extend fixes output by flattening the list
        
        return res
