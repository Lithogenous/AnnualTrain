from pyecharts import options as opts
from pyecharts.charts import Map, Page
from pyecharts.faker import Collector, Faker

C = Collector()


@C.funcs
def map_without_label() -> Map:
    c = (
        Map()
        .add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-不显示Label"))
    )
    return c




Page().add(*[fn() for fn, _ in C.charts]).render()
