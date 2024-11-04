





#Fucntion
def is_prime(num):

    if num <= 0:
        raise ValueError ("Numbers must be positive. ")
    elif num < 2:
        raise ValueError ("Numbers must be more than 1. ")
    elif num == 2:
        return True
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# check
print(is_prime(2))
print(is_prime(4))
print(is_prime(1))
print(is_prime(-5))

