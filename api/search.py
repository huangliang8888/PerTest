#! coding=utf-8
import time
from utils import get_host as host
from utils import get_headers as headers


class Search:

    def __init__(self, env):
        self.env = env

    def search_goods(self, cookies, clinicId, key):
        params = {
            "headers": headers(),
            "cookies": cookies,
            "url": f"{host(self.env)}/api/XXXXX",
            "method": "get",
            "params": {
                "key": key,
                "clinicId": clinicId
            }
        }
        return params

    def search_west(self, cookies, clinicId, key):
        params = {
            "headers": headers(),
            "cookies": cookies,
            "url": f"{host(self.env)}/api/XXXX",
            "method": "get",
            "params": {
                "key": key,
                "clinicId": clinicId
            }
        }
        return params

    def search_chinese_yp(self, cookies, clinicId, key):
        params = {
            "headers": headers(),
            "cookies": cookies,
            "url": f"{host(self.env)}/api/XXXXX",
            "method": "get",
            "params": {
                "key": key,
                "clinicId": clinicId,
                "spec": "中药饮片"
            }
        }
        return params

    def search_chinese_kl(self, cookies, clinicId, key):
        params = {
            "headers": headers(),
            "cookies": cookies,
            "url": f"{host(self.env)}/api/XXXX",
            "method": "get",
            "params": {
                "key": key,
                "clinicId": clinicId,
                "spec": "中药颗粒"
            }
        }
        return params

    def search_treatment(self, cookies, clinicId, key):
        params = {
            "headers": headers(),
            "cookies": cookies,
            "url": f"{host(self.env)}/api/XXXX?{int(time.time() * 1000)}",
            "method": "post",
            "json": {
                "clinicId": clinicId,
                "sex": "男",
                "age": {
                    "year": None,
                    "month": None,
                    "day": None
                },
                "keyword": key
            }
        }
        return params

    def search_all(self, cookies, clinicId, key):
        params = {
            "headers": headers(),
            "cookies": cookies,
            "url": f"{host(self.env)}/api/all",
            "method": "get",
            "params": {
                "key": key,
                "clinicId": clinicId
            }
        }
        return params
