from app import db
from ..models import News


class Execute_db():

    def get(self):
        news_data = db.session.query(News).all()
        data = []
        for news in news_data:
            dic = {"Title": news.news_title,
                   "Head_line": news.news_head_line,
                   "URL": news.news_url}

            data.append(dic)
        return data

    def delete(self):
        """
        delete if data is in db
        """
        news_data = db.session.query(News).all()
        if news_data:
            db.session.query(News).delete()
            db.session.commit()

    def post(self, news):
        """
        Add latest news data to db

        data: dict, dictionary of news data
        """
        for key in news.keys():
            news_detail = News(
                news_title=key, news_head_line=news[key]["Title"], news_url=news[key]["URL"])
            db.session.add(news_detail)
            db.session.commit()
