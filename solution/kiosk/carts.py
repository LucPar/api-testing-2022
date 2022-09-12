CARTS = {}


def _find_cart(session_id):
    if session_id not in CARTS:
        CARTS[session_id] = {}

    return CARTS[session_id]


def get_cart(session_id):
    cart = _find_cart(session_id)
    return list(cart.values())


def add_to_cart(session_id, item):
    cart = _find_cart(session_id)

    item_id = item['id']
    if item_id in cart:
        cart[item_id]['count'] += 1
    else:
        cart[item_id] = {
            'id': item['id'],
            'name': item['name'],
            'count': 1,
        }

    return list(cart.values())


def update_cart(session_id, item_id, count):
    cart = _find_cart(session_id)

    if item_id not in cart:
        raise Exception('Item not found in cart.')

    if count == 0:
        del cart[item_id]
    else:
        cart[item_id]['count'] = count

    return list(cart.values())
