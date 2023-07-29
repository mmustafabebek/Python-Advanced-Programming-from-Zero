"""
Create a file in the form of "football_players.txt" and place the players playing in Galatasaray, Fenerbahçe and Beşiktaş
randomly in it. Separate the players of each team from this file and write them in 3 different files as "gs.txt",
 "fb.txt", "bjk.txt".

"""

with open("football_players.txt","r",encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()

    for line in file:
        line = line[:-1]
        line_elements = line.split(",")

        if line_elements[1] == "Galatasaray":
            gs.append(line + "\n")
        elif line_elements[1] == "Beşiktaş":
            bjk.append(line + "\n")
        else:
            fb.append(line + "\n")

    with open("gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            file1.write(i)

    with open("bjk.txt", "w", encoding="utf-8") as file2:
        for i in bjk:
            file2.write(i)

    with open("fb.txt", "w", encoding="utf-8") as file3:
        for i in fb:
            file3.write(i)

