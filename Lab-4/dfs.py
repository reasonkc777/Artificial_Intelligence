class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node, target):
    if node is None:
        return False
    
    if node.value == target:
        return True
    
    for child in node.children:
        if dfs(child, target):
            return True
    
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

print(dfs(root, 'H'))  
print(dfs(root, 'X'))  
