import RetailItemClass as ri

def main():

    item1 = ri.RetailItem('Jacket',12,59.95)
    item2 = ri.RetailItem('Designer Jeans',40,34.95)
    item3 = ri.RetailItem('Shirt',20,24.95)

    print("Item 1 details:",item1.get_description(),item1.get_inventory(),item1.get_price())

main()