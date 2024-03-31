from flask import Flask, render_template, send_file, jsonify

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
    # return render_template('index.html')
    return jsonify(CPUTemp= 123, GPUTemp= 123, CPULoad= 666, GPULoad= 777, RAMLoad= 333)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
