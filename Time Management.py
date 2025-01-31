import random

# Welcome message
print("Welcome To Your Personal Time Management System! 🕒\n")
print("Let's Get Started.\n")

# User details
User = input("Enter Your Name : ")
Age = input("Enter Your Age : ")

print("Hello", User + ",")
print("I Hope You Are Doing Well In Your Life.")
print("We Are A Planner Company,")
print("We Provide You A Plan That Makes Your Life Managed And Easy.")
print(User + ", Can We Provide You A Routine To Make Your Life Easy?")

# Motivational Quotes
quotes = [
    "The secret of your future is hidden in your daily routine.",
    "Your future is created by what you do today, not tomorrow.",
    "Consistency is what transforms average into excellence.",
    "Success is the sum of small efforts, repeated day in and day out.",
    "Be stronger than your excuses."
]

# Daily Routines
Routine1 = ("""We Will Divide Your Routine Into Two Groups :

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Workout
  7:00 - 7:30 = Do Worship
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Take Rest
  6:00 - 7:00 = Go Outside For Walk
  7:00 - 8:00 = Do Study Or Your Work
  8:00 - 9:00 = Dinner Time
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = 5 Liters Of Water Intake
  Task 2 = Minimum 2 Healthy Meals
  Task 3 = Plank Exercise For Minimum 15 Minutes
  Task 4 = Read 10 Pages From Any Book
  Task 5 = Avoid Mobile Phone For Straight 5 Hours
""")

Routine2 = ("""We Will Divide Your Routine Into Two Groups:

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Yoga
  7:00 - 7:30 = Do Worship Or Prayer
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Relax
  6:00 - 7:00 = Go Outside For Walk
  7:00 - 8:00 = Complete Assignments
  8:00 - 9:00 = Dinner Time
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = 6 Liters Of Water Intake
  Task 2 = At Least 1 Fruit And 2 Healthy Meals
  Task 3 = Do 20 Minutes Of Stretching Or Yoga
  Task 4 = Read 15 Pages From Any Book
  Task 5 = Avoid Mobile Phone For Straight 6 Hours
""")

Routine3 = ("""We Will Divide Your Routine Into Two Groups:

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Stretching
  7:00 - 7:30 = Do Worship Or Prayer
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Relax
  6:00 - 7:00 = Read A Book Or Self-Improvement Material
  7:00 - 8:00 = Practice Coding
  8:00 - 9:00 = Dinner Time
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = 30 Minutes Walk
  Task 2 = Homemade Meal Instead Of Outside Food
  Task 3 = Do 20 Minutes Of Stretching Or Yoga
  Task 4 = Meditate For Straight 20 Minutes
  Task 5 = Avoid Mobile Phone For Straight 7 Hours
""")

Routine4 = ("""We Will Divide Your Routine Into Two Groups:

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Yoga
  7:00 - 7:30 = Do Worship Or Prayer
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Relax
  6:00 - 7:00 = Listen To A Podcast Or Ted Talk
  7:00 - 8:00 = Study Time
  8:00 - 9:00 = Dinner
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = Drink Warm Water In The Morning
  Task 2 = No Fried Food For The Whole Day
  Task 3 = Hold A Plank For 2 Minutes (Can Be In Breaks)
  Task 4 = Write A Small Description About Your Day
  Task 5 = Do One Kind Act Like Helping Someone
""")

Routine5 = ("""We Will Divide Your Routine Into Two Groups:

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Yoga
  7:00 - 7:30 = Do Worship Or Prayer
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Relax
  6:00 - 7:00 = Practice Python
  7:00 - 8:00 = Work On Personal Growth
  8:00 - 9:00 = Dinner Time
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = Drink Lemon Water In The Morning
  Task 2 = Have A High Protein Breakfast
  Task 3 = Do 35 Jumping Jacks
  Task 4 = Spend An Hour Without Any Screen
  Task 5 = Sleep At 10:00 PM Sharp
""")

Routine6 = ("""We Will Divide Your Routine Into Two Groups:

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Yoga
  7:00 - 7:30 = Do Worship Or Prayer
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Relax
  6:00 - 7:00 = Any Outside Activity (Cycling, Running)
  7:00 - 8:00 = Revise Notes For Exams
  8:00 - 9:00 = Dinner
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = A Healthy Drink (Juice, Lime Water)
  Task 2 = Try A New Workout Or Stretching Routine
  Task 3 = Clean Your Room
  Task 4 = Watch An Educational Video
  Task 5 = Spend Time With Family
""")

Routine7 = ("""We Will Divide Your Routine Into Two Groups:

First Group:
  6:00 - 6:15 = Wake Up
  6:15 - 6:30 = Meditation
  6:30 - 7:00 = Yoga
  7:00 - 7:30 = Do Worship Or Prayer
  7:30 - 8:00 = Breakfast And Pack Your Lunch
  8:00 - 9:00 = Get Ready For School/College/Job
  9:00 - 5:00 = School, College, Job (Including Lunch)
  5:00 - 6:00 = Relax
  6:00 - 7:00 = Plan Next Week's Goals
  7:00 - 8:00 = Relax And Meditate
  8:00 - 9:00 = Dinner Time
  9:00 - 10:00 = Watch Movie, Social Media, Or Anything To Divert Your Mind
  10:00 - 6:00 = Sleep

Second Group (Tasks That Change Daily):
  Task 1 = 8 Liters Of Water Intake
  Task 2 = No Sugar For A Day
  Task 3 = Go To The Park
  Task 4 = Write Down Your Next Week Goals
  Task 5 = Avoid Mobile Phone For Straight 8 Hours
""")

