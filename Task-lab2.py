#! /usr/bin/python3
import json
import re1

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"

def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def is_valid_phone(phone):
    return re.match(r"^01[0-2,5]{1}[0-9]{8}$", phone)

def register():
    users = load_data(USERS_FILE)
    email = input("Enter email: ")
    if not is_valid_email(email):
        print("Invalid email format!")
        return
    password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match!")
        return
    phone = input("Enter phone number: ")
    if not is_valid_phone(phone):
        print("Invalid phone number!")
        return
    for user in users:
        if user['email'] == email:
            print("Email already in use!")
            return
    users.append({"email": email, "password": password, "phone": phone})
    save_data(USERS_FILE, users)
    print("Registration successful!")

def login():
    users = load_data(USERS_FILE)
    email = input("Enter email: ")
    password = input("Enter password: ")
    for user in users:
        if user['email'] == email and user['password'] == password:
            print("Login successful!")
            return email
    print("Invalid email or password!")
    return None

def create_project(user_email):
    projects = load_data(PROJECTS_FILE)
    title = input("Project title: ")
    details = input("Project details: ")
    target = input("Target amount: ")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    projects.append({"title": title, "details": details, "target": target, "start_date": start_date, "end_date": end_date, "owner": user_email})
    save_data(PROJECTS_FILE, projects)
    print("Project created!")

def view_projects():
    projects = load_data(PROJECTS_FILE)
    if not projects:
        print("No projects found!")
        return
    for project in projects:
        print(f"Title: {project['title']}, Target: {project['target']}")

def main():
    while True:
        print("\nCrowdfunding System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n1. Create Project")
                    print("2. View Projects")
                    print("3. Logout")
                    user_choice = input("Choose an option: ")
                    if user_choice == "1":
                        create_project(user)
                    elif user_choice == "2":
                        view_projects()
                    elif user_choice == "3":
                        break
                    else:
                        print("Invalid choice!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
