import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, IDField

fireo.connection(
    from_file="firebase-project-app-380804-firebase-adminsdk-vhy7s-3289a3903b.json")


class User(Model):
    id = IDField()
    name = TextField()
    age = NumberField()


# Add data
def add_data():
    u = User()
    u.name = "TEMP"
    u.age = 24
    u.id = "custom"  # custom id
    u.save(merge=True)  # u.upsert()
    print(u.id)
    print(u.key)


def get_data():
    # Get data
    user = User.collection.get("user/2aPJ0c90Qw0eib5enSDO")
    print(user.name, user.age)


def update_data():
    u = User()
    u.name = "ABCDDD"
    u.age = 20
    u.update("user/2aPJ0c90Qw0eib5enSDO")
    print("updated data.")
    get_data()


def delete_data():
    User.collection.delete("user/2aPJ0c90Qw0eib5enSDO")
    print("deleted.")


def add_data_from_dict():
    model_dict = {
        'name': 'AASDS',
        'age': 12
    }

    u = User.from_dict(model_dict)
    u.save()
    print(u.id)


class Post(Model):
    title = TextField()
    content = TextField()


class Review(Model):
    name = TextField()
    message = TextField()


def sub_tables():
    p = Post(title="My First Post", content="Post content")
    p.save()

    r = Review(parent=p.key)
    r.name = "Azeem"
    r.message = "Nice post"
    r.save()

    print(r.key)



transaction = fireo.transaction()

@fireo.transactional
def get_user(transaction):
    user = User.collection.filter('name', '==', 'TEMP').transaction(transaction).get()
    print(user.to_dict())

get_user(transaction)