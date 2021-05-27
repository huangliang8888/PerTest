#! coding=utf-8

from login.login import Login
from api.search import Search
from utils import get_login_list, get_keys
import random


class CreateDataSearch:

    def __init__(self, env, grayflag=False):
        self.env = env
        self.grayflag = grayflag

    def search_list(self):
        """随机选择搜索接口的列表, 如果要去掉某个接口，删除这里即可"""

        s_list = [
            Search(self.env).search_goods,
            Search(self.env).search_west,
            Search(self.env).search_chinese_yp,
            Search(self.env).search_chinese_kl,
            Search(self.env).search_treatment,
            Search(self.env).search_all
        ]
        return s_list

    def create_data(self, clinic_count, req_count):
        """生成数据"""

        all_users = self._all_user()
        req_list = []

        if clinic_count is not None and self.grayflag is False:
            all_users = random.sample(all_users, clinic_count)  # 选择门店的数量
        user_count = 0
        for users in all_users:
            cookie = Login(env=self.env, openId=users['openId'], clinicId=users['clinicId'], grayflag=self.grayflag).login()
            if cookie is not None:
                clinic_req = []
                n = 0
                user_count += 1
                if clinic_count >= user_count:
                    while True:
                        if n < req_count:
                            for api in random.sample(self.search_list(), 1):
                                clinic_req.append(
                                    api(cookies=cookie, key=random.sample(self._get_keys(), 1)[0], clinicId=users['clinicId']))
                        else:
                            break
                        n += 1
                    req_list.append(clinic_req)
                else:
                    break
            else:
                pass
        return req_list

    # 私有方法
    def _all_user(self):
        return get_login_list(self.env)

    def _get_keys(self):
        return get_keys()


if __name__ == '__main__':
    data = CreateDataSearch(env='test').create_data(clinic_count=2, req_count=5)

