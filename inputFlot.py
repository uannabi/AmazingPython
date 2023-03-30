
balance=928.12

while True:
   try:
      num = float(input('Deposit:'))	
      break
   except ValueError:
      print("Must be valid quantity.")

balance+=num
print(f'Balance: {balance}')
