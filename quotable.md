import random

quote_storage = {
  "Motiv": ["Moti1", "Moti2", "Moti3", "Moti4", "Moti5"],
  "Fun": ["Fun1", "Fun2", "Fun3", "Fun4", "Fun5"],
  "Love" : ["Love1", "Love2", "Love3", "Love4", "Love5"],
}

quote_saved = {
  "Liked": [],
  "Disliked" : [],
  "Favorited":[],
  "Motiv": [],
  "Fun": [],
  "Love": [],
  "Custom": []
}

account_store = {
  "Accounts": [],
  "Passwords": [],
}

accounts = []
name = None
user_quotes = []

class Account:
  def __init__(self, username, password):
    self.username = username
    self.password = password


class QuoteCreate:
  def __init__(self, quote, category):
    self.quote = quote
    self.category = category

def createAcc():# create your account
  username = input('Username:')
  password = input('Password:')
  account_list = Account(username,password)
  accounts.append(account_list)
  main()

def login(): # feature to log you into the account
  global name
  username = input('Username:')
  for i in range(len(accounts)):
    if accounts[i].username == username:
      password = input('Password:')
      if accounts[i].password == password:
        name = accounts[i]
        print("Success")
        main()
        # break
      else:
        print("Error, wrong password")
        login()
    else:
      print("Error, wrong username")
      login()

'''def del_Acc():
  username = input('Username:')
  for i in range(len(accounts)):
    if username == accounts[i].username:
      accounts.remove(username)'''

def quote_display():
  def quote_action():
    action = input("1. Like | 2. Dislike | 3. Favorite")
    if action == '1':
      quote_saved['Liked'] += [x]
      print("Liked Quotables:", quote_saved['Liked'])
    elif action == '2':
      quote_saved['Disliked'] += [x]
      print("Disliked Quotables:", quote_saved['Disliked'])
    elif action == '3':
      quote_saved['Favorited'] += [x]
      print("Favorited Quotables:", quote_saved['Favorited'])
    else:
      print("Error, please choose a correct action")
      quote_action()
  random_quotes = random.choice(list(quote_storage.values()))
  x = random.choice(random_quotes)
  print('Your Quotable:', x)
  print("")
  quote_action()

def create_quote():
  print("")
  print("Welcome to QuotableCreate!")
  print("Categories: 1. Motivation | 2. Fun | 3. Love | 4. Custom")
  cat_sel = input("What category is your Quotable?")
  quote_text = input("Type in your quote:")

  if cat_sel == '1':
    quote_saved['Motiv'] += [quote_text]
    print("Now that's Quotable!")
  elif cat_sel == '2':
    quote_saved['Fun'] += [quote_text]
    print("Now that's Quotable!")
  elif cat_sel == '3':
    quote_saved['Love'] += [quote_text]
    print(quote_saved['Love'])
    print("Now that's Quotable!")
  elif cat_sel == '4':
    custom_cat = input("Name of new category?")
    quote_saved['Custom'] += [[quote_text,custom_cat]]
    print("Now that's Quotable!")
  else:
    print("Error, that category is not an option.")
    create_quote()


def view_saved():
  print("See 1. Liked | 2. Favorited | 3. User Made")
  query = input("Which would you like to see? ")
  if query == '1':
    print("You liked:", quote_saved['Liked'])
  if query == '2':
    print("You favorited:", quote_saved['Favorited'])
  if query == '3':
    print("1. Motivation | 2. Fun | 3. Love | 4. Custom")
    loca = input("What type of quote do you want to see?")
    if loca == '1':
      print("You made:", quote_saved['Motiv'])
    if loca == '2':
      print("You made:", quote_saved['Fun'])
    if loca == '3':
      print("You made:", quote_saved['Love'])
    if loca == '4':
      print("You made:", quote_saved['Custom'])

def search():
  print("Search for Quotes that you have interacted with!")
  # term = input("Keyword Query:")
  # if term in range(len())
  pass

def menu():
  global name
  print("1. Create account | 2. Login")
  choice = input("What would you like to do?")
  if choice == '1':
    createAcc()
  elif choice == '2':
    login()
  else:
    print('error')
menu()

def main():
  pass
  while True:
    print("1. Feed | 2. Create Quotes | 3. View Interactions | 4. Settings ")
    choice = input("What would you like to do?")
    if choice == '1':
      quote_display()
    if choice == '2':
      create_quote()
    if choice == '3':
      view_saved()
    if choice == '4':
      pass
main()
