#gym_scores

def main():
    num_judge = int(input("Please enter the number of judges: "))
    score_list = []

    for num in range(1, num_judge+1):
        score = eval(input("Pleae enter the score of the judge: "))
        score_list.append(score)
    print (avg_gym_score(score_list))

def avg_gym_score(score_list):
    score_list.sort()  
    score_list.remove(max(score_list))
    score_list.remove(min(score_list))
    average_score = sum(score_list) / len(score_list)
    return average_score

main()