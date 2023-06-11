from roboflow import Roboflow
rf = Roboflow(api_key="u3VM1jMlTP08c5ogG5GZ")
project = rf.workspace("umbc-linyj").project("megafootballplayer")
dataset = project.version(3).download("yolov8")