
class Book:
   def __init__(self, content):
      self.content = content

   def __getitem__(self, index):
      try:
         page = self.content[index]
      except IndexError:
         page  = 'Page not found...'

      return page 

book = Book(['English', 'Bangla', 'Arabic', 'Math', 'Since'])

print(book[2])
print(book[10])
