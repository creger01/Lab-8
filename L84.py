#the authors' names are: Cadyn and Sarah
def until_dot(words):
    total = 0
    while total < len(words) and words[total] != ".":
        total += 1
    print(words[:total])

until_dot("This is a sentence. This is another.")
until_dot("www.mynameiscadyn.com")
