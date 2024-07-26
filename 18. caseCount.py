def count_upper_lower(sentence):
    upper_count = 0
    lower_count = 0
    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

sentence = input("enter a sentence: ")

upper, lower =  count_upper_lower(sentence)

print("total upper case characters:", upper)
print("total lower case charchters:", lower)       