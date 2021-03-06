''''''
'''

1장 1절 시퀀스를 개별 변수로 나누기

* 시퀀스 : 데이터들의 집합. 리스트, 튜플, 딕셔너리 등등. 시퀀스는 가변형 시퀀스, 불변형 시퀀스가 있다.

        가변형 시퀀스 - list, bytes, bytearray 등
        불변형 시퀀스 - str, tuple, range 등

* 시퀀스의 연산 (x는 임의의 객체, s는 시퀀스 객체, i j k l m n 은 정수)
- x in s                  :   s의 한 요소가 x와 같으면 True 
- x not in s              :   s의 한 요소가 x와 같으면 False
- s1 + s2                 :   두 시퀀스를 결합
- s*n 혹은 n*s            :   시퀀스를 n회 반복
- s[i]                    :   시퀀스s의 i번째 요소
- s[i:j]                  :   시퀀스s의 i번째 요소 부터 j-1번째 요소까지 추출
- s[i:j:k]                :   시퀀스s의 i번째 요소 부터 j-1번째 요소까지 k 단위로 추출
- len(s)                  :   시퀀스s내의 요소의 개수
- min(s)                  :   시퀀스s내에서 최소값
- max(s)                  :   시퀀스s내에서 최대값
- s.index(x[, i[, j]])    :   x와 같은 첫 번째 요소의 인덱스
- s.count(x)              :   x와 같은 요소의 개수

* 가변형 시퀀스의 조작
- s[i] = x          :   s의 i번째 요소를 x로 교체
- s[i:j] = t        :    i번째 요소부터 j-1번째 요소를 t(iterable)로 교체
- del s[i:j]        :    i번째 요소부터 j-1번째 요소를 삭제 ( s[i:j] = [] 와 동일)
- s[i:j:k] = t      :    i번째 요소부터 j-1번째 요소(k는 스텝)를 t(iterable)로 교체 (t 와 슬라이싱 된 요소들의 크기가 같아야 한다.)
- del s[i:j:k]      :    i번째 요소부터 j-1번째 요소(k는 스텝)를 삭제
- s.append(x)       :    s의 마지막 요소로 x를 삽입
- s.extend(t)       :    t의 내용물로 s를 확장 ( s[len(s):len(s)]=t 와 동일)
- s.insert(i, x)    :    i 번째에 x를 삽입
- s.pop()           :    마지막 삭제하고 그것을 반환한다.
- s.pop(i)          :    i 번째 요소를 삭제하고 그것을 반환한다.
- s.remove(x)       :    s의 요소 중 x와 같은 첫 번째 것을 제거 (s 안에 x가 없다면 ValueError 예외가 발생한다.)
- s.reverse()       :    요소들을 역순으로 배열한다. (요소의 순서를 역순으로 바꾼다. ( 역순으로 바뀐 객체가 반환되는 것이 아니다.) )
- s.clear()         :    모든 요소 삭제 (del s[:] 과 동일)



* 시퀀스에서의 주의 사항
- 모든 시퀀스는 개별 변수로 나눌 수 있지만 반드시 변수의 개수가 시퀀스에 일치해야만 한다. 그렇지 않을 경우 ValueError 가 발생한다.
    예)

'''
# 예1.
p = (4, 5)
x, y, z = p
# Traceback (most recent call last):
# File "K:/Python/PythonStudy/p02_personal_summary/p07_bae_jun_ho/p01_week/p01_tuesday/1.1-1.17.py", line 87, in <module>

'''        
ValueError: not enough values to unpack (expected 3, got 2)
- 같은 형의 나열형 객체끼리는 비교도 가능하다. 특히 리스트와 튜플은 길이와 같은 인덱스를 가지는 모든 요소들끼리 같다면 두 리스트/튜플은 같은 것으로 판별된다.
- 나열형 객체의 복사는 ‘얕은 복사’라는 것도 유의해야 한다. 즉, 중첩된 구조는 복사되지 않는다. (얕은 복사 : 리스트의 중첩 구조는 복사하지 않고 틀만 복사함 아래 예 참조)
    예)
'''
# 예2.
lst = [[]] * 3
lst
# [[], [], []]
lst[0].append(1)
lst
# [[1], [1], [1]]

