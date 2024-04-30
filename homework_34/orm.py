from model import session, Category, Product, Order

def insert_category(category_name):
    category = Category(category_name)
    session.add(category)
    session.commit()

def insert_product(category, product_name, price=None, stock_quantity=None):
    product = Product(category, product_name, price, stock_quantity)
    session.add(product)
    session.commit()

def update_product(product_to_update, productname, category=None):
    product = session.query(Product).filter_by(product_name = product_to_update).first()

    if product:
        product.product_name = productname
        product.category_id = category
        session.commit()
    else:
        print("Product does not exists!")

def delete_product(productname):
    product = session.query(Product).filter_by(product_name = productname).first()

    if product:
        orders = session.query(Order).filter(Order.product_id == product.product_id).all()
        for order in orders:
            session.delete(order)
            session.commit()
        session.delete(product)
        session.commit()
    else:
        print("Product does not exists!")

def order_product(product_id, quantity):
    product = session.query(Product).filter_by(product_id = product_id).first()
    if product:
        if product.stock_quantity and product.stock_quantity >= quantity:
            order = Order(product_id, quantity)
            session.add(order)
            product.stock_quantity -= quantity
            session.commit()
        else:
            print("insufficient quantity!")
    else:
        print("Product does not exists!")

def change_order_status(orderid):
    order = session.query(Order).filter_by(order_id = orderid).first()
    if order:
        order.status = "Delivered"
        session.commit()
    else:
        print("Order does not exists!")


insert_category("Drinks")
insert_category("Fruits")
insert_category("Vegetables")
insert_category("Sweets")
insert_category("Meats")

insert_product(4, "Raffaello", 8, 5)
insert_product(2, "Apple", 3.5, 11)
insert_product(3, "Cucumber", 4.7, 20)
insert_product(1, "Hennessy", 55)
insert_product(4, "Snickers", 1.8, 20)
insert_product(1, "Coca-Cola", 3.9, 10)
insert_product(2, "Orange")
insert_product(5, "Bacon", 9, 6)
insert_product(1, "Fanta", 2.8, 8)
insert_product(2, "Kiwi", 4.6, 7)
insert_product(3, "Potato", 1.9, 15)
insert_product(1, "Heineken", 5.5, 15)
insert_product(3, "Tomato", 5.2, 20)
insert_product(2, "Banana", 6.2, 18)
insert_product(1, "Borjomi", 2.5, 6)

order_product(1, 5)
order_product(4, 3)
order_product(3, 8)
order_product(6, 2)
order_product(7, 6)
order_product(8, 1)
order_product(15, 2)
order_product(3, 5)
order_product(9, 3)
order_product(3, 6)
order_product(13, 1)

change_order_status(1)
change_order_status(3)
change_order_status(9)
change_order_status(8)

update_product("Coca-Cola", "Cola", 1)
delete_product("Cucumber")

joined_query = session.query(Product.product_name, Product.product_price, Product.stock_quantity, Category.category_name, Order.quantity, Order.order_date, Order.status).join(Category).join(Order).filter(Order.status == "Pending").all()

for query in joined_query:
    print(query.product_name, query.product_price, query.stock_quantity, query.category_name, query.quantity, query.order_date, query.status, sep=", ")