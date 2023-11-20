#  ======================= Bài 01 ==================================
"""
input : firstname, last name, middle name, birthday
output :
[fullname] có:
    Họ là [firstname]
    Tên là [lastname]
năm nay "[firstname]" tròn [age] tuổi.

note: 
    định dạng lại chữ viết hoa trong tên (viết hoa chữ cái đầu)
    dựa vào birthday(str) tính số tuổi [age] thuộc kiểu dữ liệu (int)
    phải đủ 12 tháng thì mới tính một tuổi:
"""

# bài 1 :
#
# nhập dữ liệu

firstname = str.capitalize((input('Nhập họ : ')))
lastname = str.capitalize((input('Nhập tên : ')))
middlename = str.capitalize((input('Nhập tên đệm : ')))
birthday = str(input(' Nhập ngày tháng năm sinh (dd/mm/yyyy) : '))

fullname = firstname + ' ' + middlename + ' ' + lastname

# // 365 chia số ngày cho 365 để tính tuổi. Kết quả trả về sẽ là tuổi (làm tròn xuống đến số nguyên gần nhất).
def age_caculate(day_bd1,month_bd,year_bd):
    # case1: month of birthday > to_month
    if month_bd > 11:
        age = (2023 - 1) - year_bd
    # case2: month of birthday < to_month
    if month_bd < 11:
        age = 2023 - year_bd
    # case3: month of birthday == to_month
    if month_bd == 11:
        # case1: day of birthday > today
        if day_bd > 15:
            age = 2023 - 1 - year_bd
        # case2: day of birthay >= today
        else:
            age = 2023 - year_bd
    return age

# DATA PROCESSING: split string of birthday to get day_bd, month_bd, year_bd and calculate age
#split string of birthday
day_bd = int(birthday[:2])
month_bd = int(birthday[3:5])
year_bd = int(birthday[-4:])

age = age_caculate(day_bd, month_bd, year_bd)

# OUTPUT - print the result
# print(day_bd)
# print(month_bd)
# print(year_bd)
# print(age)

print('fullname có:', fullname)
print("Họ là :", firstname)
print("Tên là :", lastname)
print(f"Năm nay \"{lastname}\" tròn {age} tuổi.")

"""
BÀI 01:
-> Output: SAI kết quả
-> Code format: 8/10 
    khuyến khích cmt bằng tiếng Anh
    các block code nên được phân biệt bởi khoảng cách là 1 dòng
LỖI: 
    Nhập họ : Lê
    Nhập tên : Hùng
    Nhập tên đệm : Văn
    Nhập ngày tháng năm sinh (dd/mm/yyyy) : 26/11/2001
    fullname có: Lê Văn Hùng
    Họ là : Lê
    Tên là : Hùng
    năm nay "{lastname}" tròn {age} tuổi. => sử dụng format() để điền dữ liệu vào {}
UPDATE:
    nếu trường hợp dữ liệu ngày tháng năm sinh nhập vào là dd.mm.yyyy thì cũng xử lý luôn
    trường hợp nhập sai format ngày tháng năm sinh: sử dụng try/except để báo lỗi cho người dùng.
"""

# ======================== Bài 02 ===================================
"""
input: Nhập vào họ tên đầy đủ
ouput: In ra Họ, Tên đệm, Tên (mỗi giá trị in ra trên 1 dòng)
"""

fullname = str(input(' Nhập họ tên đầy đủ : ')) 
name = fullname.split()


if len(name) >= 3:
    last_name = name[0]
    middle_name =  name[1:-1]
    first_name = name[-1]
    print("Họ:", last_name)
    print("Tên đệm:", str(middle_name))
    print("Tên:", first_name)
else:
    print("Vui lòng nhập đúng định dạng họ tên (Họ Tên đệm Tên).")


# REVIEW BÀI LÀM:
"""
BÀI 02:
-> Output: SAI kết quả
-> Code format: 7/10
    nên cmt giải thích cụ thể ở các dòng lệnh xử lý
    khuyến khích cmt bằng tiếng Anh
    các block code nên được phân biệt bởi khoảng cách là 1 dòng
Lỗi:
    Nhập họ tên đầy đủ : Lê Văn Hùng
    Họ là :  Lê Văn Hùng
    Tên đệm là :
    Tên là : ng

Sửa lại:
    - input:
    Nhập họ tên đầy đủ: Lê Văn Hùng
    - output:
    Họ là: Lê
    Tên là: Hùng
    ==> có thể sử dụng hàm split() trong string method để tách các từ trong str và lấy thông tin first name và last name để in ra màn hình
"""
