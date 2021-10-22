"""
    Generic Indivividual
"""


class Individual(object):
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def fullname(self):
            return f'{self.firstname} {self.lastname}'

        def initials(self):
            first_initial = self.firstname[0] if self.firstname else ""
            last_initial = self.lastname[0] if self.lastname else ""
            return f'{first_initial}{last_initial}'
