import json
from datetime import datetime
class PostManager:
    JSON_FILE = "data.json"

    def __init__(self):
        self.__posts = self.loadDB()

    def loadDB(self):
        with open(PostManager.JSON_FILE) as f:
            return json.load(f)


    def savePosts(self, posts):
        with open(PostManager.JSON_FILE, "w") as f:
            json.dump(posts, f)

    def insertPost(self, aPost):
        aPost.id = self.__posts[0]["id"] + 1
        aPost.count = 0
        aPost.date = datetime.strftime(datetime.now(), "%d %m %Y")
        self.__posts.insert(0, aPost.toDic())

        self.savePosts(self.__posts)

    def updatePost(self, indexID, aPost):
        for _idx, _post in enumerate(self.__posts):
            if indexID == _post["id"]:
                aPost.count = _post["count"]
                aPost.date = _post["date"]
                self.__posts[_idx] = aPost.toDic()
        self.savePosts(self.__posts)

    def deletePost(self, indexID):
        for _idx, _post in enumerate(self.__posts):
             if indexID == _post["id"]:
                del self.__posts[_idx]
        self.savePosts(self.__posts)
              
    

    def getPosts(self):
        return self.__posts

    def getPost(self, indexID):
        print("here")
        for _idx, _post in enumerate(self.__posts):
            if indexID == _post["id"]:
                _post["count"] += 1
                self.savePosts(self.__posts)
                return _post
        return None