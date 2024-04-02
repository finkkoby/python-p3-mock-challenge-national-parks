#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    park = NationalPark("Yellowstone")
    visitor = Visitor("Koby")
    trip = Trip(park, visitor, 'October 25th', 'October 31st')

    ipdb.set_trace()
