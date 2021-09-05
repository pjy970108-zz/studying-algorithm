import re
def solution(new_id):
    # 1단계 소문자로 치환
    new_id=new_id.lower()
    # 2단계 특수문자, 소문자 숫자 제외 제거
    special_word = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id=''.join(i for i in new_id if i not in special_word)
    # 3단계 만약 .가 연속으로 쓰이면 하나로 통합
    new_id = re.sub('([.]){1,}', '.', new_id) # 연속된 같은 문자 변환 (2개이상)
    # 4단계 .가 처음이나 끝이면 제거
    new_id=new_id.strip('.')
    # 5단계 빈문자열이면 new_id에 "a"대임
    if len(new_id)==0:
        new_id += 'a'
    # 6단계 16자 이상이면 15개 슬라이스
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id=new_id.rstrip('.')
    # 7단계 길이가 2자 이하면 마지막 문자를 3이 될때까지 붙임
    if len(new_id) <= 2:
        while True:
            new_id += new_id[-1]
            if len(new_id)==3:
                break
    return new_id