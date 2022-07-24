class cust_node:

    __slots__=['customer','service','next']

    def __init__(self,customer=None,service=None,next=None):
        self.customer=customer
        self.service=service
        self.next=next
    
class service_node:
    
    __slots__=['service','next']

    def __init__(self,service=None,next=None):
        self.service=service
        self.next=next

#class database:
    
    #def __init__(self):
        #start=cust_node()
