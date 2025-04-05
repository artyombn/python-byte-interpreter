from __future__ import print_function
from . import vmtest


class TestBinaryOp(vmtest.VmTestCase):
    def test_binary_operations(self):
        self.assert_ok("""
        a = 10
        b = 3

        assert a + b == 13
        assert a - b == 7
        assert a * b == 30
        assert a // b == 3
        assert a % b == 1
        assert a & b == 2
        assert a | b == 11
        assert a ^ b == 9
        assert a << b == 80
        assert a >> b == 1
        assert a ** b == 1000
        """)
