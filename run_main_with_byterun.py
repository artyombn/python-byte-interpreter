import dis

from byterun.pyvm2 import VirtualMachine

with open("main.py", "r") as f:
    source = f.read()

code = compile(source, filename="main.py", mode="exec")
# dis.dis(code, show_caches=True)
# print(list(code.co_code))

"""
  0           0 RESUME                   0

  1           2 LOAD_CONST               0 (<code object add at 0x104153910, file "main.py", line 1>)
              4 MAKE_FUNCTION            0
              6 STORE_NAME               0 (add)

  4           8 PUSH_NULL
             10 LOAD_NAME                1 (print)
             12 PUSH_NULL
             14 LOAD_NAME                0 (add)
             16 LOAD_CONST               1 (2)
             18 LOAD_CONST               2 (3)
             20 CALL                     2
             22 CACHE                    0 (counter: 0)
             24 CACHE                    0 (func_version: 0)
             26 CACHE                    0
             28 CALL                     1
             30 CACHE                    0 (counter: 0)
             32 CACHE                    0 (func_version: 0)
             34 CACHE                    0
             36 POP_TOP
             38 RETURN_CONST             3 (None)

Disassembly of <code object add at 0x104153910, file "main.py", line 1>:
  1           0 RESUME                   0

  2           2 LOAD_FAST                0 (a)
              4 LOAD_FAST                1 (b)
              6 BINARY_OP                0 (+)
              8 CACHE                    0 (counter: 0)
             10 RETURN_VALUE
[151, 0, 100, 0, 132, 0, 90, 0, 2, 0, 101, 1, 2, 0, 101, 0, 100, 1, 100, 2, 171, 2, 0, 0, 0, 0, 0, 0, 171, 1, 0, 0, 0, 0, 0, 0, 1, 0, 121, 3]
"""

vm = VirtualMachine()
vm.run_code(code)