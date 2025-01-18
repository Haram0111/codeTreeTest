binary = list(input())
binary = binary[::-1]
# Write your code here!
answer = 0
for i in range(len(binary)):
    answer += int(binary[i]) * pow(2,i)
print(answer)