
# lists
def lists():
    xs = [3, 1, 2]
    print(xs, xs[2])
    print(xs[-1])  # prints "2"
    xs[2] = 'foo'
    print(xs)  # [3, 1, 'foo']
    xs.append('bar')
    print(xs)  # [3, 1, 'foo', 'bar']
    x = xs.pop()
    print(xs)  # [3, 1, 'foo']

    # slicing
    nums = range(5)
    print(nums)  # [0, 1, 2, 3, 4]
    print(nums[2:4])  # [2, 3]
    print(nums[2:])  # [2, 3, 4]
    print(nums[:2])  # [0, 1]
    print(nums[:])  # [0, 1, 2, 3, 4]
    print(nums[:-1])  # [0, 1, 2, 3]
    nums[2:4] = [8, 9]
    print(nums)  # [0, 1, 8, 9, 4]

    # loops
    animals = ['cat', 'dog', 'monkey']
    for animal in animals:
        print(animal)
    
    for idx, animal in enumerate(animals):
        print("#%d: %s" %(idx + 1, animal))
        # "#1: cat", "#2: dog", "#3: monkey"
    
    # list comprehensions
    nums = [0, 1, 2, 3, 4]
    squares = []
    for x in nums:
        squares.append(x ** 2)
    print(squares)  # [0, 1, 4, 9, 16]

    squares = [x ** 2 for x in nums]
    print(squares)
    even_squares = [x ** 2 for x in nums if x % 2 == 0]
    print(even_squares)  # [0, 4, 16]


# dictionaries
def dicts():
    d = {'cat': 'cute', 'dog': 'furry'}
    print(d['cat'])
    print('cat' in d)  # True
    d['fish'] = 'wet'
    print(d['fish'])
    # print(d['monkey'])  # KeyError: 'monkey' not a key of d
    print(d.get('monkey', 'N/A'))  # Get an element with a default, prints "N/A"
    print(d.get('fish', 'N/A'))  # prints "wet"
    del d['fish']
    print(d.get('fish', 'N/A'))  # prints "N/A"

    # loops
    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal in d:
        legs = d[animal]
        print('A %s has %d legs' % (animal, legs))
    
    for animal, legs in d.iteritems():
        print('A %s has %d legs' % (animal, legs))

    # dict comprehensions
    nums = [0, 1, 2, 3, 4]
    even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
    print(even_num_to_square)  # {0: 0, 2: 4, 4: 16}


# sets
def sets():
    animals = {'cat', 'dog'}
    print('cat' in animals)
    print('fish' in animals)
    animals.add('fish')
    print('fish' in animals)
    print(len(animals))  # 3
    animals.add('cat')
    print(len(animals))  # 3
    animals.remove('cat')
    print(len(animals))  # 2

    # loops
    animals = {'cat', 'dog', 'fish'}  
    for idx, animal in enumerate(animals):  # NOTE: order is not guaranteed
        print('#%d: %s' % (idx + 1， animal))
        # "#1: fish", "#2: dog", "#3: cat"

    # dict comprehensions
    from math import sqrt
    nums = {int(sqrt(x)) for x in range(30)}
    print(nums)  # prints "set([0, 1, 2, 3, 4,5])"


# tuples
def tuples():
    # tuples vs lists: tuples can be used as key in dict and 
    # element in set, while lists cannot
    d = {(x, x + 1): x for x in range(10)}
    print(d)
    t = (5, 6)
    print(type(t))  # Prints "<type 'tuple'>"
    print(d[t])  # 5
    print(d[(1, 2)])  # 1
