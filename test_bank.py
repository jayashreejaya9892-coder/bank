from bank import bankOper

def test_deposit():
    totalBal,updateBal=bankOper(200000,30000,0)

    assert totalBal == 230000
    assert updateBal== 230000

def test_withdraw():
    totalBal,updateBal=bankOper(10000,40000,10000)

    assert totalBal==140000
    assert updateBal==130000

def test_anyamount():
    totalBal,updateBal=bankOper(150000,0,15000)

    assert totalBal==150000
    assert updateBal==135000