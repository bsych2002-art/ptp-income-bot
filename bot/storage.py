orders = []

def add_order(user_id, side, amount):
    orders.append({
        "user_id": user_id,
        "side": side,
        "amount": amount
    })

def get_orders():
    return orders