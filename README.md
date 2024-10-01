# Snippets

```bash
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
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
\*\*
