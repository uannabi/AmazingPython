
weather: str = 'CLEAR'
message: str = ''

message: str = 'Nice!' if weather == 'CLEAR' else 'Uh Oh....'

print(message)


if weather == 'CLEAR':
   message = 'Nice!'
else:
   message = 'Uh oh ....'

print(message)