'''
- 서로 다른 리스트를 만들고 싶은 경우
    예)
'''

# 예3.
lst = [[] for _ in range(3)]
lst
# [[], [], []]
lst[0].append(1)
lst[1].append(2)
lst[2].append(3)
lst
# [[1], [2], [3]]


'''
- 만약 ‘깊은 복사’를 수행하려면 copy 모듈의 deepcopy 함수를 이용하면 된다. (깊은 복사 : 구조까지 전부 다 복사해옴. 아래 예 참조)
    예)
'''
# 예4.
x = [11, 22]
y = [x, 33]
y
# [[11, 22], 33]

# 예5.
from copy import deepcopy

z = deepcopy(y)
z
# [[11, 22], 33]

# 예 6.
x[0] = -44
y
# [[-44, 22], 33] # x가 변하면 y도 변한다.
z
# [[11, 22], 33] # x가 변해도 z는 변함이 없다.

'''
* 언패킹
- 패킹 : 하나의 변수에 여러 값을 넣는 것
  언패킹 : 패킹된 변수에서 여러개의 값을 꺼내 오는 것
   예)
'''

# 예7.
c = (3, 4)
d, e = c  # c의 값을 언패킹하여 d, e에 값을 넣었다
f = d, e  # 변수 d와 e를 f에 패킹

'''

- 이터레이터(iterator)와 제너레이터(generator). 매우매우매우 중요!
    1. 이터레이터 : 반복가능한 객체 (초간단 이해 -> 객체에 .next가 가능하다면 이터레이터가 맞음)
        예) 이터레이터 =  iter(list) : list를 iter로 통하여 이터레이터를 만들었다, list는 반복가능하지만 이터레이터는 아니다.. 
                                       명시적으로 반복가능한객체로 만들어서 사용해줘야한다

        1-1. 이터레이블 : 반복 가능하다 (반복(loop)연산이 가능하여 해당 위치를 이동해가면서 값을 사용할수 있는 지를 말한다)

        1-2. 이터레이션 : 반복가능한객체에서 해당값을 가져오는 행위

        1-3. 이터함수(iter 함수) : list나 dict를 이터레이터로 만들어주는 함수

    2. 제너레이터 : 이터레이터를 만들어주는것을 말한다 (= 반복가능한 객체를 만들어주는 행위)

        2-1. yield : function에서 return과 동일한 역할을 수행한다. 
            -> 해당 function을 yield를 사용하여 제너레이터를 만들어줌(아래 예제 참조)

'''


# 예8.
def generator(n):
    print("get_START")
    i = 0
    while i < n:
        yield i
        print("yield 이후 %d" % i)
        i += 1
    print("get_END")


for i in generator(4):
    print("for_START %d" % i)
    print(i)
    print("for_END %d" % i)

'''
위 코드 실행 결과

get_START # generator 최초생성시점 , # yield 구문 돌입, 여기서부터 while문의 시작

for_START 0 # generator에서 yield로 리턴된 값을 받아서 for문의 시작

0

for_END 0

yield 후 0 # yield후에 잔여코드실행(while문이 아직 이때 i는 0의 상태로 실행되고 있는것), 다돌고난뒤에 while문 한번반복하여 yield를 해준다 값은 1을 리턴

for_START 1 # for loop이 최초한번 돌고 두번째 돌입

1

for_END 1

yield 후 1

for_START 2

2

for_END 2

yield 후 2

for_START 3

3

for_END 3

yield 후 3

get_END #generator 종료

'''

'''

* 언패킹을 할 때 특정 값을 무시하는 법 : 해당 변수의 공간을 _ 로 입력
  예)
'''

# 예9.
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

# shares
# 50
# price
# 91.1

