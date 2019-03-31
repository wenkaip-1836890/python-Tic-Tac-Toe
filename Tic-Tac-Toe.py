'''Tic-Tac-Toe.py
("Tic-Tac-Toe" problem)
A SOLUZION problem formulation.  UPDATED AUGUST 2018.
The XML-like tags used here may not be necessary, in the end.
But for now, they serve to identify key sections of this
problem formulation.  It is important that COMMON_CODE come
before all the other sections (except METADATA), including COMMON_DATA.
'''
#<METADATA>
SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Tic-Tac-Toe"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['Ken Pan', 'Guanxuan Wu']
PROBLEM_CREATION_DATE = "29-AUG-2018"
PROBLEM_DESC=\
'''This version differs from earlier ones by (a) using a new
State class to represent problem states, rather than just
a dictionary, and (b) avoidance of list comprehensions
and the use of default parameter values in lambda expressions.

The following are new methods here for the State version of
the formulation:
__eq__, __hash__, __str__, and the implcit constructor State().

The previous version was written to accommodate the
Brython version of the solving client
and the Brython version of Python.
However, everything else is generic Python 3, and this file is intended
to work a future Python+Tkinter client that runs on the desktop.
Anything specific to the Brython context should be in the separate 
file MissionariesVisForBRYTHON.py, which is imported by this file when
being used in the Brython SOLUZION client.

The operators are defined here in the same order as on the
worksheet "Depth-First Search for the M&C Problem."
'''

#</METADATA>

#<COMMON_DATA>
#</COMMON_DATA>

