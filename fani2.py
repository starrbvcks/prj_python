class Employee():
    def __init__(self, employee_code, employee_name, employee_number, total_sell=0 ):
        self.employee_code = employee_code #کد کارمند
        self.employee_name = employee_name #اسم کارمند
        self.employee_number = employee_number #شماره کارمند
        self.total_sell = total_sell #مجموع فروش

def add_employee(employee_list):
    """
    اضافه کردن کارمند جدید به لیست کارمندان
    """
    #گرفتن اطلاعات کارمند
    employee_code = input("Enter code: ")
    employee_name = input("Enter full name: ")
    employee_number = input("Enter your ID: ")
    
    #ساختن شی جدید از کلاس
    new_employee = Employee(employee_code, employee_name, employee_number)
    
    #افزودن کارمند جدید به لیست
    employee_list.append(new_employee)
    print(f"{employee_name} was added.")

def edit_employee(employee_list):
    """
    ویرایش اطلاعات یک کارمند موجود در لیست کارمندان.
    """
    #شناسایی کارمند
    code = input("Enter the code you want to edit: ")
    #چسنچو در لیست کارمندان
    for emp in employee_list:
        if emp.employee_code == code:
            #گرفتن اطلاعات جدید
            new_name = input("Enter new name: ")
            new_number = input("Enter new number: ")
            #ایجاد تغییرات روی کارمند
            emp.employee_name = new_name
            emp.employee_number = new_number
            print("Employee updated.")
            return
    #کارمند پیدا نشده    
    print(f"{code} >>>does not exist.")

class Customer():
    def __init__(self, username, name, customer_id, number):
        self.username = username #نام کاربری مشتری
        self.name = name #نام مشتری
        self.customer_id = customer_id #آیدی مشتری
        self.number = number #شماره مشتری
        self.total_buy = 0 #مجموع خرید مشتری
        self.off_value = 0 #مجموع تخفیف مشتری
        self.total_debt = 0 #کجموع بدهی

def add_customer(customer_list):
    """
    افزودن مشتری جدید به لیست مشتریان
    """
    #گرفتن اطلاعات مشتری
    username = input("Enter username: ")
    name = input("Enter full name: ")
    customer_id = input("Enter your ID: ")
    number = input("Enter phone number: ")
    #
    new_customer = Customer(username, name, customer_id, number)
    #
    customer_list.append(new_customer)
    print(f"{name} was added.")

def edit_customer(customer_list):
    """
    ادیت اطلاعات مشتری 
    """
    username = input("Enter the username you want to edit: ")
    #جستجوی مشتری توی لیست
    for customer in customer_list:
        if customer.username == username:
            #دریافت اطلاعات جدید
            new_name = input("Enter new name: ")
            new_id = input("Enter new ID: ")
            new_number = input("Enter new phone number: ")
            #آپدیت اطللاهات جدید
            customer.name = new_name
            customer.customer_id = new_id
            customer.number = new_number
            print("Customer updated.")
            return
    #مشتریو پیدا نکرد
    print(">>>Customer not found.")

class Product():
    def __init__(self, product_code, product_name, product_price, product_mojodi):
        self.product_code = product_code #کد محصول 
        self.product_name = product_name #اسم محصول
        self.product_price = product_price #قیمت محصول
        self.product_mojodi = product_mojodi #موجودی محصول :)

def add_product(product_list):
    """
    اضافه کردن محصول جدید
    """
    #گرفتن اطلاعات محصول
    product_code = input("Enter product code: ")        
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: ")) 
    product_mojodi = int(input("Enter product quantity: "))
    #ایجاد شی جدید از کلاس
    new_product = Product(product_code, product_name, product_price, product_mojodi)
    #اضافه کردن محصول جدید به لیست
    product_list.append(new_product)
    print(f"{product_name} added.")

