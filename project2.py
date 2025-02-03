# class Kiosk:
#     def __init__(self):
#         self.menu = ["아메리카노", "카페라떼", "카푸치노", "에스프레소"]
#         self.price = [3000, 3500, 4000, 2500]
#         self.order_menu = []
#         self.order_price = []

#     def menu_print(self):
#         for i, (item, price) in enumerate(zip(self.menu, self.price), start=1):
#             print(f"{i}. {item} : {price}원")

#     def menu_select(self):
#         try:
#             n = int(input("음료 번호를 입력하세요: "))
#             if 1 <= n <= len(self.menu):
#                 temp = "HOT" if int(input("HOT(1) / ICE(2): ")) == 1 else "ICE"
#                 self.order_menu.append(f"{temp} {self.menu[n-1]}")
#                 self.order_price.append(self.price[n-1])
#             else:
#                 print("없는 메뉴입니다. 다시 주문해 주세요.")
#         except ValueError:
#             print("숫자를 입력해 주세요.")

#     def table(self):
#         print('⟝' + '-' * 30 + '⟞')
#         for _ in range(5):
#             print('|' + ' ' * 31 + '|')
        
#         for item, price in zip(self.order_menu, self.order_price):
#             print(f"{item} : {price}원")
        
#         print(f'합계 금액 : {sum(self.order_price)}원')
        
#         for _ in range(5):
#             print('|' + ' ' * 31 + '|')
#         print('⟝' + '-' * 30 + '⟞')
    
#     def pay(self):
#         amount = sum(self.order_price)
#         print(f"지불할 금액: {amount}원")
#         payment_method = input("지불 수단을 선택하세요 (1: 현금, 2: 카드): ")
        
#         if payment_method == '1' or payment_method.lower() == 'cash':
#             print("직원을 호출하겠습니다.")
#         elif payment_method == '2' or payment_method.lower() == 'card':
#             print("IC칩 방향에 맞게 카드를 꽂아주세요.")
#         else:
#             print("다시 결제를 시도해 주세요.")

# # 실행
# a = Kiosk()
# a.menu_print()
# a.menu_select()
# a.table()
# a.pay()


# def pay(amount):
#     print(f"지불할 금액: {amount}원")
#     payment_method = input("지불 수단을 선택하세요 (1: 현금, 2: 카드): ")
    
#     if payment_method == '1' or payment_method.lower() == 'cash':
#         print("직원을 호출하겠습니다.")
#     elif payment_method == '2' or payment_method.lower() == 'card':
#         print("IC칩 방향에 맞게 카드를 꽂아주세요.")
#     else:
#         print("다시 결제를 시도해 주세요.")

# Kiosk.pay = pay
# a = Kiosk()  # 객체 생성 
# a.menu_print()  # 메뉴 출력
# a.menu_select()  # 주문
# a.pay()  # 지불

# menu_temp = ['HOT americano', 'ICE latte', 'ICE mocha', 'ICE choco_latte'] 
# price_temp = [2000, 3000, 3000, 3000] 

# # 외곽
# print('⟝' + '-' * 30 + '⟞')
# for i in range(5):
#     print('|' + ' ' * 31 + '|')

# # 주문 상품명 : 해당 금액
# for i in range(len(menu_temp)):
#     print(menu_temp[i], ' : ', price_temp[i])

# print('합계 금액 :', sum(price_temp))

# # 외곽
# for i in range(5):
#     print('|' + ' ' * 31+ '|')
# print('⟝' + '-' * 30 + '⟞')


# class Kiosk:
#     def __init__(self):
#         self.menu = ["HOT americano", "ICE latte", "ICE mocha", "ICE choco_latte"]
#         self.price = [2000, 3000, 3000, 3000]
#         self.order_menu = []
#         self.order_price = []

