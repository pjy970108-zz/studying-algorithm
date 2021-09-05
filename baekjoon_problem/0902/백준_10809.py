alpabet = ['a', 'b', 'c','d' ,'e' ,'f','g' ,'h', 'i', 'j' ,'k', 'l' ,'m','n' ,'o' , 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input().lower()
count = []
new_word=[]

for _ in range(len(alpabet)):
    count.append(str('-1'))
    
    
for i in word:
    if i not in new_word:
        new_word.append(i)

for k, i in enumerate(new_word):
    if i in alpabet:
        count[alpabet.index(i)] = str(list(word).index(str(i)))  #인덱스 추출
print(' '.join(count))
        
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')