"""quiz_bank_glossary.py — quizzes generated around each glossary topic."""
from __future__ import annotations

from glossary_topics import GLOSSARY_TOPICS


def _topic_questions(topic: dict) -> list[dict]:
    title = topic["title"]
    must = topic.get("must_know", [])
    definition = topic.get("definition", "")
    pro_tip = topic.get("pro_tip", "")
    questions = []

    if definition:
        questions.append({
            "topic": title,
            "q": f"What is the main idea of {title}?",
            "choices": [definition, "A passenger-car routing shortcut.", "A rule that applies only after a crash.", "A paperwork item that drivers can ignore."],
            "a": 0,
            "explain": definition,
        })

    if must:
        questions.append({
            "topic": title,
            "q": f"Which statement is correct for {title}?",
            "choices": [must[0], "The driver has no responsibility after dispatch assigns the trip.", "Posted signs can be ignored when an app disagrees.", "Commercial driving rules only matter during the road test."],
            "a": 0,
            "explain": must[0],
        })

    if len(must) > 1:
        questions.append({
            "topic": title,
            "q": f"What should you remember about {title}?",
            "choices": ["Only speed matters.", must[1], "The rule applies only outside New York.", "It is optional unless an officer asks."],
            "a": 1,
            "explain": must[1],
        })

    if pro_tip:
        questions.append({
            "topic": title,
            "q": f"What is the pro-driver takeaway for {title}?",
            "choices": ["Guess when unsure.", "Rely only on memory.", pro_tip, "Skip the check to save time."],
            "a": 2,
            "explain": pro_tip,
        })

    return questions


def all_topics() -> list[str]:
    return [t["title"] for t in GLOSSARY_TOPICS]


def get_topic_quiz(topic_title: str) -> list[dict]:
    for topic in GLOSSARY_TOPICS:
        if topic["title"] == topic_title:
            return _topic_questions(topic)
    return []


def get_master_test() -> list[dict]:
    combined = []
    for topic in GLOSSARY_TOPICS:
        combined.extend(_topic_questions(topic))
    return combined


def total_question_count() -> int:
    return len(get_master_test())
