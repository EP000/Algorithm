# Excluding Specific Characters
Regex_Pattern = r'^[^1234567890][^aeiou][^bcDF][^\s]'

# Matching Character Ranges
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

# Matching Word Boundaries
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'

# Capturing & Non-Capturing Groups
Regex_Pattern = r'(?:ok){3,}'

# Alternative Matching
Regex_Pattern = r'^(?:Mr|Mrs|Dr|Er)\.[a-zA-Z]+$'