def check_string(text):
    if text.startswith("The"):
        return "Found it!"
    else:
        return "Nope"
    
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

print(check_string(str1))
print(check_string(str2))
print(check_string(str3))