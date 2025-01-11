def all_variants(text):
    for length in range(1, len(text)+1):
        for pos in range(len(text)+1-length):
            yield text[pos:pos+length]

a = all_variants("abc")
for i in a:
    print(i)



