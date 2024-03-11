class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takeInput(input_list):
    if not input_list:
        return None

    root = BinaryTreeNode(input_list[0])
    queue = [root]
    i = 1

    while i<len(input_list):
        current_node = queue.pop(0)

        if input_list[i]!=-1:
            current_node.left = BinaryTreeNode(input_list[i])
            queue.append(current_node.left)

        i+=1

        if i<len(input_list) and input_list[i] != -1:
            current_node.right = BinaryTreeNode(input_list[i])
            queue.append(current_node.right)

        i+=1

    return root


def printDetail(root,level=0,prefix="root"):

    if root is not  None:
        print(" "*(level*4) + prefix + str(root.data))
        if root.left is not None or root.right is not None:
            printDetail(root.left, level+1,"L--")
            printDetail(root.right,level+1,"R--")


def countGreater_then_x(root,x):
    if root is None:
        return 0

    count = 0

    if root.data>x:
        count+=1

    count+=countGreater_then_x(root.left,x)
    count+=countGreater_then_x(root.right,x)

    return count


input_list=list(map(int,input("Enter:").split()))

root=takeInput(input_list)
printDetail(root)
ans=countGreater_then_x(root,5)
print(ans)
