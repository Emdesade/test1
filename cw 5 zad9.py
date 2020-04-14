def samogloska(data):
    for i in data:
         if i in ("a","e","i","o","u","y"):
             yield i

obiekt =samogloska("jacek")
print(next(obiekt))
print(next(obiekt))
print(next(obiekt))
