while True:
    numerator = int(input("Enter the numerator a: "))
    denominator = int(input("Enter the denominator b: "))

    try:
        result = numerator/denominator
        print(result)
    except:
        print("ZeroDivisionError: division by zero")
