# Fibonacci Rabbits

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# F(n) = F(n-1) + F(n-2)

def fibonacciRabbits(n, k):
    if type(n) != int:
        raise TypeError("n must be an int")

    if n < 3:
        return 1
    else:
        return fibonacciRabbits(n - 1, k) + fibonacciRabbits(n-2, k) * k


print(fibonacciRabbits(31, 4))
