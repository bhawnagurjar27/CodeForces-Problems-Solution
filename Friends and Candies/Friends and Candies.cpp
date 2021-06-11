#include <iostream>
using namespace std;

int main() {
	
	int number_of_testcases,i;
	cin >> number_of_testcases;
	while(number_of_testcases--){
	    
	    int num_friends;
	    cin >> num_friends;
	     int sum_of_candies = 0;
	     int candies[num_friends];
	     
	    for(i=0; i<num_friends; i++){
	        cin >> candies[i];
	        sum_of_candies += candies[i];
	    }
	    if(sum_of_candies % num_friends != 0){
	         cout << "-1" <<"\n";
	        
	       
	    }
	    else{     
	   
	       sum_of_candies /= num_friends;
	      int  min_num_friends_selected = 0;
	       for(i=0; i<num_friends; i++){
	           if(candies[i] > sum_of_candies)
	               min_num_friends_selected += 1;
	       }
	       cout << min_num_friends_selected << "\n";
	    }
	       
	
	    
	}
	return 0;
}
