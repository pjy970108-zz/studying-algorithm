# ch06. SORT
<br>

## Sort : reorder following some Criterias
<br>

if we know the sorting algorithm, we can do binary search. 
<br>

1. **selection sort** : choose the minimun every time,<br>

    1) choose the smallest number and then change this number to first number
    2) choose the second smallest number and then change this number to second number
    3) repeat that steps untill finishing 
    <br>

2. **insert sort** : It is assumed that it is already aligned up to that point. <br>
    
    1) the first location of number assume it is alread aligned, focus on second location of number. 
    we have to reorder, so insert second location of number move to left on the first number.
    2) if the second number was bigger than fir location number, the second number will not move.
    3) repeat untill finishing
<br>

3. **quick sort** : using pivot that use for change measurment. <br> it was like recursive function.

    1) choose the pivot, after that choose the number bigger than pivot from left order and choose the number smaller than pivot from right side. and then change the left side one and the right side one
    2) find the bigger one and smaller one like step 1. if there are cross the bigger one and smaller one, change the pivot with smaller one.
    3) repeat untill list number was one
<br>

4. **count sort** : it was possilble only integer type data, cause we have to declare the list that save the all data. <br> it was useful for limited data size that was duplicated.

    1) just count the same index.

<br>

**type of sort algorithm**
<br>

1. it was possible to solve using sort library
2. check princlple of sorting algorithm
3. need to faster sorting.

<br>

**contents of table**
6-1. selection_sort_source_code.py<br>
6-2. insert_sort_source_code.py<br>
6-3.quick_sort_source_code.py<br>
6-4.count_sort_source_code.py<br>
6-4.count_sort_source_code.py<br>
6-5.up_to_down.py<br>
6-6.print_grade.py<br>
6-7.change_multi_element.py
