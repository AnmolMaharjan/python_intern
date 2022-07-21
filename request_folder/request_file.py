
from datetime import datetime, timedelta, timezone, tzinfo
from email.utils import localtime
import json
import requests
import base64
from zoneinfo import ZoneInfo
import pytz


class Token:

    def exp_date(self):
        access_bytes_2 = self.access_token_2.encode('UTF-8')
        message_bytes_2 = base64.b64decode(access_bytes_2)
        a = message_bytes_2.decode()
        x = json.loads(a)
        expire_token = x['exp']

        datetime_1 = datetime(
            year=1970,
            month=1,
            day=1,
            hour=5,
            minute=45
        )

        datetime_2 = timedelta(seconds=expire_token)

        datetime_12 = datetime_1+datetime_2

        print('WAH')

        # dt_us_central = datetime.now(pytz.timezone('US/Central'))
        # datetime_3 = datetime.now(pytz.timezone('Africa/Conakry'))

        tz1 = pytz.timezone('Africa/Conakry')
        tz2 = pytz.timezone('Asia/Kathmandu')
        # dt = datetime.strptime(datetime_12,"%Y-%m-%d %H:%M:%S")
        dt = tz1.localize(datetime_12)
        dt = dt.astimezone(tz2)
        # dt = dt.strftime("%Y-%m-%d %H:%M:%S")

        datetime_exp = datetime_12 - datetime.now()

        # print(f"Time Expire Remaining: {datetime_exp}")
        print(f"Time Expire Remaining: {datetime_exp}")

class RequestPy:

    def __init__(self):
        self.base_url = 'http://172.16.10.26:8001'
        self.my_dict = {}
        self.logged_in = False

    def user_logged_in(self):
        url = f"{self.base_url}/api/user/login/"

        data = {
          "email": "admin@ewebsign.com",
          "password": "admin123`$"
        }

        response_post = requests.post(url, json = data)
        self.my_str = json.dumps(response_post.json(), indent=4)
        self.my_dict = json.loads(self.my_str)

        self.access_token = self.my_dict['access']
        self.access_token_2 = self.my_dict['access'].split('.')[1]+'==='
        self.refresh_token = self.my_dict['refresh']
        self.refresh_token_2 = self.my_dict['refresh'].split('.')[1]+'==='

        with open('file_2.json', 'r+') as f1:
            v1 = json.dumps({'Access': self.access_token, 'Refresh': self.refresh_token})
            f1.write(v1)

        self.logged_in = True

    def list_jobs(self):
        url = f"{self.base_url}/api/jobs/hrog/"

        res = requests.get(url, headers={'Authorization': f'Bearer {self.access_token}'})

        with open('file_1.json', 'r+',encoding='UTF-8') as file:
            values_a = json.dumps(res.json(), indent=4, ensure_ascii=False)
            file.write(values_a)

obj = RequestPy()
obj.user_logged_in()
obj.list_jobs()

t = Token()
t.exp_date()
