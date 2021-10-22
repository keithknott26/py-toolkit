from individual import Individual


class Student(Individual):
    """ A student is an Individual """
    def __init__(self, firstname, lastname, badge):
        super().__init__(firstname, lastname)
        self._badge = badge

    """ Class extension """
    def badge(self):
        return self._badge
