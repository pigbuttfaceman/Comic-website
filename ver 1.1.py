from bottle import run, route, view, get, post, request
from itertools import count



class Comic:

    _ids = count (0)

    def __init__(self, name, stock, image):
        self.id = next(self._ids)
        self.comic_name = name
        self.comic_image = image
        self.comic_stock = stock



comics = [
    Comic("Super Dude", "image", 8 ),
    Comic("Lizard Man", "image", 12 ),
    Comic("Water Woman", "image", 3)
    ]


#index page
@route("/")
@view ("index")
def index():

    pass

#kid
@route("Kid")
@view ("Kid")
def Kid():

    pass

run(host='0.0.0.0', port=8080, reloader = True, debug = True)


