'''
A magic index in an array A[0.. .n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
FOLLOW UP
What if the values are not distinct?
'''

'''
这道题的Follow up是说如果数组由重复项怎么处理，那么传统的二分搜索法就会失效，因为下列这种情况可能存在：

-10	-5	2	2	2	3	4		9	12	13
这种情况符合题意，但是左右两边都会出现魔法序号，所以二分查找法会失效。那么我们难道又要用地毯式搜索了么，其实也不必，
我们可以用一种类似于二分搜索法的递归方法来解决问题，就拿上面那个例子来说，第一次找到比较完中间点后，
由于左右两边都会出现答案，所以我们左右半段要分别递归一下，这里我们可以加一个trick来优化算法，比如要递归左半段时，
那么新的右边界就可以设为min(mid - 1, nums[mid])，同理递归右半段时，左边界可以设为max(mid + 1, nums[mid])。
还有个小trick，就是如果左半段搜到了答案，那么直接返回即可，不用再搜右半段，因为题目让我们找一个就行了，
没说要找出所有的Magic index
'''

#This solution is for the follow up


def findMagicIndex(array):
	if not array or len(array) == 0:
		return None

	return helper(array, 0, len(array)-1)

def helper(array, left, right):
	if right < left:
		return -1

	mid = (left + right)/2

	if mid == array[mid]:
		return mid
	else:
		left = helper(array, left, min(mid-1, array[mid]))
		if left >= 0:
			return left
		right = helper(array, max(mid+1, array[mid]), right)
		return right

print findMagicIndex([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13])