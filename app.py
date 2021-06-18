from flask import Flask, render_template, url_for, request, jsonify
import coordinates
from os import getenv
from analysis import Analysis
customer = {1: {'origin': '3.3615395462207878,101.56318183511695', 'destination': '3.1000170516638885,101.53071480907951'}, 2: {'origin': '3.049398375759954,101.58546611160301',
                                                                                                                                'destination': '3.227994355250716,101.42730357605375'}, 3: {'origin': '3.141855957281073,101.76158583424586', 'destination': '2.9188704151716256,101.65251821655471'}}

app = Flask(__name__)

# analysis = Analysis(debug=True)
# sentiment_data = analysis.run_analysis()
sentiment_data = {'citylink': 0.09074733096085409, 'poslaju': 0.09577632361689471,
                  'dhl': 0.5228696530818457, 'jnt': 0.10873915943962642, 'gdex': 0.01}


@app.route("/", methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        print(request.form)
        distance = bool(request.form['distance'])
        sentiment = (request.form['sentiment']) == 'true'
        customerNumber = int(request.form['customer'])

        print(sentiment, "  ", request.form['sentiment'])
        if sentiment:
            distanceList, bestCourier = coordinates.get_best_distance(
                customer[customerNumber]['origin'], customer[customerNumber]['destination'])
            print(distanceList)
            print(bestCourier)
            distanceList = [list(
                x) + [sentiment_data[x[0]], (1 + sentiment_data[x[0]]) * x[1]] for x in distanceList]
            distanceList = sorted(distanceList, key=lambda x: x[3])
            bestCourier = coordinates.courier[distanceList[0][0]]
            return jsonify({'data': distanceList, 'coor': customer[customerNumber], 'bestCourier': bestCourier})
            #print("Updated: ", distanceList)
        else:
            distanceList, bestCourier = coordinates.get_best_distance(
                customer[customerNumber]['origin'], customer[customerNumber]['destination'])
            return jsonify({'data': distanceList, 'coor': customer[customerNumber], 'bestCourier': bestCourier})

    else:
        return render_template("index.html", akey=getenv('API_KEY'))


@app.route("/plot.html", methods=['POST', 'GET'])
def plot():
    if request.method == 'GET':
        return render_template("plot.html")


@app.route("/courier/<path:path>", methods=['POST', 'GET'])
def courier(path):
    if request.method == 'GET':
        return render_template("/courier/" + path)


if __name__ == "__main__":
    app.run(debug=True)
