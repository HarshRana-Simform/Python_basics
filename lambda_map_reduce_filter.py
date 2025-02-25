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

# from functools import reduce

# a = [2,5,3,6,7]

# m = list(map(lambda n:n*n,a))
# print(m)

# f = list(filter(lambda n:n%2==0,a))
# print(f)

# r = reduce(lambda x,y: x+y,a)
# print(r)