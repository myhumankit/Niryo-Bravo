from flask import Flask, render_template, jsonify, request
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
    message="Info: Calibration"
    print message
    try:
        rospy.init_node('niryo_one_example_python_api', disable_signals=True)
        n.calibrate_auto()
        data = {"message":message}
        print "[ OK ] finished !"
        return jsonify(data)

    except NiryoOneException as e:
        print "[FAIL]"
        print e
        data = {"message":message, "error":str(e)}
        return jsonify(data)

@app.route("/activate_learning_mode.json")
def activate_learning_mode():
    message="Info: Activate learning mode"
    print message
    try:
        n.activate_learning_mode(True)
        data = {"message":message}
        print "[ OK ] finished !"
        return jsonify(data)

    except NiryoOneException as e:
        print "[FAIL]"
        print e
        data = {"message":message, "error":str(e)}
        return jsonify(data)

@app.route("/deactivate_learning_mode.json")
def deactivate_learning_mode():
    message="Info: Deactivate learning mode"
    print message
    try:
        n.activate_learning_mode(False)
        data = {"message":message}
        print "[ OK ] finished !"
        return jsonify(data)

    except NiryoOneException as e:
        print "[FAIL]"
        print e
        data = {"message":message, "error":str(e)}
        return jsonify(data)

@app.route("/goto_zero.json")
def goto_zero():
    message="Info: Goto zero position"
    print message
    try:
        n.activate_learning_mode(False)
        n.move_joints([0,0,0,0,0,0])
        data = {"message":message}
        print "[ OK ] finished !"
        return jsonify(data)

    except NiryoOneException as e:
        print "[FAIL]"
        print e
        data = {"message":message, "error":str(e)}
        return jsonify(data)

@app.route("/goto_rest_position.json")
def goto_rest_position():
    message="Info: Goto rest position"
    print message
    try:
        n.activate_learning_mode(False)
        n.move_joints([0,0.64,-1.397,0,0,0])
        n.activate_learning_mode(True)
        data = {"message":message}
        print "[ OK ] finished !"
        return jsonify(data)

    except NiryoOneException as e:
        print "[FAIL]"
        print e
        data = {"message":message, "error":str(e)}
        return jsonify(data)

@app.route('/move', methods=['GET', 'POST'])
def move():
    joint_1 = request.args.get('j1', type = float)
    joint_2 = request.args.get('j2', type = float)
    joint_3 = request.args.get('j3', type = float)
    joint_4 = request.args.get('j4', type = float)
    joint_5 = request.args.get('j5', type = float)
    joint_6 = request.args.get('j6', type = float)
    message="Info: Move"
    print message
    try:
        n.move_joints([joint_1,joint_2,joint_3,joint_4,joint_5,joint_6])
        data = {"message":message}
        print "[ OK ] finished !"
        return jsonify(data)

    except NiryoOneException as e:
        print "[FAIL]"
        print e
        data = {"message":message, "error":str(e)}
        return jsonify(data)
