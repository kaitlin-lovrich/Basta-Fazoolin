# Menu class takes 4 parameters 
# menu name, menu items, menu start time and end time
# Returns string containing available menu(s) at inputted time
# Contains calculate_bill() method
class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{name} Menu available from {start} to {end}".format(name=self.name, start=str(self.start_time), end=str(self.end_time))

  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]   
    return bill

# Franchise class takes 2 parameters - address of franchise and  menus available at franchise as inputs
# Returns franchise address when franchise object is called
# Contains available_menus() method 
class Franchise:

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):    
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

# Business class takes 2 parameters - name of business and  franchises as inputs
# Returns franchise names of business object when called
# Contains no written methods 
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return self.franchises

# Menu items:
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00} 

# New Take a' Arepa Menu:
arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# Menu objects:
brunch = Menu("Brunch", brunch_items, 1100, 1600)
early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)
dinner = Menu("Dinner", dinner_items, 1700, 2300)
kids = Menu("Kids", kids_items, 1100, 2100)
arepas = Menu("Arepa", arepas_menu, 1000, 2000)

# Menus for Basta Fazoolin' franchises:
all_four_menus = [brunch, early_bird, dinner, kids]

# Franchise objects:
flagship_store = Franchise('1232 West End Road', all_four_menus)
new_installment = Franchise('12 East Mulberry Street', all_four_menus)
arepas_place = Franchise('189 Fitzgerald Avenue', arepas)

bf_franchises = [flagship_store, new_installment]

# Business objects
basta_fazoolin = Business("Basta Fazoolin' with my Heart", bf_franchises)
arepa = Business("Take a' Arepa", arepas_place)
