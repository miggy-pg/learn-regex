import re

text_to_search = "John_Doe123@example.com visited https://example-site.com on 12/25/2024 at 4:30PM, and purchased 3 items worth $150.75 using the code ABC123!"

# Case #1 without backslash
pattern = re.compile(r"\.")

matches = pattern.finditer(text_to_search)

# for match in matches:
#   print(match)

text = "You can reach us at 123-456-7890 or at 987.654.3210 for assistance."
search_pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = search_pattern.finditer(text)
for match in matches:
  print(match)

# Reading contents inside 'data.txt' file and match strings according to our search pattern
with open("data.txt", "r") as f:
  content = f.read()

  matched_contents = search_pattern.finditer(content) 
  for matched_content in matched_contents:
    print("Matched Content: ", matched_content)