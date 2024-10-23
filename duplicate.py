student_id = {'id1':{'name':['Navya'], 'class':['8'], 'subject':['algebra 1', 'information technology', 'language arts']},
              'id2':{'name':['Nynika'], 'class':['8'], 'subject':['algebra 1', 'pbmf', 'language arts']},
            'id3':{'name':['Navya'], 'class':['8'], 'subject':['algebra 1', 'information technology', 'language arts']},
            'id4':{'name':['Aishni'], 'class':['8'], 'subject':['algebra 1', 'art', 'language arts']}}

res = {}

for key, value in student_id.items():
    if value not in res.values():
        res[key] = value

print(res)