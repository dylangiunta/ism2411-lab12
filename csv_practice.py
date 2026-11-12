# mv ~Downloads/sales.csv ~/Documents/ism2411-lab12/data 



import csv 
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"


print("---Exercise 1---")

with open(SALES_FILE, "r") as sales_file:
    print(f"Opened{SALES_FILE}.")

print("---Exercise 2---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


print("---Exercise 3---")

with open(SALES_FILE,"r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("---Exercise 4---")
total_revenue = 0 
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str, total_str = row 
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity 
        total_revenue += total 
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")



print("---Exercise 5---")
high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader: 
        rows_read += 1 
        product, price_str, qty_str, total_str = row 
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

print("---Exercise 6---")

dict_total = 0 
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["Price"])
        quantity = int(row["Quantity"])
        total = price * quantity 
        dict_total += total 
        print(f"{row['Product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")

print("---Exercise 7---")

summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["Product"]
        total = float(row["Price"]) * int(row["Quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


print("---Exercise 8---")

timestamp = datetime.now() .strftime("%Y-%m-%d %H: %M:$S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1 
        print(line.strip())

print(f"Log entries so far: {entries}")

