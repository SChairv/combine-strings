#Problem: Create a function that takes a list of strings as input.
#Join each string in the list to create and return one complete string.
# Each word should have a space between them.
foods = " "
favfoods=" "


while foods!="done":
    foods = input("What are some of your favorite foods? Please enter done when you are finished. ")
    if foods!="done":
        favfoods = (favfoods + " " + foods)
        print(favfoods)

    elif foods=="done":
        print("Wow, ", favfoods, "--those are some of my favorites too!")




