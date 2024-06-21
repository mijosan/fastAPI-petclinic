from elasticsearch_dsl import Document, Text, Integer

class UserDocument(Document):
    id = Integer()
    name = Text()

    class Index:
        name = 'users'
