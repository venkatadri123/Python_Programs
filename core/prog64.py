# Default argument: It gives a default value.
def grocery(item,price=50.00):
    print('item=%s,\nits price=%.2f' %(item,price))
grocery('sugar')
grocery('sugar',75.00)
