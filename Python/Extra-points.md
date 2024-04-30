- `False` in python are (it can be used as a logical statement in functions): 
    - `None`
    - ``
    - `False`
    - $0$
    - `empty list/set/dictionary/tuple`

- `list()`: creating a list from `string` or other data structures.

- `lambda`: In Python, a lambda function is a special type of function without the function name.
    
   ```python
   #lambda argument(s): expression
   #lambda argument(s): output
   
   #Normal python function
    def a_name(x):
        return x+x
        
    #Lambda function
    lambda x: x+x
   ```
   
   ```python
   
   sorted(my_points, key=lamda p:p.x) #sort the points class based on the x not euclidean distance
   ```


- `map()`: The map() function in Python is used to apply a specified function to each item in an iterable (such as a list, tuple, or string) and return an iterator that yields the results.

   ```python
    #map(function, iterable)
   
    def square(x):
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)

    print(list(squared_numbers))
   ```



- `zip()`: The zip() function in Python is used to combine elements from multiple iterables (such as lists, tuples, or strings) into a single iterator of tuples.

    ```python
    
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']
    result = zip(numbers, letters)
    result = list(result)
    print(result)
    
    ---- ANS ----
    [(1, 'a'), (2, 'b'), (3, 'c')]
    
    ```

- `join()` function


- `filter()`: This is a Python inbuilt library that returns only those values that fit certain criteria. The filter() function in Python is used to create an iterator from elements of an iterable (such as a list, tuple, or string) that satisfy a specified condition. 

    
    
    ```python
    #filter(function, iterable)
    
    list_1 = [1,2,3,4,5,6,7,8,9]
    filter(lambda x: x%2==0, list_1)
    
    ### Results
    <filter at 0xf378982348>
    list(filter(lambda x: x%2==0, list_1))
    
    ###Results
    [2, 4, 6, 8]
    ```

- `itertools`:

- `dir()`: gives the methods and attributes of an object

- Some useful attributes of classes:
    - `__class__`: return the class of the object
    - `__name__`: return the class name as a string
    
    
    
<a class="anchor" id="String Methods"></a>
## String Methods
`string`: library provides a great tools to work on strings such as: 

|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`capitalize()`|	`'foO BaR BAZ quX'.capitalize()`	|`'Foo bar baz qux'`| Capitalizes the target string. |
|`lower()`|	`'HelloARI'.lower()`	|`helloari`| Convert alphabatic to lowercase |
|`upper()`|	`'HelloAri'.upper()`	|`HELLOARI`| Convert alphabetic to uppercase |
|`swapcase()`|	`'HeLLo'.swapcase()`	|`hEllO`| Swaps case of alphabetic characters (lower <-> upper). |
|`title()`|	`'the sun arise'.title()`	|`The Sun Arise`| the first letter of each word is converted to uppercase and remaining letters are lowercase |
|``count(<sub>[, <start>[, <end>]])``|	`'foo goo moo'.count('oo', 0, 8)`	|`2`| Counts occurrences of a substring in the target string. |
|`endswith(<suffix>[, <start>[, <end>]])`|	`'foobar'.endswith('bar')`	|`True`|Determines whether the target string ends with a given substring.|
|`find(<sub>[, <start>[, <end>]])`|	`'foo bar foo baz foo qux'.find('foo')`	|`0`| Searches the target string for a given substring.|
|`index(<sub>[, <start>[, <end>]])`|	`'foo bar foo baz foo qux'.index('grault')`	|`substring not found`| Searches the target string for a given substring. |
|`rfind(<sub>[, <start>[, <end>]])`|	`'foo bar foo baz foo qux'.rfind('foo')`	|`16`|Searches the target string for a given substring starting at the end. |
|`rindex(<sub>[, <start>[, <end>]])`|	`'foo bar foo baz foo qux'.rindex('grault')`	|`substring not found`| Searches the target string for a given substring starting at the end. |
|`startswith(<prefix>[, <start>[, <end>]])`|	`'foobar'.startswith('foo')`	|`True`| Determines whether the target string starts with a given substring. |

<a class="anchor" id="Character Classification"></a>
## Character Classification

|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`isalnum()`|	`'abc123'.isalnum()`	|`True`| Determines whether the target string consists of alphanumeric characters |
|`isalpha()`|	`'ABCabc'.isalpha()`	|`True`| Determines whether the target string consists of alphabetic characters.|
|`isdigit()`|	`'123'.isdigit()`	|`True`| Determines whether the target string consists of digit characters. |
|`isidentifier()`|	`'foo32'.isidentifier()`	|`True`| Determines whether the target string is a valid Python identifier. |
|`islower()/isupper()`|	`'foo32'.islower()`	|`True`| Determines whether the target string’s alphabetic characters are lowercase/uppercase. |
|`isprintable()`|	`'a\tb'.isprintable()`	|`False`| Determines whether the target string consists entirely of printable characters |
|`isspace()`|	`'   a   '.isspace()`	|`False`| Determines whether the target string consists of whitespace characters. |
|`istitle()`|	`'This Is A Title'.istitle()`	|`True`| Conjugate a complex number |


