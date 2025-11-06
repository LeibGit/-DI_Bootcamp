user_number = int(input("Input a number: "))

def check_prime(n):
    if n <= 1:
        print("Not prime")
        return

    for i in range(2, int(n ** 5) + 1):
        if n % i == 0:
            print('Not prime')
            return
    print("prime")
        
check_prime()