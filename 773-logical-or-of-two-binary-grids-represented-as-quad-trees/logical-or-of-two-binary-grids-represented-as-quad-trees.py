# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # If quadTree1 is a leaf
        if quadTree1.isLeaf:
            return Node(True, True, None, None, None, None) if quadTree1.val else quadTree2
        
        # If quadTree2 is a leaf
        if quadTree2.isLeaf:
            return Node(True, True, None, None, None, None) if quadTree2.val else quadTree1
        
        # Recurse for all four children
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # If all four children are leaves and share the same value, merge them into a single leaf
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
           topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
            return Node(topLeft.val, True, None, None, None, None)
        
        # Otherwise, return an internal node
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)