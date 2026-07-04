def get_faq_answer(question, faq_data):

    question = question.lower()

    for item in faq_data:
        if item["question"].lower() == question:
            return item["answer"]

    return None