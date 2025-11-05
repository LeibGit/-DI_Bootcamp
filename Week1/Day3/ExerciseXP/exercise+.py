import statistics

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}
total_grade = 0
def student_report():

    for i in student_grades:
        student_averages[i] = statistics.mean(student_grades[i])
    print(student_averages)

    for i in student_averages:
        if student_averages[i] >= 90:
            student_letter_grades[i] = 'A'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        elif student_averages[i] >= 80 and student_averages[i] <= 89:
            student_letter_grades[i] = 'B'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        elif student_averages[i] >= 70 and student_averages[i] <= 79:
            student_letter_grades[i] = 'C'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        elif student_averages[i] >= 60 and student_averages[i] <= 69:
            student_letter_grades[i] = 'D'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
        else:
            student_letter_grades[i] = 'F'
            print(f"{student_averages[i]}: {student_letter_grades[i]}")
    avg_grade =  sum(student_averages.values()) / len(student_averages.keys())
    print(avg_grade)
student_report()

# Exercise 2
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

def sales_calculation():
    total_sales = {}
    for sales in sales_data:
        product = sales["product"]
        rev = sales["price"] * sales["quantity"]

        if product in total_sales:
            total_sales[product] += rev
        else:
            total_sales[product] = rev
    print("\n total sales:")
    for p, t in total_sales.items():
        print(f"Product: {p}, Total Rev: {t}")
sales_calculation()

def customer_spending_profile():
    customer_spend = {}
    for sale in sales_data:
        customer_id = sale["customer_id"]
        spend = sale["price"] * sale["quantity"]

        if customer_id in customer_spend:
            customer_spend[customer_id] += spend
        else:
            customer_spend[customer_id] = spend
    print("\nTotal spending by customer:")
    for customer, total in customer_spend.items():
        print(f"Customer {customer}: ${total}")
customer_spending_profile()

def sales_data_enhancement():
    for sale in sales_data:
        sale["total_price"] = sale["quantity"] * sale["price"]
    print(sales_data)  
sales_data_enhancement()

def high_value_price():
    all_transactions = []
    for sale in sales_data:
        sale["total_price"] = sale["price"] * sale["quantity"]
        if sale["total_price"] > 500:
            all_transactions.append(sale["total_price"]) 
    print(sorted(all_transactions, reverse=True))
high_value_price()
 
def customer_loyalty_identification():
    order_count = {}
    for user in sales_data:
        user_id = user["customer_id"]
        order = user["quantity"] 
        if order > 1:
            order_count[user_id] = order
        else:
            continue
    for k, v in order_count.items():
        print(f"\n{k} is loyal with a total of {v} orders!")
customer_loyalty_identification()

