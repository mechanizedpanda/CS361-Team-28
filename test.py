def print_adlib():
    """
    Short adlib with 3 entries (just a silly thing for the test commit)
    """
    word1 = str(input("Please enter a name: "))
    word2 = str(input("Please enter an adjective: "))
    word3 = str(input("Please enter a noun: "))
    phrase = "Hi, my name is" + " " + word1 + ". " + "I have a" + " " + word2 + " " + word3 + "."

    print(phrase)


print_adlib()