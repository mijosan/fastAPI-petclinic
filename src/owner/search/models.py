from elasticsearch_dsl import Document, Text, Integer

class OwnerDocument(Document):
    id = Integer()
    name = Text()

    class Index:
        name = 'owners'
