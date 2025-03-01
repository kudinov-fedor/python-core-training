def my_generator():
    print("Step 1")
    yield 'Assign ticket'
    print("Step 2")
    yield 'Test the functionality'
    print("Step 3")
    yield 'Leave a comment'
    print('Step 4')
    yield 'Move ticket'
    return 'End of interation'


gen = my_generator()
next(gen)
next(gen)
next(gen)
next(gen)
try:
    next(gen)
except StopIteration:
    print('Done')
try:
    next(gen)
except NameError:
    print(5 + 5)
else:
    print('It`s a Name Error')
finally:
    print('Another Stop Iteration')
