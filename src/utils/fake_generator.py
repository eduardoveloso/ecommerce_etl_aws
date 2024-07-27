from faker import Faker
import random
import datetime
import pytz

random.seed(120)
fake=Faker()

timezone_br = pytz.timezone("America/Sao_Paulo")
datetime_br = datetime.datetime.now().astimezone(timezone_br).strftime("%Y/%m/%d %H:%M:%S")
date_br = datetime.datetime.now().astimezone(timezone_br).strftime("%Y%m%d")

def generate_customers(num_customers):
    customers = []
    for _ in range(num_customers):
        customers.append(
            {
                "id": _ + 1,
                "name": fake.name(),
                "email": fake.email(),
                "address": fake.address(),
                "ingestion_proccess": "Faker_Generator",
                "ingestion_datetime": datetime_br,
            }
        )
    return customers


def generate_products(num_products):
    products = []
    for _ in range(num_products):
        products.append(
            {
                "id": _ + 1,
                "name": fake.word(),
                "price": round(random.uniform(5.0, 500.0), 2),
                "ingestion_proccess": "Faker_Generator",
                "ingestion_datetime": datetime_br,
            }
        )
    return products


def generate_order_items(orders, products, num_customers):
    order_items = []
    for order in orders:
        num_items = random.randint(1, 5)
        order_total = 0
        for _ in range(num_items):
            product_id = random.randint(1, len(products))
            quantity = random.randint(1, 10)
            price = products[product_id - 1]["price"]
            order_items.append(
                {
                    "id": len(order_items) + 1,
                    "order_id": order["id"],
                    "customer_id": random.randint(1, num_customers),
                    "product_id": product_id,
                    "quantity": quantity,
                    "price": price,
                    "total": price * quantity,
                    "ingestion_proccess": "Faker_Generator",
                    "ingestion_datetime": datetime_br,
                }
            )
            order_total += price * quantity
        order["total"] = order_total
    return order_items
