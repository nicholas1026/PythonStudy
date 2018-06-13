#!/usr/bin/python

motorycycles = ['honda','yamaha','suzuki']

print(motorycycles)

motorycycles[0] = 'ducati'

print(motorycycles)

motorycycles.append('cherry')

print(motorycycles)

motorycycles.insert(3,'audi')

print(motorycycles)

del motorycycles[2]

print(motorycycles)

popped_motorcycles = motorycycles.pop()
print(motorycycles)
print(popped_motorcycles)

motorycycles.pop(0)
print(motorycycles)

motorycycles = ['honda','yamaha','suzuki']
motorycycles.remove('yamaha') //remove()仅能删除第一个指定的值
print(motorycycles)
