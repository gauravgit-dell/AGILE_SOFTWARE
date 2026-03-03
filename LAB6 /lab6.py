courses = []
enrolled_courses = []

while True:
    print("\n--- Course Enrollment System ---")
    print("1. Add Course")
    print("2. Enroll in Course")
    print("3. Drop Course")
    print("4. View Enrolled Courses")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        course = input("Enter course name: ")
        courses.append(course)
        print("Course added successfully.") #gaurav's code

    elif choice == 2: 
        course = input("Enter course to enroll: ")
        if course in courses:
            enrolled_courses.append(course)
            print("Enrolled in course successfully.")
        else:
            print("Course not found.")

    elif choice == 3:
        course = input("Enter course to drop: ")
        if course in enrolled_courses:
            enrolled_courses.remove(course)
            print("Course dropped successfully.")
        else:
            print("You are not enrolled in this course.")

    elif choice == 4:
        print("Enrolled Courses:", enrolled_courses)

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.") #abhay's code