''' 

1장 2절 임의 순환체의 요소 나누기
 - 순환체에 정해진 요소의 개수 보다 많은 요소를 언패킹 하게 되면 값이 너무 많습니다 라는 예외가 발생한다.
   이 문제를 해결하기 위해 별( * ) 표현식을 사용한다.

   * 이 별표 구문은 길이를 알 수 없는 순환체에 매우 효과적으로 사용 할 수 있다. ( 예 - 길이가 일정하지 않은 튜플 )

   변수를 불러오고 싶지 않을 때 사용하는 버리기용 변수명 : _, ign(ignored)

   예)
'''


# 예10.
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


# 예11.
record = ('Dave', 'dave@example,com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

# 예12.
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
return avg_comparison(trailing_avg, current_qtr)

# 예13.
*trailing, current = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
trailing  # *trailing과 current 순으로 요소가 담기므로 마지막 current의 자리인 마지막 1을 빼고 나머지가 전부 trailing에 담긴다
current  # current엔 딱 한자리인 1만 담긴다

# 예14.
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

'''

1장 3절 마지막 N개의 아이템 유지
- 순환이나 프로세싱 중 마지막으로 발견한 N개의 아이템을 유지하고 싶은 경우 : collections.deque 를 사용한다.


 * 스택과 큐
    - 스택(stack) : 스택은 데이타 입/출력이 한쪽으로만 접근 할 수 있는 자료 구조이다. 스택에서 가장 나중에 들어간 데이타가 제일 먼저 나오게 된다. 그래서 스택을 LIFO(Last In First Out) 구조라고 한다.
                    스택을 조작하는 동작은 데이타를 넣은 PUSH 동작과 데이타를 빼오는 POP 동작이 있다. PUSH는 스택의 최상단 데이타 위에 새로운 데이타를 쌓는다(stack). POP은 스택의 최상단에 있는 데이타를 빼온다.
                    파이썬에는 내장 자료형 중에 하나인 리스트형이 스택을 표현하는데 사용된다. 즉, 파이썬에는 스택을 따로 구현할 필요가 없다. 

    -  큐 (queue) : 큐는 먼저 넣은 데이타가 먼저 나오는 FIFO(First-In-First-Out) 구조로 저장하는 자료구조 이다. 즉, 큐는 LIFO 구조인 스택과 반대되는 개념의 자료 구조이다. 
                    스택은 데이타가 입/출력하는 부분이 한 부분밖에 없다고 한다면, 큐는 양쪽 모두 뚤려있다. 한쪽으로는 데이타를 넣기만 하고, 다른쪽에서는 데이타를 빼내기만 한다. 
                    데이타를 넣는 연산을 PUT 동작, 데이타를 빼내는 동작을 GET 동작이라고 한다.
                    큐의 구현은 스택과 마찬가지로 리스트형으로 표현 할 수 있다. 파이썬은 프로그래머가 자료 구조에 대해 고민을 덜어 준다. 
                    앞서 다루었던 연결 리스트도 이해를 돕기 위해 class로 구현 하였지만, 리스트형으로 표현 할 수 있다. 
                    리스트형 하나만으로도 C언어의 배열과 연결 리스트, 스택, 큐를 표현 할 수 있으니, 파이썬은 대부분의 경우 자료 구조를 따로 구성 할 필요가 없다. 
                    이런 이유로 파이썬은 프로그래머에게 프로그램 로직에만 집중할 수 있게 해준다.

    deque(maxlen=큐의 길이) 로 큐를 만들 수 있다. maxlen으로 최대길이를 지정해주지 않으면 제약 없이 큐의 양쪽에 아이템을 넣고 뺄 수 있다.


    예)
'''
# 예15.
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# 위 코드 사용 예
if __name__ == '__main__':
    with open('examplefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# 스택의 예시
def Main():
    stack = []  # stack create
    stack.append(1)  # same PUSH
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print
    stack

    while stack:
        print
        "POP >", stack.pop()


Main()


# 큐의 예시
def Main():
    queue = []  # queue create
    queue.append(1)  # same PUT
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print
    queue

    while queue:
        print
        "GET > ", queue.pop(0)  # same GET


Main()

# 예16.
q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
q
# deque([1,2,3], maxlen=3)

q.append(4)
q
# deque([2,3,4], maxlen=3)

# 예17.
q = deque()
q.append(1)
q.append(2)
q.append(3)

q.appendleft(4)
q
# deque([4,1,2,3])
q.pop()  # .pop()을 하면 큐의 맨오른쪽의 아이템이 출력되면서 제거된다
# 3
q
# deque([4,1,2])
q.popleft()  # .popleft() 하면 큐의 맨왼쪽의 아이템이 출력되면서 제거된다.
# 4

'''

1장 4절 N 아이템의 최대 최소값 찾기 : 컬렉션 내부에서 가장 크거나 작은 N개의 아이템을 찾아야 할때 heapq 모듈에 있는 nlargest()와 nsmallest() 함수를 사용한다.
    - nlargest(n, collection) : 컬랙선 내부에서 가장 큰 순서대로 n개의 아이템을 뽑아서 출력
    - nsmallest(n, collection) : 컬랙션 내부에서 가장 작은 순서대로 n개의 아이템을 뽑아서 출력

    위 두 함수 모두 복잡한 구조에 사용 될 수 있도록 키 파라미터를 받는다

    * (중요) lambda 함수

    key = lambda : 익명함수

    익명함수 : 단순하게 쓰고 버리기 좋기 때문에 사용.

    lambda 사용법 : lambda 인수1, 인수2, ...  (인수를 이용한 표현식)
     - lambda 선언 뒤에, 인수들이 붙고 이 인수를 바탕으로 표현식을 처리 후, 값을 리턴.

    예) 

'''


# 예18.
def sum(a, b):  # 단순하게 a와 b를 합하는 함수를 만든다고 했을 때, 선언과 return 값을 코딩해주어야 한다.
    return a + b


x = lambda a, b: a + b  # 이에 반해 lambda는 아래와 같이 한줄로 표현 할 수 있다.

# 예19.
array = [-1, 3, -4, 10, 5, 7]
print
sorted(array,
       key=lambda x: x ** 2)  # sorted 함수에서 key값은 정렬하는 기준이 된다. lambda를 통해 key 값을 x^2으로 return 받았으므로, key 값 기준으로 정렬한다.
# [-1, 3, -4, 5, 7, 10]

# 예20.
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
# [42, 37, 2]
print(heapq.nsmallest((3, nums)))
# [-4, 1, 2]

# 예21.
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

# heapq.heapify() (힙 메소드) 의 중요한 기능은 heap[0] 이 가장 작은 요소로 정렬된다는 것이다.

# 예22.
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

import heapq

heap = list(nums)
heapq.heapify(heap)
heap
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

# heapq.heappop()을 쓰면 가장 첫번째의 아이템을 뽑아낼 수 있다.

heapq.heappop(heap)
# -4

'''

1장 5절 우선 순위 큐 구현 : 우선 순위에 따라 아이템을 정렬하는 큐를 만들고 항상 순위가 높은 아이템을 먼저 팝하도록 해야한다.

 1) heapq 모듈을 사용해서 우선 순위 큐를 구현한다.
 2) heapq.heappush()와 heapq.heappop() : heappush는 list_queue의 첫 번째 아이템이 가장 작은 아이템이 되도록 삽입 혹은 제거하고, heappop는 가장 작은 아이템을 반환해서 큐의 팝이 올바른 아이템에 적용되게 함
    예)
'''

# heapq 모듈을 사용해서 우선 순위 큐를 구현

# 예23.
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # 내부 튜플 설명 : -priority - 일반 정렬 순서의 반대 순서(높은 값에서 낮은 값으로)로 우선순위를 정렬, index - 우선 순위가 동일 할 경우 삽입 순으로 정렬하기 위해 사용, Item - 인스턴스
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# 위 코드를 사용하는 예

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()  # 우선 순위 값이 가장 큰 bar -> spam 순으로 팝 되고 우선 순위가 같을 경우 입력된 순서인 foo -> grok 순으로 팝시켜준다.
# Item('bar')
q.pop()
# Item('spam')
q.pop()
# Item('foo')
q.pop()
# Item('grok')


'''

1장 6절 딕셔너리의 키를 여러 값에 매핑하기 : 딕셔너리의 키를 하나 이상의 값에 매핑(multidict) 할 때
- 하나의 키에 하나의 값이 매핑 되어 있는 경우 이것을 딕셔너리 라고 한다.
- 하나의 키에 여러개의 값을 매핑하려면 여러 값을 리스트나 세트와 같은 전용 컨테이너에 따로 저장해 두어야 한다.
  ( 순서가 상관 있고 중복여부는 상관 없으면 리스트, 순서가 상관 없고 중복여부가 상관 있으면 세트 )

- 딕셔너리를 쉽게 만들게 해주는 모듈과 메소드 : collections 모듈의 defaultdict를 사용한다

- 여러 값을 가지는 딕셔너리를 만드려면 첫 번째 값에 대한 초기화를 스스로 해야하고 defaultdict를 사용하지 않으면 다음과 같이 생성해야 한다.
    # defaultdict 사용 X
    d = {}
    for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

    # defaultdict 사용 O
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)

'''
# 예24.

# 하나의 키에 여러 값을 매핑
d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

# defaultdict
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['a'].append(4)

d = defaultdict(set)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)

'''

1장 7절 딕셔너리 순서 유지 : 딕셔너리를 만들고 순환이나 직렬화 할 때 순서를 조절하고 싶은 경우 딕셔너리 내부 아이템의 순서를 조절하려면 collections 모듈의 OrderedDict를 사용한다.
    - OrderedDict 메소드는 삽입 초기의 순서를 그대로 기억한다.
    - 따라서 OrderedDict는 직렬화하거나 다른 포맷으로 인코딩할 다른 매핑을 만들 때 특히 유용하다. 
    - OrderedDict는 내부적으로 Doubly Linked List로 삽입 순서와 관련있는 키를 기억해둔다. 새로운 아이템을 처음으로 삽입하면 리스트의 제일 끝에 위치시킨다. 재할당을 하더라도 순서는 변하지 않게 된다.

'''

# 예25.
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])
# "foo 1", "bar 2", "spam 3", "grok 4"

