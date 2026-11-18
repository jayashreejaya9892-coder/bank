import sys
def bankOper(initialbal,deposit,withdraw):
    totalBal=initialbal+deposit
    updateBal=totalBal-withdraw

    return totalBal,updateBal

if __name__== "__main__":
    initialBal=int(input(sys.argv[1]))
    deposit=int(input(sys.argv[2]))
    withdraw=int(input(sys.argv[3]))

    totalBal,updateBal=bankOper(initialBal,deposit,withdraw)

    print("Total balance: ",totalBal)
    print("updated balance: ",updateBal)