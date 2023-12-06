def add(stock, adding):
    for item in stock: 
        if item.name == adding.name:
            item.add(adding.amount)
            return stock
    stock.append(adding)
    return stock
