class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 맨 뒤에 있는 원소와 루트 노드를 교환
        self.items[1], self.items[len(self.items) - 1] = self.items[len(self.items) - 1], self.items[1]

        # 맨 뒤에 있는 원소(원래 루트 노드)를 제거
        prev_max = self.items.pop()

        # 변경된 루트노드와 자식들을 비교
        # 자식이 더 크다면, 그 노드와 교환
        # 자식들이 더 작거나, 바닥레벨까지 왔으면 멈춤
        cur_index = 1
        while cur_index * 2 < len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            if self.items[cur_index] < self.items[left_child_index]:
                self.items[cur_index], self.items[left_child_index] = self.items[left_child_index], self.items[cur_index]
                cur_index = left_child_index
            elif self.items[cur_index] < self.items[right_child_index]:
                self.items[cur_index], self.items[right_child_index] = self.items[right_child_index], self.items[cur_index]
                cur_index = right_child_index
            else:
                break

        # 제거했던 노드를 반환
        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]