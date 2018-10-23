class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist 
    self.title = title
    self.medium = medium 
    self.year = year
    self.owner = owner 
  def __repr__(self):
    return "{artist}. {title}, {medium}, {year}, {owner} {ow}".format(artist = self.artist, title = self.title, medium = self.medium, year = self.year, owner = self.owner.name, ow = self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, old_list):
     self.listings.remove(old_list)
  def show_listing(self):
    for lists in self.listings:
      print(lists)

class Client: 
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "private collection"
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_list = Listing (artwork, price, self)
      veneer.add_listing(new_list)
  def buy_artwork(self, artwork): 
    if artwork.owner != self:
      art_listing = None
      for listings in veneer.listings:
        if listings.art == artwork:
          art_listing = listings
          break
    if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)
        
      
    
    
  
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{art}, {price}".format(art = self.art.title, price = self.price)
    


      
veneer = Marketplace()
#print(veneer.show_listing())

edytta = Client("Edytta Halpirt", None, False)
#rint(edytta)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a mandolin(Fanny Tellier)", 1910, "oil on canvas", edytta)
#print(girl_with_mandolin)
edytta.sell_artwork(girl_with_mandolin, "$6m (USD)")
#veneer.show_listing()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listing()
