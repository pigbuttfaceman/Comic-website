from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Comic:

    _ids = count (0)

    def __init__(self, name, image, stock, sold):
        self.id = next(self._ids)
        self.comic_name = name
        self.comic_image = image
        self.comic_stock = stock
        self.comic_sold = sold



comics = [
    Comic("Super Dude", "superdude.jpg", 8, 0 ),
    Comic("Lizard Man", "lizardman.png", 12, 0 ),
    Comic("Water Woman", "drip.jpg", 3, 0)
    ]


#index page
@route("/")
@view ("index")
def index():

    pass





@route('/picture/<filename>')
def saved_picture (filename):
    return static_file(filename, root='./images')



@route("/stock")
@view("stock")
def stock():
    data = dict (comic_list = comics) 
    return data       




#plus_stock
@route("/plus_stock")
@view ("plus_stock")
def plus_stock():
    data = dict (comic_list = comics) 
    return data    



@route("/cart") 
@view("cart") 
def cart(): 
    data = dict (comic_list = comics) 
    return data 





@route('/buy_success/<comic_id>')
@view ('buy_success')
def buy_success(comic_id):
    
    comic_id = int(comic_id)
    found_comic = None
    for comic in comics:
        if comic.id == comic_id:
            found_comic = comic
    data = dict (comic = found_comic)
    found_comic.comic_stock = found_comic.comic_stock - 1
    found_comic.comic_sold = found_comic.comic_sold + 1
    
    return data


@route('/add_success/<comic_id>')
@view ('add_success')
def add_success(comic_id):
    
    comic_id = int(comic_id)
    found_comic = None
    for comic in comics:
        if comic.id == comic_id:
            found_comic = comic
    data = dict (comic = found_comic)
    found_comic.comic_stock = found_comic.comic_stock + 1
    
    return data



run(host='0.0.0.0', port=8080, reloader = True, debug = True)


