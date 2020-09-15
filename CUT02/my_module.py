from db import db_read

def total_value(item_id):
    items = db_read(item_id)
    return sum(items)