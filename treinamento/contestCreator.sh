echo "DIGITE O NUMERO SERIAL DO CONTEST: "
read contest

touch "contest $contest.txt"

echo "DIGITE O starTime: "
read startTime
echo "DIGITE O endTime: "
read endTime

echo $startTime $endTime > "contest $contest.txt"

echo "DIGITE A QUANTIDADE DE PROBLEMAS: "
read qtdProblemas;

echo "DIGITE OS PROBLEMAS: "

for (( i=0; i < $qtdProblemas; ++i ))
do
    read aux
    
    echo $aux >> "contest $contest.txt"
done

rm *~
git add --all
git commit -m "update by shell"
git push -u origin master
