from flask import Blueprint, jsonify
from ..utils.execute_db import Execute_db
from ..contants import NEWS_URL
import requests
from bs4 import BeautifulSoup

view_blueprint = Blueprint("view_blueprint", __name__)


@view_blueprint.route('/news', methods=["GET"])
def read_news_data():
    """
    Read newest news data from db

    return: json, news data
    """
    execute_db = Execute_db()
    data = execute_db.get()

    return jsonify({
        "data": data,
        "status": 200
    })
