def otp_generator():
    import random
    numbers = [i for i in range(0,10)]
    otp = [random.choice(numbers) for i in range(0,6)]
    otp = ''.join(str(i) for i in otp)
    return otp

print(otp_generator())