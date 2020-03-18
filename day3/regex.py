import re

emails = 'krishna@gmail.com abc@xyz.com 98498904850948594 23234234 bikalpa jon@gmail.com'

pattern = r'\w+@\w+\.\w+'

print(re.findall(pattern, emails))