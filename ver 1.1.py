from bottle import run, route, view, get, post, request, static_file
from itertools import count



class Comic:

    _ids = count (0)

    def __init__(self, name, image, stock):
        self.id = next(self._ids)
        self.comic_name = name
        self.comic_image = image
        self.comic_stock = stock



comics = [
    Comic("Super Dude", "superdude.jpg", 8 ),
    Comic("Lizard Man", "lizardman.png", 12 ),
    Comic("Water Woman", "drip.jpg", 3)
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
    pass   




#kid
@route("/Kid")
@view ("Kid")
def Kid():

    pass


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
    for Comic in comics:
        if comic.id == comic_id:
            found_comic = Comic
    data = dict (Comic = found_comic)
    found_comic.stock = found_comic.stock - 1
    
    return data






run(host='0.0.0.0', port=8080, reloader = True, debug = True)


