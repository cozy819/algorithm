class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length_count = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length_count += 1

        end_length = length_count - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next

        return cur

    def get_kth_node_from_last_way2(self, k):
        # 1. 노드를 2개 잡는다
        slow = self.head
        fast = self.head

        # 2. 노드 사이의 간격을 k만큼 두게 한다
        for i in range(k):
            fast = fast.next

        # 3. 계속 한 칸씩 같이 이동한다
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # 4. 뒤의 노드가 끝에 도달하면 앞의 노드를 반환
        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)


print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!