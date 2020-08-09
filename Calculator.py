import math

# A program that's probably going to save you $1 on your next soda bulk purchase
# Opinion: Fluid Ounce / ML per $ is a better measurement than the other way round and much more comparable for a human

FLOZ_TO_ML: float = 29.574

floz = 16
unit = 8
price = 1

txt =(
f"{unit} container(s) sold at ${price} each containing {floz} fluid ounces mean: \n" \
f"Fl Oz /$: {floz * unit} \n" \
f"ml/$: {floz * unit * FLOZ_TO_ML}")


print(txt)


