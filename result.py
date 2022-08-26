

import requests
import subprocess
from base64 import b64encode
from pyDes import des, ECB, PAD_PKCS5

NCCU_URL = "https://es.nccu.edu.tw/"

def des_ecb_encode(source, key):
    des_obj = des("........", ECB, IV=None, pad=None, padmode=PAD_PKCS5)
    des_obj.setKey(key)
    des_result = des_obj.encrypt(source)
    return b64encode(des_result).decode()

def get_login_url(username, password):
    source = "aNgu1ar%!" + username + "X_X" + password + "!%ASjjLInGH:lkjhdsa:)_l0OK"
    return NCCU_URL + "person/" + str(des_ecb_encode(source, "angu1arjjlST@2019")) + "/"

def get_track_url(encstu):
    return NCCU_URL + "tracing/" + "zh-TW/" + encstu + "/"

try:
    usr = input("帳號: ")
    pwd = input("密碼: ")
    subprocess.run(["clear"])

    login_url = get_login_url(usr, pwd)
    login_info = requests.get(login_url)
    stu = login_info.json()[0]
    tracking_url = get_track_url(stu['encstu'])
    tracking_info = requests.get(tracking_url)
    tracking_list = tracking_info.json()

    maxlen = 0
    for sbj in tracking_list:
        maxlen = max(maxlen, len(sbj['subNam']))

    # basic info
    print("學生資料")
    print("系級： {}".format(stu['gdeNam_C']))
    print("學號： {}".format(stu['stuNum']))
    print("姓名： {}".format(stu['stuNam_C']))
    print()

    # title
    print("課堂名稱", end="")
    for _ in range(len("課堂名稱"), maxlen + 1):
        print('　', end="")
    print("狀態")
    for _ in range(maxlen):
        print("———", end="")
    print()

    # contents
    for sbj in tracking_list:
        if sbj['subSelInfo'] != "":
            print(sbj['subNam'], end="")
            for _ in range(len(sbj['subNam']), maxlen + 1):
                print('　', end="")
            print(sbj['subSelInfo'])
except:
    subprocess.run(["clear"])
    print("學號或密碼輸入錯誤 Orz \n")
    print("(\_/)\n( •_•)\n/> ♥️ >")