def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    mail = {}
    id_dict = {}
    report_count = {}
    # 신고 카운트
    for i in range(len(report)):
        user_id,  report_id =report[i].split()
        if report_id not in report_count:
            report_count[report_id]=1
        else:
            report_count[report_id]+=1

    # 누구 신고했는지 저장하기
    for i in range(len(report)):
        user_id, report_id = report[i].split()
        if user_id not in id_dict:
            id_dict[user_id]=report_id
        elif id_dict[user_id]:
            id_dict[user_id]=id_dict[user_id]+' '+report_id

    # 메일발송
    for i in id_dict:
        count = 0
        for j in list(id_dict[i].split()):
            if report_count[j] >= k:
                count+=1
        mail[i]=count

    # 메일과 아이디 매칭
    for i in range(len(id_list)):
        if id_list[i] in mail:
            answer.append(mail[id_list[i]])
        else:
            answer.append(0)
    return answer
