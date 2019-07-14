from flask import Flask, render_template, request, redirect, jsonify, Response
import sqlite3
import json

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

conn = sqlite3.connect('collection.db')

@app.route("/", methods=['GET'])
def index():

    return render_template("index.html")

@app.route("/add-asset", methods=['POST'])
def add_asset():

    if request.method == "POST":

        try:
            asset = request.form['asset']
            description = request.form['description']

            cursor = conn.cursor()
            ret_val = cursor.execute("INSERT INTO asset(name, description) VALUES('%s', '%s')" % (asset, description))
            conn.commit()

            if(not ret_val):
                return jsonify({"status": "DB Error"})

            return jsonify({"status": "Successfully Added"})
        except:
            return jsonify({"status": "Failed"})

@app.route("/add-task", methods=['POST'])
def add_task():

    if request.method == "POST":

        try:
            task = request.form['task']
            description = request.form['description']

            cursor = conn.cursor()
            ret_val = cursor.execute("INSERT INTO task(name, description) VALUES('%s', '%s')" % (task, description))
            conn.commit()

            if(not ret_val):
                return jsonify({"status": "DB Error"})

            return jsonify({"status": "Successfully Added"})
        except:
            return jsonify({"status": "Failed"})

@app.route("/add-worker", methods=['POST'])
def add_worker():

    if request.method == "POST":

        try:
            worker = request.form['worker']
            age = int(request.form['age'])
            phone = request.form['phone']

            err = ""

            if(age < 0 or age > 120):
                err += "Age out of range-"

            if(len(phone) != 10):
                err += "Incorrect phone number-"

            if(len(err) > 0):
                return jsonify({"status": err})

            cursor = conn.cursor()
            ret_val = cursor.execute("INSERT INTO worker(name, age, phone) VALUES('%s', '%s', '%s')" % (worker, age, phone))
            conn.commit()

            if(not ret_val):
                return jsonify({"status": "DB Error"})

            return jsonify({"status": "Successfully Added"})
        except:
            return jsonify({"status": "Failed"})

@app.route("/assets/all", methods=['GET'])
def all_assets():

    if request.method == "GET":

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM asset")

        data = cursor.fetchall()

        js = []

        for row in data:
            js.append({"id": row[0], "name": row[1], "description": row[2]})

        return Response(json.dumps(js),  mimetype='application/json')

@app.route("/allocate-task/", methods=['POST'])
def allocate_task():

    if request.method == "POST":

        try:
            assetId = request.form['assetId']
            taskId = request.form['taskId']
            workerId = request.form['workerId']
            timeOfAllocation = request.form['timeOfAllocation']
            taskToBePerformedBy = request.form['taskToBePerformedBy']

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM asset WHERE id=%d" % int(assetId))
            data = cursor.fetchall()

            err = ""

            if(len(data) == 0):
                err += "Asset not found-"

            cursor.execute("SELECT * FROM task WHERE id=%d" % int(taskId))
            data = cursor.fetchall()

            if(len(data) == 0):
                err += "Task not found-"

            cursor.execute("SELECT * FROM worker WHERE id=%d" % int(workerId))
            data = cursor.fetchall()

            if(len(data) == 0):
                err += "Worker not found-"

            if(len(err) > 0):
                return jsonify({"status": err})

            ret_val = cursor.execute("INSERT INTO allocatetask(aid, tid, wid, toa, etc) VALUES('%s', '%s', '%s', '%s', '%s')"
            % (assetId, taskId, workerId, timeOfAllocation, taskToBePerformedBy))
            conn.commit()

            if(not ret_val):
                return jsonify({"status": "DB Error"})

            return jsonify({"status": "Successfully Added"})
        except:
            return jsonify({"status": "Failed"})

@app.route("/get-tasks-for-worker/<workerId>", methods=['GET'])
def get_task(workerId):

    if request.method == "GET":

        wid = workerId

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM allocatetask WHERE wid=%d" % int(wid))
        data = cursor.fetchall() 

        js = []

        for row in data:
            cursor.execute("SELECT name, description FROM task WHERE id=%d" % row[1])
            task = cursor.fetchall()
            print(row)
            js.append({"assetId": row[1], "taskId": row[2], "task": task[0][0], "taskDescription": task[0][1], "workerId": row[3], "timeOfAllocation": row[4], "taskToBePerformedBy": row[5]})

        return Response(json.dumps(js),  mimetype='application/json')
