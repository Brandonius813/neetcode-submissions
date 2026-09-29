def concatenate(s1: str, s2: str) -> str:
    newstring = s1 + s2
    if len(newstring) > 10:
        return "Too long!"
    else:
        return newstring




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