'''

1장 8절 딕셔너리 계산 : 딕셔너리 데이터에 계산을 수행할 때 계산을 하기 위해선 키와 값을 뒤집어야 한다. zip() 으로 뒤집을 수 있다.
    - zip()은 단 한번만 소비할 수 있는 이터레이터를 생성해서 사용한다. 따라서 계산을 한 뒤 다시 또 계산을 하려면 한번 더 zip을 사용해야 한다.
    - 특정 데이터의 최대 최소 값을 알고 싶으면 max() min() 함수에 key 값을 제공한다.
    - 딕셔너리에 max() min()를 사용하면 변수 키값의 최대 최소값을 뽑이준다. 키값 말고 변수 값의 최대 최소값 자체가 알고 싶을 땐 max min 안에 .values()를 넣어준다.
    - 값이 최대 최소인 변수를 찾으려면 익명함수 람다를 사용한다.
    - 중복된 값이 있으면 가장 크거나 가장 작은 키 값을 반환한다.

'''

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.35,
    'HPQ': 37.20,
    'FB': 10.75,
}

# 예26.

min_price = min(zip(prices.values(), prices.keys()))
# (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# (612.78, 'AAPL')

# 예27.
min(prices)  # AAPL
max(prices)  # IBM
min(prices.values())  # 10.75
max(prices.values())  # 612.78

