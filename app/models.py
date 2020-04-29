from app import db


class News(db.Model):

    """
    Class for define structure of news db
    """

    __tablename__ = 'news'

    _id = db.Column("_id", db.Integer, primary_key=True)
    news_title = db.Column("news_title", db.String(10))
    news_head_line = db.Column("news_head_line", db.String(100))
    news_url = db.Column("news_url", db.Text)

    def __repr__(self):
        return f"News('{self.news_title}', '{self.news_head_line}', '{self.news_url}')"
