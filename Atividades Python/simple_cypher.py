content = input("Type a simple world or phrase: ")
content_cyphered = ""
for letter in content:
    if letter in "aeioulm":
        content_cyphered += '*'
    else:
        content_cyphered += letter

print("\n\nCyphered content - %s" %content_cyphered)