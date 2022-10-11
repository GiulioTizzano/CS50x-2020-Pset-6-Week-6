from csv import reader, DictReader
from sys import argv
 # prompting user correctly
if len(argv) < 3:
    print("usage error, dna.py sequence.txt database.csv")
    exit()

# reading DNA sequence from file
with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

# storing it in a string
dna = dnalist[0]
# creating a dictionary in order to store the list
sequences = {}

# extracting the sequences from the database into a list
with open(argv[1]) as peoplefile:
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)
        break

# copying the list into the dictionary, where the genes are the keys
for item in dnaSequences:
    sequences[item] = 1

# iterating through the dna sequence, if finds repetitions of the values from sequence dictionary, count them
for key in sequences:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(dna)):
        # after having counted a sequence it skips at the end of it to avoid counting again
        while temp > 0:
            temp -= 1
            continue

        # if the segment of dna corresponds to the key and there is a repetition of it we start counting
        if dna[i: i + l] == key:
            while dna[i - l: i] == dna[i: i + l]:
                temp += 1
                i += l

            # it compares the value to the previous longest sequence and if it is longer it overrides it
            if temp > tempMax:
                tempMax = temp

    # store the longest sequences in the dictionary using the correspondent key
    sequences[key] += tempMax

# open and iterate trough the database of people treating each one like a dictionary so it can compare to the sequences one
with open(argv[1], newline='') as peoplefile:
    people = DictReader(peoplefile)
    for person in people:
        match = 0
        # compares the sequences to every person and prints name before leaving the program if there is a match
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                match += 1
        if match == len(sequences):
            print(person['name'])
            exit()

    print("No match")