import random
quote_storage = {
  "Motiv": ["Moti1", "Moti2", "Moti3", "Moti4", "Moti5"],
  "Fun": ["Fun1", "Fun2", "Fun3", "Fun4", "Fun5"],
  "Love" : ["Love1", "Love2", "Love3", "Love4", "Love5"],
}

quote_saved = {
  "Liked": [],
  "Disliked" : [],
  "Favorited":[]
}

accounts = []
name = None
user_quotes = []

class Account:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.moti_pref = 0
    self.fun_pref = 0
    self.love_pref = 0

  def moti_inc(self): #increase motivational quote preference
    self.moti_pref += 1
  def moti_dec(self):#decrease motivational quote preference
    self.moti_pref -= 1
  def fun_inc(self):#increase fun quote preference
    self.fun_pref += 1
  def fun_dec(self):#decrease fun quote preference
    self.fun_pref -= 1
  def love_inc(self):#increase love quote preference
    self.love_pref += 1
  def love_dec(self):#decrease love quote preference
    self.love_pref -= 1

class QuoteCreate:
  def __init__(self, quote, category):
    self.quote = quote
    self.category = category
def main():
  pass
main()

def createAcc():# create your account
  username = input('Username:')
  password = input('Password:')
  account_list = Account(username,password)
  accounts.append(account_list)

def login(): # feature to log you into the account
  global name
  username = input('Username:')
  for i in range(len(accounts)):
    if accounts[i].username == username:
      password = input('Password:')
      if accounts[i].password == password:
        name = accounts[i]
        print("Success")
        break
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

def menu():
  global name
  while True:
    print("1. Create account | 2. Login | 3. Delete Account | 4. Feed ")
    choice = input("What would you like to do?")
    if choice == '1':
      createAcc()
    if choice == '2':
      login()
    if choice == '3':
      del_Acc()
    if choice == '4':
      quote_display()
    if choice == '5':
      print("accounts:", accounts)
menu()
