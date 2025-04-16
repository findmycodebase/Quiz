questions = [
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "London",
            "B": "Berlin",
            "C": "Paris",
            "D": "Madrid"
        },
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for data science?",
        "options": {
            "A": "Python",
            "B": "Java",
            "C": "HTML",
            "D": "CSS"
        },
        "answer": "A"
    },
    {
        "question": "What is 7 * 6?",
        "options": {
            "A": "42",
            "B": "36",
            "C": "48",
            "D": "52"
        },
        "answer": "A"
    },
    {
        "question": "Which of these is a mammal?",
        "options": {
            "A": "Crocodile",
            "B": "Shark",
            "C": "Whale",
            "D": "Penguin"
        },
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "define",
            "B": "function",
            "C": "def",
            "D": "func"
        },
        "answer": "C"
    }
]

score=0
for item in questions :
   print("\n" + item["question"])
   for key , val in item["options"].items() :
       print(f"{key}: {val}")

   user_answer = input("Your answer (A, B, C, or D): ").upper()

   if user_answer == item["answer"] :
     print("Correct!")
     score+=1
   else:
      print("Wrong. The correct answer is", item["answer"])

print(f"\nYou got {score} out of {len(questions)} correct.")