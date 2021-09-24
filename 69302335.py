text = """
!bla bla bla bla (Y, N)

Y

!bla bla bla

5.5

!number of bla

500

!number of ...

100
"""

# create result list
result = []
# go over the lines one by one, splitting on newline character
for line in text.split("\n"):
    # check if the line has content, and if it doesn't starts with !
    if len(line) > 0 and line[0] != "!":
        # add to the list
        result.append(line)
# join the list with a newline character
output = "\n".join(result)
print(output)


# remove blank lines using split and list comprehension
text = [line for line in text.split("\n") if len(line) > 0]
# only get every other line
text = text[1::2]
# join the list with a newline character
output = "\n".join(text)
print(output)