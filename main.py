import random
import datetime

class Client:
  count = 0
  random_ids = random.sample(range(1, 100000), 20)
  random_ids.sort()

  def __init__(self, fullname, age, phone_number):
    self.id_no = str(Client.random_ids[Client.count]).zfill(6)
    Client.count += 1
    self.fullname = fullname
    self.age = age
    self.phone_number = phone_number

  def get_id_no(self):
    return self.id_no

  def get_fullname(self):
    return self.fullname
  
  def set_fullname(self, fullname):
    self.fullname = fullname

  def get_age(self):
    return self.age

  def set_age(self, age):
    self.age = age

  def get_fullname(self):
    return self.fullname

  def set_fullname(self, fullname):
    self.fullname = fullname

  def __str__(self):
    return f'id: {self.id_no}, title: {self.fullname}, age: {self.age}, phone number: {self.phone_number}'

class Librarian:
  count = 0
  random_ids = random.sample(range(1, 100000), 20)
  random_ids.sort()
  
  def __init__(self, fullname, age, phone_number, salary):
    self.id_no = str(Librarian.random_ids[Librarian.count]).zfill(6)
    Librarian.count += 1
    self.fullname = fullname
    self.age = age
    self.phone_number = phone_number
    self.salary = 0.0

  def get_id(self):
    return self.id_no

  def get_fullname(self):
    return self.fullname

  def set_fullname(self, fullname):
    self.fullname = fullname

  def get_age(self):
    return self.age

  def set_age(self, age):
    self.age = age

  def get_phone_number(self):
    return self.phone_number

  def set_phone_number(self, phone_number):
    self.phone_number = phone_number

  def get_salary(self):
    return self.salary

  def set_salary(self, salary):
    self.salary = salary



class Book:
  count = 0
  random_ids = random.sample(range(1, 100000), 20)
  random_ids.sort()

  def __init__(self, title, description, author):
    self.id_no = str(Book.random_ids[Book.count]).zfill(6)
    Book.count += 1
    self.title = title
    self.description = description
    self.author = author
    self.status = 'Active'

  def get_id_no(self):
    return self.id_no

  def get_title(self):
    return self.title

  def set_title(self, title):
    self.title = title

  def get_description(self):
    return self.description

  def set_description(self, description):
    self.description = description

  def get_author(self):
    return self.author

  def set_author(self, author):
    self.author = author

  def get_status(self):
    return self.status

  def set_status(self, status):
    self.status = status

  def __str__(self):
    return f'id: {self.id_no}, title: {self.title}, description: {self.description}, author: {self.author}, status: {self.status}'


class Borrowing_order:
  count = 0
  random_ids = random.sample(range(1, 100000), 20)
  random_ids.sort()

  def __init__(self, total_days, client_id, book_id):
    self.id_no = str(Borrowing_order.random_ids[Borrowing_order.count]).zfill(6)
    Borrowing_order.count += 1

    self.start_date = datetime.datetime.now()
    self.end_date = self.start_date + datetime.timedelta(days = total_days) 
    self.client_id = client_id
    self.book_id = book_id
    self.status = self.get_status()     

  def get_id_no(self):
    return self.id_no

  def get_start_date(self):
    return self.start_date

  def get_end_date(self):
    return self.end_date

  def get_book_id(self):
    return self.book_id

  def get_client_id(self):
    return self.client_id

  def set_client_id(self, client_id):
    self.client_id = client_id

  def return_book(self, borrowing_order_id):
    if self.get_status() == 'Active':
      self.status = 'Canceled'

  def get_status(self):
    if self.end_date >= self.start_date:
      return 'Active'
    elif self.end_date < self.start_date:
      return 'Expired'

    
clients = list()
librarians = list()
books = list()
borrowed_orders = list()

client1 = Client("Joe Doe", 20, "+9721321901")
client2 = Client("Alice Doe", 25, "+9721329902")
client3 = Client("Bob Doe", 25, "+9721339903")
clients.extend([client1, client2, client3])

librarian = Librarian("Thomas Will", 31, "+9723291392", 500)
librarians.append(librarian)

book1 = Book("Structure and Interep", "blah blah balh ...", "Acd")
book2 = Book("Intro to CS", "blah blah balh ...", "Acd")
book3 = Book("Linear Algebra", "blah blah balh ...", "Acd")
book4 = Book("Digital Systems", "blah blah balh ...", "Acd")
books.extend([book1, book2, book3, book4])

books_ids = list()
for book in books:
  books_ids.append(book.get_id_no())


print('Welcome to our library system!')
while True:
  print('\nYou can do the following actions: ')
  print('1. display books')
  print('2. display clients')
  print('3. borrow a book')
  print('4. return a book')
  print('5. exit')
  action = int(input('\nEnter an action: '))
  if action == 1:
    print('\nBooks: ')
    for book in books:
      print(book)
  elif action == 2:
    print('\nClients: ')
    for client in clients:
      print(client)
  elif action == 3:
    book_id = input('\nEnter the id of the book to borrow: ')
    requested_book = list(filter(lambda book: (book.get_id_no() == book_id), books))
    
    while(len(requested_book) < 1):
      print('Invaild book id. Here are the vaild ones: ')
      for book in books:
        print(book.get_id_no())
      book_id = input('\nEnter the id of the book to borrow: ')
      requested_book = list(filter(lambda book: (book.get_id_no() == book_id), books))
    
    requested_book = requested_book[0]
    
    if(requested_book.get_status() == 'Active'):
      requested_book.set_status('In-Active')
      client_id = input('\nEnter client id: ')
      client = list(filter(lambda client: (client.get_id_no() == client_id), clients))

      while(len(client) < 1):
        print('Invaild client id. Here are the vaild ones: ')
        for user in clients:
          print(user.get_id_no())
        client_id = input('\nEnter client id: ')
        client = list(filter(lambda client: (client.get_id_no() == client_id), clients))

      borrow_order = Borrowing_order(10, client_id, book_id)
      borrowed_orders.append(borrow_order)
    else:
      print('The book is currently not active for borrowing')
  elif action == 4:
    borrowed_order_id = input('\nEnter borrowing order id: ')
    borrowed_order = list(filter(lambda borrowed_order: (borrowed_order.get_id_no() == borrowed_order_id), borrowed_orders))
    
    while(len(borrowed_order) < 1):
      print('Invaild borrowed order id. Here are the vaild ones: ')
      for borrowed_order in borrowed_orders:
        print(borrowed_order.get_id_no())
      borrowed_order_id = input('\nEnter borrowing order id: ')
      borrowed_order = list(filter(lambda borrowed_order: (borrowed_order.get_id_no() == borrowed_order_id), borrowed_orders))
    
    borrowed_order = borrowed_order[0]

    if(borrowed_order.get_status() == 'Active'):
      borrowed_order.return_book(borrowed_order.get_id_no())
      returned_book = list(filter(lambda book: (book.get_id_no() == borrowed_order.get_book_id()), books))[0]
      returned_book.set_status('Active')

  elif action == 5:
    break
  else:
    print('Invaild action! Please enter a vaild action between 1 and 4')


total_borrowed_orders = len(borrowed_orders)

total_borrowed_books = 0 # no of inactive books
total_available_books = 0 # no of active books

for book in books:
  if book.get_status() == 'In-Active':
    total_borrowed_books += 1
  else:
    total_available_books += 1


print("Total borrowing orders: " + str(total_borrowed_orders))
print("Total borrowed books: " + str(total_borrowed_books))
print("Total available books: " + str(total_available_books))