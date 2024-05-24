from classes_we_ll_be_using import merchant
print("you can spend ")
spend_money = input("would you like to spend money to gain health points Y/N: ").upper()
if spend_money == "Y":
    print("you have now gained health points ")
    input("would you like to trade wit merchant to gain xp y/n?").upper()
else: 
    print("you can now proceed with your game ")
    