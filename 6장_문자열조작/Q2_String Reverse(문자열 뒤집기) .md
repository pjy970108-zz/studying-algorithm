# Q2_String Reverse(문자열 뒤집기) 
** 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접조작하여라 **
input : ['h','e','l', 'l', 'o']
output : ['o', 'l', 'l', 'e', 'h']
~~~python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
~~~

**solution1. Swap using the two pointers**
~~~python
 def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
~~~
