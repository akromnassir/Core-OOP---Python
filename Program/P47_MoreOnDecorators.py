
# In this example, we will be seeing some more concepts of decorators, such as
# property decorator, getters, and setter methods.

class BankAccount(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property                   # property decorator
    def fullName(self):
        return self.firstName + ' ' + self.lastName

    @fullName.setter
    def fullName(self, name):
        firstName, lastName = name.split(' ')
        self.firstName = firstName
        self.lastName = lastName

if __name__ == '__main__':
    acc = BankAccount('Nasirovr', 'Akrom')
    print(acc.fullName)              # Notice that we can access the method for our class BankAccount without
                                     # parentheses! This is because of the property decorator

    # acc.fullName = 'Akrom Nasirov'    #This throws an error! Hence, the setter decorator should be used.
    acc.fullName = 'Doni Adbdujalilov'
    print(acc.fullName)
