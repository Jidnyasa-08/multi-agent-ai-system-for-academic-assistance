def get_syllabus_answer(question, pdf_text):

    question = question.lower()

    keywords = [
        "syllabus",
        "objective",
        "objectives",
        "outcome",
        "outcomes",
        "module",
        "modules",
        "unit",
        "assessment",
        "reference",
        "book",
        "books",
        "artificial intelligence"
    ]

    for keyword in keywords:
        if keyword in question:
            return pdf_text

    return None