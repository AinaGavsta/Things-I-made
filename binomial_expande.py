#Program built cause i was lazy in maths classes. Made a factorial function as micropython doesn't support math.factorial. 
def factorial(n):
    if n < 0:
        return 'bad'
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

exponent_bracket=int(input(f'Enter the exponent of the bracket'))
#uses elementary algebra formula to find coefficient of the binomial expansion
for x in range(exponent_bracket+1):
    print((factorial(exponent_bracket))/((factorial(x))*(factorial((exponent_bracket-x)))))
#eventually maybe add multiplication of the coefficient and the other nomial (is that a word?) to find just the letters by themselves
