# 노드 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#노드 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#링크드 리스트 구현
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    #리스트 뒤에 노드 추가
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
    
    #노드 값 출력
    def print_all(self):
        cur = self.head
        while cur.next is not None:
            print(cur.data)
            cur = cur.next
    
    #노드 인덱스 
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node
    
    #노드 추가
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node
        
    #노드 삭제
    def delete_ndoe(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next
