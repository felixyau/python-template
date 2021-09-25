#parse json to form arrays and lengh  of energy according to stonks
#arrays ranked according to stonk price of year
#record the lowest price and year of the arrays
#rank first elements of the arrays, subtract with capital, rank again with second element, subtract until used up
#record the elements to that we buy
#generate the jump buy ouput

sample = [{
 "energy":2,
 "capital":500,
 "timeline":{
   "2037":{
     "Apple":{
       "price":100,
       "qty":10
     },
     "banaan": {
     }
   },
   "2036":{
     "Apple":{
       "price":10,
       "qty":50
      }
   }
 }
}]

# import requests
# from flask import request, jsonify, Blueprint 

# stonks = Blueprint("test", __name__)

# #function name cant be same as blueprint
# @stonks.route("/", methods=["POST"])

# def main():
#     # data = request.get_json()
#     for i in len(sample[0]["timeline"]["2037"]):
#     stonks = []
#     return 

# main()