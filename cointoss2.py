import CoinClass as c

def show_coin_status(coin_obj):
    print('This side is up: ', coin_obj.get_sideup())


def flip(coin_obj):
    coin_obj.toss() #toss is a method


my_coin = c.Coin() #my_coin is an object
show_coin_status(my_coin)
flip(my_coin)