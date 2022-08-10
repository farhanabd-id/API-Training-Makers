from flask import Flask, request

app=Flask(__name__)
@app.route('/hurdle-race/<k>', methods=['GET'])

def hurdleRace(k):
    r = request.get_json()
    height= r['height']
    doses = max(height) - int(k)
    for i in height:
        if doses > 0:
            return {
                "min_doses" : str(doses)
            }        

        else :
            return {
                "min_doses" : str(0)
            }
    
#  print(hurdleRace(4,[1,6,3,5,2])) # Sample Input 0
# print(hurdleRace(7,[2,5,4,5,2])) # Sample Input 1