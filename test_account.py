from account import*

def test_init():

    ma = account("try")
    assert ma.getbalance() == 0
    assert ma.getname() == "try"


def test_deposit():

    ma = account("try")
    assert ma.deposit(30)
    assert ma.getbalance() == 30
    assert ma.deposit(0)
    assert ma.deposit(-70)


def test_withdraw():

    ma = account("try")
    assert ma.deposit(100)
    assert ma.withdraw(-50)
    assert ma.withdraw(50)
    assert ma.withdraw(-30)
    assert ma.withdraw(20)
    assert ma.withdraw != 0
    assert ma.getbalance() == 90
