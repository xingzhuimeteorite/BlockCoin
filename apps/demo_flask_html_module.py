from flask import Flask, render_template
import templates.demo
app = Flask(__name__,template_folder="../templates/demo")
@app.route('/')
def index():
    # 变量
    my_str = '我是字符串变量'
    my_int = 8888
    return render_template('demo.html',
                            my_str=my_str,
                            my_int=my_int
                            )
if __name__ == '__main__':
    app.run(debug=True)