#assign to text file
#create list
def quiz():
    text_file = "quiz_key.txt"
    questions = []

    #ask for questions and choices
    while True:
        print("\nEnter a question.")
        question = input("Question: ")

        choices = {}
        choices["a"] = input("\nChoice a: ")
        choices["b"] = input("Choice b: ")
        choices["c"] = input("Choice c: ")
        choices["d"] = input("Choice d: ")

        #ask for correct answer
        while True:
            answer = input("Correct answer (a/b/c/d: ").lower()
            if answer in choices:
                break
            else:
                print("Please choose a, b, c, or d.")

    #append the questions and choices
    #ask if the user wants to input more questions
    #store to text file
#call def