def playerCard(*prise_money, **person):
    prise_money_sum = sum(prise_money)
    print("*" * 30)
    print("* First Name:", person["fname"])
    print("* Last Name:", person["lname"])
    print("* Ranking:", person["ranking"])
    print("* Prise Money Sum:", prise_money_sum)
    print("*" * 30)
    
playerCard(9000, 8500, 11900, 230000, fname = "Janik", lname = "Sinner", ranking = 1)
playerCard(18000, 21000, 199000, lname = "Alcaraz", fname = "Carlos", ranking = 2)
