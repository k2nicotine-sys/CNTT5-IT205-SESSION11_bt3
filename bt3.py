product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

def input_positive_integer(message):
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue
            return value
        except ValueError:
            print("Giá/Số lượng không hợp lệ")

while True:
    try:
        choice = int(input("""
===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====
1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm mới
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm theo mã
5. Thoát chương trình

Mời bạn chọn:
"""))

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
    match choice:
        case 1:
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")

                for index, product in enumerate(product_list, start=1):
                    print(
                        f"{index}. "
                        f"Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Số lượng: {product['quantity']}"
                    )

        case 2:

            product_id = input(
                "Nhập mã sản phẩm: "
            ).strip().upper()
            duplicate = False
            for product in product_list:
                if product["product_id"] == product_id:
                    duplicate = True
                    break
            if duplicate:
                print("Mã sản phẩm bị trùng")
                continue
            product_name = input(
                "Nhập tên sản phẩm: "
            )
            price = input_positive_integer(
                "Nhập giá sản phẩm: "
            )

            quantity = input_positive_integer(
                "Nhập số lượng sản phẩm: "
            )
            new_product = {
                "product_id": product_id,
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            }

            product_list.append(new_product)
            print("Thêm sản phẩm thành công")
        case 3:
            update_id = input(
                "Nhập mã sản phẩm cần cập nhật: "
            ).strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == update_id:
                    found = True
                    product["product_name"] = input(
                        "Nhập tên mới: "
                    )
                    product["price"] = input_positive_integer(
                        "Nhập giá mới: "
                    )
                    product["quantity"] = input_positive_integer(
                        "Nhập số lượng mới: "
                    )
                    print("Cập nhật sản phẩm thành công")
                    break
            if not found:
                print(
                    "Không tìm thấy mã sản phẩm cần cập nhật!"
                )

        case 4:
            delete_id = input(
                "Nhập mã sản phẩm cần xóa: "
            ).strip().upper()
            found = False
            for product in product_list:
                if product["product_id"] == delete_id:
                    product_list.remove(product)
                    found = True
                    print("Xóa sản phẩm thành công")
                    break
            if not found:
                print(
                    "Không tìm thấy mã sản phẩm cần xoá!"
                )
        case 5:

            print("Thoát chương trình.")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")