class PartnerPhotoIterator:
    def __init__(self, data):
        self.data = data
        self.cursor = 0
        self.stop = len(self.data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == self.stop:
            raise StopIteration
        likes = self.data[self.cursor]['likes']['count']
        link = None
        for i in self.data[self.cursor]['sizes']:
            if i['type'] == 'x':
                link = i['url']
        self.cursor += 1
        return {'likes': likes, 'link': link}
