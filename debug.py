s = "ADOBECODEBANC"
t = "ABC"

cur_length, max_length = float("inf"), float("inf")
result = ""
l = 0
for r in range(len(s)):
    while t in s[l:r]:
        cur_length = min(cur_length, r-l+1)
        l += 1
    if cur_length < max_length:
        result = s[l-1:r]
        
result


