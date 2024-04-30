<a class="anchor" id="overview_of_built-in_sequences"></a>

## Overview of Built-In Sequences

The `list` type is flexible and easy to use, but depending on specific requirements, there are better options. For example, an `array` saves a lot of memory when you need to handle millions of floating-point values (arrays will be discussed later in details). On the other hand, if you are constantly adding and removing items from opposite ends of a list, it’s good to know that a `deque` (double-ended queue) is a more efficient FIFO14 data structure.

The standard library offers a rich selection of sequence types implemented in C:

- Container sequences
> Can hold items of different types, including nested containers. Some examples: `list`, `tuple`, and `collections.deque`.

- Flat sequences
> Hold items of one simple type. Some examples: `str`, `bytes`, and `array.array`.

A **container sequence** holds references to the objects it contains, which may be of any type, while a **flat sequence** stores the value of its contents in its own memory space, not as distinct Python objects. See Figure 2-1.
<img src="/Users/rhedayati/workspace/GitHub_Repositories/rhedayati/learningProgrammingNotes/images/array_list.png"/>

Thus, `flat` sequences are more compact, but they are limited to holding primitive machine values like bytes, integers, and floats.

#### list vs linked list 
  - List and linked list are both types of container-based data structures, organized as sequences, where each element contains a pointer to its data (the memory address of the data value).
  - Accessing elements in a list is generally quicker than in a linked list because of how the data is stored. 
  - Additionally, searching for data in a list has a time complexity of O(1), while in a linked list, it's O(n)



#### flat sequence vs container sequence 
- Flat-based sequences store the actual data values rather than pointers, with strings serving as an example of such a sequence. 
- Advantages of flat sequences over container sequences include faster reading and finding of data due to the absence of the need to navigate to different RAM units, and they're more efficient for caching tasks. 
- Both types of sequences have a linear time complexity (O(N)) as data increases, but flat sequences start with a smaller initial size. 
- Flat sequence use cache better than container sequence While container sequences can accommodate various data types, flat sequences require all data types to be the same.
- Moreover, flat sequences utilize caching more effectively since they only store the value itself rather than a pointer to it.


<a class="anchor" id="arrays"></a>

## Arrays

If a list only contains numbers, an `array.array` is a more efficient replacement. Arrays support all mutable sequence operations (including `.pop`, `.insert`, and `.extend`), as well as additional methods for fast loading and saving, such as `.frombytes` and `.tofile`.

Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character. The following type codes are defined:

| Type code| C Type| Python Type| Minimum size in bytes|
|:-- |:-- |:-- |:-- |
| `'b'` | signed char | int | 1 |
| `'B'`| unsigned char| int| 1 |
| `'u'` | wchar_t | Unicode character | 2 |
| `'h'` | signed short | int | 2 |
| `'H'` | unsigned short | int | 2 |
| `'i'` | signed int | int | 2 |
| `'I'` | unsigned int | int | 2 |
| `'l'` | signed long | int | 4 |
| `'L'` | unsigned long | int | 4 |
| `'q'` | signed long long | int | 8 |
| `'Q'` | unsigned long long | int | 8 |
| `'f'` | float | float | 4 |
| `'d'` | double | float | 8 |


```python
from array import array
from random import random

floats = array('d', (random() for i in range(1000)))
floats[-1]
--- ans ---
0.09549897660590423
```
```python
with open('floats.bin', 'wb') as f:
    floats.tofile(f)

floats_2 = array('d')

with open('floats.bin', 'rb') as f:
    floats_2.fromfile(f, 10**7)

# Verify that the contents of the arrays match.
floats_2[-1]

--- ans ---
0.09549897660590423
```

As you can see, `array.tofile` and `array.fromfile` are easy to use. If you try the example, you’ll notice they are also very fast. A quick experiment shows that it takes about 0.1 seconds for `array.fromfile` to load 10 million double-precision floats from a binary file created with `array.tofile`. That is nearly **60 times faster than reading the numbers from a text file**, which also involves parsing each line with the float built-in. Saving with `array.tofile` is about **seven times faster than writing one float per line in a text file**. In addition, the size of the binary file with 10 million doubles is **80,000,000 bytes (8 bytes per double, zero overhead), while the text file has 181,515,739 bytes for the same data**.


<a class="anchor" id="memory_views"></a>

### Memory Views
A `memoryview` is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLlite data-bases, NumPy arrays, etc.) without first copying. This is very important for large data sets.

The built-in `memoryview` class is a shared-memory sequence type that lets you handle slices of arrays without copying bytes. It was inspired by the NumPy library (which we’ll discuss shortly in “NumPy”). Travis Oliphant, lead author of [NumPy](https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/ch02.html#numpy_sec), answers the question, [“When should a memoryview be used?”](https://fpy.li/2-17) like this:

> A `memoryview` is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLite databases, NumPy arrays, etc.) without first copying. This is very important for large data sets.

Using notation similar to the `array` module, the `memoryview.cast` method lets you change the way multiple bytes are read or written as units without moving bits around. `memoryview.cast` returns yet another `memoryview` object, always sharing the same memory.
Please note that if you use ‍‍‍‍‍‍‍`fromfile`, you should know what is the array type because this method will consider the saved array file to read it and put it in new value. If the saved variable is different from the saved file type. The value would be wrong. 