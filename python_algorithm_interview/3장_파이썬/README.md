# ch03. python

## [Features of python]
1. Ident : the indent is 4 of spaces when you write the code
2. Naming Convention : When I defining a variable and a function , separate each word with Snake Case(_)
3. Type hint : We have to check the type such as 'str', 'int'
4. List comprehension : we can use functional things like map, filter and lamba For code efficiency,
~~~ python
a={}
for key, value in original.items():
    a[key]=value
~~~
instead of upper example, we can use down example
~~~ python
a={key:value for key, value in original.items()}
~~~

5. Generator : function that generates the iterator, using the yield keyword
6. Range : the Representative function use Generator, usually use in for code
~~~ python
a=[n for n in range(1000000)]
b=range(10000)
~~~
b is faster than a, because of using only condition.
Also, b uses memory less than a.

7. Enumerate : ordered types data such as list, set, tuple return enmerate objects including index.
~~~ python
for i, v in enumerate(a):
    print(i,v)
~~~

8. Divide Operators : //, /, %, divmod

9. Print : if you want to debug the code in codeing test, you can use 'print' for debuging

10. Pass : if you want to make the whole of code structure first, you can use the 'pass' for making the whole of code structure.

11. Locals : We can check all of variables in local enviroment.
~~~python
import pprint
pprint.pprint(locals())
~~~

## [When you write the code]
- use an intuitive varialbe name and comment.
- When you use the list comprehension, Using less than 2 list comprehension at one line.