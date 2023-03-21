def check(string):
    s = 0
    for el in string:
        try:
            s += int(el)
        except ValueError:
            pass

    return s

string = '8teh5487iu1jkb4823o7g2ov8fui3og87g73o821oyito5g4b8oop787i9uyhj'
print(check(string))
    




