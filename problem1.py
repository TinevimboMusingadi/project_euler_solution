## 
# 1. Sum of multiples of 3
# Limit is 333, so range must go to 334
count_3 = 0
for i in range(1, 334):
    count_3 += i * 3

# 2. Sum of multiples of 5
# Limit is 199, so range must go to 200
count_5 = 0
for i in range(1, 200):
    count_5 += i * 5

# 3. Sum of multiples of 15 (The overlap)
# Limit is 66, so range must go to 67
count_15 = 0
for i in range(1, 67):
    count_15 += i * 15

# Calculation
final = (count_3 + count_5) - count_15
print(final)