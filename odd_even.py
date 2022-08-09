from flask import Flask, request
import requests

app=Flask(__name__)
@app.route('/oddeven', methods=['PUT'])


def oddeven():
    # r = requests.get('http://127.0.0.1:5000')
    data_list=request.json['list']
    # list=[]
    # list=data_list

    # list=[10,23,24,35,65,78,90]
    odd=[]
    even=[]
    for i in range (len(data_list)):
        if data_list[i] % 2 !=0:
            # pass
            odd.append(data_list[i])
        else :
            even.append(data_list[i]) 
    return {
        "odd" : odd,
        "even" : even
        }

# print(odd)
# print(even)