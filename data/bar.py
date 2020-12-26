
from pyecharts.charts import Bar

def get_bar_data():
    x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
    y_data = [123, 153, 89, 107, 98, 23]

    bar = (Bar()
           .add_xaxis(x_data)
           .add_yaxis('', y_data)
          )
    return bar
    # bar.render('a.html')


if __name__ == '__main__':
        a = get_bar_data()