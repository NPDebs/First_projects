# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(string1, string2):
    # [assignment] Add your code here
    
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    if sorted(string1) == sorted(string2):
        return True
    else:
        return False
print(find_anagram("mad", "dam"))

print(find_anagram("jam", "dam"))
   
