from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Sample(Resource):
    def get(self,id):
        with open('data.json') as f:  
            data = json.load(f)
            f.close()
        if id in data:
            return data[id] 
        else:
            return {"response":"key not found"}
      

    def put(self,id):
        with open('data.json') as f:  
            data = json.load(f)
            f.close()
        if id in data:
            req = json.loads(request.data)
            data[id]=req[id]
            with open('data.json', 'w') as f:
                json.dump(data, f) 
                f.close()
            return {"response":"key value updated"}
        else:
            return {"response":"key not found"}

    def delete(self,id):
        with open('data.json') as f:  
            data = json.load(f)
            f.close()
        if id in data:
            del data[id]
            with open('data.json', 'w') as f:
                json.dump(data, f) 
                f.close()
            
            return {"response":"key value deleted"}
        else:
            return {"response":"key not found"}



class SampleAll(Resource):
    def get(self):
        with open('data.json') as f:  
            data = json.load(f)
            f.close()       
            return data
       
class SampleCreate(Resource):
    def post(self):
        with open('data.json') as f:
           data = json.load(f)
           f.close()
        data.update(json.loads(request.data))
        with open('data.json', 'w') as f:
            json.dump(data, f) 
            f.close()
        return {"reponse":"key value added"}

api.add_resource(SampleAll, '/key/getall', methods=['GET'])
api.add_resource(Sample, '/key/<string:id>', methods=['GET', 'PUT', 'DELETE'])
api.add_resource(SampleCreate, '/key', methods=['POST'])



if __name__ == '__main__':
     app.run(debug=True)