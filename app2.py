from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# ルートURLへのGETリクエストに応答

@app.route('/')
def hello_get():
    return render_template('sample.html')

@app.route('/result', methods=['GET'])
def get_request():
    data = request.args.get("data", "")
    return render_template('result.html', message = "Data: {}".format(data))

@app.route('/result', methods=['POST'])
def post_request():
    data = request.form["data"]
    return render_template('result.html', message = "Data: {}".format(data))

if __name__=='__main__':
    app.run()