print ("let's practice every thing.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explaination
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    print(">>>>secret_formula")
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    print("<<<<sercret_formula")
    return jelly_beans, jars, crates


start_point = 100
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 9999999

print("We can also do that this way:")
#assign the values returned from 'secret_formula' (called with start_point)
#to the variable 'formula'
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
#print a formatted string with the values in the list 'formula'
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
