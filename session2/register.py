from mongoengine import Document, StringField, IntField
# document da co san thao tac create, update,replace, delete
# design
class Register(Document):
    username = StringField()
    password = StringField()