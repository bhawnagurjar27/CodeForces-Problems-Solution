number_of_testcases = 1 #int(input())

for _ in range(number_of_testcases):
    number_of_cards = int(input())
    cards = []
    for i in range(number_of_cards):
        num_at_top, num_at_bottom = map(int,input().split())
        cards.append((num_at_bottom, num_at_top))
        
    cards.sort(reverse=True)
    #print(cards)
    
    current_cards = 1 
    total_score = 0 
    for card in cards:
        if current_cards < 1:
            break
        
        current_cards -= 1 
        total_score += card[1]
        current_cards += card[0]
        
    print(total_score)