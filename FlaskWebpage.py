"""This is a simple webpage that is hosted by the 
raspberry pi. This allows me to connect my computer
to the webpage and set the power level on my Laser 
Engraver instead of having to press the manual buttons
"""
from flask import Flask, render_template, request
from RaspberryPI_IO import RPIO as my_pi

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def start():

    if request.method == "POST":
        my_pi().set_value(float(request.form["Power_value"]))

    return  """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Set Power Level</title>
                </head>
                <body>
                    <h1>SET POWER LEVEL</h1>
                    <form method="POST">
                        Desired Power Value: <br>
                        <input type="text" name="Power_value">
                        <input type="submit",text="Set Power Level">
                    </form>
                </body>
                </html>
            """

# Start the webpage and set it to 192.168.0.252:8000
# this is the address of the RPI on my local network
app.run(debug=True,host='192.168.0.252')