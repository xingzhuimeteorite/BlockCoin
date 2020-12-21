from flask import Flask, render_template
from  demo_pyecharts_data import *

app = Flask(__name__, template_folder="../templates/demo")


# 第二部分：路由配置
# 01. 页面数据请求服务
# 首页渲染
@app.route("/")
def index():
    return render_template("demo_pyecharts.html")
@app.route("/bar")
def get_graph():
    c = get_pyacharts_graph()
    return c.dump_options_with_quotes()


# 403错误
@app.errorhandler(403)
def miss(e):
    return render_template('error-403.html'), 404


# 404错误
@app.errorhandler(404)
def error(e):
    return render_template('error-404.html'), 500


# 500错误
@app.errorhandler(500)
def error(e):
    return render_template('error-500.html'), 500


# 主函数
if __name__ == "__main__":
    # 模板更改后立即生效
    app.jinja_env.auto_reload = True
    # 代码更改后立即生效
    app.run()
    # 1.0以后 debug = true不再支持