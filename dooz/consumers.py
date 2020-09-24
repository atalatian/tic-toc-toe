import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
import random
from . import models
from .models import mainObject
from . import serializers
import random


class DoozConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mainObject = None
        self.end = False
        self.draw = False
        self.winner = False
        self.rand = True
        self.database_dict = {}

    def create_database_dict(self):
        for i in range(1, 10):
            self.database_dict["turn{}".format(i)] = None
        self.database_dict["user"] = None
        self.database_dict["computer"] = None
        self.database_dict["row"] = None
        self.database_dict["starter"] = None
        self.database_dict["counter"] = None

    def set_database_dict(self):
        self.database_dict = {}
        self.create_database_dict()
        for i in range(0, 3):
            for j in range(0, 3):
                if self.mainObject["items"][str(i)][str(j)]["count"]:
                    self.database_dict["turn{}".format(self.mainObject["items"][str(i)][str(j)]["count"])] = [i, j]

        self.database_dict["starter"] = self.mainObject["starter"]
        self.database_dict["counter"] = self.mainObject["turn"] - 1

        if self.mainObject["result"]["user"]:
            self.database_dict["user"] = "win"
            self.database_dict["computer"] = "lose"
            self.database_dict["row"] = False
        elif self.mainObject["result"]["computer"]:
            self.database_dict["user"] = "lose"
            self.database_dict["computer"] = "win"
            self.database_dict["row"] = False
        elif self.mainObject["result"]["row"]:
            self.database_dict["user"] = "lose"
            self.database_dict["computer"] = "lose"
            self.database_dict["row"] = True

        print(self.database_dict)
        serializer = serializers.GameHistorySerializer(data=self.database_dict)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

    def result(self):
        pre_draw = []
        for i in range(0, 3):
            row_list_test = []
            counter = 0
            for j in range(0, 3):
                if self.mainObject["items"][str(i)][str(j)]["fill"]:
                    row_list_test.append(self.mainObject["items"][str(i)][str(j)]["player"])
            if row_list_test:
                for i in row_list_test:
                    if row_list_test[0] == i:
                        counter += 1

                if counter == 3:
                    self.end = True
                    self.winner = row_list_test[0]
                    return False
                else:
                    pre_draw.append(True)

        for i in range(0, 3):
            column_list_test = []
            counter = 0
            for j in range(0, 3):
                if self.mainObject["items"][str(j)][str(i)]["fill"]:
                    column_list_test.append(self.mainObject["items"][str(j)][str(i)]["player"])

            if column_list_test:
                for z in column_list_test:
                    if column_list_test[0] == z:
                        counter += 1
                if counter == 3:
                    self.end = True
                    self.winner = column_list_test[0]
                    return False
                else:
                    pre_draw.append(True)

        cross_increase_list_test = []
        cross_decrease_list_test = []
        for i in range(0, 2):
            if i == 0:
                column = 0
                for j in range(0, 3):
                    if self.mainObject["items"][str(j)][str(column)]["fill"]:
                        cross_increase_list_test.append(self.mainObject["items"][str(j)][str(column)]["player"])
                        column += 1

                if cross_increase_list_test:
                    counter = 0
                    for j in cross_increase_list_test:
                        if cross_increase_list_test[0] == j:
                            counter += 1
                    if counter == 3:
                        self.end = True
                        self.winner = cross_increase_list_test[0]
                        return False
                    else:
                        pre_draw.append(True)

            if i == 1:
                column = 2
                for j in range(0, 3):
                    if self.mainObject["items"][str(j)][str(column)]["fill"]:
                        cross_decrease_list_test.append(self.mainObject["items"][str(j)][str(column)]["player"])
                        column -= 1
                if cross_decrease_list_test:
                    counter = 0
                    for j in cross_decrease_list_test:
                        if cross_decrease_list_test[0] == j:
                            counter += 1
                    if counter == 3:
                        self.end = True
                        self.winner = cross_decrease_list_test[0]
                        return False
                    else:
                        pre_draw.append(True)

        counter_pre_draw = 0
        counter_draw = 0
        for i in pre_draw:
            if i:
                counter_pre_draw += 1
        if counter_pre_draw == len(pre_draw):
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.mainObject["items"][str(i)][str(j)]["fill"]:
                        counter_draw += 1
            if counter_draw == 9:
                self.end = True
                self.draw = True
                return False

        return True

    def computer_move(self):
        result = [None, None]
        self.rand = True
        for i in range(0, 3):
            row_list_test = []
            counter = 0
            for j in range(0, 3):
                if self.mainObject["items"][str(i)][str(j)]["fill"]:
                    row_list_test.append(self.mainObject["items"][str(i)][str(j)]["player"])
            if row_list_test:
                for z in row_list_test:
                    if row_list_test[0] == z:
                        counter += 1

                if counter == 2:
                    for j in range(0, 3):
                        if not self.mainObject["items"][str(i)][str(j)]["fill"]:
                            result[0] = i
                            result[1] = j
                            self.rand = False

        for i in range(0, 3):
            column_list_test = []
            counter = 0
            for j in range(0, 3):
                if self.mainObject["items"][str(j)][str(i)]["fill"]:
                    column_list_test.append(self.mainObject["items"][str(j)][str(i)]["player"])

            if column_list_test:
                for z in column_list_test:
                    if column_list_test[0] == z:
                        counter += 1
                if counter == 2:
                    for j in range(0, 3):
                        if not self.mainObject["items"][str(j)][str(i)]["fill"]:
                            result[0] = j
                            result[1] = i
                            self.rand = False

        cross_increase_list_test = []
        cross_decrease_list_test = []
        for i in range(0, 2):
            if i == 0:
                column = 0
                for j in range(0, 3):
                    if self.mainObject["items"][str(j)][str(column)]["fill"]:
                        cross_increase_list_test.append(self.mainObject["items"][str(j)][str(column)]["player"])
                        column += 1

                if cross_increase_list_test:
                    counter = 0
                    for j in cross_increase_list_test:
                        if cross_increase_list_test[0] == j:
                            counter += 1
                    if counter == 2:
                        column = 0
                        for j in range(0, 3):
                            if not self.mainObject["items"][str(j)][str(column)]["fill"]:
                                result[0] = j
                                result[1] = column
                                self.rand = False
                            else:
                                column += 1

            if i == 1:
                column = 2
                for j in range(0, 3):
                    if self.mainObject["items"][str(j)][str(column)]["fill"]:
                        cross_decrease_list_test.append(self.mainObject["items"][str(j)][str(column)]["player"])
                        column -= 1
                if cross_decrease_list_test:
                    counter = 0
                    for j in cross_decrease_list_test:
                        if cross_decrease_list_test[0] == j:
                            counter += 1
                    if counter == 2:
                        column = 2
                        for j in range(0, 3):
                            if not self.mainObject["items"][str(j)][str(column)]["fill"]:
                                result[0] = j
                                result[1] = column
                                self.rand = False
                            else:
                                column -= 1

        attempt = 0
        if self.rand:
            while True:
                result[0] = random.randint(0, 2)
                result[1] = random.randint(0, 2)
                if self.mainObject["items"][str(result[0])][str(result[1])]["fill"]:
                    attempt += 1
                    if attempt > 100:
                        self.draw = True
                        return False
                    continue
                else:
                    break
            return result
        else:
            return result

    def set_computer_move(self, move):
        self.mainObject["items"][str(move[0])][str(move[1])]["fill"] = True
        self.mainObject["items"][str(move[0])][str(move[1])]["player"] = self.mainObject["this_turn_player"]
        self.mainObject["items"][str(move[0])][str(move[1])]["count"] = self.mainObject["turn"]
        self.mainObject["turn"] += 1
        self.mainObject["this_turn_player"] = self.mainObject["userPlayer"]

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        mainObject_js = json.loads(text_data)["message"]
        self.mainObject = mainObject_js

        if self.mainObject["this_turn_player"] == self.mainObject["userPlayer"]:
            self.send(text_data=json.dumps({"message": self.mainObject}))

        elif self.mainObject["this_turn_player"] == self.mainObject["computerPlayer"]:
            res = self.result()
            if res:
                move = self.computer_move()
                if not move:
                    res = self.result()
                    if self.winner == self.mainObject["userPlayer"]:
                        self.mainObject["result"]["user"] = True
                        self.set_database_dict()
                    elif self.winner == self.mainObject["computerPlayer"]:
                        self.mainObject["result"]["computer"] = True
                        self.set_database_dict()
                    elif self.draw:
                        self.mainObject["result"]["row"] = True
                        self.set_database_dict()
                    self.send(text_data=json.dumps({"message": self.mainObject}))
                elif move:
                    self.set_computer_move(move)
                    res_computer = self.result()
                    if res_computer:
                        self.send(text_data=json.dumps({"message": self.mainObject}))
                    else:
                        if self.winner == self.mainObject["userPlayer"]:
                            self.mainObject["result"]["user"] = True
                            self.set_database_dict()
                        elif self.winner == self.mainObject["computerPlayer"]:
                            self.mainObject["result"]["computer"] = True
                            self.set_database_dict()
                        elif self.draw:
                            self.mainObject["result"]["row"] = True
                            self.set_database_dict()
                        self.send(text_data=json.dumps({"message": self.mainObject}))

            else:
                if self.winner == self.mainObject["userPlayer"]:
                    self.mainObject["result"]["user"] = True
                    self.set_database_dict()
                elif self.winner == self.mainObject["computerPlayer"]:
                    self.mainObject["result"]["computer"] = True
                    self.set_database_dict()
                elif self.draw:
                    self.mainObject["result"]["row"] = True
                    self.set_database_dict()
                self.send(text_data=json.dumps({"message": self.mainObject}))
