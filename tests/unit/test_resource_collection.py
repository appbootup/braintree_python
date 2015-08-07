from tests.test_helper import *

class TestResourceCollection(unittest.TestCase):
    collection_data = {
        "search_results": {
            "page_size": 2,
            "ids": ["0", "1", "2", "3", "4"]
        }
    }

    class TestResource:
        items = ["a", "b", "c", "d", "e"]

        @staticmethod
        def fetch(query, ids):
            return [TestResourceCollection.TestResource.items[int(id)] for id in ids]

    def test_iterating_over_contents(self):
        collection = ResourceCollection("some_query", self.collection_data, TestResourceCollection.TestResource.fetch)
        new_items = []
        index = 0
        for item in collection.items:
            self.assertEquals(TestResourceCollection.TestResource.items[index], item)
            new_items.append(item)
            index += 1

        self.assertEquals(5, len(new_items))

