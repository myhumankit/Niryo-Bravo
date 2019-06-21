from flask import Flask, render_template, jsonify
from niryo_one_python_api.niryo_one_api import *
import time
import rospy

app = Flask(__name__)
n = NiryoOne()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calibrate.json")
def calibrate():
    print "Info: Calibration"
    try:
        rospy.init_node('niryo_one_example_python_api', disable_signals=True)
        n.calibrate_auto()
        print "Calibration finished !"
        data = {"message":"Calibration"}
        return jsonify(data)

    except NiryoOneException as e:
        print e
        data = {"message":"Calibration", "error":str(e)}
        return jsonify(data)

@app.route("/activate_learning_mode.json")
def activate_learning_mode():
    print "Info: Activate learning mode"
    try:
        n.activate_learning_mode(True)
        print "Activate learning mode"
        data = {"message":"Activate learning mode"}
        return jsonify(data)

    except NiryoOneException as e:
        print e
        data = {"message":"Activate learning mode", "error":str(e)}
        return jsonify(data)

@app.route("/deactivate_learning_mode.json")
def deactivate_learning_mode():
    print "Info: Deactivate learning mode"
    try:
        n.activate_learning_mode(False)
        print "Deactivate learning mode"
        data = {"message":"Deactivate learning mode"}
        return jsonify(data)

    except NiryoOneException as e:
        print e
        data = {"message":"Deactivate learning mode", "error":str(e)}
        return jsonify(data)

@app.route("/goto_rest_position.json")
def goto_rest_position():
    print "Info: Goto rest position"
    try:
        n.activate_learning_mode(False)
        n.move_joints([0,0.64,-1.397,0,0,0])
        n.activate_learning_mode(True)
        print "Goto rest position"
        data = {"message":"Goto rest position"}
        return jsonify(data)

    except NiryoOneException as e:
        print e
        data = {"message":"Goto rest position", "error":str(e)}
        return jsonify(data)
