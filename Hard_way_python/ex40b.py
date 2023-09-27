#call function from ex40_mystuff.py
import ex40_mystuff
import ex40c
ex40_mystuff.apple()
print(ex40_mystuff.tangerine)

#dict style
#ex40_mystuff['apple']
# module style
ex40_mystuff.apple()
print(ex40_mystuff.tangerine)
# class style
thing = ex40c.MyStuff()
thing.apple()
print(thing.tangerine)