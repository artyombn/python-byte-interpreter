# Python Byte Interpreter
**Byterun** modernized version - Python interpreter adapted to support the stable Python version (3.12)

#### To be capable with Python 3.12 some updates include:
- New and updated operations and their handlers: for ex. `BINARY_OPERATIONS`, `UNARY_OPERATORS`, `COMPARE_OPERATORS`
- Support for modern opcodes: `RESUME`, `CACHE`, `PUSH_NULL`
- Improved Stack and Frame management

## Usage

To run a Python script (e.g., `main.py`) using this interpreter, use the provided `run_main_with_byterun.py`:
```shell
python run_main_with_byterun.py
```

Example content of `run_main_with_byterun.py`:
```python
from byterun.pyvm2 import VirtualMachine

with open("main.py", "r") as f:
    source = f.read()

code = compile(source, filename="main.py", mode="exec")
vm = VirtualMachine()
vm.run_code(code)
```

### Debug Mode
The interpreter supports a debug mode for detailed execution logging.  
By default, debug mode is disabled to match standard Python behavior (no output on successful execution).

**Enable Debug Mode:** use `debug=True` when creating VM instance:
```python
vm = VirtualMachine(debug=True)
vm.run_code(code)
```
_This will output detailed logs about bytecode parsing, stack state, and frame execution._  

**Disable Debug Mode**:
```python
vm = VirtualMachine(debug=False)  # Default
vm.run_code(code)
```


## Running Tests
The project includes tests for BINARY operations. Use pytest to run it:
```shell
pytest tests/test_binary_op.py -v
```

## Known Issues/Changes in Python 3.12.2
**COMPARE_OP in Python 3.12.2:**
* There is a known issue with `dis.cmp_op` tuple in Python 3.12.2, where comparison operators are limited to ('<', '<=', '==', '!=', '>', '>='). This is tracked in [CPython Issue #117270](https://github.com/python/cpython/issues/117270)  

> .. versionchanged:: 3.12 The cmp_op index is now stored in the four highest bits of oparg instead of the four lowest bits of oparg. This change required adjustments in the interpreter's handling of COMPARE_OP (see parse_byte_and_args for the bit-shifting fix: intArg = intArg >> 4)

* The interpreter has been updated to correctly handle this behavior  


## Resources:  
[Original Project: GitHub - Byterun](https://github.com/nedbat/byterun)  
[Article: A Python Interpreter Written in Python](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)  










