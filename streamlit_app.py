from __future__ import annotations

import json
import random
import uuid
from datetime import date, datetime
from pathlib import Path

import streamlit as st

from glossary_topics import (
    GLOSSARY_TOPICS,
    CATEGORY_ORDER,
    topics_by_category,
    total_study_minutes,
    source_count,
)
from quiz_bank_glossary import all_topics, get_master_test, get_topic_quiz, total_question_count
from state_nav import PRETRIP_WORKFLOW, NATIONAL_HAZARD_PATTERNS, get_state_list, get_state_info

APP_DIR = Path(__file__).resolve().parent
STYLES_PATH = APP_DIR / "styles" / "cdl_pro.css"
HIGHLIGHT_DIR = APP_DIR / "user_data" / "highlights"
HIGHLIGHT_DIR.mkdir(parents=True, exist_ok=True)

st.set_page_config(page_title="CDL Glossary Pro", page_icon="🛣️", layout="wide")

if STYLES_PATH.exists():
    st.markdown(f"<style>{STYLES_PATH.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
else:
    st.warning("CSS file missing. Put cdl_pro.css inside the styles folder.")

if "session_uid" not in st.session_state:
    st.session_state.session_uid = uuid.uuid4().hex[:12]
if "current_quiz_key" not in st.session_state:
    st.session_state.current_quiz_key = None
if "current_quiz_questions" not in st.session_state:
    st.session_state.current_quiz_questions = []


def highlight_file() -> Path:
    return HIGHLIGHT_DIR / f"{st.session_state.session_uid}.json"


def load_highlights() -> list[dict]:
    path = highlight_file()
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def save_highlights(items: list[dict]) -> None:
    highlight_file().write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")


def add_highlight(topic_title: str, selected_text: str, note: str) -> bool:
    selected_text = selected_text.strip()
    note = note.strip()
    if not selected_text:
        return False
    items = load_highlights()
    items.append({
        "id": uuid.uuid4().hex[:10],
        "topic": topic_title,
        "text": selected_text,
        "note": note,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    })
    save_highlights(items)
    return True


def delete_highlight(item_id: str) -> None:
    items = [x for x in load_highlights() if x.get("id") != item_id]
    save_highlights(items)


def render_topic(topic: dict) -> None:
    saved_for_topic = [h for h in load_highlights() if h.get("topic") == topic["title"]]
    badge = f"<span class='tag-pill'>{topic['category']}</span>"
    st.markdown(
        f"<div class='topic-head'><h2>{topic['title']}</h2>{badge}<span class='minute-pill'>~{topic.get('minutes', 0)} min</span></div>",
        unsafe_allow_html=True,
    )
    st.markdown(f"<div class='definition-card'><b>Clean definition:</b><br>{topic['definition']}</div>", unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, .9])
    with c1:
        st.markdown("#### Must know")
        for item in topic.get("must_know", []):
            st.markdown(f"<div class='fact-row'>✓ {item}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='pro-tip'><b>Pro tip:</b> {topic.get('pro_tip', '')}</div>", unsafe_allow_html=True)
        st.caption(f"Duplicate alignment: {topic.get('duplicate_notes', 'Merged overlapping manual content into one clean topic.')}")
    with c2:
        st.markdown("#### Sources combined")
        for src in topic.get("sources", []):
            st.markdown(f"<div class='source-pill'>{src}</div>", unsafe_allow_html=True)
        st.markdown("#### Highlight this topic")
        with st.form(f"highlight_{topic['id']}"):
            selected = st.text_area("Paste the favorite part you want to highlight", height=120, placeholder="Copy/paste the sentence, rule, or checklist item here...")
            note = st.text_input("Optional note", placeholder="Why this matters to me...")
            submitted = st.form_submit_button("Save Highlight")
        if submitted:
            if add_highlight(topic["title"], selected, note):
                st.success("Highlight saved to this Streamlit session JSON.")
            else:
                st.error("Paste text first, then save the highlight.")

    if saved_for_topic:
        st.markdown("#### Your saved highlights for this topic")
        for h in saved_for_topic:
            st.markdown(f"<div class='highlight-card'><mark>{h['text']}</mark><br><small>{h.get('note','')}</small><br><em>{h['created_at']}</em></div>", unsafe_allow_html=True)
            if st.button("Delete", key=f"del_{h['id']}"):
                delete_highlight(h["id"])
                st.rerun()


