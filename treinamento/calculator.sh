#MODO DE USAR: $bash calculator.sh "contest number"

echo "CALCULANDO O SCORE DO CONTEST $1" 

python contestResults.py $1

echo "CALCULANDO NOVO RATING"

python ratings.py $1

rm *~
git add --all
git commit -m "update by shell"
git push -u origin master
