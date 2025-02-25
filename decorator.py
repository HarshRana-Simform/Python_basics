# Decorator
import time

def decorator_function(original_function):
    '''
    This is a decorator that calculates the time it takes to run the original function
    '''

    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = original_function(*args,**kwargs)
        t2 = time.time()-t1
        print('The {} function took {} sec to run'.format(original_function.__name__,t2))
        return result
    return wrapper


@decorator_function
def display(name,age):
    time.sleep(2)
    print('The person\'s name is {} and age is {}'.format(name,age))


display('Harsh',21)


# def decorator_function(original_function):
#     '''
#     This is a decorator that prints additional info about the original function
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

