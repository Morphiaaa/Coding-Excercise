def  reducedFractionSums(expressions):
    if not expressions or len(expressions)==0:
        return []
    
    res = []
    for exp in expressions:
        nums = []
        fractions = exp.split('+')
        for item in fractions:
            nums.extend(item.split('/'))
        
        denomi = int(nums[1]) * int(nums[-1])
        numera = int(nums[0]) * int(nums[-1]) + int(nums[1]) * int(nums[2])
        print denomi, numera
        if denomi == numera:
            prime = minPrimeFactor(denomi)
            print prime
            new_denomi = int(nums[1])/prime
            print new_denomi
            new_prime = minPrimeFactor(new_denomi)
            print new_prime
            res.append('/'.join([str(new_prime), str(new_prime)]))
        else:
            gcd = calGCD(denomi, numera)
            denomi /= gcd
            numera /= gcd
            res.append('/'.join([str(numera), str(denomi)]))
        
    return res

def minPrimeFactor(n):
    prime = [0]*(n+1)
    prime[1] = 1
    
    for i in range(2, n+1):
        if prime[i] == 0:
            prime[i] = i
            
            j = 2*i
            while j <= n:
                if prime[j] == 0:
                    prime[j] = i
                j += i
    return prime[n]
            
def calGCD(a, b):
    if a%b != 0:
        return calGCD(b, a%b)
    else:
        return b

#print minPrimeFactor(7)
print reducedFractionSums(['1/35+34/35'])