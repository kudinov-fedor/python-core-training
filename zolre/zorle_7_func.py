'''
1.Create function which gets value from global variable.
2.Create function which changes value in global variable.
'''

if __name__ == '__main__':
    x = 111

#1.
def func_zorle():
    global x
    print('global=', x)
    x = 123
    print('local=',x)

func_zorle()


#2.
def func_zorle():
    global x
    x = 123
    print('local become global=',x)

func_zorle()
print ('so global=', x)

