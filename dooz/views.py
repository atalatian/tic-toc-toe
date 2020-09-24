from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import io
import random
from . import models
from .models import mainObject
from . import serializers
import os
import json

mainObject = {
    "starter": None,
    "userPlayer": None,
    "computerPlayer": None,
    "this_turn_player": None,
    "turn": None,
    "items": None,
    "result": {
        "user": False,
        "computer": False,
        "row": False,
    },
}

first_time = [True, True, True]


def computer_move(turn, items):
    lose_arrange = {
        "row1": {
            "column1": False,
            "column2": False,
            "column3": False,
            "count": 0,
        },
        "row2": {
            "column1": False,
            "column2": False,
            "column3": False,
            "count": 0,
        },
        "row3": {
            "column1": False,
            "column2": False,
            "column3": False,
            "count": 0,
        },
        "column1": {
            "row1": False,
            "row2": False,
            "row3": False,
            "count": 0,
        },
        "column2": {
            "row1": False,
            "row2": False,
            "row3": False,
            "count": 0,
        },
        "column3": {
            "row1": False,
            "row2": False,
            "row3": False,
            "count": 0,
        },

        "cross1": {
            "row1": {
                "column1": False,
            },
            "row2": {
                "column2": False,
            },
            "row3": {
                "column3": False,
            },
            "count": 0,
        },

        "cross2": {
            "row1": {
                "column3": False,
            },
            "row2": {
                "column2": False,
            },
            "row3": {
                "column1": False,
            },
            "count": 0,
        }
    }

    for i in range(0, 3):
        for j in range(0, 3):
            lose_arrange["column" + str(i + 1)]["row" + str(j + 1)] = items[j][i]["filled"]
            lose_arrange["row" + str(i + 1)]["column" + str(j + 1)] = items[i][j]["filled"]

    for j in range(0, 3):
        lose_arrange["cross1"]["row" + str(j + 1)]["column" + str(j + 1)] = items[j][j]["filled"]
        lose_arrange["cross2"]["row" + str(j + 1)]["column" + str(3 - j)] = items[j][2 - j]["filled"]

    row = [lose_arrange["row1"], lose_arrange["row2"], lose_arrange["row3"]]
    column = [lose_arrange["column1"], lose_arrange["column2"], lose_arrange["column3"]]
    cross1 = [lose_arrange["cross1"]]
    cross2 = [lose_arrange["cross2"]]

    answer = None
    there_is_answer = False

    count = 0
    for i in row:
        count += 1
        for j in range(0, 3):
            if i["column" + str(j + 1)]:
                i["count"] += 1
        if i["count"] == 2:
            for z in range(0, 3):
                if not i["column" + str(z + 1)]:
                    there_is_answer = True
                    answer = [count, z + 1]

    count = 0
    for i in column:
        count += 1
        for j in range(0, 3):
            if i["row" + str(j + 1)]:
                i["count"] += 1
        if i["count"] == 2:
            for z in range(0, 3):
                if not i["row" + str(z + 1)]:
                    there_is_answer = True
                    answer = [z + 1, count]

    for i in cross1:
        for j in range(0, 3):
            if i["row" + str(j + 1)]["column" + str(j + 1)]:
                i["count"] += 1
        if i["count"] == 2:
            for z in range(0, 3):
                if not i["row" + str(z + 1)]["column" + str(z + 1)]:
                    there_is_answer = True
                    answer = [z + 1, z + 1]

    for i in cross2:
        for j in range(0, 3):
            if i["row" + str(j + 1)]["column" + str(3 - j)]:
                i["count"] += 1
        if i["count"] == 2:
            for z in range(0, 3):
                if not i["row" + str(z + 1)]["column" + str(3 - z)]:
                    there_is_answer = True
                    answer = [z + 1, 3 - z]

    if there_is_answer:
        print(answer)
        return answer
    elif not there_is_answer:
        rand_arr = [random.randrange(1, 4, 1), random.randrange(1, 4, 1)]
        print(rand_arr)
        return rand_arr


@api_view(["POST", "GET"])
def render_dooz(request):
    def build_mainObject():
        itemsArray = [[], [], []]
        eachElementObj = {
            "filled": False,
            "player": None,
            "count": None,
        }
        for i in range(0, 3):
            for j in range(0, 3):
                itemsArray[i].append(eachElementObj)

        mainObject["items"] = itemsArray

    def update_mainObject_from_js(request):
        stream = io.BytesIO(request.body)
        js_mainObject = JSONParser().parse(stream)
        mainObject["starter"] = js_mainObject["starter"]
        mainObject["userPlayer"] = js_mainObject["userPlayer"]
        mainObject["computerPlayer"] = js_mainObject["computerPlayer"]
        mainObject["this_turn_player"] = js_mainObject["this_turn_player"]
        mainObject["turn"] = js_mainObject["turn"]
        mainObject["items"] = js_mainObject["items"]
        mainObject["result"] = js_mainObject["result"]

    def post_to_mainObject_table(mainObject):
        queryset = models.mainObject.objects.last()
        if queryset:
            queryset.delete()
        dic = {"mainObject": mainObject, }
        serializer = serializers.mainObjectSerializer(data=dic)
        if serializer.is_valid():
            serializer.save()

    def update_mainObject_from_python(move):
        mainObject["items"][move[0]-1][move[1]-1]["filled"] = True
        mainObject["items"][move[0]-1][move[1]-1]["player"] = mainObject["this_turn_player"]
        mainObject["items"][move[0]-1][move[1]-1]["count"] = mainObject["turn"]
        mainObject["turn"] += 1
        if mainObject["this_turn_player"] == "green":
            mainObject["this_turn_player"] = "red"
        elif mainObject["this_turn_player"] == "red":
            mainObject["this_turn_player"] = "green"

    if request.method == "GET":
        return render(request, "dooz/dooz.html")
    if request.method == "POST":
        pass
        """
        update_mainObject_from_js(request)
        if mainObject["this_turn_player"] == mainObject["userPlayer"]:
            return JsonResponse(json.dumps(mainObject), safe=False)
        elif mainObject["this_turn_player"] == mainObject["computerPlayer"]:
            move = computer_move(mainObject["turn"], mainObject["items"])
            update_mainObject_from_python(move)
            return JsonResponse(json.dumps(mainObject), safe=False)
        """