st.markdown(f"""
<div class="hero">
  <div>
    <p class="eyebrow">NYC CDL GLOSSARY PRO</p>
    <h1>Glossary-First CDL Study Center</h1>
    <p>Instead of a long curriculum list, this app breaks the CDL knowledge into glossary topics. Duplicate handbook sections are merged into one clean source of truth, with matching quizzes, sources, navigation tools, and session-only JSON highlights.</p>
  </div>
  <div class="hero-card">
    <span>Study Date</span>
    <strong>{date.today().strftime('%b %d, %Y')}</strong>
    <small>Session: {st.session_state.session_uid}</small>
  </div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "CDL Pro Menu",
    ["Dashboard", "Glossary Topics", "Practice Tests", "My Highlights", "Navigation Center", "Pre-Trip Planner", "Readiness Checklist", "Official Sources"],
)
st.sidebar.caption("Highlights are unique to this browser Streamlit session and saved in user_data/highlights as JSON.")

if page == "Dashboard":
    cards = [
        (str(len(GLOSSARY_TOPICS)), "Glossary topics"),
        (str(total_question_count()), "Quiz questions"),
        (str(source_count()), "Source groups merged"),
        (str(total_study_minutes()), "Study minutes"),
    ]
    cols = st.columns(4)
    for col, (num, label) in zip(cols, cards):
        col.markdown(f"<div class='metric-card'><h2>{num}</h2><p>{label}</p></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-eyebrow">How this is organized</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="study-card">
      <p><b>Glossary-first:</b> each CDL topic is a focused study card with the definition, must-know rules, source alignment, duplicate-combine notes, and a pro-driver takeaway.</p>
      <p><b>Quiz matched:</b> every glossary topic has its own quiz category, plus a master test that mixes everything.</p>
      <p><b>Highlight system:</b> paste any favorite sentence/rule into the highlight box and it saves to your session JSON, so each user/browser session gets its own saved highlights.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Glossary Topics":
    st.markdown("## Glossary Topics")
    query = st.text_input("Search topics", placeholder="air brakes, hazmat, cargo, low bridges...")
    grouped = topics_by_category()
    for category in CATEGORY_ORDER:
        topics = grouped.get(category, [])
        if query:
            q = query.lower()
            topics = [t for t in topics if q in t["title"].lower() or q in t["definition"].lower() or any(q in x.lower() for x in t.get("must_know", []))]
        if not topics:
            continue
        st.markdown(f'<div class="section-eyebrow">{category}</div>', unsafe_allow_html=True)
        for topic in topics:
            with st.expander(topic["title"], expanded=False):
                render_topic(topic)

elif page == "Practice Tests":
    st.markdown("## Practice Tests")
    mode = st.radio("Choose test type", ["Master Test", "Per-Topic Quiz"], horizontal=True)
    if mode == "Master Test":
        quiz_key = "master"
        if st.button("Shuffle & Start Master Test", type="primary") or st.session_state.current_quiz_key != quiz_key:
            questions = get_master_test()
            random.shuffle(questions)
            st.session_state.current_quiz_key = quiz_key
            st.session_state.current_quiz_questions = questions
    else:
        topic_title = st.selectbox("Pick a glossary topic", all_topics())
        quiz_key = f"topic::{topic_title}"
        if st.session_state.current_quiz_key != quiz_key:
            st.session_state.current_quiz_key = quiz_key
            st.session_state.current_quiz_questions = get_topic_quiz(topic_title)
    questions = st.session_state.current_quiz_questions
    if questions:
        answers = []
        with st.form(f"quiz_form_{st.session_state.current_quiz_key}"):
            for i, item in enumerate(questions):
                st.markdown(f"**Q{i+1}. [{item.get('topic','')}]** {item['q']}")
                choice = st.radio("choices", item["choices"], key=f"q_{st.session_state.current_quiz_key}_{i}", label_visibility="collapsed")
                answers.append(item["choices"].index(choice))
            submitted = st.form_submit_button("Submit Test")
        if submitted:
            score = sum(1 for i, item in enumerate(questions) if answers[i] == item["a"])
            pct = round(score / len(questions) * 100)
            st.markdown(f"<div class='score-box'><h2>{score}/{len(questions)} — {pct}%</h2></div>", unsafe_allow_html=True)
            for i, item in enumerate(questions):
                ok = answers[i] == item["a"]
                st.markdown(f"**{'Correct' if ok else 'Missed'} — Q{i+1}.** {item['q']}")
                st.caption(f"Correct answer: {item['choices'][item['a']]} — {item.get('explain','')}")

elif page == "My Highlights":
    st.markdown("## My Highlights")
    st.caption(f"JSON file: {highlight_file().name}")
    items = load_highlights()
    if not items:
        st.info("No highlights saved yet. Open a glossary topic, paste your favorite part, and save it.")
    else:
        for h in items:
            st.markdown(f"<div class='highlight-card'><b>{h['topic']}</b><br><mark>{h['text']}</mark><br><small>{h.get('note','')}</small><br><em>{h['created_at']}</em></div>", unsafe_allow_html=True)
            if st.button("Delete highlight", key=f"del_all_{h['id']}"):
                delete_highlight(h["id"])
                st.rerun()
        st.download_button("Download my highlights JSON", data=json.dumps(items, indent=2, ensure_ascii=False), file_name=f"cdl_highlights_{st.session_state.session_uid}.json", mime="application/json")

elif page == "Navigation Center":
    st.markdown("## 50-State Truck Navigation & Reference Center")
    tab1, tab2 = st.tabs(["State-by-State Reference", "National Hazard Patterns"])
    with tab1:
        search = st.text_input("Filter states")
        for s in [x for x in get_state_list() if not search or search.lower() in x.lower()]:
            info = get_state_info(s)
            st.markdown(f"<div class='state-card'><div class='state-name'>{s}</div><div class='state-note'>{info.get('notes','')}</div></div>", unsafe_allow_html=True)
            st.markdown(f"[Official DOT site]({info.get('dot_url','#')}) · [Permits / oversize-overweight]({info.get('permit_url','#')})")
    with tab2:
        for hz in NATIONAL_HAZARD_PATTERNS:
            st.markdown(f"<div class='hazard-card'><div class='hazard-region'>{hz['region']}</div><div class='hazard-pattern'>{hz['pattern']}</div></div>", unsafe_allow_html=True)

elif page == "Pre-Trip Planner":
    st.markdown("## Pre-Trip Route Planning Workflow")
    for step in PRETRIP_WORKFLOW:
        st.markdown(f"<div class='step-card'><div class='step-num'>{step['step']}</div><div><div class='step-title'>{step['title']}</div><div class='step-detail'>{step['detail']}</div></div></div>", unsafe_allow_html=True)
        st.checkbox(f"Complete: {step['title']}", key=f"pretrip_{step['step']}")

elif page == "Readiness Checklist":
    st.markdown("## CDL Readiness Checklist")
    items = [
        "I know whether I need Class A, B, or C.",
        "I understand ELDT and verified my provider if needed.",
        "I can explain air brake checks out loud.",
        "I can complete a full pre-trip inspection sequence.",
        "I can plan a legal truck route and avoid parkways/low bridges.",
        "I scored 90%+ on the master test.",
    ]
    checked = sum(1 for item in items if st.checkbox(item))
    st.progress(checked / len(items))
    st.caption(f"{checked} of {len(items)} complete")

elif page == "Official Sources":
    st.markdown("## Official Sources")
    resources = [
        ("NY DMV — CDL Manual", "https://dmv.ny.gov/driver-license/commercial-drivers/new-york-state-commercial-drivers-manual"),
        ("NY DMV — CDL License Steps", "https://dmv.ny.gov/driver-license/commercial-drivers/get-a-commercial-driver-license-cdl"),
        ("FMCSA — ELDT Overview", "https://www.fmcsa.dot.gov/registration/commercial-drivers-license/entry-level-driver-training-eldt"),
        ("FMCSA — Training Provider Registry", "https://tpr.fmcsa.dot.gov/"),
        ("FMCSA — Hours of Service", "https://www.fmcsa.dot.gov/regulations/hours-service"),
        ("TSA — Hazmat Endorsement", "https://www.tsa.gov/for-industry/hazmat-endorsement"),
        ("NYC DOT — Truck Routing", "https://www.nyc.gov/html/dot/html/motorist/truckrouting.shtml"),
    ]
    for name, url in resources:
        st.markdown(f"- [{name}]({url})")
