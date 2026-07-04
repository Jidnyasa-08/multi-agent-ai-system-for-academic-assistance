def get_course_answer(question, course_data):

    question = question.lower()

    for _, row in course_data.iterrows():

        course_name = str(row["Course_Name"]).lower()

        if course_name in question:

            return (
                f"Course: {row['Course_Name']}\n"
                f"Course ID: {row['Course_ID']}\n"
                f"Department: {row['Department']}\n"
                f"Credits: {row['Credits']}\n"
                f"Faculty: {row['Faculty']}"
            )

    return None