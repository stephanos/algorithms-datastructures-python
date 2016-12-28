from map import Map

def test_set_and_get():
    hashmap = Map()
    hashmap[0] = 'A'
    hashmap[1] = 'B'
    assert hashmap[0] == 'A'
    assert hashmap[1] == 'B'

def test_replace():
    hashmap = Map()
    hashmap[0] = 'A'
    hashmap[0] = 'B'
    assert hashmap[0] == 'B'

def test_collision():
    hashmap = Map(size=2)
    hashmap[0] = 'A'
    hashmap[2] = 'B'
    assert hashmap[0] == 'A'
    assert hashmap[2] == 'B'

def test_replace_collision():
    hashmap = Map()
    hashmap[0] = 'A'
    hashmap[2] = 'B'
    hashmap[2] = 'C'
    assert hashmap[2] == 'C'
