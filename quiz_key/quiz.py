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
        questions.append({
            "questions": questions,
            "choices": choices,
            "answer": answer,
        })

        #ask if the user wants to input more questions
        cont = input("Do you want to enter another question? (y/n): ").strip().lower()
        if cont != "yes":
            break

    #store to text file
    with open(text_file, "w") as file:
        for q in questions:
            file.write(f"{q['question']}\n")
            file.write(f"{q['choices']['a']}\n")
            file.write(f"{q['choices']['b']}\n")
            file.write(f"{q['choices']['c']}\n")
            file.write(f"{q['choices']['d']}\n")
            file.write(f"answer: {q['answer']}\n")

    print(f"\n{len(questions)} question/s saved to '{text_file}'.")
    
#call def