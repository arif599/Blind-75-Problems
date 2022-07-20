def create(problem):
    problem = problem.replace(".", "")
    file_name = problem.replace(" ", "_") + ".py"
    file_name = "./Arrays & Hashing/" + file_name
    print(file_name)
    with open(file_name, "w") as f:
        f.write('"""\n')
        f.write("Understand:\n")
        f.write("\tProblem Statement:\n")
        f.write("\tQuestions:\n")
        f.write("\tTest Cases:\n")
        f.write("\n")
        f.write("Match:\n")
        f.write("\n")
        f.write("Plan:\n\n")
        f.write("Optimization:\n")
        f.write('"""\n')
        f.write("\n")
        f.write('if __name__ == "__main__":\n\tpass')

if __name__ == "__main__":
    user_input = input("Enter problem: ")
    create(user_input)