from pytest import raises
from queue import Queue


def test_new_queue_is_empty():
    queue = Queue()
    assert queue.is_empty()

def test_enqueue_and_dequeue():
    queue = Queue()
    queue.enqueue(0)
    queue.enqueue(1)
    assert queue.dequeue() == 0
    assert queue.dequeue() == 1
    assert queue.is_empty()

def test_peek():
    queue = Queue()
    assert queue.peek() is None
    queue.enqueue(0)
    assert queue.peek() == 0
    queue.enqueue(1)
    assert queue.peek() == 0

def test_dequeue_empty_queue():
    queue = Queue()
    with raises(RuntimeError):
        queue.dequeue()