def edit_product(product_list):
    """
    ویرایش اطلاعات یک محصول
    """
    code = input("Enter code of product you want to edit: ")
    #جستجوی محصول
    for product in product_list:
        if product.product_code == code:
            #دریافت اطلاعات جدید
            name = input("Change the name: ")
            price = float(input("Change the price: "))        
            mojodi = int(input("Change the quantity: ")) 
            #اپدیت اطلاعات
            product.product_name = name
            product.product_price = price
            product.product_mojodi = mojodi
            print("Product updated.")
            return 
    print(">>>Product not found.")

class Orders():
    def __init__(self, order_num, customer_code, order_code, order_date, order_delivery, product_tedad):
        self.or_num = order_num
        self.customer_code = customer_code
        self.order_code = order_code
        self.order_date = order_date
        self.order_delivery = order_delivery
        self.product_tedad = product_tedad
        self.delivered = False 

def add_order(order_list, product_list, customer_list):
    """
    ایجاد سفارش جدید برای یک مشتری.
    """
    print("New order: ")
    order_num = input("Enter order number: ") 
    customer_code = input("Enter customer code: ")
    order_code = input("Enter product code: ")
    order_date = input("Enter order date (e.g. 1404-05-07): ")
    order_delivery = input("Enter delivery date (e.g. 1404-06-01): ")
    product_tedad = int(input("Enter quantity: "))

    #بررسی تعداد محصول
    if product_tedad <= 0:
        print("Invalid quantity.")
        return
    #پیدا کردن مشتری بر اساس کد
    customer = None
    for c in customer_list:
        if c.customer_id == customer_code:
            customer = c
            break
    if not customer:
        print("Customer not found.")
        return
    #بررسی بدهی مشتری
    if customer.total_debt > 0:
        print("Customer has unpaid debt.")
        return
    #پیدا کردن محصول
    product = None
    for p in product_list:
        if p.product_code == order_code:
            product = p
            break
    if not product:
        print("Product not found.")
        return
    #بررسی تعداد محصول موجود
    if product.product_mojodi < product_tedad:
        print("Not enough stock.")
        return

    #استفاده از تخفیف
    discount_percent = customer.off_value  
    total_price = product.product_price * product_tedad
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    #کاهش موجودی
    product.product_mojodi -= product_tedad

    #ساخت سفارش جدید
    new_order = Orders(order_num, customer_code, order_code, order_date, order_delivery, product_tedad)
    order_list.append(new_order)

    print(f"Order {order_num} added.")
    print(f"Original Price: {total_price}")
    print(f"Discount ({discount_percent}%): -{discount_amount}")
    print(f"Final Price: {final_price}")

    #حدف تخفیف بعد از استفاده
    customer.off_value = 0  
    # اگر این خرید بیش از ۲ عدد بود، تخفیف برای خرید بعدی ذخیره شود
    if product_tedad >= 2:
        customer.off_value = 5
        

def deliver_order(order_list):
    order_num = input("Enter order number: ") #شماره سفارشو از مشتری میگیریم
    for order in order_list: #جستجو در بین سفارش‌ ها
        if order.or_num == order_num:
            if order.delivered: #اگر سفارش قبلا تحویل شده 
                print("This order is already delivered.")
                return
            order.delivered = True
            print(f"Order {order_num} has been marked as delivered.")
            return
    print("Order not found.")


def main(): #منو
    employees = []
    customers = []
    products = []
    orders = []

    while True:
        print("\n<<< MENU >>>")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Add Customer")
        print("4. Edit Customer")
        print("5. Add Product")
        print("6. Edit Product")
        print("7. Add Order")
        print("8. Deliver Order")
        print("9. Exit")

        key = input("Choose an option (1-9): ")

        if key == "1":
            add_employee(employees)
        elif key == "2":
            edit_employee(employees)
        elif key == "3":
            add_customer(customers)
        elif key == "4":
            edit_customer(customers)
        elif key == "5":
            add_product(products)
        elif key == "6":
            edit_product(products)
        elif key == "7":
            add_order(orders, products, customers)
        elif key == "8":
            deliver_order(orders)
        elif key == "9":
            print("Exiting...")
            break
        else:
            print("Invalid key. Try again.")

if __name__ == "__main__":
    main()