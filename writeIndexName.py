import csv

row_list = [["index", "name"],
            ["0", "半夏"],
            ["1", "柴胡"],
            ["2", "大黄"],
            ["3", "大枣"],
            ["4", "芍药"],
            ["5", "黄芩"],
            ["6", "生姜"],
            ["7", "枳实"],
            ["8", "人参"],
            ["9", "甘草"],
            ["100","未知药"]]

with open('IndexName.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)
