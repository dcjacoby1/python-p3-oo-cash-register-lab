#!/usr/bin/env python3
#pytest lib/testing/cash_register_test.py

class CashRegister:
  def __init__(self, discount = 0, total = 0, items = None):
    self.discount = discount
    self.total = total
    if not items is None:
      self.items = items
    else:
      self.items = []

  def add_item(self, title, price, quantity = 1, item_price = None):
    self.total += price * quantity
    
    if item_price is None:
      self.item_price = []
    self.item_price.append({"price": price, "quantity": quantity})
    for _ in range(quantity):
      self.items.append(title)
    
    

  def apply_discount(self):
    self.total = int(self.total * ((100 - self.discount) /100))
    if self.discount > 0:
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if len(self.item_price) > 0:
      self.total -= (self.item_price[-1]["price"] * self.item_price[-1]["quantity"])
      self.item_price.pop()
    else:
      self.total = 0.0


   