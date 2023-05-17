path = "books/frankenstein.txt"
f = open(path,"r")
file_contents = f.read()
file_contents = file_contents.lower()

words = file_contents.split()
wordcount = len(words)

lettercount = dict()
for letter in file_contents:
    if letter in lettercount:
        lettercount[letter] += 1
    else:
        lettercount[letter] = 1

listofletters = []
for k,v in lettercount.items():
    if k.isalpha():
        listofletters.append((k,v))


listofletters.sort(key=lambda x:x[1],reverse= True)

print("--- Begin report of {} ---".format(path))
print(f"{wordcount} words found in the document\n")

for pair in listofletters:
    print(f"The '{pair[0]}' character was found {pair[1]} times")