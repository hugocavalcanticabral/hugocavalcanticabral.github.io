from sys import argv, exit
import urllib
import json
import time

PENALIDADE_WA = 50

usuarios = ["a.winston.s97", "hugo_cabral", "victoragnez", "RailtonT", "luizbarros", "tyronedamasceno", "heliobdf"]

pontuacao = {usuario: 0 for usuario in usuarios}

questoes = []
arquivo_contest = open("contest " + argv[1] + ".txt")

intervalo = arquivo_contest.readline().split(' ')
for line in arquivo_contest:
    questoes.append(line.rstrip())

def points(p, ti, wa):
	ti = ti - int(intervalo[0])
	h = time.gmtime(ti)[3]
	m = time.gmtime(ti)[4]
	totalTime = h*60+m
	if p<=500:
		return max(150, p - 2*totalTime - PENALIDADE_WA*wa);
	elif p<=1000:
		return max(300, p - 4*totalTime - PENALIDADE_WA*wa);
	elif p<=1500:
		return max(450, p - 6*totalTime - PENALIDADE_WA*wa);
	elif p<=2000:
		return max(600, p - 8*totalTime - PENALIDADE_WA*wa);
	else:
		return max(750, p - 10*totalTime - PENALIDADE_WA*wa);

for usuario in usuarios:
	url = "http://codeforces.com/api/user.status?handle=" + usuario + "&from=1&count=100";
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	for question in questoes:
		wrong = 0
		acc = False
		timeAcc = 0
		point = 0
		for submission in data['result']:
			ti = submission['creationTimeSeconds']
			q = str(submission['problem']['contestId']) + submission['problem']['index']
			if ti >= int(intervalo[0]) and ti <= int(intervalo[1]) and q == question and submission['verdict'] == 'OK':
				point = submission['problem']['points']
				if acc == False:
					acc = True
					timeAcc = ti
				else:
					timeAcc = min(timeAcc, ti)
		
		if acc == True:
			for submission in data['result']:
				ti = submission['creationTimeSeconds']
				q = str(submission['problem']['contestId']) + submission['problem']['index']
				if ti >= int(intervalo[0]) and ti <= int(intervalo[1]) and q == question:
					if submission['verdict'] != 'OK' and ti < timeAcc:
						wrong = wrong + 1
			pontuacao[usuario] += points(point, timeAcc, wrong)

for usuario in usuarios:
	f = open("score " + argv[1] + ".txt", 'a')
	f.write(str(usuario) + " " + str(pontuacao[usuario]) +"\n")
