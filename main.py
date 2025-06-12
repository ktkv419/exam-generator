import random, math, json

num_of_questions = 2

with open("input.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


slice_size = math.floor(len(questions) / num_of_questions)
splitted = []


for i in range(num_of_questions):
    splitted.append(questions[i * slice_size : (i + 1) * slice_size])


def generate_exam_paper(index, num_of_questions):
    res_array = [f"# Билет {index + 1}"]

    for i in range(num_of_questions):
        random_index = random.randint(0, len(splitted[i]) - 1)
        res_array.append(f"№{i + 1} {splitted[i].pop(random_index)}")

    return "\n\n".join(res_array)


exam_papers = []
for i in range(math.floor(len(questions) / 2)):
    exam_papers.append(generate_exam_paper(i, num_of_questions))

with open("output.md", "w", encoding="utf-8") as file:
    file.write(("\n\n").join(exam_papers))
