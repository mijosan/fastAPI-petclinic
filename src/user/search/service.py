import json
import logging

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

from .exceptions import DocumentNotFoundException
from .schemas import UserRequest, UserResponse, UserSchema

logger = logging.getLogger('app')

class UserSearchService:
    def __init__(self, es: Elasticsearch):
        self.es = es

    def search_users(self, user_request: UserRequest) -> UserResponse:
        if user_request.name:
            search = Search(using = self.es, index="users").query("match", name=user_request.name)
        else:
            search = Search(using = self.es, index="users").query("match_all")
        
        # 디버깅을 위해 to_dict() 출력
        logger.info("Search Query:", json.dumps(search.to_dict(), indent=2))

        # 직접 HTTP 요청 보내기
        response = self.es.transport.perform_request(
            method = 'POST',
            headers = {"Content-Type": "application/json"},
            target = '/users/_search',
            body = search.to_dict()
        )

        response_data = response.body

        if not response_data['hits']['hits']:
            raise DocumentNotFoundException(user_request.name)

        results = []
        for hit in response_data['hits']['hits']:
            results.append(UserSchema(id = hit['_source']['id'], name = hit['_source']['name']))

        return UserResponse(
            total = len(results),
            users = results
        )