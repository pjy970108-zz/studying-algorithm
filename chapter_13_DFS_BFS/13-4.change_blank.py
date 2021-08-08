def balanced_index(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0: 
                return False
            cnt -= 1
    return True 

def solution(p):
    res = ''
    if p == '':
        return res
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    if check_proper(u):
        res = u + solution(v)
    else:
        res = '('
        res += solution(v)
        res += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        res += "".join(u)
    return res