# Task Completion Tracking
task_status = {
    "Task 1": False,
    "Task 2": False,
    "Task 3": False,
    "Task 4": False,
    "Task 5": False
}

# Weekly Progress
weekly_progress = {
    "Monday": {"completed": 0, "total": 5},
    "Tuesday": {"completed": 0, "total": 5},
    "Wednesday": {"completed": 0, "total": 5},
    "Thursday": {"completed": 0, "total": 5},
    "Friday": {"completed": 0, "total": 5},
    "Saturday": {"completed": 0, "total": 5},
    "Sunday": {"completed": 0, "total": 5}
}

# Habit Tracker
habit_tracker = {
    "Water Intake": 0,
    "Healthy Meals": 0,
    "Exercise": 0,
    "Reading": 0,
    "Screen Time": 0
}

# Daily Reflection Journal
daily_journal = []

# Reminder System
reminders = [
    "Don't forget to drink water! 💧",
    "Take a short break and stretch. 🧘‍♂️",
    "Have you completed your tasks for the day? ✅",
    "Remember to meditate for 10 minutes. 🧘‍♀️",
    "Avoid junk food today! 🥗"
]

# Export Routine to File
def export_routine(day, routine):
    with open(f"{day}_routine.txt", "w", encoding="utf-8") as file:
        file.write(routine)
    print(f"Routine for {day} exported to {day}_routine.txt!")

# Customizable Routine
def edit_routine(day):
    print(f"Editing routine for {day}...")
    new_task = input("Enter a new task: ")
    Routine1 += f"\n  Task 6 = {new_task}"
    print("Task added successfully!")

# View All Routines
def view_all_routines():
    for day in range(1, 32):
        print(f"\nDay {day} Routine:")
        print(Routine1 if day % 7 == 1 else Routine2
              if day % 7 == 2 else Routine3
              if day % 7 == 3 else Routine4
              if day % 7 == 4 else Routine5
              if day % 7 == 5 else Routine6
              if day % 7 == 6 else Routine7)

# Reset Progress
def reset_progress():
    global task_status, weekly_progress, habit_tracker, daily_journal
    task_status = {task: False for task in task_status}
    weekly_progress = {day: {"completed": 0, "total": 5} for day in weekly_progress}
    habit_tracker = {habit: 0 for habit in habit_tracker}
    daily_journal = []
    print("Progress reset successfully!")

# Main Menu
def main_menu():
    while True:
        print("\n📋 Main Menu:")
        print("1. View Today's Routine")
        print("2. View Weekly Progress")
        print("3. Track Habits")
        print("4. Write Daily Reflection")
        print("5. View Motivational Quote")
        print("6. Export Routine to File")
        print("7. View All Routines")
        print("8. Reset Progress")
        print("9. Exit")

        choice = input("\nEnter your choice (1-11): ").strip()

        if choice == "1":
            day = input("Enter the day (e.g., Day 1): ").strip().lower()
            day_number = int(''.join(filter(str.isdigit, day))) if any(char.isdigit() for char in day) else None
            if day_number in range(1, 32):
                print(Routine1 if day_number % 7 == 1 else Routine2
                      if day_number % 7 == 2 else Routine3
                      if day_number % 7 == 3 else Routine4
                      if day_number % 7 == 4 else Routine5
                      if day_number % 7 == 5 else Routine6
                      if day_number % 7 == 6 else Routine7)
            else:
                print("❌ Invalid day! Please enter a valid day between 1 and 31.")
        
        elif choice == "2":
            print("\n📊 Weekly Progress:")
            for day, progress in weekly_progress.items():
                print(f"{day}: {progress['completed']}/{progress['total']} tasks completed")
        
        elif choice == "3":
            print("\n📈 Habit Tracker:")
            for habit, count in habit_tracker.items():
                print(f"{habit}: {count} times")
            habit = input("Enter the habit to update (e.g., Water Intake): ").strip()
            if habit in habit_tracker:
                habit_tracker[habit] += 1
                print(f"{habit} updated! ✅")
            else:
                print("❌ Invalid habit!")
        
        elif choice == "4":
            reflection = input("\n📝 Write your daily reflection: ")
            daily_journal.append(reflection)
            print("Reflection saved! ✅")
        
        elif choice == "5":
            print("\n💬 Motivational Quote of the Day:")
            print(random.choice(quotes))
        
        elif choice == "6":
            day = input("Enter the day to export (e.g., Day 1): ").strip().lower()
            day_number = int(''.join(filter(str.isdigit, day))) if any(char.isdigit() for char in day) else None
            if day_number in range(1, 32):
                export_routine(f"Day {day_number}", Routine1
                               if day_number % 7 == 1 else Routine2
                               if day_number % 7 == 2 else Routine3
                               if day_number % 7 == 3 else Routine4
                               if day_number % 7 == 4 else Routine5
                               if day_number % 7 == 5 else Routine6
                               if day_number % 7 == 6 else Routine7)
            else:
                print("❌ Invalid day! Please enter a valid day between 1 and 31.")

        elif choice == "7":
            view_all_routines()
        
        elif choice == "8":
            reset_progress()
        
        elif choice == "9":
            print("\nThank you for using the Time Management System! Goodbye! 👋")
            break
        
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 11.")

# Run the program
main_menu()
