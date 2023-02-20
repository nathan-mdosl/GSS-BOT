import os

#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import time
#from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import simplejson as json
from pathlib import Path
import pandas as pd
import numpy as np
from subprocess import call
from apscheduler.schedulers.background import BackgroundScheduler


root = Path(__file__).parent.resolve()


class main:
    def __init__(self):

        with open("D:\\Nathan\\GSS s3\\records.json", "r") as rf:  # change

            decoded_data = json.load(rf)
            for p in decoded_data["timechanges"]:
                self.Json_Hour = p["Json_Hour"]
                self.Json_Minute = p["Json_Minute"]
                self.Json_Date = p["Json_Date"]

        print(
            "Scheduled to run at:",
            self.Json_Hour,
            ":",
            self.Json_Minute,
            "on",
            self.Json_Date,
        )

        sched = BlockingScheduler(job_defaults={'misfire_grace_time': 15*60},
        )

        sched.add_job(
            self.StartBot,
            "cron",
            day_of_week=self.Json_Date,
            hour=self.Json_Hour,
            minute=self.Json_Minute,
        )
        sched.start()

    def StartBot(self):
        print("Starting Job")
        call(["python", "D:\\Nathan\\GSS s3\\GSS_Report_downloader.py"])  # change


if __name__ == "__main__":
    main()
