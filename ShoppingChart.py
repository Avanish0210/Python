class ShoppingCart:
    def __init__(self):
        self.item={}  #item = {price:float , quantity:Integer}

    def addItem(self , name , unit_price , quantity=1):
        if quantity<0 :
            print("quantity must be greater than 0")
            return
        
        if name in self.item:  
            self.item[name]['quantity'] += quantity
        else:
            self.item[name] = {'price':unit_price , 'quantity':quantity}
        print("item is added in the chart")

    def removeItem(self , name , quantity):

        if name not in self.item[name]:
            print("The item is not in the chart")
        
        if quantity is None:
            del self.item[name]
            print("Item is removed")
        elif quantity >= self.item[name]['quantity']:
            del self.item[name]
            print("removed all names")
        else:
            self.item[name]['quantity'] -= quantity
            print("removed item")

    def subtotal(self):
        total = 0
        for item in self.item.values():
            total += item['price'] * item['quantity']
        return total
    
    def apply_discount(self , code):
        discount_rates= {
            'SALE10' : 0.10,
            'FESTIVAL20' : 0.20
        }

        if code not in discount_rates:
            print("Invalid code")
            return 0
        
        rate = discount_rates[code]
        subtotal = self.subtotal()
        discount_amount = subtotal*rate
        print("Congratulation the discount code is added")
        return discount_amount
    
    def get_final_amount(self , discountCode=None):
        subtotal = self.subtotal()
        discount=0
        discount = self.apply_discount(discountCode)
        total = subtotal - discount

        return total , discount
    
    

        