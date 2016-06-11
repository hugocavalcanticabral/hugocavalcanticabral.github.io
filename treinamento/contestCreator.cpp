#include <bits/stdc++.h>

using namespace std;

int main () {
	string contest;
	cout<<"DIGITE O NUMERO SERIAL DO CONTEST: ";
	cin>>contest;
	
	string file = "contest\\ " + contest + ".txt";
	string createFileContest = "touch " + file;
	system(createFileContest.c_str());
	
	string startTime, endTime;
	cout<<"DIGITE O starTime E O endTime: ";
	cin>>startTime>>endTime;
	
	string content;
	content = "echo " + startTime + " " + endTime + " >" + file;
	system(content.c_str());
	
	int qtdProblemas;
	cout<<"DIGITE A QUANTIDADE DE PROBLEMAS: ";
	cin>>qtdProblemas;
	
	for(int i=0 ; i<qtdProblemas ; i++){
		string aux;
		cin>>aux;
		
		content = "echo " + aux + " >>"+file;
		system(content.c_str());
	}
	
	cout<<"CALCULANDO O SCORE DO CONTEST "<<contest<<endl;
	//CALCULANDO O SCORE DOS USERS BASEADO NO ARQUIVO DO CONTEST
    string calcScore;
    calcScore = "python contestResults.py " + contest;
    system(calcScore.c_str());

	cout<<"CALCULANDO NOVO RATING"<<endl;
    //CALCULANDO O NOVO RATING DOS USERS BASEADO NOS SCORES DO CONTEST
    string calcRating;
    calcRating = "python ratings.py "+ contest;
    system(calcRating.c_str());
}
