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
        node_1 = self.head
        length_count = 1

        while node_1.next is not None:
            node_1 = node_1.next
            length_count += 1
        print("length_count: ", length_count)

        index_k = length_count - 2
        k_count = 0
        node_2 = self.head
        while k_count != index_k:
            node_2 = node_2.next
            k_count += 1

        return node_2


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)


print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!