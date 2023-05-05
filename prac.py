class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: {self.price}원"
    def __repr__(self) -> str: 
        return f"{self.name}: {self.price}원"
      
class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        """메뉴에 메뉴 아이템 객체 추가"""
        self.items[item_name] = item

    def show_menu(self):
        """메뉴에 저장된 모든 아이템을 출력"""
        for key in self.items:
            print(self.items[key])

    def get_items(self):
        """메뉴에 저장된 모든 아이템을 딕셔너리 형태로 리턴"""
        return self.items

    def get_item(self, item_name):
        """{item_name}의 value, 메뉴 아이템 객체를 리턴"""
        return self.items[item_name]


class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

    def add_quantity(self, quantity):
        """아이템의 수량 증가"""
        self.quantity += quantity

    def remove_quantity(self, quantity):
        """아이템의 수량 감소. 결과가 0개 미만일 경우 에러"""
        if self.quantity - quantity < 0:
            raise ValueError(f"{self.name}이 충분하지 않습니다. 재고: [{self.quantity}]")
        self.quantity -= quantity


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, item):
        """인벤토리에 인벤토리 아이템 객체 추가"""
        self.items[item_name] = item

    def get_items(self):
        """인벤토리에 저장된 모든 아이템을 딕셔너리 형태로 리턴"""
        return self.items

    def get_item(self, item_name):
        """{item_name}의 value, 인벤토리 아이템 객체를 리턴"""
        return self.items[item_name]

    def add_item_quantity(self, item_name, quantity):
        """인벤토리에 {item_name}를 key로 등록된 인벤토리 아이템 객체의 수량 증가"""
        self.items[item_name].add_quantity(quantity)

    def remove_item_quantity(self, item_name, quantity):
        """인벤토리에 {item_name}를 key로 등록된 인벤토리 아이템 객체의 수량 감소"""
        self.items[item_name].remove_quantity(quantity)


class Person:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def action(self, param):
        pass

    def info(self):
        """Person 객체의 이름, 인벤토리 정보를 출력"""
        print(f"이름 : {self.name}")
        print("소지품")
        items = self.inventory.get_items()
        for key in items:
            print(items[key])


class Customer(Person):
    def __init__(self, name, inventory):
        super().__init__(name, inventory)
        self.order = None

    # 주문
    def action(self, order_item):
        """
        Q. Person 클래스에게 상속받은 action 메소드를 오버라이딩하여 고객이 주문하는 메소드를 만들어봅시다.
        요구사항.
        1. action 메소드의 인자로는 메뉴 아이템 객체를 받습니다.
        2. 아이템의 가격보다 고객이 가진돈이 적을 경우에는 주문할 수 없습니다. (에러 발생 등 예외처리를 해주세요)
        3. 아이템의 가격을 충분히 지불할 수 있다면 self.order에 아이템을 저장해주세요
        """
        item = self.inventory.get_item("money")
        try:
            if order_item.price > item.quantity:
                raise Exception("<잔액 부족!>")

            else:
                self.order = ''
                self.order += order_item.name
                print("<구매 완료!>")
                print(f"{self.name}이(가) 구매한 커피 : {self.order}")
                return True
            
        except Exception as e:
            print(e)
            return False

class Barista(Person):
    def __init__(self, name, inventory):
        super().__init__(name, inventory)

    # 커피 제조
    def action(self, customer):
        """
        Q. Person 클래스에게 상속받은 action 메소드를 오버라이딩하여 바리스타가 커피를 제조하는 메소드를 만들어봅시다.
        요구사항.
        1. action 메소드의 인자로는 주문하는 고객 객체를 받습니다.
        2. 고객의 주문을 만들기 위해 필요한 제료를 바리스타의 인벤토리에서 빼줍니다.(재료가 충분하지 않다면 InventoryItem 객체에서 에러가 발생합니다)
        3. 제조가 완료 되었다면 고객 인벤토리에서 돈을 빼주고 바리스타 인벤토리에 돈을 더해줍니다.
        교수님 저는 멀티가 안되는 타입입니다 .. ㅠ ㅠ네 .. ! 
        
        """
        amu = 0
        b_money = self.inventory.get_item("money")
        print(customer_inventory.get_item("money").quantity)
        print(customer.order is not None)
        if customer_inventory.get_item("money").quantity >= 3000 and customer.order is not None:
            print(f"{customer.order}주문이 들어왔습니다.")
            print("제조를 시작합니다.")
            if customer.order == "Americano":
                b_item = menu.get_item("americano").ingredients
                print(b_item, "확인")
                for key, value in b_item.items():
                    if value <= self.inventory.get_item(key).quantity:
                        self.inventory.get_item(key).remove_quantity(value)
                    else:
                        print("아메리카노를 만들 수 있는 재고가 없습니다.")
                        amu = 1
            elif customer.order == "Latte":
                b_item = menu.get_item("latte").ingredients
                print(b_item, "확인")
                for key, value in b_item.items():
                    if value <= self.inventory.get_item(key).quantity:
                        self.inventory.get_item(key).remove_quantity(value)
                    else:
                        print("라떼를 만들 수 있는 재고가 없습니다.")
                        print(f"재고 {self.inventory.get_item(key)}")
                        amu = 1
            if amu == 0:
                customer_inventory.get_item("money").quantity -= 3000
                b_money.quantity += 3000

        else:
          print("잔액이 부족합니다.")

    def get_income(self):
        """Barista 객체가 보유한 money를 리턴"""
        return self.inventory.get_item("money").quantity


# 카페 메뉴 생성
menu = Menu() #Menu클래스 객체 생성 
menu.add_item("americano", MenuItem("Americano", 3000, {"bean": 2, "water": 2}))
#MenuItem 클래스의 생성자를 호출하여 새로운 MenuItem객체를 만들고 반환함
#이 객체는 변수에 할당하지 않더라도 메모리에 존재!
menu.add_item("latte", MenuItem("Latte", 3000, {"bean": 2, "milk": 2}))
print("--메뉴 정보--")
menu.show_menu()
print(menu.get_items())


#고객 생성
customer_inventory = Inventory()
customer_inventory.add_item("money", InventoryItem("Money", 5000))
customer = Customer("철수", customer_inventory)
print("--고객 정보--")
customer.info()

# 바리스타 생성
barista_inventory = Inventory()
barista_inventory.add_item("water", InventoryItem("Water", 20))
barista_inventory.add_item("bean", InventoryItem("Bean", 20))
barista_inventory.add_item("milk", InventoryItem("Milk", 10))
barista_inventory.add_item("money", InventoryItem("Money", 0))
barista = Barista("민수", barista_inventory)
print("--바리스타 정보--")
barista.info()


# 주문
customer.action(menu.get_item("latte"))

print("\n==========\n")

# 커피 제조

barista.action(customer)
barista.action(customer)




# 정보 확인
print("--고객 정보--")
customer.info()
print("--바리스타 정보--")
barista.info()
print("")
print(f"바리스타 수입 : {barista.get_income()}")