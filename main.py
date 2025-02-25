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


# class C(A,B,D):
#     def display(self):
#         return super(A,self).display()

# obj = C()

# D.display(obj)

# Multi-processing Practice
# import multiprocessing
# import time

# def worker(i):
#     print(f'Worker {i} Started Working!')
#     time.sleep(3)
#     print(f'Worker {i} ended work!')

# def apply_multiprocess():
#     processes = []
#     for i in range(1,11):
#         p = multiprocessing.Process(target=worker, args=[i])
#         p.start()
#         processes.append(p)

#     print('All processes have finished their work!')

# if __name__ == '__main__':
#     apply_multiprocess()
