#assign a string with a tab escape sequence.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

ayylmao = "\ue8a2"

print("this is my first line" + "\nthis is my second." +
        "\nhere is some unicode\n" + f"{ayylmao}")
