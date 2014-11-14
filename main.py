from stack import *
from queue1 import *
from recursion import *
from fibonacci import *

# stack
food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')
print('1st off the Stack: {0}'.format(food.pop()))

food = Queue1()
food.enqueue('steak')
food.enqueue('bourbon')
print('1st off the Queue: {0}'.format(food.dequeue()))
print('2nd off the Queue: {0}'.format(food.dequeue()))


print(factorial(5))
print('Factorial({0}) = {1}'.format(5, factorial(5)))

# .format(arg, )
for x in range(20):
    print('fibinacci({0}) = {1}'.format(x, fibinacci(x)))



x = 42