#
# import datetime
# import uuid
#
# from src.common.database import Database
#
# '''from src.common.pymongo.database import Database'''
#
# from src.models.post import Post
#
#
# class Blog(object):
#     def __init__(self, author, author_id,  title, description,_id=None):
#         self.author= author,
#         self.author_id= author_id,
#         self.title= title,
#         self.description= description,
#         self._id= uuid.uuid4.hex() if _id is None else _id
#
#     def new_post (self, title, content, date= datetime.datetime.utcnow()):
#         '''title= input("This is my title"),
#         content= input("This is my content"),
#         #author= self.author,
#         date= input("Enter the date or leave blank for today(in format DDMMYYY)")
#         if date == "":
#             date  = datetime.datetime.utcnow()
#         else:
#             date = datetime.datetime.strptime(date, "%d%m%Y" )'''
#         post= Post(blog_id= self._id,
#                    title= title,
#                    content=content,
#                    author=self.author,
#                    created_date=date)
#         post.save_to_mongo()
#
#     def get_post(self):
#         return Post.from_blog(self._id)
#
#
#     def save_to_mongo(self):
#         Database.insert(collection='blogs', data=self.json())
#
#
#
#     def json(self):
#         return {
#          'title':self.title,
#          'author_id': self.author_id,
#          'description':self.description,
#          'author':self.author,
#          'id':self._id
#         }
#
#
#     @classmethod
#     def from_mongo(cls, id):
#         blog_data= Database.find_one(collection='blogs', query={'_id': id})
#         return cls(**blog_data)
#
#     @classmethod
#     def find_by_author_id(cls, author_id):
#         blogs = Database.find_one(collection='blogs', query={'author_id': author_id})
#         return [cls(**blog) for blog in blogs]