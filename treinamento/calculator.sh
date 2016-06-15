#MODO DE USAR: $bash calculator.sh "contest number"

echo "CALCULANDO O SCORE DO CONTEST $1" 

python contestResults.py $1

echo "CALCULANDO NOVO RATING"

python ratings.py $1
