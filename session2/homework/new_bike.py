from mongoengine import Document, StringField, IntField
# document da co san thao tac create, update,replace, delete
# design
class New_bike(Document):
    model = StringField()
    dailyFee = StringField()
    image = StringField()
    year = StringField()
