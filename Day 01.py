students = []

while True:
    print("\n" + "=" * 55)
    print("🎓        STUDENT PROFILE GENERATOR")
    print("=" * 55)
    print("1. ➕ Add New Student")
    print("2. 📋 View All Students")
    print("3. 🚪 Exit")
    print("=" * 55)

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\n📝 Enter Student Details")

        name = input("👤 Name        : ")
        age = int(input("🎂 Age         : "))
        roll = input("🆔 Roll No.    : ")
        college = input("🏫 College     : ")
        course = input("📚 Course      : ")
        city = input("🏙️ City        : ")
        percentage = float(input("📊 Percentage  : "))

        student = {
            "Name": name,
            "Age": age,
            "Roll No": roll,
            "College": college,
            "Course": course,
            "City": city,
            "Percentage": percentage
        }

        students.append(student)

        print("\n✅ Student Profile Saved Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("\n❌ No student profiles found.")
        else:
            print("\n" + "=" * 60)
            print("📚 ALL STUDENT PROFILES")
            print("=" * 60)

            for i, student in enumerate(students, start=1):
                print(f"\n🎓 Student {i}")
                print("-" * 40)
                print(f"👤 Name        : {student['Name']}")
                print(f"🎂 Age         : {student['Age']}")
                print(f"🆔 Roll No.    : {student['Roll No']}")
                print(f"🏫 College     : {student['College']}")
                print(f"📚 Course      : {student['Course']}")
                print(f"🏙️ City        : {student['City']}")
                print(f"📊 Percentage  : {student['Percentage']:.2f}%")

    elif choice == "3":
        print("\n👋 Thank you for using Student Profile Generator!")
        break

    else:
        print("\n❌ Invalid choice! Please enter 1, 2, or 3.")