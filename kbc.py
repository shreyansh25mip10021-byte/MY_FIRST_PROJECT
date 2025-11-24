questions = [
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"],
    ["In which language Windows is written?", "a. python",
        "b. javascript", "c. c language/ c++", "d. English", "c"]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
ch = "y"
money_won = 0

for i in range(len(questions)):
    check = 1
    question = questions[i]
    while check == 1:
        print(f"\n\nQuestion for {levels[i]} is: ")
        print(question[0])
        print(question[1])
        print(question[2])
        print(question[3])
        print(question[4])
        c = input("Enter your choice :\n").lower()

        if c in ["a", "b", "c", "d"]:
            if c == question[-1]:
                print(
                    "\nCongrats your answer is correct and you win ", levels[i])
                money = levels[i]
                ch = input(
                    "\nPress any key to continue or 'q' to quit : ").lower()
                check = 0
                if ch == "q":
                    break
            else:
                print("\nSorry, your answer is wrong!!")
                check = 1
                break

        else:
            print("\nInvalid choice")
            continue
    if ch == "q":
        break
    if check == 1:
        break


if check == 1:
    if money >= 0 and money < 10000:
        money_won = 0
    elif money >= 10000 and money < 320000:
        money_won = 10000

else:
    money_won = money


if money_won == 0:
    print("\nSorry you have won nothing.")
else:
    print(f"\nCongrats!! You have won {money_won}")

print("\n\nThank You")
