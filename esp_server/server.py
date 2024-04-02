from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return "Hello World"

@app.route('/data', methods=['POST'])
def handle_data():
    data = request.get_json()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    magnitude = data['magnitude']
    data_line = f"{timestamp}, {magnitude}\n"
    with open("data.md", "a") as file:
            file.write(data_line)
    return str(200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    