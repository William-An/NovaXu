# NovaXu
自动续命机 for [Nova.live](https://nova.live)
## Preparation
1. 克隆这个repo
1. python 安装 [requests HTTP Lib](http://docs.python-requests.org/en/master/)
1. 更名folder里的的`config_demo.py` 为 `config.py`
1. 登陆 Nova 获得cookies_string
1. 设置`expire_in`字段为未来时

## Usage
### Windows
1. 任务计划创建任务
1. follow your heart
1. 添加任务
1. 脚本设置为`python`(python3+)
1. 参数为`novaxu.py`的路径

### Linux
1. `/etc/init`?忘记了

### macOS
1. 穷