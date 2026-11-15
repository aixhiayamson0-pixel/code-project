import time

# PYTHON LEARNING SYSTEM - COMPLETE VERSION
# Lessons, Motivation, Progress Tracker, Time Challenge, and Final Boss

completed = []

print("PYTHON LEARNING SYSTEM - COMPLETE VERSION")

while True:
    print("MAIN MENU")
    print("  [1]  " + "Introduction to Programming")
    print("  [2]  " + "Python Basic Syntax")
    print("  [3]  " + "Arithmetic Operators and Expressions")
    print("  [4]  " + "Basic Input and Output")
    print("  [5]  " + "Conditional Statements")
    print("  [6]  " + "Logical Operators")
    print("  [7]  " + "Introduction to Iteration and Loops")
    print("  [8]  " + "Progress Tracker")
    print("  [9]  " + "Time Challenge")
    print("  [10] " + "Final Boss Challenge")
    print("  [0]  " + "Exit Program")
    print("  Lessons Completed: " + str(len(completed)) + " / 7")
    choice = input("Enter your choice: ").strip()

    # LESSON 1
    if choice == "1":
        print("\nLESSON 1: INTRODUCTION TO PROGRAMMING")

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
        print("\nLESSON 2: PYTHON BASIC SYNTAX")

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
        print("\nLESSON 3: ARITHMETIC OPERATORS AND EXPRESSIONS")

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
        print("\nLESSON 4: BASIC INPUT AND OUTPUT")

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
        print("\nLESSON 5: CONDITIONAL STATEMENTS")

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
        print("\nLESSON 6: LOGICAL OPERATORS")

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
        print("\nLESSON 7: INTRODUCTION TO ITERATION AND LOOPS")

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
        print("\nPROGRESS TRACKER")
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


    # TIME CHALLENGE
    elif choice == "9":
        print("\nTIME CHALLENGE")
        print("Answer each question within 30 seconds.")
        print("The program checks your time after you submit your answer.")
        print("You will still see the explanation if your answer is wrong or late.\n")

        time_questions = [
            ("What command displays text on the screen?", "print",
             "The print() command displays information. Example: print('Hello')"),
            ("What is 8 + 4?", "12",
             "The plus sign (+) is used for addition. 8 + 4 equals 12."),
            ("What data type is 'Hello'?", "string",
             "Text enclosed in quotation marks is a string."),
            ("Which keyword is used to check a condition?", "if",
             "The if keyword runs code when a condition is true."),
            ("Which loop is commonly used to repeat a set number of times?", "for",
             "A for loop is commonly used when the number of repetitions is known."),
            ("Which symbol is used for multiplication in Python?", "*",
             "The asterisk (*) symbol is used for multiplication."),
            ("Which data type represents True or False?", "boolean",
             "Boolean is the data type that has True or False values."),
            ("Which operator means 'not equal to'?", "!=",
             "The != operator checks whether two values are not equal."),
            ("Which statement is used to repeat while a condition is true?", "while",
             "A while loop repeats its block as long as its condition is true."),
            ("Which command gets information from the user?", "input",
             "The input() function allows the user to enter information.")
        ]

        time_score = 0

        for question_number in range(len(time_questions)):
            question = time_questions[question_number]
            print("Question", question_number + 1, "of", len(time_questions))
            print(question[0])

            start_time = time.time()
            answer = input("Your answer: ").strip().lower()
            elapsed_time = time.time() - start_time

            if elapsed_time > 30:
                print("TIME'S UP! You took", round(elapsed_time, 1), "seconds.")
                print("Correct answer:", question[1])
            elif answer == question[1]:
                print("Correct! You earned 10 points.")
                time_score = time_score + 10
            else:
                print("Not quite. Correct answer:", question[1])

            print("Explanation:", question[2])

        print("\nTIME CHALLENGE RESULT")
        print("Your score:", time_score, "/", len(time_questions) * 10)

        if time_score == len(time_questions) * 10:
            print("Amazing! You answered all questions correctly.")
        elif time_score >= 30:
            print("Good effort! Review the explanations and keep practicing.")
        else:
            print("Do not give up. Learning is more important than speed.")

    # FINAL BOSS CHALLENGE
    elif choice == "10":
        print("\nFINAL BOSS CHALLENGE")

        if len(completed) < 7:
            print("FINAL BOSS IS LOCKED!")
            print("You must complete all 7 lessons first.")
            print("Lessons completed:", len(completed), "/ 7")
            print("Study each lesson, then come back when you are ready.")
        else:
            print("You have completed all 7 lessons.")
            print("Answer these 10 questions to defeat the Final Boss!\n")

            boss_questions = [
                ("1. What is a step-by-step process for solving a problem called?",
                 "algorithm",
                 "An algorithm is a step-by-step process used to solve a problem."),
                ("2. Which command displays output in Python?",
                 "print",
                 "print() displays information on the screen."),
                ("3. What is the result of 9 * 3?",
                 "27",
                 "The asterisk (*) is the multiplication operator. 9 times 3 is 27."),
                ("4. Which function is used to receive user input?",
                 "input",
                 "input() receives information entered by the user."),
                ("5. Which keyword runs when an if condition is false and no other condition matches?",
                 "else",
                 "The else block runs when the previous conditions are false."),
                ("6. Which logical operator is true only when both conditions are true?",
                 "and",
                 "The and operator is true only when both conditions are true."),
                ("7. Which loop repeats while a condition is true?",
                 "while",
                 "A while loop repeats its instructions while its condition remains true."),
                ("8. What is the result of 15 // 4?",
                 "3",
                 "The // operator performs floor division and gives the whole-number quotient."),
                ("9. Which logical operator is true when at least one condition is true?",
                 "or",
                 "The or operator is true when one or both conditions are true."),
                ("10. Which keyword is used to start a loop that repeats while a condition is true?",
                 "while",
                 "The while keyword starts a loop that continues while its condition is true.")
            ]

            boss_score = 0

            for boss_question in boss_questions:
                print(boss_question[0])
                boss_answer = input("Your answer: ").strip().lower()

                if boss_answer == boss_question[1]:
                    print("Correct! +10 points.")
                    boss_score = boss_score + 10
                else:
                    print("Incorrect. Correct answer:", boss_question[1])

                print("Explanation:", boss_question[2])

            print("\nFINAL BOSS RESULT")
            print("Your score:", boss_score, "/ 100")

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
        print("\nTHANK YOU FOR USING THE PROGRAM!")
        print("Lessons completed:", len(completed), "/ 7")
        print("Keep learning and practicing Python!")
        break

    else:
        print("\nInvalid choice! Please select a valid menu number from 0 to 10.")
        print("Returning to the main menu. Please try again.")
        continue

    # RETURN TO THE MAIN MENU AFTER A VALID SELECTION
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("\n" + "Press ENTER to return to the main menu.")
        input()
