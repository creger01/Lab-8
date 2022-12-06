#the authors' names are: Cadyn and Sarah
def total_length(words):
    total = 0
    for x in words:
        total = len(x) + total
    print(total)


total_length(["Queen", "rules"])
