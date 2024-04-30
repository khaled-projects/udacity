import logging
import os

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from flask import jsonify
from sqlalchemy import and_, text
from random import randint

from config import app, db


port_number = int(os.environ.get("APP_PORT", 5153))


@app.route("/health_check")
def health_check():
    return "ok"
