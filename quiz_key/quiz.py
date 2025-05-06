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
        choices["a"] = input("Option a: ")
        choices["b"] = input("Option b: ")
        choices["c"] = input("Option c: ")
        choices["d"] = input("Option d: ")

        while not all(choices[key] for key in ['a', 'b', 'c', 'd']):
            print("Please make sure all options are filled in.")
            choices['a'] = input("Option a: ")
            choices['b'] = input("Option b: ")
            choices['c'] = input("Option c: ")
            choices['d'] = input("Option d: ")

        #ask for correct answer
        while True:
            answer = input("Correct answer (a/b/c/d): ").lower()
            if answer in choices:
                break
            else:
                print("Please choose a, b, c, or d.")

        #append the questions and choices
        questions.append({
            "question": question,
            "choices": choices,
            "answer": answer,
        })

        #ask if the user wants to input more questions
        cont = input("Do you want to enter another question? (y/n): ").strip().lower()
        if cont != "y":
            print("Bye.")
            break

    #store to text file
    with open(text_file, "a") as file:
        for q in questions:
            file.write(f"{q['question']}\n")
            file.write(f"a. {q['choices']['a']}\n")
            file.write(f"b. {q['choices']['b']}\n")
            file.write(f"c. {q['choices']['c']}\n")
            file.write(f"d. {q['choices']['d']}\n")
            file.write(f"answer: {q['answer']}\n")
            file.write("\n")

    print(f"\n{len(questions)} question/s saved to '{text_file}'.")

#call def
if __name__ == "__main__":
    quiz()
