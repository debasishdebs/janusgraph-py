# Name: Debasish Kanhar
# Emp ID: 05222V

from gremlin_python.driver.client import Client


class SchemaBuilder(object):
    def __init__(self, connection):
        """

        Args:
            connection (Client):
        """

        self.query = ""
        self.client = connection
        pass

    def create(self, query):
        self.query = query

        result_set = self.client.submit(self.query)
        future_results = result_set.all()
        results = future_results.result()

        return results