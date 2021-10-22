from individual import Individual


class Teacher(Individual):
    """ A teacher is an individual """
    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        self._subject = subject

    """ Override the parent method """
    def fullname(self):
        return f'{self.lastname}, {self.firstname} teaches {self._subject}'

    """
        Overloading the parent method.
        In python you can't have multiple method with the same function name,
        you achieve overloading by providing a list of optional parameters.
        (https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python)
    """
    def initials(self, prefix='Prof.'):
        return f'{prefix} - {super().initials()}'
