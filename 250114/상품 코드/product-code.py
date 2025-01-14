product_name, product_code = input().split()
product_code = int(product_code)

# Write your code here!
class Goods:
    def __init__ (self, name="codetree", code=50):
        self.name = name
        self.code = code

goods = Goods()
goods1 = Goods(product_name, product_code)
print("product", goods.code, "is", goods.name)
print("product", goods1.code, "is", goods1.name)