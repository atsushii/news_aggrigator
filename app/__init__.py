from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()


def do():
    scrape = Scrape()
    data = scrape.scrape_news()
    execute_db = Execute_db()
    execute_db.delete()
    execute_db.post(data)
    print("complete")


def start_batch():
    scheduler = BackgroundScheduler(demon=True)
    scheduler.add_job(do, 'interval', minutes=1)
    scheduler.start()
    print("start")


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from .views.views import view_blueprint
    app.register_blueprint(view_blueprint)

    from app.models import db
    from app.utils.execute_db import db

    db.init_app(app)
    Migrate(app, db)
    from app.utils.scrape import Scrape
    from app.utils.execute_db import Execute_db

    return app, Execute_db, Scrape


app, Execute_db, Scrape = create_app()

app.app_context().push()


start_batch()
