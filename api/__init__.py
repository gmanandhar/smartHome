from flask import Flask
import redis
from rq import Queue

app = Flask(__name__)
#Redis Server Connection
r = redis.Redis()
q = Queue(connection=r)
from api.models import *
app.secret_key = "HomeAutomationSystemMDPS"

