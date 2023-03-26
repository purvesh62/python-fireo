import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import dataclasses

# Use a service account.
cred = credentials.Certificate('firebase-project-app-380804-firebase-adminsdk-vhy7s-3289a3903b.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


@dataclasses.dataclass
class City:
    name: str
    state: str
    country: str
    capital: bool = False
    population: int = 0
    regions: list = dataclasses.field(default_factory=list)

    def to_dict(self):
        _dict = self.__dict__.copy()
        return _dict


city = City(name=u'Los Angeles', state=u'CA', country=u'USA')
print(city.to_dict())
db.collection(u'cities').document().set(city.to_dict())
