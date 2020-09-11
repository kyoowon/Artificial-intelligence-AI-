from abc import ABC, abstractmethod #abstract base class
from collections import defaultdict
import math

class MCTS:
    "Monte Carlo tree searcher. 먼저 rollout한 다음. 위치(move) 선택"
    def __init__(self, c=1):
        self.Q = defaultdict(int)   # 노드별 이긴 횟수(reward) 값을 0으로 초기화
        self.N = defaultdict(int)   # 노드별 방문횟수(visit cout)를 0으로 초기화
        self.childen = dict()       # 노드의 자식노드
        self.c = c                  # UCT 계산에 사용되는 계수


    def choose(self, node):
        "node의 최선인 자식 노드 선택"
        if node.is_terminal():      # node가 단말인 경우 오류
            raise RuntimeError(f"choose called on terminal node {node}")
        if node not in self.childen:    # node가 childen에 포함되지 않으면 무작위 선택
            return node.find_random_child()

        def score(n):   # 점수 계산
            if self.N[n] == 0:
                return float("-inf")    # 한번도 방문하지 않은 노드인 경우 - 선택 배제
            return self.Q[n] / self.N[n] # 평균 점수
        
        return max(self.childen[node], key=score)

    def do_rollout(self, node):
        "게임 트리에서 한 층만 더 보기"
        path = self._select(node)
        leaf = path[-1]
        self._expand(leaf)
        reward = self._simulate(leaf)
        self._backpropagate(path, reward)
    
    def _select(self, node):    #t선택 단계
        "node의 아직 시도해보지 않은 자식 노드 찾기"
        path = []
        while True:
            path.append(node)
            if node not in self.childen or not self.childen[node]:
                # node의 child나 grandchild가 아닌 경우: 아직 시도해보지 않은 것 또는 단말 노드
                return path
            unexplored = self.childen[node] - self.childen.keys() # 차집합
            if unexplored:
                n = unexplored.pop()
                path.append(n)
                return path
            node = self._uct_select(node) # 한 단계 내려가기

    def _expand(self, node):
        if node in self.childen:
            return
        self.childen[node] = node.find_children()

    def _simulate(self, node):
        invert_reward = True
        while True:
            if node.is_terminal():
                reward = node.reward()
                return 1 - reward if invert_reward else reward
            node = node.find_random_child()
            invert_reward = not invert_reward
            
    def _backpropagate(self, path, reward): #역전파 단계
        for node in reversed(path): #역순으로 가면서 Monte Carlo 시뮬레이션 결과 반영
            self.N[node] += 1
            self.Q[node] += reward
            reward = 1 - reward # 자신에게는 1 상대에게는 0, 또는 그 반대

    def _uct_select(self, node):
        assert all(n in self.childen for n in self.childen[node])
        log_N_vertex = math.log(self.N[node])

        def uct(n):
            return self.Q[n] / self.N[n] + self.c * math.sqrt(2*log_N_vertex / self.N[n])

        return max(self.childen[node], key=uct)

class Node(ABC):
    
    @abstractmethod
    def find_children(self):
        return set()

    @abstractmethod
    def find_random_child(self):
        return None

    @abstractmethod
    def is_terminal(self):
        return True

    @abstractmethod
    def reward(self):
        return 0

    @abstractmethod
    def __hash__(self):
        return 123456789

    @abstractmethod
    def __eq__(node1, node2):
        return True


from collections import namedtuple
from random import choice

TTTB = namedtuple("TicTacToeBoard", "tup turn winner terminal")

class TicTacToeBoard(TTTB, Node):
    def find_children(board):
        if board.terminal:
            return set()
        return {
            board.make_move(i) for i, value in enumerate(board.tup) if value is None
        }

    def reward(board):
        if board.terminal:
            return None
        empty_spots = [i for i, value in enumerate(board.tup) if value is None]
        return board.make_move(choice(empty_spots))

    def reward(board):
        if not board.terminal:
            raise RuntimeError(f"reward called on nonterminal {board}")
        if board.winner is board.turn:
            