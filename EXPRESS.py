# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import unittest
from enum import Enum

class State(Enum):
    '''
    we can take the simplify operation as a finite state machine which has three states.
    For each '(', we create a new level.
    There are three stack symbols and each represents the state of the machine for the current level:
    PRE: The state after creating a new level.
    Transfer to other state when encountering any characters except ')'.
    
    INNER: The state we are in the inside of the bracket which need to be deleted.
    Enter this state when we encounter a '(' in state PRE.
    
    FINISH: The state that when the current level has been processed. 

    '''
    PRE = 0
    INNER = 1
    FINISH = 2
    
class Parser(object):
    def __init__(self, expressionTree):
        '''
        type expressionTree: str
        '''
        exp, opt = expressionTree.strip().split('/')
        t_expression = []   
        # Remove all the spaces in expressions.
        for e in exp:
            if e != ' ':
                t_expression.append(e)
        self.expression = ''.join(t_expression)
        
        t_operators = []
        # Remove all the spaces in operators.
        for o in opt:
            if o != ' ':
                t_operators.append(o)
        self.operators = ''.join(t_operators)
                
    
    def operate(self):
        '''
        Process the expressions by each operator.
        '''            
        for op in self.operators:
            if op == 'R':
                self.reverse()
            elif op == 'S':
                self.simplify()
                
    def reverse(self):
        array = list(self.expression)
        array.reverse()
        #Reverse the expression
        for i in range(len(array)):
            if array[i] != '(' and array[i] != ')':
                continue
            #Replace left bracket with right bracket and vice versa
            elif array[i] == '(':   
                array[i] = ')'
            else:
                array[i] = '('
        self.expression = ''.join(array)
    
    def simplify(self):
        '''
        When encountering a '(', we append a new symbol into the stack, and the machine create a new level.
        when encountering a ')', we pop the one symbol from stack, and the machine leaving from this level.
        All input characters will be appended into the stack except when we are in the 'PRE->INNER' and 
        'INNER->FINISH' process.
        '''
        level = [State.PRE]
        res = []
        
        for char in self.expression:
            if char == '(':
                if level[-1] == State.PRE:
                    level[-1] = State.INNER  #Do the transiton of 'PRE->INNER'
                else:
                    res.append(char)   
                level.append(State.PRE)
            elif char == ")":
                level.pop()
                if level[-1] == State.INNER:  
                    level[-1] = State.FINISH  #Do the transition of 'INNER->FINISH'
                else: 
                    res.append(char)
            else:
                if level[-1] == State.PRE:
                    level[-1] = State.FINISH
                res.append(char)
        self.expression = ''.join(res)
                          
def main():
    for line in sys.stdin:
        p = Parser(line)
        p.operate()
        print p.expression

if __name__ == '__main__':
    main()
'''
More Test Cases:
test_input and expected_output:
<'(AB)C((DE)F)/SRS', 'FEDCBA'>
<'(AB)(C(DE))/SS', '(AB)(C(DE))'>
<'((AB)C)D(((E)FG)H)/SR', 'HGFE(DCBA)'>
<'((AB)C)D(((E)FG)H)/RS', 'H(GF(E))D(C(BA))'>
<'(AB(CD((EF)G)H))(IJ)/SRSRRSRS', 'AB(CD(EFG)H)IJ'>
<'(A(BC(D(E((X)K(L)))F))GH(IJK))/S', A(BC(D(E(XK(L)))F))GH(IJK)'>

'''