# 예28.
min(prices, key=lambda k: prices[k])  # FB
max(prices, key=lambda k: prices[k])  # AAPL

'''

1장 9절 두 딕셔너리의 유사점 찾기 : 두 딕셔너리가 있고 유사점(동일한 키나 동일한 값)을 찾고 싶은 경우 keys()와 items() 메소드에 집합 연산을 수행하면 된다.
- 집합 연산
    차 집합 : A - B , A.difference(B)
    교 집합 : A & B , A.intersection(B)
    합 집합 : A | B , A.union(B)


'''

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 예28.
# 동일 키 찾기
a.keys() & b.keys()
# {'x', 'y'}
# 없는 키 찾기
a.keys() - b.keys()
# {'z'}
# 키, 값 모두 동일한 것 찾기
a.items() & b.items()
# {('y', 2)}
# 특정 키를 제거한 새로운 딕셔너리 생성
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
c
# {'x' : 1, 'y' : 2}

'''

1장 10절 순서를 깨지 않고 시퀀스의 중복 없애기 : 시퀀스에서 중복된 값을 없애되 아이템의 순서를 유지하고 싶을 땐 해쉬 여부에 따라 적용 방법이 달라진다.

* hash

대응 관계를 나타낼 수 있는 자료형을 연관 배열(Associative array) 또는 해시(Hash)라고 한다. ( 예 - '이름' = '홍길동' )
파이썬에서는 이러한 자료형이 딕셔너리(Dictionary)이다.
딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다. (예 - Key : 'baseball', Value : '야구')
딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요소값을 구하지 않고 Key를 통해 Value를 얻는다. 
이것이 바로 딕셔너리의 가장 큰 특징이다. 
baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.

    1) 해쉬 가능할 때 (hashable) : 세트와 제너레이터를 사용해서 해결

    2) 해쉬 불가능할 때 (not hashable)

- key 인자의 목적은 중복 검사를 위해 함수가 시퀀스 아이템을 hashable 하게 변환한다고 명시하는데 있다.
- 시퀀스를 세트로 생성하면 중복을 없앨 수 있으나 세트를 사용할 경우 데이터의 순서가 훼손된다. 따라서 이를 방지하기 위해 데이터를 읽어올 때 아래 함수를 사용하여 다음과 같이 불러오면 된다.
    with open(somefile, 'r') as f:
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)


'''


