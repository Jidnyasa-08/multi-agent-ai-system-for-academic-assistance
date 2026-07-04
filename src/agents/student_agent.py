def get_student_answer(question, student_data):

    question = question.lower()

    for _, row in student_data.iterrows():

        student_name = str(row["Name"]).lower()

        if student_name in question:

            return (
                f"Student Name: {row['Name']}\n"
                f"Student ID: {row['Student_ID']}\n"
                f"Department: {row['Department']}\n"
                f"Semester: {row['Semester']}\n"
                f"CGPA: {row['CGPA']}"
            )

    return None