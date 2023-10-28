from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

weight_lim = 10
weight=item_id["mass"]+item_laptop["mass"]+item_money["mass"]

# Start game at the reception
current_room = rooms["Reception"]
