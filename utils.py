#! coding=utf-8
import yaml
import datetime, time, arrow
from dateutil.relativedelta import relativedelta
import random


def get_host(env):
    domain = {
        "test": "https://test.abczs.cn",
        "pre": "https://abcyun.cn",
        "gray": "https://abcyun.cn",
        "prod": "https://abcyun.cn"
    }
    return domain[env]


def get_headers():
    headers = {
        "API-TEST": '123',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    return headers


def get_login_list(env):
    return yaml.safe_load(open(f"config/users_{env}.yml", encoding='utf-8'))


def get_keys():
    return yaml.safe_load(open(f"config/keys.yml", encoding='utf-8'))


def write_config(path):
    """将openID  clinicId excel文件 写入yml中"""
    try:
        import xlrd
        workBook = xlrd.open_workbook(path)
    except FileNotFoundError:
        return {"error": "没有找到文件", "path": path}
    login_list = []
    worksheet = workBook.sheet_by_name('result')
    for row in range(worksheet.nrows):
        users = {}
        row_value = worksheet.row_values(row)
        # 取excel的第一行
        users['clinicId'] = row_value[0]
        # 取excel 第二行
        users['clinic_name'] = row_value[1]
        # 取excel 第五行
        users['openId'] = row_value[4]
        login_list.append(users)

    from ruamel import yaml

    with open("config/users_gray.yml", "w", encoding="utf-8") as f:
        yaml.dump(login_list, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)


def cur_time():
    return str(time.strftime("%Y-%m-%d", time.localtime()))


def round_time():
    """总体时间周期"""
    return str(datetime.date.today() + relativedelta(days=-random.randint(1, 180)))


def interval_period(appoint_time, interval=7):
    """在指定的日期往前推N天"""
    return str(datetime.datetime.strptime(appoint_time, '%Y-%m-%d').date() + relativedelta(days=-interval))




if __name__ == '__main__':
    # print(get_login_list('test'))
    # print(write_config(r"C:\Users\YD\Documents\WXWork\1688850995605461\Cache\File\2021-05\连锁门店-gray.xlsx"))
    print(interval_period("2021-05-10"))