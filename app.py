from flask import Flask, render_template, request, url_for, flash, redirect, abort
from ping import *
from RenderGraph import *
from symbols import *


app = Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'your secret key'


@app.route('/', methods = ["GET", "POST"])
def stock():
    

    symbols = getSymbols()
    # count = 0
    # for symbol in symbols:
    #     count += 1
    
    # print(count)

    if request.method == "POST":
        symbol = request.form['symbol']
        timeSeries = request.form['timeSeries']
        chartType = request.form['chartType']
        startDateStr = request.form['startDate']
        endDateStr = request.form['endDate']
        # if(startDateStr == ""):
        #     flash("Start Date is required!")
        # elif(endDateStr == ""):
        #     flash("End Date required!")

        try:
            startDate = datetime.strptime(startDateStr, "%Y-%m-%d")
        except:
            flash("Start Date Required!")
            return render_template("stock.html", symbols = symbols)

        try:
            endDate = datetime.strptime(endDateStr, "%Y-%m-%d")
        except:
            flash("End Date required!")
            return render_template("stock.html", symbols = symbols)

        if(symbol == ""):
            flash("Symbol is required!")
        elif(timeSeries == ""):
            flash("Time Series is Required!")
        elif(chartType == ""):
            flash("Chart Type is Required!")
        elif(endDate < startDate):
            flash("End Date must be after start date!")
        else:
            #data = pingAPI(timeSeries, symbol, "2023-03-01", "2023-03-31")
            data = pingAPI(timeSeries, symbol, startDateStr, endDateStr)
            chart = render_graph(chartType, startDateStr, endDateStr, data, symbol)
            return render_template("stock.html", chart = chart, symbols = symbols)
            


    return render_template("stock.html", symbols = symbols)


app.run()