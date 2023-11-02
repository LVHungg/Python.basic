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
# ======================== Bài 02 ===================================
"""
input: Nhập vào họ tên đầy đủ
ouput: In ra Họ, Tên đệm, Tên (mỗi giá trị in ra trên 1 dòng)
"""

#bài 1 :
#nhập dữ liệu
firstname = str.capitalize((input('Nhập họ : ')))
lastname = str.capitalize((input('Nhập tên : ')))
middlename = str.capitalize((input('Nhập tên đệm : ')))
birthday = str(input(' Nhập ngày tháng năm sinh (dd/mm/yyyy) : '))
fullname = firstname + ' ' + middlename + ' ' + lastname
#khai báo thư viện datetime để kiếm ngày hiện tại
from datetime import datetime
year_bd = datetime.strptime(birthday, "%d/%m/%Y") #phân tích một chuỗi ngày tháng thành một đối tượng  #"%d/%m/%Y" định dạng ngày tháng năm 
age = (datetime.now() - year_bd).days // 365  #// 365 chia số ngày cho 365 để tính tuổi. Kết quả trả về sẽ là tuổi (làm tròn xuống đến số nguyên gần nhất).

print('fullname có:',fullname)
print("Họ là :",firstname)
print("Tên là :",lastname)
print("năm nay \"{lastname}\" tròn {age} tuổi.")

#bài 2 :
fullname = str(input(' Nhập họ tên đầy đủ : '))  #Nguyễn Trần Vĩnh An
firstname = (fullname[0:11])
middlename = (fullname[12:16])
lastname = (fullname[-2:])
print("Họ là : ",firstname)
print("Tên đệm là : ",middlename)
print( "Tên là :",lastname)





