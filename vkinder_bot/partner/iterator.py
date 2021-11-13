class PartnerPhotoIterator:
    def __init__(self, data):
        self.data = data
        self.cursor = 0
        self.stop = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == self.stop:
            raise StopIteration
        likes = self.data[self.cursor]['likes']['count']
        comments = self.data[self.cursor]['comments']['count']
        likes_and_comments = likes + comments
        media_id = self.data[self.cursor]['id']
        self.cursor += 1
        return {'likes_and_comments': likes_and_comments, 'id': media_id}
