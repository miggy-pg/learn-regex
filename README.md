# Snippets

```bash
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary(are indicated by whitespace or alpha numeric numbers)
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

```

## What is a raw string?

A raw string in python is just a string prefixed with an **r**. This tells python not to handle any back slashes in any either way.

```python
import re

print("\tTab")
# Output:      Tab
# Python added a tab before the 'Tab' string

print(r"\tTab")
# Output: Tab
# Python did not interpret '\t' is a tab

```

## The dot `.` is a Special character

```python
text_to_search = "John_Doe123@example.com visited https://example-site.com on 12/25/2024 at 4:30PM, and purchased 3 items worth $150.75 using the code ABC123!"

# Case #1 without backslash
pattern = re.compile(r".")

matches = pattern.finditer(text_to_search)

for match in matches:
  print(match)

# Output: It matches almost everything

# Case #2 uses backslash
pattern = re.compile(r"\.")

for match in matches:
  print(match)

# Will only match characters that are period `.`

```

## Escaping Characters

We can escape characters by using the backslash **`\`**

```python
import re

text = "You can reach us at 123-456-7890 or at 987.654.3210 for assistance."
search_pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = search_pattern.finditer(text)
for match in matches:
  print(match)

# Output:
# 123-456-7890
# 987.654.3210

# 123-456-7890 will match because it consists of three digits, followed by a hyphen, three more digits, another hyphen, and four digits.
# 987.654.3210 will also match because it follows the same format but with periods as separators.

```

## Using Character Set

```python
import re

# Before
search_pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# After (added a period & dash inside a square bracket)
# This will only match characters inside the square bracket (see other matches characters in our attached snippet above)
search_pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

with open("data.txt", "r") as f:
  content = f.read()

  matched_contents = search_pattern.finditer(content)
  for matched_content in matched_contents:
    print("Matched Content: ", matched_content)

```
