def is_prime(function):
    def wrapper(a,b,c):
        res_f = function(a,b,c)
        if res_f < 2:
            return res_f
        for number in range(2, res_f):
            if res_f % number == 0:
                print("Составное")
                return res_f
        print("Простое")
        return res_f

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c



result = sum_three(2, 3, 6)

print(result)