<a class="anchor" id="String Formatting"></a>
## String Formatting


|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`center(<width>[, <fill>])`|	`'bar'.center(10, '-')`	|`'---bar----'`| Centers a string in a field. |
|`expandtabs(tabsize)`|	`'aaa\tbbb\tc'.expandtabs()`	|`'aaa     bbb     c'`| Expands tabs in a string.|
|`ljust(<width>[, <fill>])/rjust(<width>[, <fill>])`|	`'foo'.ljust(10, '-')`	|`'foo-------'`| Left/Right-justifies a string in field. |
|`lstrip([<chars>])/rstrip([<chars>])`|	`'   foo bar baz   '.lstrip()`	|`'foo bar baz   '`| Trims leading characters from a string. |
|`strip([<chars>])`|	`'www.realpython.com'.strip('w.moc')`	|`'realpython'`|Strips characters from the left and right ends of a string.|
|`replace(<old>, <new>[, <count>])`|	`'foo bar foo baz foo qux'.replace('foo', 'grault')`	|`'grault bar grault baz grault qux'`| Replaces occurrences of a substring within a string. |
|`zfill(<width>)`|	`'42'.zfill(5)`	|`'00042'`| Pads a string on the left with zeros. |


<a class="anchor" id="Converting"></a>
## Converting between Lists and Strings


|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`join(<iterable>)`|	`', '.join(['foo', 'bar', 'baz', 'qux'])`	|`'foo, bar, baz, qux'`| Concatenates strings from an iterable. |
|`list()`|	`list(`corge`), ':'.join('corge')`	|`['c', 'o', 'r', 'g', 'e'], 'c:o:r:g:e'`|  |
|`partition(<sep>)`|	`'foo.bar'.partition('.')`	|`('foo', '.', 'bar')`| Divides a string based on a separator. |
|`rpartition(<sep>)`|	`'foo bar baz qux'.rsplit()`	|`['foo', 'bar', 'baz', 'qux']`| Divides a string based on a separator. |
|`rsplit(sep=None, maxsplit=-1)`|	`complex_num.conjugate()`	|`(1+3j) --> (1-3j)`| Splits a string into a list of substrings. |
|`split(sep=None, maxsplit=-1)`|	`'www.realpython.com'.split('.', maxsplit=1)`	|`['www', 'realpython.com']`| Splits a string into a list of substrings. |
|`splitlines([<keepends>])`|	`'foo\nbar\r\nbaz\fqux\u2028quux'.splitlines()`	|`['foo', 'bar', 'baz', 'qux', 'quux']`| Breaks a string at line boundaries. |



<a class="anchor" id="List Methods"></a>
## List Methods
The string methods you saw in the previous tutorial did not modify the target string directly. That is because strings are immutable.
List methods are different. Because lists are mutable, the list methods shown here modify the target list in place.

|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`append(<obj>)`|	`[1, 2, 3].append([4, 5])`	|`[1, 2, 3, [4, 5]]`| Appends an object to a list.|
|`+`|	`[1, 2 , 3] + [4, 5]`	|`[1, 2, 3, 4, 5]`| |
|`extend(<iterable>)`|	`[1, 2, 3].append([4, 5])`	|`[1, 2, 3, 4, 5]`| Extends a list with the objects from an iterable.|
|`insert(<index>, <obj>)`|	`['foo', 'bar', 'baz'].insert(1, 3.14159)`	|`['foo', 3.14159, 'bar', 'baz']`| Inserts an object into a list. |
|`remove(<obj>)`|	`['foo', 'bar', 'baz'].remove('baz')`	|`['foo', 'bar']`| Removes an object from a list. |
|`pop(index=-1)`|	`['foo', 'bar', 'baz'].pop()`	|`['foo', 'bar']`| Conjugate a complex number |

<a class="anchor" id="Tuple Methods"></a>
## Tuple Methods
Tuples are immutable, so they don't have many built-in methods (and that's why they are a lighter data type compared to lists).

|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`count(<value>)`|	`(1, 1, 1, 2, 2, 3).count(1)`	|`3`| Counts occurrences of `<value>` in the target tuple.|
|`index(<value>[, <start>[, <stop>]])`|	`('foo', 'bar', 'baz').index('baz')`	|`2`| Searches the target tuple for a given value.(`<value>`)|

<a class="anchor" id="Dictionary Methods"></a>
## Dictionary Methods

