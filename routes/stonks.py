# parse json to form arrays and lengh  of energy according to stonks
# arrays ranked according to stonk price of year
# record the lowest price and year of the arrays
# rank first elements of the arrays, subtract with capital, rank again with second element, subtract until used up
# record the elements to that we buy
# generate the jump buy ouput

from typing import Final


sample = [{
    "energy": 2,
    "capital": 500,
    "timeline": {
        "2037": {
            "Apple": {
                "price": 100,
                "qty": 10
            },
            "ple": {
                "price": 60,
                "qty": 20
            }
        },
        "2036": {
            "Apple": {
                "price": 10,
                "qty": 50
            },
            "ple": {
                "price": 70,
                "qty": 10
            }
        }
    }
}]

# import requests
# from flask import request, jsonify, Blueprint

# stonks = Blueprint("test", __name__)

# #function name cant be same as blueprint
# @stonks.route("/", methods=["POST"])


def main():
    # data = request.get_json()
    stonks = [[] for i in range(len(sample[0]["timeline"]["2037"]))]
    stonks_d = {}
    stonks_d_reverse = {}
    x = 0
    for i in sample[0]["timeline"]["2037"]:
        stonks_d[str(x)] = i
        x += 1
    x = 0
    for i in sample[0]["timeline"]["2037"]:
        stonks_d_reverse[i] = x
        x += 1

    for i in sample:  # test cases
        for j, val in i["timeline"].items():  # reduce according to energy later
            i = 0
            for k in val:
                x, y = val[k]["price"], val[k]["qty"]
                stonks[i].append((j, x, y))
                i += 1
    highest = ()
    for i in stonks:
        i.sort(key=lambda stonk: stonk[1])
        print(i)
        highest += (i[len(i)-1][1],)
    stock = 0
    final = []
    for i in stonks:
        print("i:", i)
        year = 0
        if not final:
            print("1")
            final.insert(0, [stonks_d[str(stock)], i[year]])
            print("final:", final)
        else:
            print("2")
            d = 0
            print("i:", i)
            final_item = [stonks_d[str(stock)], i[year]]
            print("final_item:", final_item)
            for j in final.copy():
                if (highest[stonks_d_reverse[final_item[0]]] - final_item[1][1] > highest[stonks_d_reverse[j[0]]] - j[1][1]):
                    final.insert(d, final_item)
                    break
                else:
                    d+=1
                    continue
            if d == len(final) - 1:
                final.insert(d, final_item)
            print("final:", final)
        stock += 1
                
    print("final", final)
    #    for j in i[x]:
    #        d = {stonks_d[str(k)]: j}
    #        final.append(d.copy())
    #        x += 1
    #        print("final:", final)
    return


main()
