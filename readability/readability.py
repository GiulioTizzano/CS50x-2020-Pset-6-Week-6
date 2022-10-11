from cs50 import get_string

def main():
    # prompting user for text
    s = get_string("Text: ")
    letters = 0
    words = 1
    sentences = 0
    # setting conditions for the letters, words and sentences
    for i, n in enumerate(s):
        if n.isalpha():
            letters += 1
        elif n.isspace() and (s[i+1].isalpha() or s[i+1] == '"'):
            words += 1
        elif n == "!" or n == "?" or n == ".":
            sentences += 1
    # print(f"Letters: {letters}\nWords: {words}\nSentences: {sentences}")


    # calculation with the Coleman.Liau index formula
    # defining L and S in a mathematical fractional ratio

    L = letters * 100 / words
    S = sentences * 100 / words
    grade = round(0.0588 * L - 0.296 * S - 15.8)

    #print the grade
    if grade >= 0 and grade < 16:
        print(f"Grade {grade}")

    elif grade < 0:
        print(f"Before Grade 1")

    else:
        print(f"Grade 16+")
main()