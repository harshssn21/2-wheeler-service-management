class Customer():

    __slots__=['name','mail','phone','pwd']

    def __init__(self,name,mail,phone,pwd):
        self.name=name
        self.mail=mail
        self.phone=phone
        self.pwd=pwd
    
    def changename(self,newname):
        self.name=newname
    
    def changemail(self,newmail):
        self.mail=newmail
    
    def changephone(self,newphone):
        self.phone=newphone
    
    def changepwd(self,newpwd):
        self.pwd=newpwd

    '''incase the customer wants to edit is profile,
       the customer details are stored in a list '''
    
    def custdetails(self):
        self.details=[self.name,self.mail,self.phone,self.pwd]
        return self.details
    
    def login_cred(self):
        self.login=[self.mail,self.phone,self.pwd]

    '''to print the entire customer details'''

    def getdetails(self):
        info=''
        for i in self.details:
            info+=str(i)+'\n'
        return info
