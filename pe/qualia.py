from random import uniform
nums = [round(uniform(0, 1000), 3) for _ in range(100)]

nums.sort(key = lambda x: x - int(x))
print nums

# Sort nums using only the fractional portion of each number. 
# So under this ordering 50.10 is bigger than 100.01