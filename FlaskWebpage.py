from flask import Flask, render_template, request
from RaspberryPI_IO import RPIO as my_pi

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def start():

    if request.method == "POST":
        num = 0.0
        num = float(request.form["Power_value"])
        my_pi().set_value(num)

    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Power Level</title>
</head>
<body>
    <h1>SET POWER LEVEL</h1>
        Desired Power Value: <br>
        <input type="text" name="Power_value">
        <input type="submit",text="Set Power Level">
    </form>
</body>
</html>
    """


app.run(debug=True,host='192.168.0.252')