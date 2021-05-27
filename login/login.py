#! coding=utf-8
import requests
from utils import get_host as host


class Login:

    def __init__(self, env, openId, clinicId, grayflag=False):
        self.openId = openId
        self.clinicId = clinicId
        self.grayflag = grayflag
        self.env = env

    def login(self):
        s = requests.session()
        login = {
            "url": f"{host(self.env)}/api/XXXXX",
            "method": "post",
            "json": {
                "mobile": "XXXXX",
                "password": "XXXXX",
                "openId": self.openId
            }
        }

        switch = {
            "url": f"{host(self.env)}/api/XXXX",
            "method": "post",
            "json": {"clinicId": self.clinicId}
        }

        login_code = s.request(**login)
        if login_code.status_code == 200:
            switch_code = s.request(**switch)
            if switch_code.status_code == 200:
                cookie = requests.utils.dict_from_cookiejar(switch_code.cookies)
                isGray = cookie['grayflag']
                if self.grayflag is True:
                    if len(isGray) > 0:
                        return cookie
                    else:
                        return None
                if self.grayflag is False:
                    return cookie
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    login = Login(env='test', openId='111', clinicId='222', grayflag=False)
    print(login.login())

