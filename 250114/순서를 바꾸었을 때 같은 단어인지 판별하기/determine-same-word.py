word1 = list(input())
word2 = list(input())

# Write your code here!
word1.sort()
word2.sort()

print("Yes") if word1 == word2 else print("No")