# def solution(survey, choices):
#     answer =""
#     dict = {
#         'R':0,
#         'T':0,
#         'C':0,
#         'F':0,
#         'J':0,
#         'M':0,
#         'A':0,
#         'N':0
#     }
#     for i in range(len(survey)):
#         if choices[i] < 4:
#             dict[survey[i][0]]+= (4-choices[i])
#         elif choices[i] >4:
#             dict[survey[i][1]] += (choices[i]-4)
#         else:
#             continue
#     if dict["R"] > dict["T"]:
#         answer += "R"
#     if dict["R"] <= dict["T"]:
#         answer += "T"
#     if dict["F"] > dict["C"]:
#         answer += "F"
#     if dict["F"] <= dict["C"]:
#         answer += "C"
#     if dict["M"] > dict["J"]:
#         answer += "M"
#     if dict["M"] <= dict["J"]:
#         answer += "J"
#     if dict["N"] > dict["A"]:
#         answer += "N"
#     if dict["N"] <= dict["A"]:
#         answer += "A"
#     return answer

def solution(survey, choices):
    answer =""
    type = ["R","T","C","F","J","M","A","N"]
    result = [0] * 8
    
    for i in range(len(survey)):
        if choices[i] < 4:
            result[type.index(survey[i][0])]+= (4-choices[i])
        elif choices[i] >4:
            result[type.index(survey[i][1])] += (choices[i]-4)
        else:
            continue
    
    for i in range(0,7,2):
        if result[i] < result[i+1]:
            answer += type[i+1]
        else:
            answer += type[i]

    return answer

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
result = solution(survey,choices)
print(result)