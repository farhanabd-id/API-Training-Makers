import requests, base64
from flask import Flask, request


app = Flask(__name__)

def BasicAuth() :
    pass_str = request.headers.get('Authorization')
    pass_bersih = pass_str.replace('Basic ',"")
    hasil_decode = base64.b64decode(pass_bersih)
    # auth_header = request.headers.get('username')
    hasil_decode_bersih = hasil_decode.decode('utf-8')
    username_aja = hasil_decode_bersih.split(":")[0]
    pass_aja = hasil_decode_bersih.split(":")[1]
    # return pass_bersih
    if username_aja == 'tes' and pass_aja == 'tes123' :
        return True

app = Flask(__name__)

@app.route('/weather', methods=(['GET']))
def hello_world():
    if BasicAuth():
        j = request.headers.get("city")
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={j}&appid=0af7650b00321f8081a8a9ad3a838f51')
        x = r.json()
        # return x
        return {
                'Weather' : x['weather'][0]['main'],
                'Coord' : x['coord'],
                'Temp' : x['main']['temp']
            }
    else :
            return {
                '401' : ':('
            }