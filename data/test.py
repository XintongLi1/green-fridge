from 'SheHacks 2021'.green-fridge.Queries import queries 
from data.queries import format_strings
from .filters import Filter
from .show import show

s = ["Receipt"," ","BREAD 2000001 $1.99","MILK 2000002 $4.99","ICECREAM 2000003 $5.99","Sweet COOKIE 2000004 $6.99","EGGS 2000005 $3.79","SUBTOTAL: $23.32","TAX $1.23","\f"]

print(show(s, 1, [("rating", 4.0), ("cuisine", "Chinese"), ("course", "Appetizers")]))

