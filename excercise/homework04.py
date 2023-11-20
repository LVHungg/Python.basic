"""
TOÁN TIỂU HỌC:

Để tổ chức liên hoan cho gia đình, mẹ nhờ Nguyễn Trần Vĩnh An đi chợ mua heo, bò và tôm sú. Mẹ có một vài yêu cầu như sau:
  - tổng số cân nặng của 3 loại (tôm, bò, heo) là 2.9 ki-lô-gam.
  - tiền chi mua mỗi loại (tôm, bò, heo) là như nhau

Được biết: 
  - giá thịt bò: 280vnd/kg
  - giá thịt heo: 160vnd/kg
  - giá tôm sú: 320vnd/kg

Hỏi mỗi loại thực phẩm thằng An mua được bao nhiêu ki-lô-gam?
 ----------------------------------------------------------

Input:
  giá thịt bò: [price]
  giá thịt heo: [price]
  giá tôm sú: [price]
  tổng cân nặng mua 3 loại thực phẩm: [weight]

Output:
  Có thể mua được:
    {weight} ki-lô-gam thịt bò
    {weight} ki-lô-gam thịt heo
    {weight} ki-lô-gam tôm

----------------------------------------------------------------
Test case:
- input:
giá thịt bò: 280
giá thịt heo: 160
giá tôm sú: 320
tổng cân nặng mua 3 loại thực phẩm: 2.9

- output:
  Có thể mua được:
    0.8 ki-lô-gam thịt bò
    1.4 ki-lô-gam thịt heo
    0.7 ki-lô-gam tôm
"""
weight = float(input('tổng cân nặng 3 loại thực phẩm : '))
price_beef = int(input(' giá của thịt bò là : ')) 
price_pork = int(input(' giá của thịt heo là : '))
price_shrimp = int(input(' giá của tôm số là : '))
# Giá tiền cho mỗi loại thực phẩm (tương đồng nhau)
total_cost = weight * ((price_beef + price_pork + price_shrimp)/3) /3    # Giá tiền tổng cộng

# Sử dụng giá tiền và giá/kg để tính số kilogram cho từng loại thực phẩm
beef_weight = total_cost / price_beef
pork_weight = total_cost / price_pork
shrimp_weight = total_cost / price_shrimp
#làm tròn số
beef_weight = round((beef_weight),1)
pork_weight = round((pork_weight),1)
shrimp_weight = round((shrimp_weight),1)
# In số kilogram cho từng loại thực phẩm
print("có thể mua được")
print(f'{beef_weight} số kilogram thịt bò ')
print(f'{pork_weight} số kilogram thịt heo')
print(f'{shrimp_weight} số kilogram tôm sú')
