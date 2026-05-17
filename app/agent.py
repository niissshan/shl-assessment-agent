from retriever import search_assessments


def chat_with_agent(messages):

    latest_user_message = messages[-1]["content"]

    retrieved_docs = search_assessments(latest_user_message)

    recommendations = []

    for item in retrieved_docs:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": "Technical"
        })

    reply = "Recommended SHL assessments for your hiring query."

    return {
        "reply": reply,
        "recommendations": recommendations[:5],
        "end_of_conversation": False
    }