#     def menu_print(self):
#         print("⟝" + "-" * 30 + "⟞")
#         for _ in range(5):
#             print("|" + " " * 31 + "|")
#         for i, (item, price) in enumerate(zip(self.menu, self.price), start=1):
#             print(f"{i}. {item} : {price}원")
#         print("⟝" + "-" * 30 + "⟞")

#     def menu_select(self):
#         try:
#             n = int(input("음료 번호를 입력하세요: "))
#             if 1 <= n <= len(self.menu):
#                 self.order_menu.append(self.menu[n-1])
#                 self.order_price.append(self.price[n-1])
#             else:
#                 print("없는 메뉴입니다. 다시 주문해 주세요.")
#         except ValueError:
#             print("숫자를 입력해 주세요.")

#     def table(self):
#         print('⟝' + '-' * 30 + '⟞')
#         for _ in range(5):
#             print('|' + ' ' * 31 + '|')
        
#         for item, price in zip(self.order_menu, self.order_price):
#             print(f"{item} : {price}원")
        
#         print(f'합계 금액 : {sum(self.order_price)}원')
        
#         for _ in range(5):
#             print('|' + ' ' * 31 + '|')
#         print('⟝' + '-' * 30 + '⟞')
    
#     def pay(self):
#         amount = sum(self.order_price)
#         print(f"지불할 금액: {amount}원")
#         payment_method = input("지불 수단을 선택하세요 (1: 현금, 2: 카드): ")
        
#         if payment_method == '1' or payment_method.lower() == 'cash':
#             print("직원을 호출하겠습니다.")
#         elif payment_method == '2' or payment_method.lower() == 'card':
#             print("IC칩 방향에 맞게 카드를 꽂아주세요.")
#         else:
#             print("다시 결제를 시도해 주세요.")

# # 실행
# a = Kiosk()
# a.menu_print()
# a.menu_select()
# a.table()
# a.pay()


class Kiosk:
    def __init__(self):
        self.menu = ["HOT americano", "ICE latte", "ICE mocha", "ICE choco_latte"]
        self.price = [2000, 3000, 3000, 3000]
        self.order_menu = []
        self.order_price = []

    def menu_print(self):
        print("⟝" + "-" * 30 + "⟞")
        for _ in range(5):
            print("|" + " " * 31 + "|")
        for i, (item, price) in enumerate(zip(self.menu, self.price), start=1):
            print(f"{i}. {item} : {price}원")
        print("⟝" + "-" * 30 + "⟞")

    def menu_select(self):
        while True:
            try:
                n = int(input("음료 번호를 입력하세요 (0 입력 시 종료): "))
                if n == 0:
                    break
                elif 1 <= n <= len(self.menu):
                    self.order_menu.append(self.menu[n-1])
                    self.order_price.append(self.price[n-1])
                    print(f"주문 추가: {self.menu[n-1]} - {self.price[n-1]}원")
                else:
                    print("없는 메뉴입니다. 다시 주문해 주세요.")
            except ValueError:
                print("숫자를 입력해 주세요.")

    def table(self):
        print('⟝' + '-' * 30 + '⟞')
        for _ in range(5):
            print('|' + ' ' * 31 + '|')
        
        for item, price in zip(self.order_menu, self.order_price):
            print(f"{item} : {price}원")
        
        print(f'합계 금액 : {sum(self.order_price)}원')
        
        for _ in range(5):
            print('|' + ' ' * 31 + '|')
        print('⟝' + '-' * 30 + '⟞')
    
    def pay(self):
        amount = sum(self.order_price)
        print(f"지불할 금액: {amount}원")
        payment_method = input("지불 수단을 선택하세요 (1: 현금, 2: 카드): ")
        
        if payment_method == '1' or payment_method.lower() == 'cash':
            print("직원을 호출하겠습니다.")
        elif payment_method == '2' or payment_method.lower() == 'card':
            print("IC칩 방향에 맞게 카드를 꽂아주세요.")
        else:
            print("다시 결제를 시도해 주세요.")

# 실행
a = Kiosk()
a.menu_print()
a.menu_select()
a.table()
a.pay()
