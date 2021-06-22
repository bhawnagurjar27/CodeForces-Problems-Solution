def vova_and_train():
    ans = destination_point//period_of_lantern - (segment_occupied_2//period_of_lantern - (segment_occupied_1 -1)/period_of_lantern)
    return(int(ans))
    
    
    
    
    
num_of_testcases = int(input())
for _ in range(num_of_testcases):
    destination_point, period_of_lantern, segment_occupied_1, segment_occupied_2 = map(int,input().split())
    print(vova_and_train())
    