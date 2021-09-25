import sys
from collections import deque
import json
import copy
from flask import request, jsonify, Blueprint
import requests

asteroid = Blueprint("asteroid", __name__)

input = {
  "test_cases": [
    "CCCAAABBBAAACCC",
    "BBAAABBB",
    "CCCAAAAABBBAAACCC",
    "ABBBBA"
  ]
}

@asteroid.route("/", methods=["POST"])
def main():
    input = request.get_json()
    output = []
    for i in range(len(input["test_cases"])):
      print(i)
      str = input["test_cases"][i] 
      output.append({"input": str, "score": checkTotalScore(
          str), "origin": checkOptimalMove(str)})
    return jsonify(output)

def calScore(countSize):
    totalScore=1
    if(countSize <= 6):
        totalScore=countSize
    elif(countSize >= 7 and countSize < 10):
        totalScore=(countSize*1.5)
    else:
        totalScore=(countSize*2)
    return (int)(totalScore)


def checkTotalScore(string):
    trackFirst=0
    trackEnd=0
    currentSize=string[0]
    countSize=0
    countSizeFirst=0
    countSizeEnd=0
    for i in range(len(string)):
        if(string[i] == currentSize):
            countSizeFirst += 1
        else:
            trackFirst=i-1
            break
    for i in range(len(string)-1, -1, -1):
        if(string[i] == currentSize):
            countSizeEnd += 1
        else:
            trackEnd=i+1
            break

    countSize=countSizeFirst + countSizeEnd
    if(trackFirst >= trackEnd):
        return calScore(len(string))
    else:
        return calScore(countSize) + checkTotalScore(string[countSizeFirst:len(string)-countSizeEnd])



def checkOptimalMove(string):
    trackFirst=0
    trackEnd=0
    currentSize=string[0]
    countSize=0
    countSizeFirst=0
    countSizeEnd=0
    for i in range(len(string)):
        if(string[i] == currentSize):
            countSizeFirst += 1
        else:
            trackFirst=i-1
            break
    for i in range(len(string)-1, -1, -1):
        if(string[i] == currentSize):
            countSizeEnd += 1
        else:
            trackEnd=i+1
            break

    countSize=countSizeFirst + countSizeEnd
    if(countSize/2 == len(string)):
        return int(len(string)/2)
    else:
        return countSizeFirst + checkOptimalMove(string[countSizeFirst:len(string)-countSizeEnd])



