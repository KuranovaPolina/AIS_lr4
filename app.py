from flask import Flask, render_template, send_file, jsonify, request

# import py.critical as critical
import py.params as params
import collector
from collector import collect

import py.interval as interval

import threading
import psycopg2

from datetime import datetime
from datetime import timedelta

# initialize flask application
app = Flask(__name__)

# sample api endpoint
@app.route('/')
def get_page():
    print("page request")
    return render_template('index.html')


@app.route('/index.js', methods=['GET'])
def get_script():
    print("script request")
    return send_file('js/index.js')

@app.route('/stats', methods=['POST'])
def get_stat():
    print("stats request")

    datetimes = []
    CPUTemps = []
    GPUTemps = []
    CPULoads = []
    GPULoads = []
    RAMLoads = []

    start_date = datetime.strptime('2024-04-01 13:50', '%Y-%m-%d %H:%M')
    end_date = datetime.strptime('2024-04-01 15:50', '%Y-%m-%d %H:%M')

    inter = interval.interval_generator(start_date, end_date, 0)

    try:
        conn = psycopg2.connect("dbname='logger' user='polina' host='kuranov.sknt.ru' port='8000' password='****'")
        # print(conn)
    except:
        print("I am unable to connect to the database")
        exit(0)

    with conn.cursor() as curs:
        try:
            # simple multi row system query
            for value in inter:
                # print(value)
                query = f"select * from params where params.date_ = '{value[0]}' and params.time_ = '{value[1]}';"
                # print(query)
                curs.execute(query)

                records = (curs.fetchmany(1))

                # print(records)

                datetimes.append(value[0] + " " + value[1])

                if records == []:
                    CPUTemps.append(0)
                    GPUTemps.append(0)
                    CPULoads.append(0)
                    GPULoads.append(0)
                    RAMLoads.append(0)
                else:
                    CPUTemps.append(records[0][2])
                    GPUTemps.append(records[0][3])
                    CPULoads.append(records[0][4])
                    GPULoads.append(records[0][5])
                    RAMLoads.append(records[0][6])

        # a more robust way of handling errors
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # print(datetimes)

    return jsonify(CPUTemp= params.last_params["CPUTemp"], 
                   GPUTemp= params.last_params["GPUTemp"], 
                   CPULoad= params.last_params["CPULoad"], 
                   GPULoad= params.last_params["GPULoad"], 
                   RAMLoad= params.last_params["RAMLoad"],
                   CPUTemp_critical= collector.critical_params["CPUTemp"], 
                   GPUTemp_critical= collector.critical_params["GPUTemp"], 
                   CPULoad_critical= collector.critical_params["CPULoad"], 
                   GPULoad_critical= collector.critical_params["GPULoad"], 
                   RAMLoad_critical= collector.critical_params["RAMLoad"], 
                   datetimes = datetimes,
                   CPUTemps = CPUTemps,
                   GPUTemps = GPUTemps,  
                   CPULoads = CPULoads,
                   GPULoads = GPULoads,
                   RAMLoads = RAMLoads
                   )

@app.route('/updateGraph', methods=['POST'])
def updateGraph():
    print("stats request")

    datetimes = []
    CPUTemps = []
    GPUTemps = []
    CPULoads = []
    GPULoads = []
    RAMLoads = []

    start_date = datetime.strptime('2024-04-01 13:50', '%Y-%m-%d %H:%M')
    end_date = datetime.strptime('2024-04-01 15:50', '%Y-%m-%d %H:%M')

    print(request.json['freq'])

    inter = interval.interval_generator(start_date, end_date, request.json['freq'])

    try:
        conn = psycopg2.connect("dbname='logger' user='polina' host='kuranov.sknt.ru' port='8000' password='****'")
        # print(conn)
    except:
        print("I am unable to connect to the database")
        exit(0)

    with conn.cursor() as curs:
        try:
            # simple multi row system query
            for value in inter:
                # print(value)
                query = f"select * from params where params.date_ = '{value[0]}' and params.time_ = '{value[1]}';"
                # print(query)
                curs.execute(query)

                records = (curs.fetchmany(1))

                # print(records)

                datetimes.append(value[0] + " " + value[1])

                if records == []:
                    CPUTemps.append(0)
                    GPUTemps.append(0)
                    CPULoads.append(0)
                    GPULoads.append(0)
                    RAMLoads.append(0)
                else:
                    CPUTemps.append(records[0][2])
                    GPUTemps.append(records[0][3])
                    CPULoads.append(records[0][4])
                    GPULoads.append(records[0][5])
                    RAMLoads.append(records[0][6])

        # a more robust way of handling errors
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    # print(datetimes)

    return jsonify( datetimes = datetimes,
                   CPUTemps = CPUTemps,
                   GPUTemps = GPUTemps,  
                   CPULoads = CPULoads,
                   GPULoads = GPULoads,
                   RAMLoads = RAMLoads
                   )

@app.route('/updateCritical', methods=['POST'])
def updateCritical():
    print("updateCritical request")

    collector.critical_params = request.json

    print(collector.critical_params)

    return ""


def run_server():
    app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    thread1 = threading.Thread(target=run_server, name="Thread-1")
    thread2 = threading.Thread(target=collect, name="Thread-2") 
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
