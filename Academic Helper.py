def calculate_marks_and_grades():

    print("**********************1.MARKS AND GRADES CALCULATOR**********************")
    subject = input("Enter subject name (e.g., CSE, Maths): ")
    cat_marks = float(input(" enter your CAT marks for" ,subject," (out of 50): "))
    class_avg = float(input("Enter the class average for ",subject))

    if cat_marks >= class_avg +10:
        grade = 'S'
    elif cat_marks >= class_avg +5:
        grade = 'A'
    elif cat_marks >= class_avg:
        grade = 'B'
    elif cat_marks >= class_avg- 5:
        grade = 'C'
    elif cat_marks >= class_avg - 10:
        grade = 'D'
    else:
        grade = 'F'

    print(subject," Grade Result: {grade}<<<<<")

def calculate_only_attendance():

    print("**********************2. ONLY ATTENDANCE **********************")
    subject = input("Enter subject name (e.g., cse, maths): ")
    total = int(input("enter TOTAL classes Scheduled for", subject,";"))
    attended = int(input("enter ATTENDED classes for", subject, ": "))

    if total == 0:
        print("No classes scheduled. Attendance calculation is not applicable.")
        return

    percentage = (attended / total) * 100
    margin = attended - (0.75 * total)

    if margin > 0:
        skips = (attended / 0.75) - total
        status = "You can safely bunk " + str(int(skips)) + " upcoming classes."
    elif margin == 0:
        status = "exactly at 75%. Do not bunk the next class!"
    else:
        needed = (0.75 * total - attended) / 0.25
        if needed != int(needed):
            needed = int(needed) + 1
        else:
            needed = int(needed)
        status = "warning! You must attend the next " + str(needed) + " classes to reach 75%."

    print("*************************",subject,"Attendance:","" + str(percentage) + "%","*************************")
    print(">>>   {status}  <<<")

def calculate_sgpa():
    print("**********************3. SGPA ESTIMATOR **********************")
    num_subjects = int(input("how many subjects are you taking? "))

    total_credits = 0
    total_points = 0

    for i in range(num_subjects):
        print("Subject " + str(i + 1) + ":")
        credits = int(input("Enter credits for this subject (e.g., 3, 4): "))
        grade = input("Enter expected grade (S, A, B, C, D, F): ")

        if grade == 'S' or grade == 's':
            points = 10
        elif grade == 'A' or grade == 'a':
            points = 9
        elif grade == 'B' or grade == 'b':
            points = 8
        elif grade == 'C' or grade == 'c':
            points = 7
        elif grade == 'D' or grade == 'd':
            points = 6
        else:
            points = 0

        total_credits = total_credits + credits
        total_points = total_points + (points * credits)

    if total_credits > 0:
        sgpa = total_points / total_credits
        print(">>> Your Estimated SGPA is: " + str(sgpa) + " <<<")
    else:
        print(">>> No credits entered. <<<")

def study_priority_finder():
    """ Function 4:  Finds the weakest subject without using built-in min() functions."""
    print("**********************4. STUDY PRIORITY FINDER **********************")
    print("Enter marks for 3 subjects to see what needs the most focus.")

    sub1 = input("Enter first subject name: ")
    marks1 = float(input("Enter marks for " + sub1 + ": "))

    sub2 = input("Enter second subject name: ")
    marks2 = float(input("Enter marks for " + sub2 + ": "))

    sub3 = input("enter third subject name: ")
    marks3 = float(input("Enter marks for " + sub3 + ": "))

    lowest_subject =sub1
    lowest_mark = marks1

    if marks2 <lowest_mark:
        lowest_subject = sub2
        lowest_mark = marks2

    if marks3 < lowest_mark:
        lowest_subject = sub3
        lowest_mark =marks3

    print(">>> Focus Warning: Spend your weekend studying " + lowest_subject + " (Lowest Mark: " + str(lowest_mark) + ") <<<")

def main():
    while True:
        print("\n=====Academic Helper Main Menu ====")
        print("1.Calculate Marks and Grades")
        print("2.Calculate Attendance & Bunk Status")
        print("3.SGPA Estimator")
        print("4. study Priority Finder")
        print("5. exit Program")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            calculate_marks_and_grades()
        elif choice == '2':
            calculate_only_attendance()
        elif choice == '3':
            calculate_sgpa()
        elif choice == '4':
            study_priority_finder()
        elif choice == '5':
            print("Exiting program. Good luck with your studies!")
            break
        else:
            print("invalid input. please type a number between 1 and 5.")

main()
