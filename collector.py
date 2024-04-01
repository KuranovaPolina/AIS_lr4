import os
import psutil
import json
from datetime import datetime


# from py.critical import critical_params
import py.params as params

import py.send_mail as send_mail

import py.logger as logger

import time

import psycopg2
# import gpustat
# import sensors

from passwords import password_db

critical_params= {
    "CPUTemp": 1, 
    "GPUTemp": 1, 
    "CPULoad": 1, 
    "GPULoad": 1, 
    "RAMLoad": 1
}

def getCPUTemp():
    # tmp = os.popen("powermetrics --samplers smc -n 1 |grep -i 'CPU die temperature'").read()

    # tmp = psutil.sensors_temperatures()
    # print(tmp)

    # tmp = tmp.split(' ')
    # tmp = tmp[3]

    # return float(tmp)
    return 0

def getGPUTemp():
    # tmp = os.popen("sudo powermetrics --samplers smc -n 1 |grep -i 'GPU die temperature'").read()
    # if (not tmp):
    #     tmp = os.popen("sudo powermetrics --samplers smc -n 1 |grep -i 'CPU die temperature'").read()

    # tmp = tmp.split(' ')
    # tmp = tmp[3]

    # return float(tmp)
    return 0

def getCPULoad():
    return psutil.cpu_percent()

def getGPULoad():
    # return gpustat.percent()
    return 0

def getRAMLoad():
    return psutil.virtual_memory().percent

def getData():
    res = {'CPUTemp': 0,
           'GPUTemp': 0,
           'CPULoad': 0,
           'GPULoad': 0,
           'RAMLoad': 0}

    res['CPUTemp'] = getCPUTemp()
    res['GPUTemp'] = getGPUTemp()
    res['CPULoad'] = getCPULoad()
    res['GPULoad'] = getGPULoad()
    res['RAMLoad'] = getRAMLoad()

    return res

def collect():
    try:
        conn = psycopg2.connect(f"dbname='logger' user='polina' host='kuranov.sknt.ru' port='8000' password='{password_db}'")
        print(conn)
    except:
        print("I am unable to connect to the database")
        exit(0)

    while 1:
        datetime_now = datetime.now()
        date_ = datetime_now.strftime("%d/%m/%Y")
        time_ = datetime_now.strftime("%H:%M")
        new_params = getData()

        if new_params['CPUTemp'] >= critical_params['CPUTemp'] or \
            new_params['GPUTemp'] >= critical_params['GPUTemp'] or \
            new_params['CPULoad'] >= critical_params['CPULoad'] or \
            new_params['GPULoad'] >= critical_params['GPULoad'] or \
            new_params['RAMLoad'] >= critical_params['RAMLoad']:

            send_mail.send_mail_main()
            logger.log(datetime_now.strftime("%d/%m/%Y %H:%M"))

        params.last_params = new_params
        # asd = new_params

        print(params.last_params)

        query = f"insert into params values ('{date_}', '{time_}', {new_params['CPUTemp']}, {new_params['GPUTemp']},  {new_params['CPULoad']}, {new_params['GPULoad']}, {new_params['RAMLoad']});"
        
        print(query)

        with conn.cursor() as curs:
            try:
                # simple multi row system query
                curs.execute(query)

                conn.commit()

            # a more robust way of handling errors
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        time.sleep(60)
