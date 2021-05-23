number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    num_circles = int(input())
    radii_of_circles = list(map(int,input().split()))
    pie_value = 3.1415926536
    red_part_area = 0
    ans = 0
    radii_of_circles.sort(reverse = True)
    
    while num_circles > ans:
        if num_circles > (ans + 1):
           red_part_area += pie_value*(radii_of_circles[ans]*radii_of_circles[ans] - radii_of_circles[ans+1]*radii_of_circles[ans+1])
           ans += 2 
        else:
            red_part_area += pie_value*(radii_of_circles[ans]*radii_of_circles[ans])
            ans += 1
            
    print(red_part_area)