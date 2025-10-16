# Định nghĩa một nút trong danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def dem_so_phan_tu(node):
    if node is None:
        return 0
    else:
        return 1 + dem_so_phan_tu(node.next)
# Tạo danh sách liên kết: 1 -> 2 -> 3 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# Đếm số phần tử
so_phan_tu = dem_so_phan_tu(head)
print("Số phần tử trong danh sách liên kết là:", so_phan_tu)
