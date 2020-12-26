from flask import Flask, render_template
from data import bar

app = Flask(__name__, template_folder="../templates",static_folder ="../static" )


# 第二部分：路由配置
# 01. 页面数据请求服务
# 首页渲染
@app.route("/")
def index():
    return render_template("dev/index.html")


# 节点图谱
@app.route("/bar")
def index_bar():
    return render_template("chart_py/bar.html")

# 节点图谱
@app.route("/barChart")
def get_graph():
    c = bar.get_bar_data()
    print(c)
    return c.dump_options_with_quotes()

# 403错误
@app.errorhandler(403)
def miss(e):
    return render_template('error/error-403.html'), 404


# 404错误
@app.errorhandler(404)
def error(e):
    return render_template('error/error-404.html'), 500


# 500错误
@app.errorhandler(500)
def error(e):
    return render_template('error/error-500.html'), 500


# 主函数
if __name__ == "__main__":
    # 模板更改后立即生效
    app.jinja_env.auto_reload = True
    # 代码更改后立即生效
    app.run(debug = True)
    # 1.0以后 debug = true不再支持