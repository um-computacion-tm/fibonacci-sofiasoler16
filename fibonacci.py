import unittest


def fibonacciiter(number):
    fibonacci_number = [0, 1]
    total = 1
    print("number " + str(number))
    for index in range (2, number+1):
        total = (
            fibonacci_number[-2] + 
            fibonacci_number[-1]
        )
        fibonacci_number.append(total)
        print("fibonacci_number " + str(fibonacci_number))
        print("total" + str(total))
    print (total)
    fibonacci_number.pop(5)
    return fibonacci_number


if __name__ == "__main__":
    unittest.main()