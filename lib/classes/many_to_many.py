import re

class NationalPark:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is str and len(value) >= 3 and not hasattr(self, 'name'):
            self._name = value
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        return max(self.visitors(), key=lambda v: v.total_visits_at_park(self))


class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) is str and len(start_date) >= 7:
            pattern = re.compile(r"^[A-Z][a-z]*\s[0-9]{1,2}[a-z]{2}")
            match = pattern.fullmatch(start_date)
            if match is not None:
                self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) is str and len(end_date) >= 7:
            pattern = re.compile(r"^[A-Z][a-z]*\s[0-9]{1,2}[a-z]{2}")
            match = pattern.fullmatch(end_date)
            if match is not None:
                self._end_date = end_date


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) is str and 1 <= len(value) <= 15:
            self._name = value
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        trips = self.trips()
        return len([trip for trip in trips if trip.national_park == park])