import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, DateTime, IDField, BooleanField, ListField, Field

fireo.connection(
    from_file="firebase-credentials.json")



class Event(Model):
    id = IDField()
    title = TextField()
    description = TextField()
    banner_image = TextField()
    images = ListField()
    date = TextField()
    time = TextField()
    address = TextField()
    price = NumberField()
    city = TextField()
    country = TextField()
    runtime = NumberField()
    organizer = TextField()
    type = TextField()


def add_event(*kwargs):
    print(kwargs)


price = 358.00

e = Event(
    title="Small Soft Tuna",
    description="New range of formal shirts are designed keeping you in mind. With fits and styling that will make you stand apart",
    banner_image="https://loremflickr.com/640/480/sports",
    images=["https://loremflickr.com/640/480/business"],
    date="2017-03-23T19:18:27.946Z",
    time="2087-09-23T17:16:41.104Z",
    address="9679 Kenya Lakes",
    price=358.00,
    city="Benedictport",
    country="Saudi Arabia",
    runtime=2,
    organizer="57148ea9e01faffe3a58cdf9",
    type="Paid" if price > 0 else "Free"
)

e.save()
print(e.id)
print(e.key)
