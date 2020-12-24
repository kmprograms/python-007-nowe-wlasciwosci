from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo

# 1. Nowe operatory dla dict

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 10, "c": 30}

# dict update - zawsze brane pod uwage sa klucze najbardziej z prawej strony
d3 = d1 | d2  # podobne do + w listach
print(d3)

# dict merge - zawsze brane pod uwage sa klucze najbardziej z prawej strony
d1 |= d2 # podobne do += w listach
print(d1)


# 2. Nowe funkcje dla napisow

filename1 = 'log_some_name.txt'

# usuwanie prefix
filename2 = filename1.removeprefix('log')
print(filename2)

# usuwanie suffix
filename3 = filename1.removesuffix('.txt')
print(filename3)


# 3. Dodanie do standardowej biblioteki stref czasowych IANA
# Mozna jes spotkac pod nazwa tz lub zone info

# Na Windows moze byc wymagana instalacja tzdata ktora umozliwi korzystanie z bazy danych stref czasowych
# Zainstaluj:
# >> python -m pip install tzdata
zone1 = ZoneInfo("America/Vancouver")
print(zone1)

now_warsaw = datetime.now(tz=ZoneInfo("Europe/Warsaw"))
print(now_warsaw)

now_london = datetime.now(tz=ZoneInfo("Europe/London"))
print(now_london)

[print(zone) for zone in zoneinfo.available_timezones()]

print(zone1.utcoffset(datetime.now()))
print(ZoneInfo("Europe/Warsaw").utcoffset(datetime.now()))


# 4. Rozbudowanie mozliwosci annotacji dla funkcji

from typing import Annotated, get_type_hints


def rectangle_area(a: Annotated[float, 'First side of rectangle'], b: Annotated[float, 'Second side of rectangle']):
    return a * b


print(rectangle_area(10, 20))

# dostep do annotacji:
print(rectangle_area.__annotations__)
print(rectangle_area.__annotations__["a"])
print(rectangle_area.__annotations__["a"].__metadata__)
print(rectangle_area.__annotations__["a"].__metadata__[0])
print(get_type_hints(rectangle_area))
print(get_type_hints(rectangle_area, include_extras=True))

# Ewentualnie mozna zapisac jeszcze tak:
Side = Annotated[float, 'Side of square']


def square(a: Side):
    return a ** 2


print(square(11))


# 5. Gruntowna przebudowa parsera

# -> Glownym skladnikiem python interpretera jest parser, ktory zostal w ostatnim czasie
#    gruntownie przebudowany

# -> Przed nowsza wersja Python domyslnie uzywal LL(1) parser. Teraz uzywa PEG parser
#    https://en.wikipedia.org/wiki/LL_parser
#    https://medium.com/@gvanrossum_83706/peg-parsing-series-de5d41b2ed60

# 6. Nowe funkcje matematyczne
import math
print(math.gcd(12, 18))
print(math.lcm(12, 18))
