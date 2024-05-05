
# function to add new appliacnt
def add_applicant(applicants):
    # ask user for appliaction number, name, gpa, sat score and extracurriculars
    app_number = input("Enter application number: ")
    name = input("Enter applicant name: ")
    gpa = float(input("Enter GPA: "))
    sat_score = int(input("Enter SAT score: "))
    extracurriculars = input("Enter extracurricular activities (comma-separated): ").split(',')
    # store data into dictionary and pass value to key 
    applicant = {
        "app_number": app_number,
        "name": name,
        "gpa": gpa,
        "sat_score": sat_score,
        "extracurriculars": extracurriculars
    }
    applicants.append(applicant)
    print("Applicant added successfully!")
    
# function to analyze applicant dtat
def analyze_applicant_data(applicants, gpa_threshold, sat_threshold, required_activity):
    # create empty list to append applicent into it after looping through applicants
    qualified_candidates = []
    for applicant in applicants:
        if applicant["gpa"] >= gpa_threshold and applicant["sat_score"] >= sat_threshold and required_activity in applicant["extracurriculars"]:
            qualified_candidates.append(applicant)
    return qualified_candidates

# function to generate admissions decision
def generate_admissions_decision(qualified_candidates):
    # start with empty dictionary
    admissions_decision = {}
    # loop through qualified_candidates 
    for applicant in qualified_candidates:
        # check if sat score >= 1400 and gpa >= 3.5 
        if applicant["sat_score"] >= 1400 and applicant["gpa"] >= 3.5:
            # if condition achived set name == "Accepted"
            admissions_decision[applicant["name"]] = "Accepted"
            # And if sat score >= 1300 and gpa >= 3.0 set name == "Waitlisted"
        elif applicant["sat_score"] >= 1300 and applicant["gpa"] >= 3.0:
            admissions_decision[applicant["name"]] = "Waitlisted"
        else:
            # if condtions above not achived set name = "Rejected"
            admissions_decision[applicant["name"]] = "Rejected"
    return admissions_decision

# function to generate admissions report
def generate_admissions_report(admissions_decision):
    print("Admissions Report:")
    # loop through nam admissions_decision and print name and value 
    for name, decision in admissions_decision.items():
        print(f"{name}: {decision}")
    print("Summary:")
    # use sum() to count accepted, waitlisted and rejected applicant that returned form loop into admissions_decision if condtion achived 
    accepted_count = sum(1 for decision in admissions_decision.values() if decision == "Accepted")
    waitlisted_count = sum(1 for decision in admissions_decision.values() if decision == "Waitlisted")
    rejected_count = sum(1 for decision in admissions_decision.values() if decision == "Rejected")
    print(f"Accepted: {accepted_count}")
    print(f"Waitlisted: {waitlisted_count}")
    print(f"Rejected: {rejected_count}")
 
    
def main():
    applicants = []
    # main points of app 
    while True: # while True print main system functions 
        print("\nAdmissions Management System")
        print("1. Add Applicant")
        print("2. Analyze Applicant Data")
        print("3. Generate Admissions Decision")
        print("4. Generate Admissions Report")
        print("5. Exit")

        # ask user for choice from main functions of system
        choice = input("Enter your choice: ")

        if choice == '1':
            add_applicant(applicants)
        elif choice == '2':
            gpa_threshold = float(input("Enter GPA threshold: "))
            sat_threshold = int(input("Enter SAT score threshold: "))
            required_activity = input("Enter required extracurricular activity: ")
            qualified_candidates = analyze_applicant_data(applicants, gpa_threshold, sat_threshold, required_activity)
            print(f"{len(qualified_candidates)} qualified candidates found.")
        elif choice == '3':
            qualified_candidates = analyze_applicant_data(applicants, 3.0, 1200, "Leadership")
            admissions_decision = generate_admissions_decision(qualified_candidates)
            print("Admissions decisions generated.")
        elif choice == '4':
            generate_admissions_report(admissions_decision)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()    