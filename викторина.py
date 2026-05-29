# игра на выбор правильного ответа из тесктового файла


import sys
def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print(f"Unable to open the file {file_name}. Ending program.\n, {e}")
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct.strip()
    
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    print("Welcome to the Trivia Challenge!\n")
    print(f"\t\t\t {title} \n")

def main():
    trivia_file = open_file("trivia_file1.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(trivia_file)
    
    while category:
        print(category)
        print(question)
        for i in range (4):
            print(f"\t {i + 1} - {answers[i]}")
        answer = input("What's ur answer?: ")
        if answer == correct:
            score += 1
        else:
            print("\n Wrong", end = " ")
        print(explanation)
        print(f"Score: {score} \n\n")

        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()
    print("That's was the last question!")
    print(f"U are final score is {score}!")

main()
input("\n\nPress the enter key to exit.")




