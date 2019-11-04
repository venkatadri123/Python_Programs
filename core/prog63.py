# Keyword arguments:
# these are that identify the parameters by their name.
def grocery(item,price):
    print('item=%sa,\nits price=%.2f' %(item,price))
grocery(item='sugar',price=50.00)

# Keyword arguments:
def grocery(item,price):
    print('item=%sa,\nits price=%.2f' %(item,price))
grocery(price=50.00,item='sugar')
