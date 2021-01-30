# ch05. List&Dictionary type

**list** : list means the sequence and Mutable list that is stored in order. The list maintains input order and internally implemented as a dynamic array.
<br><br>
**features of list** : the list are implemented in the form of managing pointer lists for objects. It is managed in the form of an array, so it boasts a function that combines an array and a list of connections. But It was slower than the oter programming language.
<br><br>

**Dictionary** : The dictionary consists of keys/values. It is implemented as a hash table. Various types, including letters, can be used as keys. Save data using Hash table. Hash tables support a variety of types with keys, with almost all time complexity being O (1).
<br><br>

**Dictionary module**
<br>
- defaultdict object: when querying a key that does not exist, generate a dictionary item for the key based one the default value instead of the error value
<br>
- Counter object : Calculate the number of items and return them to the dictionary. At this time, the key contains the value of the item and the number of the item is included in the value. 

**Hash talbe?**
![해시테이블](https://user-images.githubusercontent.com/63804074/106355085-39445f80-6339-11eb-8ed4-cb6f82aa7a27.png)

It is one of the data structures that stores data in key and value, which allows data to be retrieved quickly. The hash table provides a fast search speed because it stores data internally using an array.  A hash function is applied to each key value to create a unique index of the array, which is used to store or retrieve the value.

출처 :https://mangkyu.tistory.com/102
https://ratsgo.github.io/data%20structure&algorithm/2017/10/25/hash/
