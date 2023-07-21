from collections import Counter
import re

text = '''Python is an easy programming language. Python syntax is like the english language. Python language is easy to learn and adapt to compared with Java and C. In python language, the same task can be performed using fewer lines of code. Its easy learning and easy to code.'''

words = re.findall('\w+', text)

count = Counter(words)

print(count.most_common(3))
