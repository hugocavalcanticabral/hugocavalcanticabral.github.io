#-*- encoding: utf-8 -*-
import urllib, json

handles = ["a.winston.s97", "hugo_cabral", "heliobdf", "RailtonT", "victoragnez", "luizbarros", "tyronedamasceno"]

possible_contests = []
print "Obtendo lista de contests..."
url_contestlist = "http://codeforces.com/api/contest.list?gym=false"
response = urllib.urlopen(url_contestlist)
data = json.loads(response.read())
if data['status'] == 'OK':
    print "Obtido com sucesso!"
    for contest in data['result']:
        if contest['phase'] == "FINISHED":
            possible_contests.append(contest['id'])

    for handle in handles:
        print "Checando as submissões de " + handle
        url = "http://codeforces.com/api/user.status?handle="+handle
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        if data['status'] == 'OK':
            for submission in data['result']:
                if submission['contestId'] in possible_contests:
                    possible_contests.remove(submission['contestId'])
                    

print possible_contests
