from datetime import datetime

class Post:
    def toDic(self):
        return {"id": self.id, "title": self.title, "name": self.name, "date": self.date,"count": self.count, "desciption":self.description}

    @staticmethod
    def populate(row):
        aPost = Post()
        aPost.id = row.get("id")
        aPost.title = row.get("title")
        aPost.name = row.get("name")
        aPost.description = row.get("description")
        aPost.date = row.get("date")
        aPost.count = row.get("count")
        
        return aPost