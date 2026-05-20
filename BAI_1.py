bill = int(input("Nhập tổng tiền hóa đơn ban đầu"))
print("---- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")

if bill > 500000:
    price_cut = bill * 0.1
    new_bill = bill - price_cut

    print(new_bill)
    print(price_cut)

    print(f"""
        Số tiền được giảm giá : {int(price_cut)} VNĐ
        Tổng tiền khách phải trả : {int(new_bill)} VNĐ
            """)
else :
    print(f"Tổng tiền khách phải trả {bill}")