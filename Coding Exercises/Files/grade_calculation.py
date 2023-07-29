def calculate_grade(line):

    line = line[:-1]

    list1 = line.split(",")

    name = list1[0]
    grade1 = int(list1[1])
    grade2 = int(list1[2])
    grade3 = int(list1[3])

    final_note = grade1 * (3/10) + grade2 * (3/10) + grade3 * (4/10)

    if final_note >= 90:
        letter = "AA"
    elif final_note >= 85:
        letter = "BA"
    elif final_note >= 80:
        letter = "BB"
    elif final_note >= 75:
        letter = "CB"
    elif final_note >= 70:
        letter = "CC"
    elif final_note >= 65:
        letter = "DC"
    elif final_note >= 60:
        letter = "DD"
    elif final_note >= 55:
        letter = "FD"
    else:
        letter = "FF"

    return name + "-------------------------------------->" + letter + "\n"




with open("file.txt","r",encoding ="utf-8") as file:

    to_add_list = []

    for i in file:
        to_add_list.append(calculate_grade(i))

    with open("grades.txt","w",encoding = "utf-8") as file:

        for i in to_add_list:
            file.write(i)

