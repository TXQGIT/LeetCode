class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key  # 删除hashMap中节点使用
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # 采用双向链表+Hash表实现
    # 双向链表存储每个key对应的val, 链表头表示最近使用的, 链表尾表示最久未使用的
    # Hash表存储每个key对应双向链表中val结点
    def __init__(self, capacity: int):
        self.hashMap = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head


    def move_node_to_head(self, node):
        #将node结点的前后结点相连
        node.pre.next = node.next
        node.next.pre = node.pre
        #将node结点移到链表头
        self.head.next.pre = node
        node.next = self.head.next
        self.head.next = node
        node.pre = self.head


    def get(self, key: int) -> int:
        # 如果key存在, 则在获取值的同时将对应结点移至链表头
        node = self.hashMap.get(key, None)
        if node:
            self.move_node_to_head(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap.get(key)
            node.val = value
            #更新已存在的结点也算使用,需要把结点移到链表头
            self.move_node_to_head(node)
        else:
            if self.capacity<=len(self.hashMap):
                #当前容量已经使用完
                #获取尾结点
                tailNode = self.tail.pre
                #从链表中移除尾结点
                self.tail.pre = tailNode.pre
                tailNode.pre.next = self.tail
                #从Hash表中移除尾结点的key
                self.hashMap.pop(tailNode.key)
            #当前容量有富余, 直接添加至链表头
            node = ListNode(key, value)
            self.hashMap[key] = node
            node.next = self.head.next
            node.pre = self.head
            self.head.next.pre = node
            self.head.next = node

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))