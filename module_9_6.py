def all_variants(text):
    for n in range(len(text)):
        for m in range(len(text) - n):
            yield text[m:m + n + 1]


a = all_variants("abc")
for i in a:
    print(i)
