class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs(root, target):
    if root is None:
        return False
    
    queue = [root]
    
    while queue:
        current_node = queue.pop(0)
        if current_node.value == target:
            return True
        queue.extend(current_node.children)
    
    return False


root = TreeNode('A')
root.children.append(TreeNode('B'))
root.children.append(TreeNode('C'))

node_b = root.children[0]
node_b.children.append(TreeNode('D'))
node_b.children.append(TreeNode('E'))

node_c = root.children[1]
node_c.children.append(TreeNode('F'))
node_c.children.append(TreeNode('G'))

node_d = node_b.children[0]
node_d.children.append(TreeNode('H'))
node_d.children.append(TreeNode('I'))

print(bfs(root, 'H'))  
print(bfs(root, 'X'))  
