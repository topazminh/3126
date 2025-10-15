def tong_de_quy(n):
    if n <= 1:
        return n
    return n + tong_de_quy(n - 1)

n = 10
print("Tổng từ 1 đến", n, "là:", tong_de_quy(n))
