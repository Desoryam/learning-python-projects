# kon banega karorpati

ques = [
    "What is the capital of Australia?",
    "Who wrote the play Romeo and Juliet?",
    "Which planet in our solar system is known as the Red Planet?",
    "What is the chemical symbol for gold?",
    "In which year did the Titanic sink?",
    "Which country is home to the Great Wall?",
    "Who painted the Mona Lisa?",
    "What is the largest ocean on Earth?"
]

ans = [
    ["Canberra", "Sydney", "Melbourne", "Perth"],
    ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    ["Mars", "Venus", "Jupiter", "Saturn"],
    ["Au", "Ag", "Cu", "Fe"],
    ["1912", "1913", "1914", "1915"],
    ["China", "India", "Russia", "Mexico"],
    ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
    ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
]

c_ans = ["Canberra", "William Shakespeare", "Jupiter", "Au", "1912", "China", "Leonardo da Vinci", "Pacific Ocean"]
won = 0
q = 0
prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

print("Welcome to KBC".center(150))
print(f"the total prize is {sum(prize)}")
for i in range(len(ques)):
    print('The question for prize of ' + str(prize[i]) + ' is:')
    print(ques[i])
    print("Your options are:\n" + str(ans[i]))
    op = input("Enter your Answer: ")
    if op.lower() == c_ans[i].lower():  # Convert both to lowercase for comparison
        print("Correct Answer")
        q = q + 1
        won = won + prize[i]
    else:
        print("Sorry wrong Answer")
        break


if won!=0:
    print("You got " + str(q) + " question(s) correct")    
    print("You have won the prize of " + str(won) + " rupees")
else:
    print("you have not won anything,try again..")


