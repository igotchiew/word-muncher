from flask import Flask
from config import Config
from textblob import TextBlob
from pymongo import MongoClient
from app.models import User

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL="amqp://")

celery = Config.make_Celery(app)


@celery.task()
def tags(message):
    blob = TextBlob(message)
    result = build_entry(blob, User, message)
    client = MongoClient()
    db = client.my_database
    results = db.my_database
    result_id = results.insert_one(result).inserted_id
    print(result_id)