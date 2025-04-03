import dis

def add(a, b):
    return a + b

bytecode = add.__code__.co_code
print(f"Actual bytecode {bytecode} and it's disaasembly\n")
dis.dis(add)