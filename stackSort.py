class Solution(object):
	def stacksort(self, stack):
		if len(stack) != 0:
			temp = stack.pop()       #First pop all the elements from the stack and store poped element in variable 'temp'. 
			self.stacksort(stack)
			self.stackinsert(stack, temp)   #Now stack is empty and 'stackinsert' function is called and it inserts 
             # element at the bottom of the stack. 

	def stackinsert(self, stack, x):
		if not stack or x > stack[-1]:
			stack.append(x)
		else:
			temp = stack.pop()
			self.stackinsert(stack, x)
			stack.append(temp)

S = Solution()
stack = [-2, 7, 0, 28, -9, 32]
S.stacksort(stack)
print stack
