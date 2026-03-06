import re

with open("raw.txt", "r") as file:
    data = file.read()

prices = re.findall(r"Price: (\d+)", data)
print("Prices:", prices)
total = sum(int(price) for price in prices)
print("Calculated Total:", total)