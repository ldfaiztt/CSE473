# shopSmart.py
# ------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""

import shop

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """    
    "*** YOUR CODE HERE ***"
    totalCost = {}
    for shop in fruitShops:
        totalCost[shop] = 0.0

    for order in orderList:
        fruit, pounds = order
        for shop in totalCost.keys():
            cost = shop.getCostPerPound(fruit)
            if cost == None:
                print "%s doesn't have %s" % (shop, fruit)
                del totalCost[shop]
            else:
                totalCost[shop] += cost * pounds

    if len(totalCost.keys()) == 0:
        return None

    bestShop = (totalCost.keys())[0]
    minCost = totalCost[bestShop]
    for shop, cost in totalCost.items():
        if cost < minCost:
            bestShop = shop
            minCost = cost

    return bestShop
    
if __name__ == '__main__':
  "This code runs when you invoke the script from the command line"
  orders = [('apples',1.0), ('oranges',3.0)]
  dir1 = {'apples': 2.0, 'oranges':1.0}
  shop1 =  shop.FruitShop('shop1',dir1)
  dir2 = {'apples': 1.0, 'oranges': 5.0}
  shop2 = shop.FruitShop('shop2',dir2)
  shops = [shop1, shop2]
  print "For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName()
  orders = [('apples', 3.0)]
  print "For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName()
