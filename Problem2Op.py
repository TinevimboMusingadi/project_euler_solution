# Start with the first two even terms
#The Logic (The "Every 3rd" Trick)
#If you write out the sequence:1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
#We  will see that the even numbers (2, 8, 34, 144) obey 
#their own recursive formula:E_{next} = 4* E_{current} + E_{prev}

# We assume a 'ghost' previous even term of 0 to make the formula work for the first step
prev_even = 0
curr_even = 2

total_sum = 0

while curr_even <= 4000000:
    total_sum += curr_even
    
    # Calculate the next even number directly
    # Formula: Next = 4 * Current + Previous
    next_even = 4 * curr_even + prev_even
    
    # Update variables
    prev_even = curr_even
    curr_even = next_even

print(total_sum)

