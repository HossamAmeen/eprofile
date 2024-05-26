import time
from django.db import connection
from django.utils.deprecation import MiddlewareMixin


class QueryDebugMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        self.initial_queries = len(connection.queries)

    def process_response(self, request, response):
        total_time = time.time() - self.start_time
        final_queries = connection.queries[self.initial_queries:]
        num_queries = len(final_queries)
        
        print(
            f"Total Time: {total_time:.2f}s | "
            f"Number of Queries: {num_queries}"
        )
        for query in final_queries:
            print(query['sql'])

        return response
