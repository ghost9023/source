
from math import *
import random
import copy
import time
# sTime = time.time()
BOARD_FORMAT = "|-|---|1|------|2|------|3|------|4|------|5|------|6|------|7|------|8|------|9|---\n" \
               "|1| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|2| {9} | {10} | {11} | {12} | {13} | {14} | {15} | {16} | {17} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|3| {18} | {19} | {20} | {21} | {22} | {23} | {24} | {25} | {26} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|4| {27} | {28} | {29} | {30} | {31} | {32} | {33} | {34} | {35} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|5| {36} | {37} | {38} | {39} | {40} | {41} | {42} | {43} | {44} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|6| {45} | {46} | {47} | {48} | {49} | {50} | {51} | {52} | {53} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|7| {54} | {55} | {56} | {57} | {58} | {59} | {60} | {61} | {62} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|8| {63} | {64} | {65} | {66} | {67} | {68} | {69} | {70} | {71} |\n|" \
               "-|---------------------------------------------------------------------------------\n" \
               "|9| {72} | {73} | {74} | {75} | {76} | {77} | {78} | {79} | {80} |\n|" \
               "-|---------------------------------------------------------------------------------"
NAMES = [' ', 'X', 'O']

table = [x for x in range(81)]


# 수 계산에 사용할 조건인 승리(end) 조건을 담는 부분
end=[]

# 가로 직선
for a in range(0,5,1):
    for b in range(a,a+73,9):
        end.append(tuple([b,b+1,b+2,b+3,b+4]))
# print(len(end))

# 세로 직선
for c in range(0,45,1):
    end.append(tuple([c,c+9,c+18,c+27,c+36]))
# print(len(end))

# 대각선 ↘
for d in range(0,37,9):
    for e in range(d,d+5,1):
        end.append(tuple([e,e+10,e+20,e+30,e+40]))
# print(len(end))

# 대각선 ↙
for i in range(4,41,9):
    for j in range(i,i+5,1):
        end.append(tuple([j,j+8,j+16,j+24,j+32]))

class TicTacToe:
    def __init__(self, state=None):
        if state is None:
            state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.playerJustMoved = 2
        self.state = state

    def Clone(self):                # 판 상태를 복사해서 지속적으로 게임을 진행하게 복사를 하는 함수
        state = TicTacToe()         # TicTacToe 클래스를 state에 담는다
        state.state = self.state[:] # state의 상태가 self.state
        state.playerJustMoved = self.playerJustMoved
        return state

    def DoMove(self, move):         # 턴을 정하는 함수
        assert int(move) >= 0 and int(move) <= 80 and self.state[move] == 0     # assert : 뒤 조건이 아니면
        self.playerJustMoved = 3 - self.playerJustMoved     # 턴을 넘기는 곳. 플레이어 1이 두면 3-self.playerJustMoved는 1이므로 새 self.playerJustMoved에 2가 저장된다
        self.state[move] = self.playerJustMoved             # 그렇다면 수를 둘(state[move]) 플레이어의 값이 2로 저장되어 턴이 넘어 간다.

    def GetMoves(self):             # 수를 둘 수 있는 빈칸을 찾아서 그 칸의 자리가 입력되면 그 자리에 수를 둘 수 있게 하는 함수
        if self.checkState() != 0:  # checkstate가 0이 아닌경우 빈 리스트를 반환한다.
            return []

        else:                       # 그게 아닌 모든 경우(checkstate가 값이 있을 경우) 빈 리스트 moves를 생성하고
            moves = []              # 0부터 80까지 숫자에 대해 self.state[i] 값이 0이면 해당 i값을 moves에 입력한다.
            for i in range(81):
                if self.state[i] == 0:
                    moves.append(i)

            return moves            # 그리고 moves를 반환한다.

    def GetResult(self, playerjm):
        result = self.checkState()
        assert result != 0
        if result == -1:
            return 0.5

        elif result == playerjm:
            return 2.0
        else:
            return 0.0

    def checkState(self):
        for (x, y, z, p, q) in end:
            if self.state[x] == self.state[y] == self.state[z] == self.state[p] == self.state[q]:
                if self.state[x] == 1:
                    return 1
                elif self.state[x] == 2:
                    return 2

        if [i for i in range(81) if self.state[i] == 0] == []:
            return -1
        return 0

    def __repr__(self):
        cells = []
        for i in range(81):
            cells.append(NAMES[self.state[i]].center(6))
        return BOARD_FORMAT.format(*cells)


# class Node:
#     def __init__(self, move=None, parent=None, state=None):
#         self.move = move
#         self.parentNode = parent
#         self.childNodes = []
#         self.wins = 0
#         self.visits = 0
#         self.untriedMoves = state.GetMoves()
#         self.playerJustMoved = state.playerJustMoved
#
#     def UCTSelectChild(self):
#         s = sorted(self.childNodes, key=lambda c: c.wins / c.visits + sqrt(2 * log(self.visits) / c.visits))
#         return s[-1]
#
#     def AddChild(self, m, s):
#         n = Node(move=m, parent=self, state=copy.deepcopy(s))
#         self.untriedMoves.remove(m)
#         self.childNodes.append(n)
#         return n
#
#     def Update(self, result):
#         self.visits += 1
#         self.wins += result
#
#     def __repr__(self):
#         return "[M" + str(self.move) + " W/V " + str(self.wins) + "/" + str(self.visits) + " U" + str(
#             self.untriedMoves) + "]"
#
#     def ChildrenToString(self):
#         s = ""
#         for c in self.childNodes:
#             s += str(c) + "\n"
#         return s
#
#
# def UCT(rootstate, itermax):
#     rootnode = Node(state=rootstate)
#
#     for i in range(itermax):
#         node = rootnode
#         state = copy.deepcopy(rootstate)
#
#         # selection
#         while node.untriedMoves == [] and node.childNodes != []:
#             node = node.UCTSelectChild()
#             state.DoMove(node.move)
#
#         # Expansion
#         if node.untriedMoves != []:
#             m = random.choice(node.untriedMoves)
#             state.DoMove(m)
#             node = node.AddChild(m, state)
#
#         # simulation
#         while state.GetMoves() != []:
#             state.DoMove(random.choice(state.GetMoves()))
#
#         # BackPropagation
#         while node != None:
#             node.Update(state.GetResult(node.playerJustMoved))
#             node = node.parentNode
#
#     print(rootnode.ChildrenToString())
#
#
#     s = sorted(rootnode.childNodes, key=lambda c: c.wins / c.visits)
#     return sorted(s, key=lambda c: c.visits)[-1].move



def UCTPlayGame():
    state = TicTacToe()

    while state.GetMoves() != []:
        print(str(state))
        if state.playerJustMoved == 1:
            a = random.choice(table)
            m = a
            table.remove(a)
        else:
            a = random.choice(table)
            m = a
            table.remove(a)
        state.DoMove(m)

    if state.GetResult(state.playerJustMoved) == 2.0:


        print("Player " + str(state.playerJustMoved) + " Wins!!")
        # eTime = time.time()
        # print('AI가 수를 계산하는데 걸린 시간 : ', eTime - sTime)
    elif state.GetResult(state.playerJustMoved) == 0.0:


        print("Player " + str(3 - state.playerJustMoved) + " Wins!!")
        # eTime = time.time()
        # print('AI가 수를 계산하는데 걸린 시간 : ', eTime - sTime)
    else:
        print("Draw!!")
        # eTime = time.time()
        # print('AI가 수를 계산하는데 걸린 시간 : ', eTime - sTime)

if __name__ == "__main__":
    UCTPlayGame()

