

# zero=S.count("0")
# one=S.count("1")
# A=S[0:zero]
# B=S[zero:]
# print(A)
# print(B)
# sum=A.count("0")+B.count("1")
# print(sum)

def addbinary(s):
    ones = s.count("1")
    zeros,ans = 0, 0
    for i in range(len(s) - 1):
        if s[i] == "0":
            zeros += 1
        else:
            ones -= 1
        ans = max(ans, ones + zeros)
    return ans
S=input()
print(addbinary(S))

