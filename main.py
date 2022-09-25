#Binary Tree Traversals
class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value
#Inorder Traversal
def Inorder(head):
    if head:
        Inorder(head.left)              #Recur on left child
        print(head.val,end = " ")       #print data of node
        Inorder(head.right)             #recur on right child
#PreOrder Traversal
def Preorder(head):
    if head:
        print(head.val,end = " ")         #print data of node
        Preorder(head.left)               #recur on left child
        Preorder(head.right)              #recur on right child
#PostOrder Traversal
def Postorder(head):
    if head:
        Postorder(head.left)             #recur on left child
        Postorder(head.right)            #recur on right child
        print(head.val, end =" ")        #print node value
head = node(1)
head.left=node(2)
head.right= node(3)
head.left.left=node(4)
head.left.right=node(5)
#Function Calls
print ("\nInorder Traversal Of Binary Tree")
Inorder(head)
print ("\nPreOrder Traversal Of Binary Tree")
Preorder(head)
print("\nPostOrder Traversal Of Binary Tree")
Postorder(head)
