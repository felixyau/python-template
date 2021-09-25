# parse json to form arrays and lengh  of energy according to stonks
# arrays ranked according to stonk price of year
# record the lowest price and year of the arrays
# rank first elements of the arrays, subtract with capital, rank again with second element, subtract until used up
# record the elements to that we buy
# generate the jump buy ouput

# data = [{
#     "energy": 2,
#     "capital": 500,
#     "timeline": {
#         "2037": {
#             "Apple": {
#                 "price": 100,
#                 "qty": 10
#             },
#             # "ple": {
#             #     "price": 60,
#             #     "qty": 20
#             # }
#         },
#         "2036": {
#             "Apple": {
#                 "price": 10,
#                 "qty": 50
#             },
#             # "ple": {
#             #     "price": 70,
#             #     "qty": 10
#             # }
#         }
#     }
# }]

import requests
from flask import request, jsonify, Blueprint
import json

stonks = Blueprint("stonks", __name__)

#function name cant be same as blueprint
@stonks.route("/", methods=["POST"])
def main():
    data = request.get_json()
    output = []
    for sample in data:
        stonks = [[] for i in range(len(sample["timeline"]["2037"]))]
        stonks_d = {}
        stonks_d_reverse = {}
        capital = sample["capital"]   
        x = 0
        for i in sample["timeline"]["2037"]:
            stonks_d[str(x)] = i
            x += 1
        x = 0
        for i in sample["timeline"]["2037"]:
            stonks_d_reverse[i] = x
            x += 1

        for j, val in sample["timeline"].items():  # reduce according to energy later
            i = 0
            for k in val:
                x, y = val[k]["price"], val[k]["qty"]
                stonks[i].append((j, x, y))
                i += 1
        highest = []
        print("St:", stonks)
        ind = 0
        for i in stonks:
            i.sort(key=lambda stonk: stonk[1])
            highest.append((stonks_d[str(ind)], i[len(i)-1][0], i[len(i)-1][1]))
            ind += 1
        print("highest:", type(highest[0][1]))

        final = []
        year = 0
        remaining = capital

        while(year < len(stonks[0])-1):
            stock = 0
            for i in stonks:
                if not final:
                    final.insert(0, [stonks_d[str(stock)], i[year]])
                else:
                    d = 0
                    final_item = [stonks_d[str(stock)], i[year]]
                    for j in final.copy():
                        if (highest[stonks_d_reverse[final_item[0]]][2] - final_item[1][1] > highest[stonks_d_reverse[j[0]]][2] - j[1][1]):
                            final.insert(d, final_item)
                            break
                        else:
                            d += 1
                            continue
                    if d == len(final):
                        print()
                        final.insert(d, final_item)
                stock += 1
            for i in range(year + 1):
                price = final[i][1][1]
                qty = final[i][1][2]
                remaining -= price * qty
            if remaining < 0:
                break
            year += 1
        time = "2037"
        final.sort(key=lambda x: x[1][0], reverse=True)
        command = []
        used_stocks = []
        money_left = capital

        for i in final:
            no = i[1][2] if money_left // (i[1][1] *
                                        i[1][2]) > 1 else money_left // i[1][1]
            print("moneyleft:", money_left)
            print(i[0] + ":", str(no))
            command.append("j-" + time + "-" + i[1][0])
            command.append("b-" + str(i[0]) + "-" + str(no))
            money_left -= no * i[1][1]
            used_stocks.append([i[0], str(no)])
            time = i[1][0]
        used_stocks.sort(key=lambda x: highest[stonks_d_reverse[x[0]]][1])
        print("used_stocks:", used_stocks)
        for i in used_stocks:
            command.append("j-" + time + "-" + highest[stonks_d_reverse[i[0]]][1])
            command.append("s-" + i[0] + "-" + i[1])
        print("command:", command)
        output.append(command)  
    ot = dict(output)
    return json.dumps(ot)

