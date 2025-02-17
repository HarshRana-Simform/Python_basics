# print(2+2)

# a :int  = input("Enter your number: ")
# print(a)

# def test(a,b):
#     '''
#     This function takes 2 agrs and prints them
#     params: 
#         a : intger  
#         b : string
#     '''
#     print(a , b)
#     print(type(a))
#     print(type(b))

# test('1.1',2)
# class Display:

#     status = 'WOH'

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #  Operator overloading to add two object's name and age 
#     def __add__(self,other):
#         name = self.name + other.name
#         age = self.age + other.age
#         new_obj = Display(name,age)

#         return new_obj 
    
#     def show(self):
#         print(self.name, self.age,sep=' ')
        

#     def display_info(self, *args, **kwargs):
#         print(f"Name: {self.name}, Age: {self.age}")
#         print(f"Additional arguments: {args}")
#         print(f"Keyword arguments: {kwargs}")

#         a,b = kwargs.items()
#         print(a[1],end=' ')
#         print(b[1])
#         print(Display.status)

#     @classmethod
#     def set_status(cls,status):
#         cls.status = status

#     @staticmethod
#     def info():
#         print('This is a static method.')

# Calling the function
# obj = Display("Harsh",10)
# obj2 = Display("Rana",11)

# obj3 = obj+obj2

# obj3.show()



# Display.set_status('Office')
# obj.display_info("Developer", "Python","Flask","Django", location="Ahmedabad", job="Engineer")
# obj2.display_info("Developer", "Python","Flask","Django", location="Ahmedabad", job="Engineer")

# obj.info()

# from threading import Thread
# from time import sleep

# class A(Thread):
    
#     def run(self):
#         for i in range(5):
#             print("Hello")
#             sleep(1)


# class B(Thread):

#     def run(self):
#         for i in range(5):
#             print('hi')
#             sleep(1)


# t1 = A()
# t2 = B()
 
# t1.start()
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()
# print("Main thread")

# Handling files using context manager
# %%
with open('Test.txt','r') as f:
    print(f.read())

print(f.closed)
# %%

# Without context manager

# f = open('Test.txt','r')

# f1 = open('new.txt','w')

# # f1.write('Hello world')
# # f1.write('Hello Nation')
# for data in f:
#     print(data)


# for i in range(500):
#     print(id(i), i)

# Map, reduce , filter and lambda function , Generator and ABC class
# from functools import reduce

# a = [2,5,3,6,7]

# m = list(map(lambda n:n*n,a))
# print(m)

# f = list(filter(lambda n:n%2==0,a))
# print(f)

# r = reduce(lambda x,y: x+y,a)
# print(r)


# def gen():
#     for i in range(10):
#         yield i

# for i in gen():
#     print(id(i))

# d = gen()
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


# a = iter([1,2,3,4,5,6])

# print(next(a))
# print(next(a))
# print(next(a))

# from abc import ABC,abstractmethod

# class Abstract(ABC):

#     @abstractmethod
#     def sum(self):
#         pass

# class MyClass(Abstract):

#     def sum(self):
#         print("Overriding sum")
    
#     def run(self):
#         print("Hello from run")

# # obj = Abstract()
# obj = MyClass()

# obj.sum()
# obj.run()

# # Custom map function
# def my_map(fun,arg_list):

#     result = []

#     for i in arg_list:
#         result.append(fun(i))

#     return result

# def square(n):
#     return n*n

# squares = my_map(lambda n:n*n,[1,2,3,4,5])
# squares = my_map(square,[1,2,3,4,5])
# cubes = my_map(lambda n:n*n*n,[1,2,3,4,5])
# print(squares)
# print(cubes)

#Decorator

# def decorator_function(original_function):
#     '''
#     This is a decorator that calculates the time it takes to run the original function
#     '''
#     import time

#     def wrapper(*args,**kwargs):
#         t1 = time.time()
#         result = original_function(*args,**kwargs)
#         t2 = time.time()-t1
#         print('The {} function took {} sec to run'.format(original_function.__name__,t2))
#         return result
#     return wrapper

# import time

# @decorator_function
# def display(name,age):
#     time.sleep(1)
#     print('The person\'s name is {} and age is {}'.format(name,age))


# display('Harsh',21)

# def decorator_function(original_function):
#     '''
#     This is a decorator that prints additional info about from the original function
#     '''

#     def wrapper(*args,**kwargs):
#         if(len(args)>2):
#             original_function(*args,**kwargs)
#             print('Their work location is {}'.format(args[2]))
#         else:
#             print('The work location is a required param after the last update.')
#     return wrapper

# @decorator_function
# def display(*args):
#     print('The person\'s name is {} and age is {}'.format(args[0],args[1]))


# display('Harsh',21,'Ahmedabad')


# Multiple Inheritance calling the method out-off order of MRO. 

# class A:
#     def display(self):
#         print('A')

    
# class B:
#     def display(self):
#         print('B')

# class D:
#     def display(self):
#         print('D')        


# class C(B,A,D):
#     def display(self):
#         return super(B,self).display()

# obj = C()

# obj.display()
