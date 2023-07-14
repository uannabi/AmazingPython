
import sys
from datetime import datetime

now = datetime.now()

massage = f'{now:%M:%S} Logged!'

print(massage)

print(massage, file=sys.stderr)

with open('logs.text', 'a') as file:
    print(massage, file=file)

