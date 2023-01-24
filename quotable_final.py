import random
import shelve

quote_storage = {
  "Motiv": ["You can do it!", "Just believe!", "Never stop!", "You are him.", "Never doubt yourself, ever.", "You are the best player in the game.", "Everybody is counting on you.", "In spite of everything you've done for them, eventually they will hate you.", "Those who doubted you will soon retell how they met you."],
  "Fun": ["He he ha ha", "Your mother", "Joe mama", "Throw it on a dime", "Do you want to get candy?", "I missed the rage!!!!", "Its genover", "stewie, its not your fault, its not your fault","two L's make a Y, get em up, take it down, amariLLO, LLamar, me LLamo"],
  "Love" : ["You are my sunshine.", "I'm so glad we are together.", "Always be by my side.", "All that you are is all I ever need.", "Every moment is a good one with you."],
}

accounts = {

}

a = None

class Account:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.quote_saved = { #
      "Liked": [],
      "Disliked" : [],
      "Favorited":[],
      "Motiv": [],
      "Fun": [],
      "Love": [],
      "Custom": []
    }

  def quote_save(self, type, text):
    self.quote_saved[type].append(text)

class QuoteCreate:
  def __init__(self,text):
    self.text = text
  def quote_mot(self, text):
    self.text = text
    a.quote_saved["Motiv"].append(text)
    print("Now that's Quotable!")
  def quote_fun(self, text):
    self.text = text
    a.quote_saved["Fun"].append(text)
    print("Now that's Quotable!")
  def quote_love(self, text):
    self.text = text
    a.quote_saved["Love"].append(text)
    print("Now that's Quotable!")
  def quote_custom(self, category, text):
    self.category = category
    self.text = text
    a.quote_saved["Custom"].append([category,text])
    print("Now that's Quotable!")

with shelve.open("accounts") as db:
  if 'accounts' in db:
    accounts = db["accounts"] #pull

def main():
  global a
  while True:
    print("1. Feed | 2. Create Quotes | 3. View Interactions | 4. Search | 5. Account Settings")
    choice = input("What would you like to do?")
    if choice == '1':
      quote_display()
    if choice == '2':
      create_quote()
    if choice == '3':
      view_saved()
    if choice == '4':
      search()
    if choice == '5':
      account_set()

def account_set():
  action = input("1. Delete Account | 2. Logout")
  if action == '1':
    delete_account()
  elif action == '2':
    logout()
  else:
    print("Invalid Action")

def createAcc():# create your account
  global a
  username = input('Username:')
  password = input('Password:')
  a = Account(username,password)
  accounts[username] = a
  with shelve.open("accounts") as db:
    db["accounts"] = accounts
  print("Account created! Welcome to Quotable,", username,"!")
  main()

def login(): # feature to log you into the account
  global a
  username = input('Username:')
  if username in accounts:
    a = accounts[username]
    password = input('Password:')
    if a.password == password:
      print("Success, you are logged in! Welcome to Quotable,",username,".")
      main()
    else:
        print("Error, wrong password")
        login()
  if username not in accounts:
    print("Error, wrong username.")
    login()

def delete_account():
  global a
  username = input('Username:')
  if username in accounts:
    password = input('Password:')
    if a.password == password:
      del accounts[username]
      with shelve.open("accounts") as db:
        db["accounts"] = accounts
      print("Account deleted! Goodbye.")
      menu()
  else:
    print("Error, wrong username.")
    delete_account()

def logout():
  global a
  a = None
  menu()

def quote_display():
  def quote_action():
    action = input("1. Like | 2. Dislike | 3. Favorite")
    if action == '1':
      a.quote_save('Liked', x)
      with shelve.open("accounts") as db:
        db["accounts"] = accounts
      print("Liked!")
    elif action == '2':
      a.quote_save('Disliked',x)
      with shelve.open("accounts") as db:
        db["accounts"] = accounts
      print("Disliked!")
    elif action == '3':
      a.quote_save('Favorited', x)
      with shelve.open("accounts") as db:
        db["accounts"] = accounts
      print("Favorited!")
    else:
      print("Error, please choose a correct action")
      quote_action()
  print('')
  random_quotes = random.choice(list(quote_storage.values()))
  x = random.choice(random_quotes)

  print('Your Quotable:', x)
  print("")
  quote_action()

def create_quote():
  print("")
  print("Welcome to QuotableCreate!")
  print('')
  print("Categories: 1. Motivation | 2. Fun | 3. Love | 4. Custom")
  cat_sel = input("What category is your Quotable?")
  text = input("Type in your quote:")

  Quote = QuoteCreate(text)

  if cat_sel == '1':
    Quote.quote_mot(text)
    with shelve.open("accounts") as db:
        db["accounts"] = accounts
  elif cat_sel == '2':
    Quote.quote_fun(text)
    with shelve.open("accounts") as db:
        db["accounts"] = accounts
  elif cat_sel == '3':
    Quote.quote_love(text)
    with shelve.open("accounts") as db:
        db["accounts"] = accounts
  elif cat_sel == '4':
    custom_cat = input("Name of new category?")
    Quote.quote_custom(custom_cat, text)
  else:
    print("Error, that category is not an option.")
    create_quote()

def view_saved():
  print("See 1. Liked | 2. Favorited | 3. User Made")
  query = input("Which would you like to see? ")
  if query == '1':
    print("You liked:", a.quote_saved['Liked'])
  if query == '2':
    print("You favorited:", a.quote_saved['Favorited'])
  if query == '3':
    print("1. Motivation | 2. Fun | 3. Love | 4. Custom")
    loca = input("What type of quote do you want to see?")
    if loca == '1':
      print("You made:", a.quote_saved['Motiv'])
    if loca == '2':
      print("You made:", a.quote_saved['Fun'])
    if loca == '3':
      print("You made:", a.quote_saved['Love'])
    if loca == '4':
      print("You made:", a.quote_saved['Custom'])

def search():
  print("Welcome to Quotable Advanced Search!")
  print('')
  print("Search for Quotes that you have interacted with!")
  term1 = input("What category is this quote in:")
  term2 = input("Text of Quote to search for:")

  if term1 in a.quote_saved:
    if term2 in a.quote_saved[term1]:
      print("You have interacted with this quote.")
    else:
      print("You have not interacted with this quote.")
  if term1 not in a.quote_saved:
    print("Error: Invalid category. Please choose a valid category.")


def menu():
  print("1. Create account | 2. Login")
  choice = input("What would you like to do?")
  if choice == '1':
    createAcc()
  elif choice == '2':
    login()
  else:
    print('error')
menu()
