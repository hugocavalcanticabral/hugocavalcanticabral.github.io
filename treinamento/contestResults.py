from sys import argv, exit
import urllib
import json

PENALIDADE_WA = 20

usuarios = ["a.winston.s97", "hugo_cabral", "victoragnez", "RailtonT", "luizbarros", "tyronedamasceno", "heliobdf"]

pontuacao = {usuario: 0 for usuario in usuarios}

questoes = []
arquivo_contest = open("contest " + argv[1] + ".txt")

intervalo = arquivo_contest.readline().split(' ')
for line in arquivo_contest:
    questoes.append(line.rstrip())

for usuario in usuarios:
    questoes_ja_contadas = []
    url = "http://codeforces.com/api/user.status?handle=" + usuario + "&from=1&count=100";
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    if data['status'] == 'OK':
        for submission in data['result']:
            ti = submission['creationTimeSeconds']
            q = str(submission['problem']['contestId']) + submission['problem']['index']
            if ti >= int(intervalo[0]) and ti <= int(intervalo[1]) and q in questoes:
                if submission['verdict'] == 'OK' and q not in questoes_ja_contadas:
                    p = submission['problem']['points']
                    pontuacao[usuario] += p - (float(p)/300.0)*(ti - int(intervalo[0]))/60.0
                    questoes_ja_contadas.append(q)

                if submission['verdict'] == 'WRONG_ANSWER':
                    pontuacao[usuario] -= PENALIDADE_WA

for usuario in usuarios:
	f = open("score " + argv[1] + ".txt", 'a')
	f.write(str(usuario) + " " + str(pontuacao[usuario]) +"\n")