# hashable 할 때

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))


# [1, 5, 2, 9, 10]

# not hashable 할 때

def dedupe(items):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 예29.
# 필드가 하나이거나 커다란 자료 구조에 기반한 값의 중복을 없앨 때 사용

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe(a, key=lambda d: (d['x'], d['y'])))
# [{'x' : 1, 'y' : 2}, {'x' : 1, 'y' : 3}, {'x' : 2, 'y' : 4}]     # x, y가 모두 중복인 것을 제거
list(dedupe(a, key=lambda d: d['x']))
# [{'x' : 1, 'y' : 2}, {'x' : 2, 'y' : 4}]    # x가 중복인 것을 제거

'''

1장 11절 슬라이스 이름 붙이기 : 프로그램 코드에 슬라이스를 지시하는 하드코딩이 너무 많아 정리가 필요할 때 슬라이스된 각 부분에 이름을 붙여주면 이해하기가 훨씬 수월하다

- 내장함수 slice() 는 슬라이스 가능한 모든 곳에 사용 가능하다.
- 슬라이스에 인스턴스를 생성하면 인스턴스명.start 로 시작지점을 알 수 있고 인스턴스명.step 으로 중간단계를 알 수 있고 인스턴스명.stop 으로 마지막 종료지점을 알 수 있다.
- indices(size) 메소드를 사용하면 특정 크기의 시퀀스에 슬라이스를 매핑하는 경우 튜플 (start, stop, step)이 반환되는데 인덱스에 접근할 때 IndexError를 발생시키지 않기 위해 이 튜플은 경계를 넘지 않게 제약이 걸려있다. 

'''

# 예30.
###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25  ..........'
cost = int(record[20:32]) * float(record[40:48])  # 별로 좋지 못하다.

SHARES = slice(20, 32)
PRICE = slice(40, 48)

cost = int(record[SHARES]) * float(record[PRICE])  # 아주 깔끔하다.

# 예31.
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
items[2:4]
# [2, 3]
items[a]
# [2, 3]

items[a] = [10, 11]
items
# [0, 1, 10, 11, 4, 5, 6]   # 2와 3이 있던 자리를 10, 11로 대체하였다

del items[a]
items
# [0, 1, 4, 5, 6]

# 예32.
s = 'HelloWorld'
a.indices(len(s))
# (5, 10, 2)
for i in range(*a.indices(len(s))):
    print(s[i])
# W
# r
# d
