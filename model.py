from app import db


class News(db.Model):

    """
    Class for define structure of news db
    """

    __tablename__ = 'news'

    _id = db.Column("id", db.Integer, primary_key=True)
    news_title = db.Column("news title", db.String(10))
    news_head_line = db.Column("head_line", db.String(100))
    news_url = db.column("url", db.Text)

    def __init__(self, news_title, news_head_line, news_url):
        self.news_title = news_title
        self.news_head_line = news_head_line
        self.news_url = news_url

    def get_news_data(self):
        """
        null check

        return: bool
        """

        news_data = db.session.query(News).all()

        if news_data:
            return news_data
        return []

    def delete_news_data(self, data):
        """
        delete if data is in db
        """
        db.session.delete(data)
        db.session.commit()

    def register_news_data(self, data):
        """
        Add latest news data to db

        data: dict, dictionary of news data
        """
