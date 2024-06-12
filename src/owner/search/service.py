from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from .exceptions import DocumentNotFoundException
from .schemas import OwnerRequest, OwnerResponse, Owner
import json

class OwnerSearchService:
    def __init__(self, es: Elasticsearch):
        self.es = es

    def search_owners(self, owner_request: OwnerRequest) -> OwnerResponse:
        if owner_request.name:
            search = Search(using=self.es, index="owners").query("match", name=owner_request.name)
        else:
            search = Search(using=self.es, index="owners").query("match_all")
        
        # 디버깅을 위해 to_dict() 출력
        print("Search Query:", json.dumps(search.to_dict(), indent=2))

        # 직접 HTTP 요청 보내기
        response = self.es.transport.perform_request(
            method='POST',
            headers={"Content-Type": "application/json"},
            target='/owners/_search',
            body=search.to_dict()
        )

        response_data = response.body

        if not response_data['hits']['hits']:
            raise DocumentNotFoundException(owner_request.name)

        results = []
        for hit in response_data['hits']['hits']:
            results.append(Owner(id=hit['_source']['id'], name=hit['_source']['name']))

        return OwnerResponse(
            total=len(results),
            owners=results
        )