strings = input().split()
palindrome = input()

palindromes = [word for word in strings if word == "".join(reversed(word))]

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")
