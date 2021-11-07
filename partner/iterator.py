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
        media_id = self.data[self.cursor]['id']
        self.cursor += 1
        return {'likes': likes, 'id': media_id}
