# create multple objects
# Can have inheritance
# operator overloading

class Account1:
    def adduser(self, n):
        self.name = n

    def viewuser(self):
        return self.name

    bank = 'ICICI'

    @classmethod
    def bankrules(cls, area):
        return 'Bank Rules ' + area
    
    @staticmethod
    def bankinfo():
        return 'Bank Info'
    
    def __init__(self):
        print('SB Logic here')


cust1 = Account1()
cust2 = Account1()

cust1.adduser('Dawn')
cust2.adduser('C2')

print(cust1.viewuser())
print(cust2.viewuser())
print(Account1.bank)
print(cust1.name)
print(Account1.bankrules('BLR'))
print(Account1.bankinfo())

print(Account1.viewuser(cust1))

# self is used to pass the instance of the object so that python knows which variable o call
# methods having the instances of the data these variablea are known as insance methods
# self.name is used to keep the varaible in each and every instances -> thus this is know as instance variables
# Account1 is the class object here, there is only one class object with the class name
# two types of object -> instance object -> class object(only 1)
line = '-'*40
print(line)

class Account2(Account1):
    def addadhar(self, a):
        self.adhar = a
    
    def viewadhar(self):
        return self.adhar
   
    def viewuser(self):
        return 'Welcome '+self.name

    def __init__(self):
        super().__init__()
        Account1.__init__(self)
        print('CA LOGIC HERE') 


cust3 = Account2()
cust3.adduser('c3')

print(cust3.viewuser())
print(Account2.bank)
print(Account2.bankrules('CHN'))
print(Account2.bankinfo())
cust3.addadhar('Ai')
print(cust3.viewadhar())
print(line)

class RBI:
    def viewrules(self):
        return 'RBI Rules'


class Account3(Account2, RBI):
    pass


cust4 = Account3()
print(cust4.viewrules())
print(line)


class Govt:
    def viewrules(self):
        return 'Govt rules'


class Account4(Account3, Govt):
    pass


cust5 = Account4()
print(cust5.viewrules())
print(Govt.viewrules(cust5))
print(line)

class Account5(Account3):
    def __init__(self):
        self.gov = Govt()


cust6 = Account5()
print(cust6.viewrules())
print(cust6.gov.viewrules())


class Account6:
    def __init__(self, n):
        self.name = n

    def __add__(self, x):
        return self.name + x.name


cust7 = Account6('abc')
cust8 = Account6('xyz')

result = cust7 + cust8
print('result =', result)

print('cust7 =', cust7)