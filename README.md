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

### Using Character Set to Match a Pattern

```python
text_to_search = """John_Doe123@example.com visited https://example-site.com on 12/25/2024 at 4:30PM, and purchased 3 items worth $150.75 using the code ABC123!
321-555-4321
1234.555.1234
1234*555*1234
900*555*5431
800-555-1234

"""

pattern = re.compile(r"[89]00[-*]\d\d\d[-*]\d\d\d")
matches = pattern.finditer(text_to_search)

for match in matches:
  print(match)

# Output:
#  <re.Match object; span=(182, 193), match='900*555*543'>
#  <re.Match object; span=(195, 206), match='800-555-123'>

```

### Using Quantifiers

```python
text_to_search = """John_Doe123@example.com visited https://example-site.com on 12/25/2024 at 4:30PM, and purchased 3 items worth $150.75 using the code ABC123!
321-555-4321
1234.555.1234
1234*555*1234
900*555*5431
800-555-1234

Mr. Schafer
Mr Smith
Ms David
Mrs. Robinson
Mr. T

"""
# The value in the bracket means to match the n-amount of the digits(\d). So in this case, match 3 digits, 3 digits and 4 digits
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
matches = pattern.finditer(text_to_search)

for match in matches:
  print(match)

# Using Quantifier to match certain character in a string
# The question mark means its optional(similar to JavaScript). So, the pattern is the period(\.) is optional and will collect "Mr" with or without whitespace
pattern = re.compile(r"Mr\.?")

# Will match characters including with or without whitespace then collect the first character after the white space that should be capital and the rest
# pattern = re.compile(r"Mr\.?\s[A-Z]\w*")

# Will match characters including with or without whitespace then collect the first character after the white space that should be capital and should have 1 or more characters after the capital string
# In this case, it will not collect 'Mr.T' because after 'T' there is no characters
# pattern = re.compile(r"Mr\.?\s[A-Z]\w+")

matches = pattern.finditer(text_to_search)


```

## Using Either

```python
# Means to collect string that have Mr or Ms or Mrs and the following characters
# Approach #1
pattern = re.compile(r"M(r|s|rs)\.?\s[A-Z]\w*")

# Approach #2
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")

```

## Matching an Email

```python
emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafery@my-work.net
"""

pattern = re.compile(r"[a-zA-Z]+@[a-zA-Z]+\.com")
# Output:
# CoreyMSchafer@gmail.com

# We have added a period to the first bracket quantifier since the 2nd email has a period
pattern = re.compile(r"[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)")
# Output:
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu

pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")
# Output:
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafery@my-work.net

```

- "[a-zA-Z]+" ensures that there is at least one letter in the username and the domain name.
- "[a-zA-Z]+" before the **@** and after the **@** means that both the username and domain must contain one or more letters. So, this pattern requires at least one letter before the **@** and after it.
- If there are no letters (like @.com), it will not match because the **+** enforces at least one character.

```python
import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

"""

# The good thing about this is there the characters are inside a group and we can access this
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

matches = pattern.finditer(urls)


# Group 0 is the entire collected string
# ------ Based on our 'urls' string example with a 'group' quantifier used in our pattern, we can collect the following
# Group 1 = www or None
# Group 2 = the domain name
# Group 3 = the top-level domain
for match in matches:
  print(match.group(0))

```

## Substitutions

```python
urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

"""

# The good thing about this is there the characters are inside a group and we can access this
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
# 'sub' will return according to the substitution made. In this case, we want to return the group 2(\w+) and 3(\.\w+)
subbed_urls = pattern.sub(r"\2\3", urls)

print(subbed_urls)

# Output:
# google.com
# coreyms.com
# youtube.com
# nasa.gov

```

## findall()

```python
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")

```

- returns and match only that group, in this case "Mr|Ms|Mrs" since this is a group
- if there are multiple groups, then it will return a list of tuples and the tuples would contains all of the group
- if there are no groups, then it will return all of the matches in a list of strings

## match()

- This method tries to match the pattern at the start of the string.

```python
import re

# Example string
text = "Hello world! This is a test of Regex in Python. hello again!"

# Example pattern: Let's look for the word "hello"
pattern = r"hello"

# match() checks if the pattern matches **from the beginning** of the string

result = re.match(pattern, text, re.IGNORECASE)
if result:
    print(f"match() found: {result.group()} at position {result.start()}-{result.end()}")
else:
    print("match() found nothing.")a

# Output: match() found nothing.

```

## search

- search() looks for the first occurrence of the pattern **anywhere in the string**
- This method scans through the entire string and returns the first match it finds.

```python
result = re.search(pattern, text, re.IGNORECASE)
if result:
    print(f"search() found: {result.group()} at position {result.start()}-{result.end()}")
else:
    print("search() found nothing.")

# Output: search() found: Hello at position 0-5

```

## findall

- findall() returns **all matches** in the string
- This method returns all matches of the pattern in the string as a list.

```python

results = re.findall(pattern, text, re.IGNORECASE)
print(f"findall() found: {results}")

# Output: findall() found: ['Hello', 'hello']

### 4. Using `search()` with multiple flags
# Multiple flags can be combined using the `|` (OR) operator

# re.DOTALL makes the dot (.) match newlines as well
multi_flag_pattern = r"hello.*again"
multi_flag_result = re.search(multi_flag_pattern, text, re.IGNORECASE | re.DOTALL)

if multi_flag_result:
    print(f"search() with multiple flags found: {multi_flag_result.group()}")
else:
    print("search() with multiple flags found nothing.")

# Output: search() with multiple flags found: Hello world! This is a test of Regex in Python. hello again

```

Flags: Flags like re.IGNORECASE (for case-insensitivity) and re.DOTALL (to make . match newlines) can be used to modify the behavior of regex matching.
