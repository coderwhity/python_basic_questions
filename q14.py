# Ask user to enter their marks of 5 subjects, display average score & percentage with their grade. Maximum marks per subject are 70

score_list= []
for i in range(0,5):
    while True:
        mark = int(input(f"Enter marks of {i+1} subject : "))
        if(mark<=70):
            score_list.append(mark)
            break
        else:
            print("Maximum marks is 70")
total = sum(score_list)
avg = total/5
perc = (total/(70*5))*100
print(f"Total : {total}")
print(f"Percentage : {round(perc,2)}")
print(f"Average : {round(avg,2)}")
if(perc <35):
    print("Fail")
elif(perc >=35 and perc<=50):
    print("C Grade")
elif(perc >= 51 and perc<80):
    print("B Grade")
elif(perc >=90 and perc<=100):
    print("A Grade")