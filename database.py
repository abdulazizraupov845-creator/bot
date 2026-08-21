ORDERS = []

def save_order(user_id, full_name, phone, order_text):
    order = {
        "user_id": user_id,
        "full_name": full_name,
        "phone": phone,
        "order": order_text
    }
    ORDERS.append(order)
    return order