from flask import Flask, render_template, send_file, jsonify, request

# import py.critical as critical
import py.params as params
import collector
from collector import collect

import threading

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

    print(params.last_params)

    return jsonify(CPUTemp= params.last_params["CPUTemp"], 
                   GPUTemp= params.last_params["GPUTemp"], 
                   CPULoad= params.last_params["CPULoad"], 
                   GPULoad= params.last_params["GPULoad"], 
                   RAMLoad= params.last_params["RAMLoad"],
                   CPUTemp_critical= collector.critical_params["CPUTemp"], 
                   GPUTemp_critical= collector.critical_params["GPUTemp"], 
                   CPULoad_critical= collector.critical_params["CPULoad"], 
                   GPULoad_critical= collector.critical_params["GPULoad"], 
                   RAMLoad_critical= collector.critical_params["RAMLoad"])

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
