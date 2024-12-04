##### matplotlib.后端管理
```python
matplotlib.get_backend()
# 查看当前后端
# pycharm 使用 'module://backend_interagg' 交互式后端

matplotlib.use(backend)
# matplotlib.use('QtAgg')
# 选择用于渲染和 GUI 集成的后端
# 在创建任何图形之前调用
# 交互式后端：GTK3Agg、GTK3Cairo、GTK4Agg、GTK4Cairo、MacOSX、nbAgg、QtAgg、QtCairo、TkAgg、TkCairo、WebAgg、WX、WXAgg、WXCairo、Qt5Agg、Qt5Cairo。
# 非交互式后端：agg、cairo、pdf、pgf、ps、svg
```

