import dis

def add(a, b):
    return a + b

bytecode = add.__code__.co_code
print(f"Actual bytecode {bytecode} and it's disaasembly\n")
# dis.dis(add)

print(dis.opname[125])

# for i in dis.opname:
#     print(i)

def func_dis(y):
    count = []
    for i in y:
        count.append(i)
    return count

print(f"---------------------------")
# dis.dis(func_dis)


print(f"---------------------------")
def func1(y):
    z = y + 3
    return z

def func2():
    a = 1
    b = 2
    return a + func1(b)

func2()

dis.dis(func2)
