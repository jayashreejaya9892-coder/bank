def bankOper(initialbal,deposit,withdraw):
    totalBal=initialbal+deposit
    updateBal=totalBal-withdraw

    return totalBal,updateBal

if __name__== "__main__":
    initialBal=int(input("Enter amount as initial:"))
    deposit=int(input("Enter amount to deposit:"))
    withdraw=int(input("Enter amount to withdraw:"))

    totalBal,updateBal=bankOper(initialBal,deposit,withdraw)

    print("Total balance: ",totalBal)
    print("updated balance: ",updateBal)