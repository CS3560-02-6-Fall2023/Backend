from flask import jsonify,request,make_response,send_file
import io
import json
from utils.validator import validate_input
from Exceptions.apiExceptions import *
from flask.views import MethodView

from database.userDB import User
import os
class Account(MethodView):
    
    
    def post(self):
        # get the data from 
        
        required_field = ["username","password","email"]
        
        data = json.loads(request.data.decode('utf-8'))
        
        try:
            validate_input(data.keys(), required_field)

        except MissingArgumentException as e:
            
            return jsonify({"error":e.message}),e.error_code
        if "image" not in data.keys():
            with open(os.path.join(os.getcwd(),"image","userProfiles","download.jpg"),"rb") as file:
                image = file.read()
            
        else:
            #implement image here if they do put an image
            pass
        
        User.createAccount(data["username"],data["email"],data["password"],image )
        

        return jsonify({"success":"created"}),201
    def get(self):
        data = request.args.get("email")
        # implement a check on required arguments (when using validator function make sure is_body  is false to ensure correct error is sent)
        db_val = User.getAccount(email=data)
        
        for i in db_val:
            print(i)
        # return send_file(
        #     io.BytesIO(image_bytes),
        #     download_name='logo.png',
        #     mimetype='image/png'
        # )
        return "test"
    def patch(self):
        # changes the account
        data = json.loads(request.data.decode('utf-8'))
        # impelemt a check onr equired argeuments
        return jsonify("implement accoutn patch endpoint"),501
       
    def delete(self):
        email = request.args.get("email")
        User.deteleteAccount(email=email)
        return jsonify("taks completed")
