from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)

from api.models import *
r = redis.Redis()

q = Queue(connection=r)

