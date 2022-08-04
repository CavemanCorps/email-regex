#! python3
# emailExtractor.py - Simplified version of extractorProject.py. Only finds emails.

import pyperclip, re

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

# Finds matches in the Clipboard 
text = str(pyperclip.paste())                               
matches = []
for groups in emailRegex.findall(text):                    
    matches.append(groups[0])                              

# Copies matches from clipboard                 
pyperclip.copy('\n'.join(matches))
print('MATCHES FOUND: ' str(len(matches)))
print('\n'.join(matches))
