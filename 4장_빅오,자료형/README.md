# ch04. big-O

## big-o: mathematica notation that explain the upper bound of a fuction when the input value is directed to infinity(=Time complexity) and explain the time that perform an algorithm
<br>
<br>
- O(1) : the best algorithm. No matter how large the input value is, the execution time is constant.
<br>
<br>
- O(log(n)) : log is not significantly affected by large input values. EX) using at Binary search
<br>
<br>
- O(n) : The time taken to perform the algorithm is proportional to the input value and is affected by the execution time. callled linear-time algorithm. but when you find the max or min value in case of an unordered list, search all of input values
<br>
<br>
- O(nlog(n)) : Most efficient sorting algorithms, including merge sorting. No good algorithm can be faster than O(nlog(n)). EX) Timsort
<br>
<br>
- O(n^2) : the inefficient sorting algorithms, such as bubble sorting
<br>
<br>
- O(2^n): An algorithm that calculates the number of Fibonacci as recursive. It's more complicated that O(n^2)
<br>
<br>
- O(n!): when we solve the salesman problem with brute force.

## upper-bound, lowerbound, mean
<br>
- big_0(O) : when the function runs last. it means upper bound
<br><br>
- big_omega(Ω) : when the function runs fast. it means lowerbound
<br><br>
- big_theta(θ) : when the function runs mean speed. it means meanbound.
<br><br>
usally use big_O(O)

## Data-Type
Data type is an attribute of data that tells a complier or interpreter how a programmer uses the data. The Data type is more specific than the data structure and refers to all data types.
![KakaoTalk_20210125_214246786](https://user-images.githubusercontent.com/63804074/105707657-a2515f00-5f56-11eb-8ff1-d230c722e081.jpg)

### Number-Data-Type
class bool : A subclass of int type that is internally treated as 1(T) and 0(F) in Python
* sturture in Number-Data-Type
    object type > int type > bool type

### Set-Data-Type
class set : the type that doesn't have the duplicate values. Input order is not maintained, and if there is duplicate value, only one value is maintained
<br>
~~~ python
a= set() # 빈 집합 만들기
a = {1, 2, 3} #원소를 가지고 있는 집합 만들기
~~~

### Mapping-Data-Type
class dict : Compound data types consisting of keys and values.

### Sequence-Type
* Sequence : Indicates an ordered list of certain targets
    * immutable-type : cannot change the values
        * class str : Sequential of string
        * class tuple 
        * 바이트(class bytes)
    * mutable-type
        * class list : A dynamic array of values that can add and delete freely, consisting of various values in an ordered array
<br>
<br>
## Speed of Python
Because python uses objects for calculation, it is slower than C-programming


## Data-Structure
Data-Structure refers to the organization, mangement and storage structure of data for efficient access and manipulation of data.<br>
Typically, an array, list of connections and objects based on a raw data type.
<br><br>

## Abstract Data Type
It is called ADT that refer to mathematical  models about Data-Type
