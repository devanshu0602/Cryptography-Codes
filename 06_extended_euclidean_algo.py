def find_gcd(a, b):
    print(f"   = GCD({a}, {b})")
    # Edge cases
    if a == 0 or a == b: 
        return b
    # Using recursion to find answer
    return find_gcd(b % a, a)


def extended_euclidean_algo(a, b, gcd):
    # Find x and y recursively
    if a == 0:
        return 0, 1
    x1, y1 = extended_euclidean_algo(b % a, a, gcd)
    # Update x and y from the results
    x = y1 - (b // a) * x1
    y = x1
    print(f"   {gcd} = {a} * ({x}) + {b} * ({y})")
    # Return the results
    return x, y 
    

print("\n\n### EXTENDED EUCLIDEAN ALGORITHM ###\n\n")
# Get the two numbers
print("-> Enter the values:")
num1 = int(input("   Number 1 = "))
num2 = int(input("   Number 2 = "))
# Assign lower value to a and larger to b
if num1 < num2: a, b = num1, num2
else: a, b = num2, num1
# Find the GCD
print(f"\n-> GCD of {a} and {b}:")
gcd_value = find_gcd(a=a, b=b)
print(f"   => GCD({a}, {b}) = {gcd_value}")
# Find equation -> gcd value = (a * x) + (b * y)
print("\n-> Linear equation: ", end="")
print(f"{gcd_value} = ({a} * x) + ({b} * y)")
x, y = extended_euclidean_algo(a=a, b=b, gcd=gcd_value)
# Result
print(f"\n\n==> Equation: {gcd_value} = ({a} * x) + ({b} * y)")
print(f"    Value of x = {x}")
print(f"    Value of y = {y}")
# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")