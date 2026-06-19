# 🎯 Quiz Game
# Concepts used: variables, list, loops, conditionals, operators

import time

# =====================
# Questions & Answers
# =====================
questions = [
    "1. Python mein list banane ke liye kaunsa bracket use hota hai?\n   a) {}  b) []  c) ()  d) <>\n   Answer: ",
    "2. HTML ka full form kya hai?\n   a) Hyper Text Markup Language\n   b) High Tech Modern Language\n   c) Hyper Transfer Mode Language\n   d) None\n   Answer: ",
    "3. CSS ka use kisliye hota hai?\n   a) Database banane ke liye\n   b) Website styling ke liye\n   c) Server banane ke liye\n   d) None\n   Answer: ",
    "4. Python mein comment likhne ke liye kaunsa symbol use hota hai?\n   a) //  b) /* */  c) #  d) --\n   Answer: ",
    "5. Loop ka use kisliye hota hai?\n   a) Variable store karne ke liye\n   b) Ek kaam baar baar karne ke liye\n   c) Error pakadne ke liye\n   d) None\n   Answer: ",
]

correct_answers = ["b", "a", "b", "c", "b"]

explanations = [
    "✅ Sahi! Python mein list [] se banti hai. Jaise: fruits = ['apple', 'mango']",
    "✅ Sahi! HTML = Hyper Text Markup Language — web pages banane ki language.",
    "✅ Sahi! CSS = Cascading Style Sheets — website ko sundar banana CSS ka kaam hai.",
    "✅ Sahi! Python mein # se comment likhte hain. Jaise: # yeh comment hai",
    "✅ Sahi! Loop se ek kaam baar baar bina repeat likhe kiya ja sakta hai.",
]

# =====================
# Game Start
# =====================
print("=" * 50)
print("       🎯 PYTHON & WEB QUIZ GAME 🎯")
print("=" * 50)

name = input("\nApna naam batao: ")
print(f"\nWelcome, {name}! Quiz shuru ho raha hai...\n")
time.sleep(1)

# Variables
score = 0
total = len(questions)
wrong_questions = []

# =====================
# Quiz Loop
# =====================
for i in range(total):
    print("-" * 40)
    answer = input(questions[i]).strip().lower()

    if answer == correct_answers[i]:
        print(explanations[i])
        score = score + 1
    else:
        print(f"❌ Galat! Sahi answer tha: ({correct_answers[i]})")
        print(explanations[i].replace("✅ Sahi!", "💡 Explanation:"))
        wrong_questions.append(i + 1)

    print()
    time.sleep(0.5)

# =====================
# Result
# =====================
print("=" * 50)
print(f"       📊 {name} KA RESULT")
print("=" * 50)
print(f"  Sahi jawab  : {score} / {total}")
print(f"  Score       : {score * 20} / 100")

# Grade using conditionals
if score == 5:
    grade = "⭐ Excellent! Perfect Score!"
elif score == 4:
    grade = "👍 Very Good! Almost perfect!"
elif score == 3:
    grade = "😊 Good! Thoda aur practice karo."
elif score == 2:
    grade = "📚 Average. Concepts revise karo."
else:
    grade = "💪 Keep trying! Practice se sab aata hai."

print(f"  Grade       : {grade}")

# Wrong questions
if len(wrong_questions) > 0:
    print(f"\n  ⚠️  Yeh questions dobara padho: {wrong_questions}")
else:
    print("\n  🎉 Waah! Sabhi questions sahi the!")

print("=" * 50)
print("Quiz khelne ke liye shukriya! 😊")
