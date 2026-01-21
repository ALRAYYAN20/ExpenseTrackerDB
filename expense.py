'''
# create employee class and enter id and salary and display who has higher salary

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
        
emp1 = Employee(1, 35000)
emp2 = Employee(2, 40000)

#comparing salary
if emp1.salary > emp2.salary:
    print('Emp1 has higher salary')
    
elif emp2.salary > emp1.salary:
    print('Emp2 has higher salary')
    
else:
    print('Both have equal salary')

- - THIS IS EXAMPLE CODE I LEARNED FROM PYTHON COURSE - - 
    
'''
class Expense:
    def __init__(self, name, amount, category, id=None) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f'<Expense #{self.id}: {self.name}, ₹{self.amount:.2f}, {self.category}>'


'''
class Expense:

    def __init__(self, name, amount, category, id=None)->None:
        self.id = id
        self.name = name 
        self.amount = amount
        self.category = category



# now the output without below code will look like this : <expense.Expense object at 0x000001E619C06B70>
# to avoid this and get data as a string , we will use a default function called __repr__ stands for representation 
    def __repr__(self):
        return f'< Expense:{self.id}, {self.name} , ₹{self.amount:.2f} , {self.category} >'                                                             
    '''