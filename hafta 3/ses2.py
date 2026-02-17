
def trade(rsi):
    if rsi<20:
        print('..................alım yapıldı')
    elif rsi>80:
        print('satış yapıldı..................')
    else:
        print('====pozisyonu koru===')