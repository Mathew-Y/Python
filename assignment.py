import json

file = open("QA_Pairs.txt", "r+")
output = open("Dictionary.txt", "w")


counter = 1
num = 0

# for line in file:
#     if counter % 2 == 0:
#         answer = line.removeprefix("answer :")
#         output.write(answer)
#     else:
#         question = line.removeprefix("question ")
#         output.write(question)
#     counter += 1

for line in file:
    if(num % 2 == 1):
        continue
    line = line.removeprefix("answer ")
    nextline = file.readlines()[counter].removeprefix("question ")
    input_str = line + " : " + nextline
    output.write(input_str)
    counter += 2
    num += 1










# entry = {'carl': 34}
#
# overlapping = open("Overlapping.json", "r+")
# data_overlapping = json.load(overlapping)
# data_overlapping.append(entry)
# file.seek(0)
# json.dump(data_overlapping, overlapping)



# for key in data_pairs:





