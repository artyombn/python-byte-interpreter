from byterun.pyvm2 import VirtualMachine

with open("main.py", "r") as f:
    source = f.read()

code = compile(source, filename="main.py", mode="exec")

vm = VirtualMachine()
vm.run_code(code)