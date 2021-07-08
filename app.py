"""
 * @Author: Nuanxinqing
 * @Email：nuanxinqing@gmail.com
 * @File:  app.py
 * @Date: 2021/7/6 16:27
"""

from flask import Flask
import srun_login

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = srun_login.Start()
    print(result)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5999, host='192.168.31.224')