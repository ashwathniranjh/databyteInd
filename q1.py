def fizzBuzz():
    i = 1;
    while( i <= 100):
        if i%15 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        i = i+1
        
fizzBuzz()
