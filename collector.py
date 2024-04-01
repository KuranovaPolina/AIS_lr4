import os
import psutil
import json
from datetime import datetime

# from py.critical import critical_params
import py.params as params
import time
# import gpustat
# import sensors

critical_params= {
    "CPUTemp": 90, 
    "GPUTemp": 90, 
    "CPULoad": 85, 
    "GPULoad": 85, 
    "RAMLoad": 0
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
    while 1:
        new_params = getData()
        new_data = {
            # 'datetime': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            # 'data': getData()

            datetime.now().strftime("%d/%m/%Y %H:%M"): new_params
        }

        if new_params['CPUTemp'] >= critical_params['CPUTemp'] or \
            new_params['GPUTemp'] >= critical_params['GPUTemp'] or \
            new_params['CPULoad'] >= critical_params['CPULoad'] or \
            new_params['GPULoad'] >= critical_params['GPULoad'] or \
            new_params['RAMLoad'] >= critical_params['RAMLoad']:
            print("SOMETHING WRONG")
            print(new_params)
            print(critical_params)

        params.last_params = new_params
        # asd = new_params

        print(params.last_params)

        time.sleep(60)

# collect()
# with open('data.json', 'a+') as file:
#     file.write(json.dumps(new_data))
#     file.write(',')
#     file.write('\n')
#     # print(new_data)
#     # # # file.seek(0, 2)
#     # json.dump(new_data, file)
#     # json.dump(new_data, file)

