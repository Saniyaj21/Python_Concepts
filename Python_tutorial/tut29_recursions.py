#  factorial using recursion

def fact(n):
    """
    factorial of 5 = 5 * 4 * 3 * 2 * 1 
    formola : n! = n * n-1 * n-2 *....1
    """
    if n == 1:  # base condition for recursion
        return 1
    else:
        return n*(fact((n-1)))


#  factorial using itration
def fact2(n):
    fact_result = 1
    for i in range(n):
        fact_result = fact_result * (i+1)
    return fact_result


number = 5
print(fact(number))    
print(fact2(number))   


# fibonachi number
def febonachi(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return febonachi(n-1)+febonachi(n-2)

print(febonachi(5))