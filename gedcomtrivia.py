import random
from gedcomparser import gedcomParse

#Enter GEDCOM file path here
filepath = ""

num = int(input("How many questions should be generated? "))
gedcom = gedcomParse(filepath)

def generateQuestions(person):
    questions = []

    if person.birth:
        if person.birth[0][0]:
            questions.append([f"On what date was {person.name} born?", person.birth[0][0]])
        if person.birth[0][1]:
            questions.append([f"At which location was {person.name} born?", person.birth[0][1]])

    if person.death:
        if person.death[0][0]:
            questions.append([f"On what date did {person.name} die?", person.death[0][0]])
        if person.death[0][1]:
            questions.append([f"In which location did {person.name} die?", person.death[0][1]])

    if person.familyChild:
        if person.familyChild.parentOne:
            questions.append([f"Who is the father of {person.name}?", person.familyChild.parentOne.name])

        if person.familyChild.parentTwo:
            questions.append([f"Who is the mother of {person.name}?", person.familyChild.parentTwo.name])

    if person.familySpouses:
        family = person.familySpouses[0]
        if family.children:
            questions.append([f"How many children does {person.name} have?", len(family.children)])

        if family.parentOne == person:
            if family.parentTwo:
                questions.append([f"Who is the spouse of {person.name}?", family.parentTwo.name])

        if family.parentTwo == person:
            if family.parentOne:
                questions.append([f"Who is the spouse of {person.name}?", family.parentOne.name])

    return questions


for x in range(num):
    person = random.choice(gedcom.fullGedcom)
    questions = generateQuestions(person)

    if questions:
        question = random.choice(questions)
        print(f"Question: {question[0]}\nAnswer: {question[1]}")
