from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Job

class JobDocument(Document):
    class Index:
        name = "jobs"
        settings = {"number_of_shards": 2}

    class Django:
        model = Job 
        fields = ["title", "location"]
