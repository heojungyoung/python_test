class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
def tree(li):
    nodes = [Node(i) for i in li]
    
    # nodes = [ Node(3), Node(5) Node(8) ... Node(21)]
    
    for i in range(1, len(li)):
        # len(li) : 7
        nodes[(i-1)//2].children.append(nodes[i])
        # 위 배열에서 (i-1)//2 한 인덱스에 해당되는 객체의 children 배열에 nodes[i]를 추가하라는 뜻
        # nodes[i]는 Node(3), Node(5)...
    return nodes[0]
    # Node(3) 리턴
    
        # i=1, nodes[0].children.append(nodes[1])
        # i=2, nodes[0].children.append(nodes[2])
        # i=3, nodes[1].children.append(nodes[3])
        # i=4, nodes[1].children.append(nodes[4])
        # i=5, nodes[2].children.append(nodes[5])
        # i=6, nodes[2].children.append(nodes[6])
        
        # nodes[0] = Node(3) -> value=3, children[ Node(5), Node(8)]
        # nodes[1] = Node(5) -> value=5, children[ Node(12), Node(15)]
        # nodes[2] = Node(8) -> value=8, children[ Node(17), Node(21)]
        # nodes[3] = Node(12) -> value=12, children[]
        # nodes[4] = Node(15) -> value=15, children[]
        # nodes[5] = Node(17) -> value=17, children[]
        # nodes[6] = Node(21) -> value=21, children[]
        
         
def calc(node, level=0):
    return node.value if level % 2 else 0 + sum(calc(n, level+1) for n in node.children) if node else 0        

# 삼항 연산자
# level % 2 참이면 node.value 리턴하고 아닌 경우에는 if node 조건문을 실행하여 참이면 0 + sum(calc(n, level+1) for n in node.children)
# 거짓이면 0 리턴

# level은 주어진게 없으므로 level=0을 % 2 시에 거짓
# 0 + sum(calc(n, level+1) for n in node.children)
# [Node(5) , Node(8)]
# calc(Node(5), 1) -> level % 2 가 1이므로 node.value 리턴 value =5
# calc(Node(8), 1) -> level % 2 가 1이므로 node.value 리턴 value =8


li = [3,5,8,12,15,17,21]


root = tree(li)


print(calc(root))


# 13

        
# def calc(node, level=0):
    # Step 1: Handle the 'node is None' case first
#    if node is None:
#        return 0

    # Step 2: level 홀수 나머지가 1이라는 것은 true 를 의미하므로...
#    if level % 2 != 0: # If level is ODD
 #       return node.value       
#    else: # If level 짝수 해당 구문에는 다시 재귀함수로 호출함.       
#        return 0 + sum(calc(n, level + 1) for n in node.children)