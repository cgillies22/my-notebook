lefthand_beers = ["Milk Stout", "Good Juju", "Fade to Black", "Polestar Pilsner"]
lefthand_beers += ["Black Jack Porter", "Wake Up Dead Imperial Stout","Warrior IPA"]

from math import factorial
def comb(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
from scipy.misc import comb
print(comb(12,9))
