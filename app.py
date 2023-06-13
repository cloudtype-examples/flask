import requests
import json
from flask import Flask, request, jsonify
from werkzeug.serving import WSGIRequestHandler


app = Flask (__name__)


@app.route('/order')
def get_data():
    data = [{
        "ORDER_ID": "20230611979998990001",
        "STATE_CODE": "3",
        "ADDR_MAIN_R": "서울시 강동구",
        "ADDR_ETC_R": "도쿄타워",
        "ETC_INFO_R": "자유여신상 앞",
        "X": "37.515298",
        "Y": "127.059464",
        "RECEIVER_TEL": "01033976817"
    },
    {
        "ORDER_ID": "20230611979998990002",
        "STATE_CODE": "4",
        "ADDR_MAIN_R": "경기도 용인시",
        "ADDR_ETC_R": "성복구",
        "ETC_INFO_R": "만리장성 뒤",
        "X": "37.515298",
        "Y": "127.059464",
        "RECEIVER_TEL": "01041161705"
    }]

    return json.dumps(data, ensure_ascii=False, indent="\t") #jsonify(data)

if __name__ == "__main__":
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host="0.0.0.0", port=5000, debug=True)
