from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)

from api.models import *

r = redis.Redis()
app.secret_key = "HomeAutomationSystemMDPS"


q = Queue(connection=r)

