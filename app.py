from flask import Flask, render_template

# initialize flask application
app = Flask(__name__)

# sample api endpoint
@app.route('/')
def hello():
    return render_template('index.html')

# @app.route('/2')
# def hello2():
#     return render_template('index2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7878)
