from pytest import raises
from stack import Stack


def test_new_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()

def test_push_and_pop():
    stack = Stack()
    stack.push(0)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == 0
    assert stack.is_empty()

def test_peek():
    stack = Stack()
    assert stack.peek() is None
    stack.push(0)
    assert stack.peek() == 0
    stack.push(1)
    assert stack.peek() == 1

def test_pop_on_empty_stack():
    stack = Stack()
    with raises(RuntimeError):
        stack.pop()
