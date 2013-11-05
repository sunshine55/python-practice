def outputFizzBuzz(numbers=range(1, 101)):
    result = []
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 5 == 0:
            result.append('Buzz')
        elif i % 3 == 0:
            result.append('Fizz')
        else:
            result.append(i)
    return result