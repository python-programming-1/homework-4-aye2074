vegetables = ['carrot', 'lettuce', 'onion', 'radish']


def my_function(mylist):
    for i in range(len(mylist[0:-1])):
        print(mylist[i] + ',', end=' ')
    print('and ' + mylist[-1])
    return my_function


my_function(vegetables)
