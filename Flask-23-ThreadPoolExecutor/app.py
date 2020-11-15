from flask import Flask
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(2)

app = Flask(__name__)


@app.route('/tasks')
def run_background_tasks():
    # 提交2个任务，一个带参、一个不带参
    executor.submit(background_task1)
    executor.submit(background_task2, 'hello', 'future')
    return 'tasks started in background!'


def background_task1():
    print("background_task1 started!")
    time.sleep(10)
    print("background_task1 done!")


def background_task2(arg1, arg2):
    print(f"background_task2 started with args: {arg1} {arg2}!")
    time.sleep(5)
    print("background_task2 done!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)