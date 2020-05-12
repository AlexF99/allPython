
#classes


class User:

    def __init__(self, name, password, current):
        self._name = name
        self._password = password
        self._categories = ["food", "car", "shopping", "undefined"]
        self._current = current


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name


    @property
    def current(self):
        return self._current
    @current.setter
    def current(self, new_current): #there shouldnt be public access to this, only through user actions
        self._current = new_current


    def set_password(self, old_psw, new_psw):
        """setter will be used to change a users password, will have encryption."""
        if old_psw == self._password:
            self._password = new_psw
        else:
            print("wrong password")




class Action:
    """this class will make actions on user's current amount of money"""
    #tipo = "true or false"
    def __init__(self, amount, date, category, user_object):
        self._amount = amount # any expense or gain
        self._date = date # string containing date in aaaammdd format
        self._category = category # could be any listed category
        self._user = user_object


    def increment(self):
        curr = self._user.current
        curr += self._amount
        self._user.current = curr

    def decrement(self):
        curr = self._user.current
        curr -= self._amount
        self._user.current = curr
    # the methods below will allow user to edit the action they will make.

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, new_date):
        self._date = new_date


    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_catg):
        self._category = new_catg

    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, new_amt):
        self._amount = new_amt







#functions

def login():
    """function that verifies if user has signed up (has to check database). if they have, it starts app normally, else it calls sign up function
    this will be the authentication process"""
    pass

def sign_up():
    """adds a new user to the database, including name, password and current amount"""
    pass



#tests
user_test = User("alex", "lele123", 1200)
gasto1 = Action(200, "hoje", "car", user_test)
ganho1 = Action(200, "hoje", "car", user_test)

