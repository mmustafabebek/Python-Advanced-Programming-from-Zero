"""
Have two lists of first and last names.

names -----> ["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sükran","Merve"]

surnames -----> ["Yilmaz","Ozturk","Dagdeviren","Atatürk","Dikmen","Kaya","Polat"]

Match these names and surnames in order and print the names and surnames on the screen one after the other.
Note: try to use the zip() function.

"""

names = ["Kerim","Tarik","Ezgi","Kemal","Ilkay","Sükran","Merve"]
surnames = ["Yilmaz","Ozturk","Dagdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(names,surnames):
    print(i,j)
