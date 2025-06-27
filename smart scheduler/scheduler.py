# scheduler.py

exam_schedule = []

def add_exam():
    print("\n--- Add New Exam ---")
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter exam room: ")
    exam = {
        "name": name,
        "date": date,
        "time": time,
        "room": room
    }
    exam_schedule.append(exam)
    print("✅ Exam added successfully!")

def view_exams():
    print("\n--- All Scheduled Exams ---")
    if not exam_schedule:
        print("No exams scheduled yet.")
    else:
        for idx, exam in enumerate(exam_schedule, start=1):
            print(f"{idx}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")

def edit_exam():
    print("\n--- Edit Exam ---")
    view_exams()
    if not exam_schedule:
        return
    try:
        index = int(input("Enter exam number to edit: ")) - 1
        if 0 <= index < len(exam_schedule):
            print("Leave blank to keep current value.")
            name = input(f"New name ({exam_schedule[index]['name']}): ") or exam_schedule[index]['name']
            date = input(f"New date ({exam_schedule[index]['date']}): ") or exam_schedule[index]['date']
            time = input(f"New time ({exam_schedule[index]['time']}): ") or exam_schedule[index]['time']
            room = input(f"New room ({exam_schedule[index]['room']}): ") or exam_schedule[index]['room']
            exam_schedule[index].update({
                "name": name,
                "date": date,
                "time": time,
                "room": room
            })
            print("✅ Exam updated successfully!")
        else:
            print("❌ Invalid exam number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_exam():
    print("\n--- Delete Exam ---")
    view_exams()
    if not exam_schedule:
        return
    try:
        index = int(input("Enter exam number to delete: ")) - 1
        if 0 <= index < len(exam_schedule):
            removed = exam_schedule.pop(index)
            print(f"🗑️ Exam '{removed['name']}' deleted successfully!")
        else:
            print("❌ Invalid exam number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main_menu():
    while True:
        print("\n===== SMART SCHEDULER MENU =====")
        print("1. Add New Exam")
        print("2. View All Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("👋 Exiting Smart Scheduler. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
