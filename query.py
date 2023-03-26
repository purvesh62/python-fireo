import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, IDField, BooleanField, ListField

fireo.connection(
    from_file="firebase-project-app-380804-firebase-adminsdk-vhy7s-3289a3903b.json")


class City(Model):
    short_name = IDField()
    name = TextField()
    state = TextField()
    country = TextField()
    capital = BooleanField()
    population = NumberField()
    regions = ListField()

    @classmethod
    def get_capital_cities(cls):
        return cls.collection.filter('capital', '==', True).fetch()


def db_init():
    City.collection.create(
        short_name='SF', name='San Francisco', state='CA', country='USA',
        capital=False, population=860000, regions=['west_coast', 'norcal']
    )

    City.collection.create(
        short_name='LA', name='Los Angeles', state='CA', country='USA',
        capital=False, population=3900000, regions=['west_coast', 'socal']
    )

    City.collection.create(
        short_name='DC', name='Washington D.C.', state='CA', country='USA',
        capital=True, population=680000, regions=['east_coast']
    )

    City.collection.create(
        short_name='TOK', name='Tokyo', country='Japan',
        capital=True, population=9000000, regions=['kanto', 'honshu']
    )

    City.collection.create(
        short_name='BJ', name='Beijing', country='China',
        capital=True, population=21500000, regions=['hebei']
    )


# cities = City.collection.filter('state', '==', 'CA').fetch()
# # OR
# cities = City.collection.filter(state='CA')
#
# print(f"All cities with state = 'CA' {cities}")
#
# # The following query returns all the capital cities
# capital_cities = City.collection.filter('capital', '==', True).fetch()
#
# # Multiple equality operator can also apply in same single filter
# City.collection.filter(state='CA', capital=True)
#
# # Direct assignment is only work with equality(==) operator for others user regular filter
# # For example:
# # Get cities with state CA and population is greater than 1000000
#
# City.collection.filter(state='CA').filter('population', '>', 1000000)
#
# # Return the first entry
# city = City.collection.filter('state', '==', 'CA').get()
#
# # The filter() method takes three parameters: a field to filter on, a comparison operation, and a value.
# # The comparison can be <, <=, ==, >, >=, array-contains, in and array-contains-any.
# City.collection.filter('state', '==', 'CA')
# City.collection.filter('population', '<', 1000000)
# City.collection.filter('name', '>=', 'San Francisco')
#
# sydney_query = City.collection.filter('state', '==', 'CO').filter('name', '==', 'Denver')
#
# large_us_cities_query = City.collection.filter('state', '==', 'CA').filter('population', '>', 1000000)

# The following query returns all the capital cities
def custom_for_loop(iterable, action_to_do):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item.to_dict())

capital_cities = City.get_capital_cities()

custom_for_loop(capital_cities, print)
