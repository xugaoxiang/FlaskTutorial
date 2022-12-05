from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():

    # 获取请求的json数据
    req_json = request.get_json()
    print(req_json)

    # 对接收到的数据进行简单处理
    if req_json["operatorID"] != "0001":
        return jsonify({"error": "error."})

    dict_ret = {}
    dict_ret["responseType"] = 2
    dict_ret["status"] = 1000
    dict_ret["num"] = 1
    dict_ret["MD5"] = "4F3D2A1E"

    return jsonify(dict_ret)


if __name__ == '__main__':

    # 启动服务
    app.run(host='0.0.0.0', port=80, debug=True)