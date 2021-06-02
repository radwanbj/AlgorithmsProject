from flask import Flask, render_template, url_for, request, jsonify
import coordinates
from os import getenv

customer = {1: {'origin': '3.3615395462207878,101.56318183511695', 'destination': '3.1000170516638885,101.53071480907951'}, 2: {'origin': '3.049398375759954,101.58546611160301',
                                                                                                                                'destination': '3.227994355250716,101.42730357605375'}, 3: {'origin': '3.141855957281073,101.76158583424586', 'destination': '2.9188704151716256,101.65251821655471'}}

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def root():
    if request.method == 'POST':
        print(request.form)
        distance = bool(request.form['distance'])
        sentiment = bool(request.form['sentiment'])
        customerNumber = int(request.form['customer'])

        distanceList, bestCourier = coordinates.get_best_distance(
            customer[customerNumber]['origin'], customer[customerNumber]['destination'])

        return jsonify({'data': distanceList, 'coor': customer[customerNumber], 'bestCourier': bestCourier})

    else:
        return render_template("index.html", akey=getenv('API_KEY'))


if __name__ == "__main__":
    app.run(debug=True)
