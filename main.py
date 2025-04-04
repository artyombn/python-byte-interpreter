import dis

def add(a, b):
    return a + b

dis.dis(add)

print(f"-----------------")
print((dis.opmap.get("RESUME")))
print((dis.opname[151]))
