text = input()
desti = input()

if desti in text:
    print(text.find(desti))
else:
    print("-1")