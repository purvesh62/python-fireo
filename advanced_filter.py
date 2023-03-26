import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, DateTime, IDField, BooleanField, ListField

fireo.connection(
    from_file="firebase-project-app-380804-firebase-adminsdk-vhy7s-3289a3903b.json")


class Post(Model):
    title = TextField()
    content = TextField()

    @classmethod
    def get_detail(cls, key):
        post = cls.collection.get(key)
        recent_review = Review.collection.parent(key).order('-created_on').fetch(3)

        return post, recent_review


class Review(Model):
    name = TextField()
    stars = NumberField()
    created_on = DateTime(auto=True)


def db_init():
    p = Post(title="First Post", content="Post Content")
    p.save()

    r1 = Review(parent=p.key)
    r1.name = "Azeem"
    r1.stars = 5
    r1.save()

    r2 = Review(parent=p.key)
    r2.name = "Azeem"
    r2.stars = 4
    r2.save()

    r2 = Review(parent=p.key)
    r2.name = "Arfan"
    r2.stars = 3
    r2.save()

# db_init()

post, reviews = Post.get_detail("post/8EphAi15FSTuaI3uFCFN")

print(post.title)

for r in reviews:
    print(r.name, r.stars)
