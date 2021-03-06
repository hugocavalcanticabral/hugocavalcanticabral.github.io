#	MODO DE USAR:
#		CRIAR UM ARQUIVO COM O NOME:"contest 'number'.txt" onde 'number' sera um numero sequencial a partir de 1 para numerar os contest realizados
#		O ARQUIVO DEVE TER O FORMATO:	(DEVERAO SER CADASTRADOS TODOS OS USUARIOS, INCLUSIVE OS QUE NAO FIZERAM O CONTEST COM RATE = 0)
#			USER RATE
#			USER RATE
#			...
#
#		EXECUTAR "python rating.py 'number'" EM QUE 'number' EH O NUMERO DO CONTEST
#		CADA ARQUIVO "USER.txt" TERA NA ULTIMA LINHA O NOVO RATING DO 'USER'
#		NOVOS USUARIOS COMECARAO COM RATE 1000, E BASTA COLOCAR SUA HANDLE NO VETOR 'usuarios'
#		SERA USADO O RATE 1200 PARA SEPARAR AS DIVISOES 1 E 2

from sys import argv

def getContestResult(number):
	f = open("score " + str(number) + ".txt")
	dic = {}
	for line in f:
		dic[line.split(' ')[0]] = float(line.split(' ')[1])
	return dic

def lastRating(handle):
    f = open(r"users/"+handle + ".txt")	###################
    return float(f.readlines()[-1])

#TESTA SE OS USER 'A' E 'B' ESTAO NA MESMA DIVISAO
def same_div(userA, userB):
	return (rating_antigo[userA]<rate_divisor and rating_antigo[userB]<rate_divisor) or (rating_antigo[userA]>=rate_divisor and rating_antigo[userB]>=rate_divisor)

#UTILIZA A FORMULA DE ELO
#ESCORE ESPERADO 
def calcular_escore(handle):
	soma = 0.0
	for usuario in usuarios:
		if usuario != handle and same_div(handle, usuario):
			soma += 1.0/(1 + 10**((rating_antigo[usuario] - rating_antigo[handle])/400.0))
	return soma

def calcular_novo_rating(handle):
	soma1 = 0.0						#ESCORE DO CONTEST
	soma2 = calcular_escore(handle)
	for usuario in usuarios:
		if usuario != handle and same_div(handle, usuario):
			if resultado_contest[handle] > resultado_contest[usuario]:
				soma1 += 1.0
			elif resultado_contest[handle] == resultado_contest[usuario]:
				soma1 += 0.5
	
	if soma2 == 0.0:								#UNICO DA SUA DIVISAO
		if resultado_contest[handle] != 0:			#ESTAVA PRESENTE NO CONTEST
			return rating_antigo[handle] + 10.0
		else:
			return rating_antigo[handle] - 10.0
	else:
		return rating_antigo[handle] + FATOR_K*(soma1 - soma2)

FATOR_K = 32
rate_divisor = 1200
usuarios = ["a.winston.s97", "hugo_cabral", "heliobdf", "victoragnez", "RailtonT", "tyronedamasceno", "luizbarros"]
rating_antigo = {usuario: lastRating(usuario) for usuario in usuarios}
resultado_contest = getContestResult(argv[1])

for usuario in usuarios:
	f = open(r"users/"+usuario+".txt", 'a')########################3
	f.write("\n"+str(calcular_novo_rating(usuario)))