#<COMMON_CODE>
#M=0
#C=1
#LEFT=0
#RIGHT=1
import random
import copy
class State:
    def __init__(self, old=None):        # Default new state is a state objects initialized as the
        # initial state.
        # If called with old equal to a non-empty state, then
        # the new instance is made to be a copy of that state.
        self.map = [[0,0,0],
                [0,0,0],
                [0,0,0]]
        if not old is None:
            self.map = copy.deepcopy(old.map)

    def can_move(self, row, col):
        '''Tests whether it is legal to put the chess piece on
        the aimed cell'''
        if (self.map[row][col] == 0):
            return True
        return False

    def move(self, row, col, person):
        '''Assuming it is legal to make the move, this makes a new
        state representing the result of puting a new chess piece
        on a cell.'''
        flag = False
        news = State(old=self) # Make a copy of the current state.
        if (person == 'X'):
            news.map[row][col] = 1
            for i in range(len(news.map)):
                for j in range(len(news.map[i])):
                    if (news.map[i][j] == 0):
                        ait=news.ai_move(2)
                        news.map[ait[0]][ait[1]] = 2
                        flag = True
                    if(flag):
                        break
                if(flag):
                    break

        elif (person == 'O'):
            news.map[row][col] = 2
            ait = news.ai_move(1)
            news.map[ait[0]][ait[1]] = 1
        return news

    def ai_move(self, role):
        initialstate = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        countofX=0
        if self.map == initialstate:
            if role == 1:
                rd = random.choice(list(range(3)))
                if rd == 0:
                    return (0,0)
                elif rd == 1:
                    return (1,1)
                elif rd == 2:
                    return (2,2)
        else:
            for i in self.map:
                for j in i:
                    if j==1:
                        countofX+=1
            if (role == 2)&(countofX==1):
                if (self.map[0][0] == 1) or (self.map[0][2] == 1) or (self.map[2][0] == 1) or (self.map[2][2] == 1):
                    print('ping')
                    return (1,1)
                elif self.map[1][1] == 1:
                    rd = random.choice(list(range(4)))
                    if rd == 0:
                        return (0,0)
                    elif rd == 1:
                        return (2,0)
                    elif rd == 2:
                        return (0,2)
                    else:
                        return (2,2)
        return self.ai_move_common(role)
    def ai_move_common(self, role):
        d = {(self.map[0][0], self.map[0][1], self.map[0][2]): ([0, 0], [0, 1], [0, 2]), \
             (self.map[0][0], self.map[1][1], self.map[2][2]): ([0, 0], [1, 1], [2, 2]), \
             (self.map[0][0], self.map[1][0], self.map[2][0]): ([0, 0], [1, 0], [2, 0]), \
             (self.map[0][1], self.map[1][1], self.map[2][1]): ([0, 1], [1, 1], [2, 1]), \
             (self.map[0][2], self.map[1][2], self.map[2][2]): ([0, 2], [1, 2], [2, 2]), \
             (self.map[1][0], self.map[1][1], self.map[1][2]): ([1, 0], [1, 1], [1, 2]), \
             (self.map[2][0], self.map[2][1], self.map[2][2]): ([2, 0], [2, 1], [2, 2]), \
             (self.map[0][2], self.map[1][1], self.map[2][0]): ([0, 2], [1, 1], [2, 0])}
        available_nodes = []
        noq = {}
        for i in range(3):
            for j in range(3):
                if self.map[i][j] == 0:
                    available_nodes.append((i, j))
        for i in available_nodes:
            routes = []
            qz = 0
            jj = 0
            for route, pts in d.items():
                valid = False
                for j in pts:
                    if (j[0] == i[0]) & (j[1] == i[1]):
                        routes.append(pts)
                        valid = True
                        break
                if valid:
                    countr = 0
                    counte = 0
                    countd = 0
                    for j in route:
                        if j == role:
                            countr += 1
                        elif j == 0:
                            counte += 1
                        else:
                            countd += 1
                    if counte == 3:
                        qz += 2
                    elif (counte == 2) & (countr == 1):
                        qz += 3
                        jj += 1
                    elif (counte == 2) & (countd == 1):
                        qz += 1
                    elif countr==2:
                        qz+=65536
                    elif countd==2:
                        qz+=32768
            if jj >= 2:
                qz = 16384
            noq[i] = qz
        best = -1
        bestc = []
        for i, qz in noq.items():
            if qz > best:
                bestc.clear()
                best = qz
                bestc.append(i)
            elif qz == best:
                bestc.append(i)
        choice = random.choice(bestc)
        return (choice[0],choice[1])

    def is_goal(self):
        '''If one player gets three in a row or if there is no more
        cell to put the chess piece in, then s is a goal state.'''
        if (self.map[0][0] == self.map[1][0] == self.map[2][0] != 0):
            if (self.map[0][0] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[0][1] == self.map[1][1] == self.map[2][1] != 0):
            if (self.map[0][1] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[0][2] == self.map[1][2] == self.map[2][2] != 0):
            if (self.map[0][2] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[0][0] == self.map[0][1] == self.map[0][2] != 0):
            if (self.map[0][0] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[1][0] == self.map[1][1] == self.map[1][2] != 0):
            if (self.map[1][0] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[2][0] == self.map[2][1] == self.map[2][2] != 0):
            if (self.map[2][0] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[0][0] == self.map[1][1] == self.map[2][2] != 0):
            if (self.map[0][0] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        if (self.map[0][2] == self.map[1][1] == self.map[2][0] != 0):
            if (self.map[0][2] == 1):
                print('X wins')
            else:
                print('O wins')
            return True

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if (self.map[i][j] == 0):
                    return False
        print('Draw')
        return True

    def __eq__(self, s2):
        if s2==None: return False
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if (self.map[i][j] != s2.map[i][j]):
                    return False
        return True

    def __str__(self):
        st = '(' + str(self.map) + ')'
        return st

    def __hash__(self):
        return (str(self)).__hash__()

def goal_test(s): return s.is_goal()

def goal_message(s):
  return "Congratulations on successfully completing the tic-tac-toe game!"

def copy_state(s):
  return State(old=s)

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_STATE = State()
#</INITIAL_STATE>

choice=''
while (choice != 'X') and (choice != 'O'):
    choice = input("Choose 'X' or 'O' to use for one game: ")
    if choice != 'X' and choice != 'O':
        print("Invalid input!")
if (choice == 'X'):
    AI_player = 'O'
else:
    i = random.choice([0,1,2])
    INITIAL_STATE.map[i][i] = 1
    AI_player = 'X'

#<OPERATORS>
phi0 = Operator("Put the character on cell 1",
  lambda s: s.can_move(0,0),
  lambda s: s.move(0,0,choice))

phi1 = Operator("Put the character on cell 2",
  lambda s: s.can_move(0,1),
  lambda s: s.move(0,1,choice))

phi2 = Operator("Put the character on cell 3",
  lambda s: s.can_move(0,2),
  lambda s: s.move(0,2,choice))

phi3 = Operator("Put the character on cell 4",
  lambda s: s.can_move(1,0),
  lambda s: s.move(1,0,choice))

phi4 = Operator("Put the character on cell 5",
  lambda s: s.can_move(1,1),
  lambda s: s.move(1,1,choice))

phi5 = Operator("Put the character on cell 6",
  lambda s: s.can_move(1,2),
  lambda s: s.move(1,2,choice))

phi6 = Operator("Put the character on cell 7",
  lambda s: s.can_move(2,0),
  lambda s: s.move(2,0,choice))

phi7 = Operator("Put the character on cell 8",
  lambda s: s.can_move(2,1),
  lambda s: s.move(2,1,choice))

phi8 = Operator("Put the character on cell 9",
  lambda s: s.can_move(2,2),
  lambda s: s.move(2,2,choice))

OPERATORS = [phi0, phi1, phi2, phi3, phi4, phi5, phi6, phi7, phi8]

#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>

#</STATE_VIS>
