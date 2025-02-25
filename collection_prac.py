from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = (1,2,2,3,3,3,3,4,2,3)
c = Counter(a)
print(c.most_common(3)[0][0])
i = c.items()
print(list(i))
i = c.elements() #returns a iterator
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

print(list(c.elements()))

Coordinate = namedtuple('Coordinate','x,y')
loc = Coordinate(2,-2)
print(loc)
print(loc.x , loc.y)


# OrderedDict -> remembers the insertion order 
# In newer python versions --3.7 the built-in dictionary also has this ability, thus this are used less and less.


#for the values that don't exists it returns a default value for that data type.
d = defaultdict(float)
d[1]= 'a'
d[2]= 'b'
print(d[4])


q = deque()

q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4)
print(q)

q.extendleft([5,6,7])
print(q)


print(q.pop())
print(q.popleft())
print(q)

q.rotate(2)
print(q)

q.rotate(-1)
print(q)