import csv

row_list = [["name", "composition", "function", "indication", "label"],
            ["大柴胡汤", "柴胡,黄芩,芍药,半夏,生姜,枳实,大枣,大黄", "和解少阳,内泻热结.", "少阳阳明合病.往来寒热,胸胁苦满,呕不止,郁郁微烦,心下痞硬,或心下满痛,大便不解或协热下利,舌苔黄,脉弦有力.", "和解剂"]]

with open('TCM.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)