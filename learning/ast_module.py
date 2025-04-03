import ast
import dis
source = 'sum([1, 2, 3]) + 42'
# https://docs.python.org/3.9/library/parser.html
# import parser
# st = parser.suite(source)
# print(parser.st2list(st), end="\n\n")
node = ast.parse(source, mode='eval')
print(ast.dump(node), end="\n\n")
codeobj = compile(node, '<string>', mode='eval')
dis.disassemble(codeobj)
print(eval(codeobj))