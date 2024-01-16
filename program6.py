# Návštěvník si nejdříve zvolí velikost pizzy (S, M, L). Za velikost S se platí 100 Kč, za M 150 Kč a za L 200 Kč.
# Poté se zeptáte, zda chce feferonky. Pokud ano, tak u velikosti S se bude platit 20 Kč navíc a u velikostí M a L 30 Kč navíc.
# Poté se ještě zeptáte, zda chce návštěvník sýr navíc. Pokud ano, tak si připlatí dalších 15 Kč.


print("Vítejte v aplikaci na objednání pizzy")
size = input("Jakou velikost pizzy chcete? S, M nebo L. ")
chilli_peppers = input("Chcete feferonky? A nebo N. ")
extra_cheese = input("Chcete extra sýr? A nebo N. ")


bill = 0


if size == "S":
    bill += 100
elif size == "M":
    bill += 150
elif size == "L":
    bill += 200


if chilli_peppers == "A":
    if size != "S":
        bill += 30
    else:
       bill += 20


if extra_cheese == "A":
    bill += 15


print(f"Částka k zaplacení: {bill} Kč")
