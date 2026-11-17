import time
import os
import sys

if os.name == "nt":
    import msvcrt

# ==========================================
# PYTHON LEARNING SYSTEM
# ==========================================

completed = []

print("WELCOME TO THE PROGRAMMING PROGRAM!")
print("Hello, future programmer!")
print("Ready ka na bang matuto ng Python step by step?")
print("No need to be perfect. Learn at your own pace, try your best, and enjoy the process.")
print("Every line of code you learn is one step closer to becoming a programmer!")
input("\nPress Enter to start your learning journey...")

while True:
    print("+==========================================+")
    print("|                                          |")
    print("|          PYTHON LEARNING SYSTEM          |")
    print("|                                          |")
    print("|             LEARN PYTHON STEP BY STEP    |")
    print("|                                          |")
    print("+==========================================+")
    print("                  MAIN MENU")
    print("  ------------------------------------------")
    print("  [1]  " + "Introduction to Programming")
    print("  [2]  " + "Python Basic Syntax")
    print("  [3]  " + "Arithmetic Operators and Expressions")
    print("  [4]  " + "Basic Input and Output")
    print("  [5]  " + "Conditional Statements")
    print("  [6]  " + "Logical Operators")
    print("  [7]  " + "Introduction to Iteration and Loops")
    print("  [8]  " + "Progress Tracker")
    print("  [9]  " + "Final Boss Challenge")
    print("  [0]  " + "Exit Program")
    print("  ------------------------------------------")
    print("  Lessons Completed: " + str(len(completed)) + " / 7")
    choice = input("Enter your choice: ").strip()

    # LESSON 1
    if choice == "1":
        print("\n========== LESSON 1: INTRODUCTION TO PROGRAMMING ==========")

        print("""
Programming is the process of giving instructions to a
computer so it can perform a certain task.

We can compare programming to preparing our school things.
First, we get our bag, then our books, and after that, we
arrange our supplies. A computer also needs instructions
in the correct order. It cannot guess what we want it to do.

A program is a set of instructions written using a
programming language. Python is one language used to
create programs, solve problems, and automate tasks.

IMPORTANT TERMS:

1. Program
   - A group of instructions that tells the computer what to do.

2. Programmer
   - A person who writes and creates programs.

3. Programming Language
   - A language used to communicate instructions to a computer.

4. Algorithm
   - A step-by-step process used to solve a problem.
""")
        print("EXAMPLE:")
        print("print('Welcome to Python!')")
        print("\nOUTPUT:")
        print("Welcome to Python!")
        print("\nRemember: A program starts with instructions.")

        print("""
WHEN THIS LESSON FEELS CONFUSING:
Think of a program like a recipe. A recipe gives steps to
follow, and a computer follows the instructions in a program.
You do not need to understand everything at once. Start by
understanding what each instruction is asking the computer to do.
""")
        print("MOTIVATION: Every programmer started as a beginner. Learning the basics is already progress!")

        if 1 not in completed:
            completed.append(1)

    # LESSON 2
    elif choice == "2":
        print("\n========== LESSON 2: PYTHON BASIC SYNTAX ==========")

        print("""
Syntax means the rules we follow when writing code.

Just like writing a sentence, Python code must be written
in the correct way. A small mistake, such as a missing
quotation mark or parenthesis, can cause an error.

BASIC PARTS OF PYTHON SYNTAX:

1. Print Statement
   - The print() command displays information on the screen.

2. Variables
   - Variables store information that we can use later.

3. Data Types
   - String: Text or characters.
   - Integer: Whole numbers.
   - Float: Numbers with decimal points.
   - Boolean: True or False values.

4. Comments
   - Comments are notes written in the code. They start with #.

5. Indentation
   - Spaces at the beginning of a line help organize code.
""")
        student_name = "Alex"
        student_age = 17
        student_grade = 90.5
        is_enrolled = True

        print("EXAMPLE:")
        print("student_name = 'Alex'")
        print("student_age = 17")
        print("student_grade = 90.5")
        print("is_enrolled = True")
        print("\nOUTPUT:")
        print(student_name)
        print(student_age)
        print(student_grade)
        print(is_enrolled)

        print("""
WHEN THIS LESSON FEELS CONFUSING:
Read the code one line at a time. A variable is just a labeled
container for a value, while print() shows that value.
If you see an error, check spelling, quotation marks,
parentheses, and indentation first.
""")
        print("MOTIVATION: Small mistakes are part of learning. Finding and fixing them makes you better!")

        if 2 not in completed:
            completed.append(2)

    # LESSON 3
    elif choice == "3":
        print("\n========== LESSON 3: ARITHMETIC OPERATORS ==========")

        print("""
Arithmetic operators are symbols used to perform
mathematical operations in Python.

They can be used when calculating allowance, expenses,
savings, and other numbers.

COMMON ARITHMETIC OPERATORS:

1. Addition (+)        - Combines numbers.
2. Subtraction (-)     - Gets the difference.
3. Multiplication (*)  - Multiplies numbers.
4. Division (/)        - Divides numbers.
5. Modulus (%)         - Gets the remainder.
6. Exponent (**)       - Raises a number to a power.
7. Floor Division (//) - Divides and removes the decimal part.

EXAMPLE:
A student has 100 pesos and spends 30 pesos on snacks
and 20 pesos on school supplies.
""")
        allowance = 100
        snacks = 30
        supplies = 20
        remaining = allowance - snacks - supplies

        print("CALCULATION:")
        print("Allowance:", allowance)
        print("Snacks:", snacks)
        print("School supplies:", supplies)
        print("Remaining money:", remaining)

        print("\nOTHER EXAMPLES:")
        print("10 + 5 =", 10 + 5)
        print("10 - 5 =", 10 - 5)
        print("10 * 5 =", 10 * 5)
        print("10 / 5 =", 10 / 5)
        print("10 % 3 =", 10 % 3)
        print("2 ** 3 =", 2 ** 3)
        print("10 // 3 =", 10 // 3)

        print("""
WHEN THIS LESSON FEELS CONFUSING:
Treat each operator like a different math instruction.
The plus sign adds, the minus sign subtracts, and the
asterisk multiplies. Try one example at a time using small
numbers, then compare your answer with the program.
""")
        print("MOTIVATION: You already use math in everyday life. Python is another way to practice it!")

        if 3 not in completed:
            completed.append(3)

    # LESSON 4
    elif choice == "4":
        print("\n========== LESSON 4: BASIC INPUT AND OUTPUT ==========")

        print("""
Input and output allow a program to communicate with
the person using it.

INPUT:
- Input is information entered by the user.
- Python uses input() to receive information.

OUTPUT:
- Output is the result displayed by the program.
- Python uses print() to show information.

DATA CONVERSION:
- int() converts a value into a whole number.
- float() converts a value into a decimal number.

EXAMPLE:
A simple student information program.
""")
        while True:
            name = input("Enter your name: ").strip()
            if name:
                break
            print("Name cannot be blank. Please try again.")

        while True:
            section = input("Enter your section: ").strip()
            if section:
                break
            print("Section cannot be blank. Please try again.")

        while True:
            age_text = input("Enter your age: ").strip()
            if age_text.isdigit():
                age = int(age_text)
                break
            else:
                print("Invalid age. Please enter a whole number.")

        print("\n---------- STUDENT INFORMATION ----------")
        print("Name:", name)
        print("Section:", section)
        print("Age:", age)
        print("\nInformation successfully displayed!")
        print("""
WHEN THIS LESSON FEELS CONFUSING:
Remember the difference: input() receives an answer from
the user, while print() displays information on the screen.
For example, input() asks for your name and print() shows it.
""")
        print("MOTIVATION: You can make a program interact with people now. That is a real programming skill!")
        if 4 not in completed:
            completed.append(4)

    # LESSON 5
    elif choice == "5":
        print("\n========== LESSON 5: CONDITIONAL STATEMENTS ==========")

        print("""
Conditional statements allow a program to make decisions
based on certain conditions.

THREE COMMON CONDITIONAL KEYWORDS:

1. if
   - Runs a block of code when a condition is true.

2. elif
   - Checks another condition if the previous condition
     was false.

3. else
   - Runs when none of the conditions above are true.

EXAMPLE:
A school can use a grading system to identify a student's
performance.
""")
        while True:
            grade_text = input("Enter your grade: ").strip()
            try:
                grade = float(grade_text)
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be from 0 to 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if grade >= 90:
            print("Excellent! Keep up the good work.")
        elif grade >= 75:
            print("Passed! Continue doing your best.")
        else:
            print("Failed. You can still improve.")

        print("""
WHEN THIS LESSON FEELS CONFUSING:
Imagine a decision in real life: if it is raining, bring an
umbrella; otherwise, you may leave it at home. Python uses
if, elif, and else to follow decisions like these.
""")
        print("MOTIVATION: A wrong result does not mean you cannot learn. Review the condition and try again!")

        if 5 not in completed:
            completed.append(5)

    # LESSON 6
    elif choice == "6":
        print("\n========== LESSON 6: LOGICAL OPERATORS ==========")

        print("""
Logical operators are used to combine or change conditions
in a Python program. They are helpful when a decision
depends on more than one condition.

THREE MAIN LOGICAL OPERATORS:

1. AND
   - True only when both conditions are true.

2. OR
   - True when at least one condition is true.

3. NOT
   - Changes True into False, or False into True.

EXAMPLE:
A student wants to join a school activity. The student
must have permission and a school ID. Both conditions
must be true to join.
""")
        while True:
            permission = input("Do you have permission? (yes/no): ").lower().strip()
            if permission == "yes" or permission == "no":
                break
            print("Please answer only yes or no.")

        while True:
            school_id = input("Do you have a school ID? (yes/no): ").lower().strip()
            if school_id == "yes" or school_id == "no":
                break
            print("Please answer only yes or no.")

        if permission == "yes" and school_id == "yes":
            print("You are allowed to join the activity.")
        else:
            print("You cannot join the activity yet.")

        print("\nOTHER EXAMPLES:")
        print("True and True =", True and True)
        print("True or False =", True or False)
        print("not True =", not True)

        print("""
WHEN THIS LESSON FEELS CONFUSING:
AND means both conditions must be true. OR means at least
one condition must be true. NOT reverses a condition.
Try saying the conditions out loud to see what the program
needs before it makes a decision.
""")
        print("MOTIVATION: Complicated decisions become easier when you break them into smaller conditions!")

        if 6 not in completed:
            completed.append(6)

    # LESSON 7
    elif choice == "7":
        print("\n========== LESSON 7: ITERATION AND LOOPS ==========")

        print("""
Iteration means repeating a set of instructions until
a certain task is completed.

Loops help us avoid writing the same instruction many times.

TWO COMMON TYPES OF LOOPS:

1. FOR LOOP
   - Used when we want to repeat something a specific
     number of times.

2. WHILE LOOP
   - Repeats instructions while a condition remains true.

EXAMPLE 1: FOR LOOP

The range(1, 6) starts at 1 and stops before 6.
That is why the numbers displayed are 1 to 5.
""")
        print("FOR LOOP OUTPUT:")
        for number in range(1, 6):
            print("School day", number)

        print("\n" + "WHILE LOOP OUTPUT:")
        number = 1
        while number <= 3:
            print("Study session", number)
            number = number + 1

        print("""
WHEN THIS LESSON FEELS CONFUSING:
A loop is simply a repeated action. Think of doing three
practice problems: you repeat the same kind of task until
you finish. In a while loop, always check that something
changes so the loop can eventually stop.
""")
        print("MOTIVATION: Practice makes repetition easier to understand. Keep tracing each loop one step at a time!")

        if 7 not in completed:
            completed.append(7)

    # PROGRESS TRACKER
    elif choice == "8":
        print("\n========== PROGRESS TRACKER ==========")
        print("Completed lessons:", len(completed), "/ 7")
        print()

        lesson_names = [
            "Introduction to Programming",
            "Python Basic Syntax",
            "Arithmetic Operators and Expressions",
            "Basic Input and Output",
            "Conditional Statements",
            "Logical Operators",
            "Iteration and Loops"
        ]

        for lesson_number in range(1, 8):
            if lesson_number in completed:
                print("[DONE] " + lesson_names[lesson_number - 1])
            else:
                print("[NOT YET] " + lesson_names[lesson_number - 1])


        if len(completed) == 7:
            print("ACHIEVEMENT: PYTHON LEARNER!")
            print("You completed all seven lessons. Be proud of your effort!")
        else:
            print("Keep going. You do not have to finish everything in one sitting.")
            print("Choose one lesson, understand it, and move forward at your own pace.")


    # FINAL BOSS CHALLENGE
    elif choice == "9":
        print("\n========== FINAL BOSS CHALLENGE ==========")

        if len(completed) < 7:
            print("FINAL BOSS IS LOCKED!")
            print("You must complete all 7 lessons first.")
            print("Lessons completed:", len(completed), "/ 7")
            print("Study each lesson, then come back when you are ready.")
        else:
            print("You have completed all 7 lessons.")
            print("Answer all 10 questions. You have 15 seconds for each question!\n")

            boss_questions = [
                ("What is a step-by-step process for solving a problem called?", "algorithm", "An algorithm is a step-by-step process used to solve a problem."),
                ("Which command displays text or output in Python?", "print", "The print() command displays output on the screen."),
                ("What data type is the value 25?", "integer", "An integer is a whole number without a decimal point."),
                ("What function is used to get input from the user?", "input", "The input() function receives information from the user."),
                ("What is the result of 8 + 4 * 2?", "16", "Multiplication is done before addition, so 8 + 8 equals 16."),
                ("Which keyword is used to make a decision in Python?", "if", "The if keyword checks whether a condition is true."),
                ("Which keyword runs when the if condition is false?", "else", "The else block runs when the if condition is false."),
                ("Which logical operator is true only when both conditions are true?", "and", "The and operator requires both conditions to be true."),
                ("Which loop repeats while its condition is true?", "while", "A while loop repeats as long as its condition remains true."),
                ("What symbol is used to check if two values are equal?", "==", "The double equal sign (==) compares two values for equality.")
            ]

            boss_score = 0
            boss_times = []

            for boss_index, boss_question in enumerate(boss_questions, start=1):
                print("\nQuestion", str(boss_index) + " of 10")
                print("Time limit: 15 seconds")
                print(boss_question[0])
                boss_answer = ""
                boss_time_up = False
                boss_start = time.time()

                if os.name == "nt":
                    boss_typed_answer = ""
                    last_boss_countdown = -1
                    print("Time remaining: 15 seconds")
                    print("Your answer: ", end="", flush=True)

                    while time.time() - boss_start < 15:
                        boss_remaining = 15 - int(time.time() - boss_start)

                        if msvcrt.kbhit():
                            boss_key = msvcrt.getwch()
                            if boss_key in ("\r", "\n"):
                                boss_answer = boss_typed_answer.strip().lower()
                                print()
                                break
                            elif boss_key == "\003":
                                raise KeyboardInterrupt
                            elif boss_key == "\b":
                                if boss_typed_answer:
                                    boss_typed_answer = boss_typed_answer[:-1]
                                    print("\b \b", end="", flush=True)
                            elif boss_key not in ("\x00", "\xe0"):
                                boss_typed_answer = boss_typed_answer + boss_key
                                print(boss_key, end="", flush=True)
                        else:
                            if boss_remaining != last_boss_countdown:
                                sys.stdout.write("\rTime remaining: " + str(boss_remaining) + " seconds   ")
                                sys.stdout.flush()
                                last_boss_countdown = boss_remaining
                            time.sleep(0.05)
                    else:
                        boss_time_up = True
                        print("\nTIME'S UP!")

                    if not boss_time_up and boss_answer == "" and boss_typed_answer.strip():
                        boss_answer = boss_typed_answer.strip().lower()
                else:
                    print("Your answer: ", end="", flush=True)
                    boss_answer = input().strip().lower()
                    if time.time() - boss_start > 15:
                        boss_time_up = True

                boss_elapsed = min(15, int(time.time() - boss_start + 0.999))
                boss_times.append(boss_elapsed)

                if boss_time_up:
                    print("TIME'S UP! Correct answer:", boss_question[1])
                elif boss_answer == boss_question[1]:
                    print("Correct! +10 points.")
                    boss_score = boss_score + 10
                else:
                    print("Incorrect. Correct answer:", boss_question[1])

                print("Time used:", boss_elapsed, "seconds")
                print("Explanation:", boss_question[2])
                print("------------------------------------------")

            print("\n========== FINAL BOSS RESULT ==========")
            print("Your score:", boss_score, "/ 100")
            print("TIME USED PER QUESTION:")
            for boss_index, boss_elapsed in enumerate(boss_times, start=1):
                print("Question", boss_index, "-", boss_elapsed, "seconds")
            print("Total time:", sum(boss_times), "seconds")

            if boss_score == 100:
                print("RANK: PYTHON MASTER!")
                print("You defeated the Final Boss with a perfect score!")
            elif boss_score >= 70:
                print("RANK: PYTHON WARRIOR!")
                print("Great work! You have a strong understanding of Python.")
            elif boss_score >= 40:
                print("RANK: RISING CODER!")
                print("You are improving. Review the lessons and try again.")
            else:
                print("RANK: BEGINNER CODER")
                print("Do not give up. Review the explanations and try again.")

    # EXIT
    elif choice == "0":
        print("\n+==========================================+")
        print("|            THANK YOU FOR USING THE PROGRAM!        |")
        print("+==========================================+")
        print("Lessons completed:", len(completed), "/ 7")
        print("Keep learning and practicing Python!")
        break

    else:
        print("\nInvalid choice! Please select only 0 to 9.")
        print("Returning to the main menu. Please try again.")
        continue

    # RETURN TO THE MAIN MENU AFTER A VALID SELECTION
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("\n" + "Press ENTER to return to the main menu.")
        input()
