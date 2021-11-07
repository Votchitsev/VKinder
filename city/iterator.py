class CityIterator:

    def __init__(self, data):
        self.data = data['response']['items']
        self.cursor = 0
        self.stop = data['response']['count'] - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == self.stop:
            raise StopIteration
        city_id = self.data[self.cursor]['id']
        city_title = self.data[self.cursor]['title']
        result = (city_id, city_title)
        self.cursor += 1
        return result
