from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        self.movie_to_unrented = defaultdict(SortedList)
        self.rented = SortedList()
        self.price_lookup = {}

        for shop, movie, price in entries:
            self.movie_to_unrented[movie].add((price, shop))
            self.price_lookup[(shop, movie)] = price

    def search(self, movie):
        return [shop for price, shop in self.movie_to_unrented[movie][:5]]

    def rent(self, shop, movie):
        price = self.price_lookup[(shop, movie)]
        self.movie_to_unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        price = self.price_lookup[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.movie_to_unrented[movie].add((price, shop))

    def report(self):
        return [[shop, movie] for price, shop, movie in self.rented[:5]]

