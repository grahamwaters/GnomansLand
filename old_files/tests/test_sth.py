'''
Doc string
'''

import os
import typing

from module_example import demo_variable_imported_from_module

print(demo_variable_imported_from_module)


class MyClass:
    x = 5


p1: MyClass = MyClass()
print(p1.x)

#
x: int = 1


def test_1() -> None:
    assert 1 == 1


def test_2() -> None:
    assert demo_variable_imported_from_module == "Hello! I come from the module 'module_example.py'"
