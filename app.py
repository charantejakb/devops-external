# from flask import Flask
# app = Flask(__name__)
# @app.route("/",methods=["GET"])
# def home():
#     return "devops Flask rest api is running"
# if __name__=="__main__":
#     app.run(debug=True,port=5000)

from flask import Flask,jsonify,request
app = Flask(__name__)
Students=[
    {"id":1,"name":"jhon","marks":85},
    {"id":2,"name":"jane","marks":90}
]

@app.route("/",methods=["GET"])
def home():
    return "devops Flask rest api is running"

#GET-retrievi all students
@app.route("/Students",methods=["GET"])
def get_students():
    return jsonify(Students),200

#POST-create a new student
@app.route("/Students",methods=["POST"])
def create_Student():
    data=request.get_json(silent=True)
    if not isinstance(data,dict):
        return jsonify({"error":"Invalid input"}),400
    if any(s["id"]==data["id"] for s in Students):
        return jsonify({"error":"Student id already exists"}),409

    Students.append(data)
    return jsonify({"message":"student created success","Student":data}),201

#PUT-update a student
@app.route("/Students/<int:id>",methods=["PUT"])
def update_Student(id):
    data=request.get_json(silent=True)
    if not isinstance(data,dict):
        return jsonify({"error":"Invalid input"}),400
    for student in Students:
        if student["id"]==id:
            student.update(data)
            return jsonify({"message":"student updated success","Student":student}),200
    return jsonify({"error":"Student not found"}),404

#DELETE-delete a student
@app.route("/Students/<int:id>",methods=["DELETE"])
def delete_Student(id):
    for student in Students:
        if student["id"]==id:
            Students.remove(student)
            return jsonify({"message":"student deleted success"}),200
    return jsonify({"error":"Student not found"}),404

if __name__=="__main__":
    app.run(debug=True,port=5000)




