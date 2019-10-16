class ItemToPurchase:
   

    def __init__(self,item_name="none",item_price=0,item_quantity=0):   #default constructor
        self.item_name=item_name   #setting default values for variables above
        self.item_price=item_price
        self.item_quantity=item_quantity
        

    def print_item_cost(self):  #method/printing
        total = self.item_quantity * self.item_price
        print(self.item_name+ ''' '''+str(self.item_quantity)+''' @ $'''+str(self.item_price)+''' = $'''+str(total))      
    def get_item_cost(self):
        return self.item_price * self.item_quantity
    def __lt__(self,other):
        return self.get_item_cost()<other.get_item_cost()
class Receipt:
    
    def __init__(self,customer_name="Real Human",date="Today"): #constructor once again
        self.customer_name = customer_name
        self.date = date
        self.cart_items=[]

    def add_item(self,item):
        self.cart_items.append(item)
        return                        #return nothing 
    
    def print_receipt(self,isevil=True):
        total=0
        if isevil==True:
            print("Welcome to EvilMart," + str(self.customer_name))
            print(self.date)
            print("Have an EVIL day!")
            self.cart_items.sort() #sort, we must think backwards in this situation
            for item in self.cart_items:
                item.print_item_cost()
                total+= item.get_item_cost()
            
        if isevil !=True:
            print("Welcome to GoodCo," + str(self.customer_name))
            print(self.date)
            print("Have a GOOD day!")
            self.cart_items.sort(reverse=True)   #sort in reverse       
            for item in self.cart_items:
                item.print_item_cost()
                total+= item.get_item_cost()
        print("Total: $", total)
        return total
    
def main():
    new_name= input('''Enter Customer Name:
''')
    new_date= input('''Enter Today's Date:
''')
    evil_ques=input('''Are you evil?
''')
    evil_check= False
    if 'y' in evil_ques.lower(): #NH
        evil_check = True
    else:
        evil_check = False
    receipt = Receipt(new_name, new_date)
    while True:
        item_name= input('''Enter the item name:
''')
        if item_name == "":  #if nothing is entered it will break 
            break
        item_price=int(input('''Enter the item price:
'''))
        item_quantity=int(input('''Enter the item quantity:
'''))
        receipt.add_item(ItemToPurchase(item_name,item_price,item_quantity))
    receipt.print_receipt(evil_check)  #Professor Hanford 

if __name__ == '__main__':
    # "Am I being run as a script?"
    main()

            
            
        