|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`clear()`|	`{'a': 10, 'b': 20, 'c': 30}.clear()`	|`{}`| Clears a dictionary. |
|`get(<key>[, <default>])`|	`{'a': 10, 'b': 20, 'c': 30}.get('b')/ print(d.get('z', 'Nabod'))`	|`20, 'Nabod'`| Returns the value for a key if it exists in the dictionary.|
|`items()`|	`{'a': 10, 'b': 20, 'c': 30}.items()`	|`[('a', 10), ('b', 20), ('c', 30)]`| Returns a list of keys-values in a dictionary. |
|`keys()`|	`{'a': 10, 'b': 20, 'c': 30}.keys()`	|`['a', 'b', 'c']`| Returns a list of keys in a dictionary. |
|`values`|	`{'a': 10, 'b': 20, 'c': 30}.values()`	|`[10, 20, 30]`| Returns a list of values in a dictionary. |
|`pop(<key>[, <default>])`|	`{'a': 10, 'b': 20, 'c': 30}.pop('b')`	|`20`| Removes a key from a dictionary, if it is present, and returns its value.|
|`popitem()`|	`{'a': 10, 'b': 20, 'c': 30}.popitem()`	|`('c', 30)`| Removes a key-value pair from a dictionary. |
|`update(<obj>)`|	`{'a': 10, 'b': 20, 'c': 30}.update({'b': 200, 'd': 400})/d1.update(b=200, d=400)/d1.update([('b', 200), ('d', 400)])`	|`{'a': 10, 'b': 200, 'c': 30, 'd': 400}`| Merges a dictionary with another dictionary or with an iterable of key-value pairs. |


<a class="anchor" id="Set Methods"></a>
## Set Methods

|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`union()`/ `|`|	`x1.union(x2[, x3 ...])/ x1` | | Compute the union of two or more sets. |
|`intersection()`/ `&`|	`x1.intersection(x2[, x3 ...])/` `x1 & x2 [& x3 ...]`	|| Compute the intersection of two or more sets. |
|`difference()`/ `-`|	`x1.difference(x2[, x3 ...])`/ `x1 - x2 [- x3 ...]`	|``| Compute the difference between two or more sets. |
|`symmetric_difference`/ `^`|	 `x1.symmetric_difference(x2)` / `x1 ^ x2 [^ x3 ...]`	|`(1+3j) --> (1-3j)`| Compute the [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) between sets. |
|`isdisjoint()`/ ``|	``x1.isdisjoint(x2)``	|`True/False`| Determines whether or not two sets have any elements in common. |
|`issubset()` / `<=`|	`x1.issubset(x2)` /  `x1 <= x2`	|`True/False`| Determines whether one set is a subset of the other. |
|`issuperset()` / `>=`|	`x1.issuperset(x2)` / `x1 >= x2`	|`True/False`| Determines whether one set is a superset of the other. |
|`update()` / `|=`|	`x1.update(x2[, x3 ...])` / `x1 |= x2 [| x3 ...]`	|| Modify a set by union.|
|`intersection_update()` / `&=`|	`x1.intersection_update(x2[, x3 ...])` \ `x1 &= x2 [& x3 ...]`	|``| Modify a set by intersection. |
|`difference_update()` / `-=`|	`x1.difference_update(x2[, x3 ...])` \ `x1 -= x2 [| x3 ...]`	|``| Modify a set by difference. |
|`symmetric_difference_update()` / `^=`|	`x1.symmetric_difference_update(x2)` \ `x1 ^= x2`	|``| Modify a set by symmetric difference. |
|`add(<elem>)`|	`{'foo', 'bar', 'baz'}.add('qux')`	|`{'bar', 'baz', 'foo', 'qux'}`| Adds an element to a set.|
|`remove(<elem>)`|	`{'foo', 'bar', 'baz'}.remove('bar')`	|`{'foo', 'baz'}`| Removes an element to a set.|
|`discard(<elem>)`|	`{'foo', 'bar', 'baz'}.discard('bar')`	|`{'foo', 'baz'}`| Removes an element to a set.|
|`pop()`|	`{'foo', 'bar', 'baz'}.pop()`	|`{'foo', 'bar'}`| Removes a random element from a set.|
|`clear()`|	`{'foo', 'bar', 'baz'}.clear()`	|`set()`| Clears a set.|

<a class="anchor" id="Other Methods"></a>
## Other Methods
The following table lists the arithmetic operators supported by Python:


|Method | Example | Result | Description |
|:--|:--|:--|:--|
|`is_integer()`|	`float_num.is_integer()`	|`True`| Checking if or not a number is integer |
|`conjugate()`|	`complex_num.conjugate()`	|`(1+3j) --> (1-3j)`| Conjugate a complex number |
|`.real   .imag`|	`(complex_num.real, complex_num.imag)`	|`(1, 3)`| get real and imaginary part of a complex num |



