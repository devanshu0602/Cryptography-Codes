def get_equations(total_equations):
    equations = []
    a_values, m_values = [], []
    # Get the a and m values input
    for i in range(1, total_equations + 1):
        # a values
        a = input(f"\na{i} = ")
        a_values.append(int(a))
        # m values
        m = input(f"m{i} = ")
        m_values.append(int(m))
        # Equation for x
        x = a + " mod " + m
        equations.append(x)
        print(f"\tEq{i} => x : {x}")
    # Return all inputs
    return a_values, m_values, equations


def get_M_value(m_values):
    # Find M (M = m1 * m2 * ... * mn)
    M = 1
    for m in m_values:
        M = M * m
    return M


def get_z_values(M, m_values):
    z_values = []
    # zi = M / mi
    for i in range(len(m_values)):
        z = int(M / m_values[i])
        print(f"   z{i + 1} = {M} / {m_values[i]} = {z}")
        z_values.append(z)
    return z_values


def get_y_values(z_values, m_values):
    y_values = []
    # (zi * yi) mod mi = 1
    for i in range(len(z_values)):
        y = 1
        while (((z_values[i] * y) % m_values[i]) != 1):
            y = y + 1
        print(f"   y{i + 1} : ({z_values[i]} * y{i + 1}) mod {m_values[i]}", end="")
        print(f" => y{i + 1} = {y}")
        y_values.append(y)
    return y_values


def find_x(a_values, z_values, y_values, M):
    total = 0
    # Find sum of product of a, z, y
    print("   x = (", end="")
    for i in range(len(a_values)):
        if (i == len(a_values) - 1):
            print(f"({a_values[i]}*{z_values[i]}*{y_values[i]})", end="")    
        else:
            print(f"({a_values[i]}*{z_values[i]}*{y_values[i]}) + ", end="")
        prod = a_values[i] * z_values[i] * y_values[i]
        total = total + prod
    print(f") mod {M}")
    # Find the actual value of x -> The Answer
    x = total % M
    return x


print("\n\n### CHINESE REMAINDER THEOREM ###\n\n")
# Get the number of equations
num_of_equations = int(input("Enter the number of equations -> "))
# Get the equations
print("\n\n--> Enter the equations:")
a_values, m_values, equations = get_equations(total_equations=num_of_equations)
# M = Product of all m values
print("\n\n-> M = m1 * m2 * ... * mn")
M = get_M_value(m_values=m_values)
print(f"   M = {M}")
# Find z-values
print("\n\n-> Z-values : zi = M / mi")
z_values = get_z_values(M=M, m_values=m_values)
# Find y-values
print("\n\n-> Y-values : (zi * yi) mod mi = 1")
y_values = get_y_values(z_values=z_values, m_values=m_values)
# Find x -> sum(ai * yi * zi) mod M
print("\n\n-> Value of x : x = ((a1*z1*y1) + ... + (ai*zi*yi)) mod M")
x = find_x(a_values=a_values, z_values=z_values, y_values=y_values, M=M)
print(f"   x = {x}")
# Result
print(f"\n\n=> The value of X is {x}")
# Footer
print("\n\nDevanshu Gupta 21BCE0597\n\n")