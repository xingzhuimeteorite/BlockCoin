
from pyecharts.charts import *
from pyecharts import options as opts
import random




def bar_datazoom_both_way():
    x_data = ["2020/10/{}".format(i + 1) for i in range(30)]

    # 随机生成点数据
    y_data = [random.randint(10, 20) for i in range(len(x_data))]
    bar = Bar(init_opts=opts.InitOpts(theme='light',
                                      width='1000px',
                                      height='600px'))
    bar.add_xaxis(x_data)
    bar.add_yaxis('', y_data)
    # 通过list传入两个datazoom_opts
    bar.set_global_opts(datazoom_opts=[opts.DataZoomOpts(),
                                       opts.DataZoomOpts(type_='inside', range_start=50, range_end=100)])
    return bar


chart = bar_datazoom_both_way()
chart.render('a.html')


# if __name__ == '__main__':
#     print('测试工程局部代码')