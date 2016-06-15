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
	
	cout<<"DIGITE OS PROBLEMAS: ";
	for(int i=0 ; i<qtdProblemas ; i++){
		string aux;
		cin>>aux;
		
		content = "echo " + aux + " >>"+file;
		system(content.c_str());
	}
}
