def thap_ha_noi(n, cot_nguon, cot_trung_gian, cot_dich):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ {cot_nguon} sang {cot_dich}")
    else:
        thap_ha_noi(n - 1, cot_nguon, cot_dich, cot_trung_gian)
        print(f"Di chuyển đĩa {n} từ {cot_nguon} sang {cot_dich}")
        thap_ha_noi(n - 1, cot_trung_gian, cot_nguon, cot_dich)
# Nhập số đĩa từ người dùng
n = int(input("Nhập số đĩa: "))
print("Các bước di chuyển:")
# Gọi hàm với 3 cọc: A (nguồn), B (trung gian), C (đích)
thap_ha_noi(n, 'A', 'B', 'C')
