from flask import Flask,jsonify,request

app=Flask(__name__)

data=[
    {
        'id':1,
        'name':"Keshu",
        'contact':"8210039605",
        'done':False
    
    },
     {
        'id':2,
        'name':"Jiya",
        'contact':"9321787732",
        'done':False
    
    }
]

@app.route("/add-data", methods=["POST"])
def add_contact(): 
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
        contact={
              'id':contact[-1]['id']+1,
              'Name':request.json['Name'],
              'Contact':request.json.get('Contact',""),
              'done':False
        }
        data.append(contact)
        return jsonify({
            "status":"sucess",
            "message":"contact added sucessfully"
        })

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data":contact
    })

if(__name__=="__main__"):
    app.run()
