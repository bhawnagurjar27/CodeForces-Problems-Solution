#include <iostream>
using namespace std;

int main() {
	
	int number_of_testcases,i;
	cin >> number_of_testcases;
	while(number_of_testcases--){
	    
	    int num_stones;
	    cin >> num_stones;
	    
	    int power_of_stones[num_stones];
	    int lowest_power, greatest_power;
	    
	    for(int i=0; i<num_stones; i++)
	         cin >> power_of_stones[i];
	    
	    for(int i=0; i<num_stones; i++){
	        if(power_of_stones[i] == 1)
	            lowest_power = i;
	        if(power_of_stones[i] == num_stones)
	            greatest_power = i;
	    }
	    
	    int deleted_power_left = lowest_power + 1;
	    int deleted_power_right = greatest_power + 1;
	    
	    int ans_left_side = max(deleted_power_right, deleted_power_left);
	    int ans_right_side = max(num_stones - lowest_power, num_stones - greatest_power);
	    int ans_left_right_deleted = min(deleted_power_left + num_stones - greatest_power, deleted_power_right + num_stones - lowest_power);
	    int answer = min(ans_left_side, min(ans_right_side,ans_left_right_deleted));
	    cout <<answer << "\n";
	    
	     
	    
	}
	return 0;
}
