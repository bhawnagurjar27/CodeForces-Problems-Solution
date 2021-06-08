#include <iostream>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int number_of_testcases = 1;
	int N, M, flag;
	vector< int > prime_numbers;
	
	for(int i=0; i <= number_of_testcases; i++){
	    cin >> N >> M;
	    
	    for(int prime = N; prime <= M + 1; prime++ ){
	        flag = 1;
	        if(prime > 1){
	            for(i = 2; i<= prime / 2; ++i){
	                if(prime % i == 0){
	                    flag = 0;
	                    break;
	                }
	            }
	                  
	        }
	        
	        if (flag == 1)
            prime_numbers.push_back(prime);
        
	    }
	    
	    
	   int len_of_prime_numbers = end(prime_numbers) - begin(prime_numbers);
	   
	    //cout << len_of_prime_numbers;
	    if(len_of_prime_numbers > 1){
	        if(prime_numbers[1] == M)
	            cout << "YES";
	        else
	          cout << "NO";
	    }
	    else
	      cout << "NO";
	}
	return 0;
}
