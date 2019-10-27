from collections import OrderedDict

String = "Hello, how are you today?"
List = []

for x in String:
    List.append(x)

print(list(OrderedDict.fromkeys(List)))