from flask import Flask, jsonify, request

app = Flask(__name__)

#creating an array of tasks with each task taken as a different object in it
tasks = [
    {
        "id": 1, 
        "title": "Buying Groceries",
        "description": "milk, cheese, fruits, vegetables",
        "done": False
    },
    {
        "id": 2,
        "title": "Finish homework",
        "description": "math, english, science",
        "done": False
    }
]

@app.route("/add-data", methods= ["POST"])

def add_task():
    if(not request.json): 
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)
    task = {
        "id": tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

def hello_world():
    return "Hello World"

if(__name__ == "__main__"):
    app.run(debug = True)