from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'  
    
@app.route('/baidu')
def baidu():
    url = 'www.baidu.com'
    return '<h1>{}</h1>'.format(url)
    
if __name__ == '__main__':
    app.run(debug=True)