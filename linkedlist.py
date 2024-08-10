class Node:

    data=None
    next_node=None

    def __init__(self,data):
        self.data=data

n1=Node(3)
n2=Node(4)
n3=Node(5)
n4=Node(6)
n5=Node(7)
n6=Node(8)

n1.next_node=n2
n2.next_node=n3
n3.next_node=n4
n4.next_node=n5
n5.next_node=n6

currentnode=n1
while currentnode:
    print(currentnode.data,end=" --> ")
    currentnode=currentnode.next_node
print("Null")

    
        
