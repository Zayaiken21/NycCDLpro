import streamlit as st
import random
from datetime import date

from curriculum import MODULES, SECTIONS_ORDER, modules_by_section, total_study_minutes
from quiz_bank import all_topics, get_master_test, get_topic_quiz, total_question_count
from state_nav import PRETRIP_WORKFLOW, NATIONAL_HAZARD_PATTERNS, get_state_list, get_state_info

st.set_page_config(page_title="NYC Pro CDL Study & Navigation Bundle", page_icon="🛣️", layout="wide")

try:
    with open("cdl_pro.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("CSS file not found. Make sure cdl_pro.css is in the same folder as this file.")


for key, default in {
    "quiz_answers": {},
    "quiz_submitted": False,
    "current_quiz_key": None,
    "current_quiz_questions": [],
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


st.markdown("""
<div class="hero">
  <div>
    <p class="eyebrow">NYC PRO CDL BUNDLE</p>
    <h1>Pro Truck Driver Study &amp; Navigation Center</h1>
    <p>A full CDL knowledge curriculum built around the New York / NYC driving environment plus a
       50-state trip-planning and navigation reference center. Study it, test yourself on it, and
       use it as a working reference once you're behind the wheel.</p>
  </div>
  <div class="hero-card">
    <span>Study Date</span>
    <strong>{}</strong>
    <small>Built for New York / NYC drivers</small>
  </div>
</div>
""".format(date.today().strftime("%b %d, %Y")), unsafe_allow_html=True)


st.sidebar.title("CDL Pro Menu")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Curriculum", "Practice Tests", "Navigation Center", "Pre-Trip Planner", "Readiness Checklist", "Official Sources"],
)
st.sidebar.markdown("---")
st.sidebar.caption(
    "The Navigation Center is a trip-planning and reference tool — official state truck-route "
    "links, regional hazard patterns, and a pre-trip checklist. It is not a live turn-by-turn GPS."
)


if page == "Dashboard":
    c1, c2, c3, c4 = st.columns(4)
    cards = [
        (str(len(MODULES)), "Curriculum modules"),
        (str(total_question_count()), "Practice questions"),
        (str(len(get_state_list())), "States in nav center"),
        (f"{total_study_minutes()}", "Minutes of core content"),
    ]
    for col, (num, label) in zip([c1, c2, c3, c4], cards):
        col.markdown(f"<div class='metric-card'><h2>{num}</h2><p>{label}</p></div>", unsafe_allow_html=True)

    st.markdown('<div class="section-eyebrow">How to use this bundle</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="study-card">
      <ol>
        <li><b>Start with Curriculum &rarr; "Getting Licensed."</b> Confirm your class and ELDT requirements before spending money on anything.</li>
        <li><b>Work through each section in order</b>, repeating the drill at the end of every module out loud.</li>
        <li><b>Take per-topic quizzes</b> right after finishing the matching module.</li>
        <li><b>Take the Master Test</b> once you've covered everything, and retake it until consistently above 90%.</li>
        <li><b>Use the Navigation Center and Pre-Trip Planner as living tools</b> once you're driving, not just study material.</li>
        <li><b>Run the Readiness Checklist</b> before contacting a CDL school or booking your skills test.</li>
      </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-eyebrow">What this bundle is, and isn\'t</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="study-card">
      <p><b>It is:</b> a deep knowledge curriculum mirroring real CDL manual structure, a large practice
      test bank, and a 50-state trip-planning reference center with official state resources and a
      structured pre-trip workflow.</p>
      <p><b>It isn't:</b> a replacement for behind-the-wheel training, a live turn-by-turn GPS with
      real-time traffic and a licensed bridge-clearance database, or legal/regulatory advice — always
      confirm current rules with your state DMV/DOT and the FMCSA before making licensing decisions.</p>
    </div>
    """, unsafe_allow_html=True)


elif page == "Curriculum":
    st.markdown("## Full CDL Knowledge Curriculum")
    st.caption(f"{len(MODULES)} modules across {len(SECTIONS_ORDER)} sections, organized to mirror real CDL manual structure, with NYC operating knowledge woven in.")

    grouped = modules_by_section()
    for section in SECTIONS_ORDER:
        mods = grouped.get(section, [])
        if not mods:
            continue
        st.markdown(f'<div class="section-eyebrow">{section}</div>', unsafe_allow_html=True)
        for m in mods:
            with st.expander(m["title"], expanded=False):
                st.markdown(
                    f'<span class="exit-badge">EXIT <span class="exit-num">{m["exit"]}</span></span> '
                    f'<span class="tag-pill">{m["tag"]}</span> '
                    f'<span style="color:var(--muted);font-size:.85rem;margin-left:8px;">~{m["minutes"]} min</span>',
                    unsafe_allow_html=True,
                )
                st.markdown(m["content"])
                st.info(f"**Drill:** {m['drill']}")


elif page == "Practice Tests":
    st.markdown("## Practice Tests")
    test_mode = st.radio("Choose a test type", ["Master Test (all topics)", "Per-Topic Quiz"], horizontal=True)

    if test_mode == "Master Test (all topics)":
        quiz_key = "master"
        start_clicked = st.button("Shuffle & Start Master Test", type="primary")
        if start_clicked or st.session_state.current_quiz_key != quiz_key:
            questions = get_master_test()
            random.shuffle(questions)
            st.session_state.current_quiz_questions = questions
            st.session_state.current_quiz_key = quiz_key
            st.session_state.quiz_submitted = False
        questions = st.session_state.current_quiz_questions
    else:
        topic = st.selectbox("Pick a topic", all_topics())
        quiz_key = f"topic::{topic}"
        if st.session_state.current_quiz_key != quiz_key:
            st.session_state.current_quiz_questions = get_topic_quiz(topic)
            st.session_state.current_quiz_key = quiz_key
            st.session_state.quiz_submitted = False
        questions = st.session_state.current_quiz_questions

    if not questions:
        st.info("No questions loaded yet, pick a topic or start the master test above.")
    else:
        st.caption(f"{len(questions)} questions")
        answers = []
        with st.form(f"quiz_form_{st.session_state.current_quiz_key}"):
            for i, item in enumerate(questions):
                st.markdown(f"**Q{i+1}. [{item.get('topic','')}]** {item['q']}")
                choice = st.radio("choices", item["choices"], key=f"q_{st.session_state.current_quiz_key}_{i}",
                                   label_visibility="collapsed")
                answers.append(item["choices"].index(choice))
                st.markdown("")
            submitted = st.form_submit_button("Submit Test")

        if submitted:
            st.session_state.quiz_submitted = True
            score = sum(1 for i, item in enumerate(questions) if answers[i] == item["a"])
            pct = round(score / len(questions) * 100)
            st.markdown(f"<div class='score-box'><h2>{score}/{len(questions)} — {pct}%</h2></div>", unsafe_allow_html=True)

            if pct >= 90:
                st.success("Pro level. Keep repeating until answers feel automatic.")
            elif pct >= 70:
                st.warning("Solid, but review the missed concepts below before moving on.")
            else:
                st.error("Spend more time in the matching Curriculum modules, then retake this quiz.")

            st.markdown('<div class="section-eyebrow">Review</div>', unsafe_allow_html=True)
            for i, item in enumerate(questions):
                correct = item["choices"][item["a"]]
                was_right = answers[i] == item["a"]
                icon = "Correct" if was_right else "Missed"
                st.markdown(f"**{icon} — Q{i+1}.** {item['q']}")
                st.caption(f"Correct answer: **{correct}** — {item.get('explain','')}")


elif page == "Navigation Center":
    st.markdown("## 50-State Truck Navigation & Reference Center")
    st.info(
        "This is a trip-planning reference tool: official state DOT/permit links, known regional hazard "
        "patterns, and the structured pre-trip workflow below. It does not provide live turn-by-turn GPS, "
        "real-time traffic, or a live bridge-clearance database — use it alongside a dedicated truck GPS app."
    )

    nav_tab1, nav_tab2 = st.tabs(["State-by-State Reference", "National Hazard Patterns"])

    with nav_tab1:
        states = get_state_list()
        search = st.text_input("Filter states", placeholder="Type a state name...")
        filtered = [s for s in states if search.lower() in s.lower()] if search else states

        for s in filtered:
            info = get_state_info(s)
            st.markdown(f"""
            <div class="state-card">
              <div class="state-name">{s}</div>
              <div class="state-note">{info.get('notes','')}</div>
            </div>
            """, unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"[Official DOT site]({info.get('dot_url','#')})")
            with c2:
                st.markdown(f"[Permits / oversize-overweight]({info.get('permit_url','#')})")
            st.markdown("")

    with nav_tab2:
        st.markdown("Recurring regional patterns worth knowing before you route through these areas:")
        for hz in NATIONAL_HAZARD_PATTERNS:
            st.markdown(f"""
            <div class="hazard-card">
              <div class="hazard-region">{hz['region']}</div>
              <div class="hazard-pattern">{hz['pattern']}</div>
            </div>
            """, unsafe_allow_html=True)


elif page == "Pre-Trip Planner":
    st.markdown("## Pre-Trip Route Planning Workflow")
    st.caption("Run this checklist before every trip, not just in NYC, for any state you're routing through.")

    for step in PRETRIP_WORKFLOW:
        st.markdown(f"""
        <div class="step-card">
          <div class="step-num">{step['step']}</div>
          <div>
            <div class="step-title">{step['title']}</div>
            <div class="step-detail">{step['detail']}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-eyebrow">Quick interactive run-through</div>', unsafe_allow_html=True)
    st.caption("Check off each step for your current trip — this resets each time you reload the page.")
    for step in PRETRIP_WORKFLOW:
        st.checkbox(f"{step['step']}. {step['title']}", key=f"pretrip_{step['step']}")


elif page == "Readiness Checklist":
    st.markdown("## CDL Readiness Checklist")
    items = [
        "I know whether I need Class A, B, or C.",
        "I confirmed my driving type self-certification (excepted/non-excepted, interstate/intrastate).",
        "I studied the curriculum sections for my class and any endorsements I want.",
        "I confirmed whether ELDT applies to me, and verified my provider is on the FMCSA TPR.",
        "If pursuing Hazmat, I've started the TSA background check process, it has the longest lead time.",
        "I can explain the air brake check sequence out loud, with the reasoning behind each step.",
        "I can perform a full pre-trip inspection flow without notes.",
        "I can explain GOAL and when to use it.",
        "I can plan an NYC truck route legally, including bridge/tunnel/parkway restriction checks.",
        "I understand HOS limits (11-hour, 14-hour, 30-minute break, 60/70-hour).",
        "I scored 90%+ on the Master Test, retaking it until it's consistent.",
        "I understand that a car GPS is not sufficient for truck routing in NYC or anywhere else.",
    ]
    checked = 0
    for item in items:
        if st.checkbox(item):
            checked += 1
    st.progress(checked / len(items))
    st.caption(f"{checked} of {len(items)} complete")
    if checked == len(items):
        st.success("You've covered the full readiness list. Time to book your test with confidence.")


elif page == "Official Sources":
    st.markdown("## Official Sources")
    st.caption("Always confirm current rules directly with these sources, regulations and provider listings change.")

    RESOURCES = [
        ("NY DMV — CDL License Steps", "https://dmv.ny.gov/driver-license/commercial-drivers/get-a-commercial-driver-license-cdl"),
        ("NY DMV — CDL Manual", "https://dmv.ny.gov/driver-license/commercial-drivers/new-york-state-commercial-drivers-manual"),
        ("NY DMV — ELDT", "https://dmv.ny.gov/driver-license/commercial-drivers/entry-level-driver-training"),
        ("FMCSA — ELDT Overview", "https://www.fmcsa.dot.gov/registration/commercial-drivers-license/entry-level-driver-training-eldt"),
        ("FMCSA — Training Provider Registry", "https://tpr.fmcsa.dot.gov/"),
        ("FMCSA — Hours of Service", "https://www.fmcsa.dot.gov/regulations/hours-service"),
        ("TSA — Hazmat Endorsement Threat Assessment", "https://www.tsa.gov/for-industry/hazmat-endorsement"),
        ("NYC DOT — Truck Routing", "https://www.nyc.gov/html/dot/html/motorist/truckrouting.shtml"),
        ("NYC Open Data — Truck Route Map", "https://data.cityofnewyork.us/Transportation/New-York-City-Truck-Routes-Map/wnu3-egq7"),
    ]
    for name, url in RESOURCES:
        st.markdown(f"- [{name}]({url})")

    st.markdown('<div class="section-eyebrow">State DOT Sources</div>', unsafe_allow_html=True)
    st.caption("Every state's official DOT and permit office, also available in the Navigation Center.")
    cols = st.columns(2)
    states = get_state_list()
    half = len(states) // 2 + 1
    for col, chunk in zip(cols, [states[:half], states[half:]]):
        with col:
            for s in chunk:
                info = get_state_info(s)
                st.markdown(f"- **{s}**: [DOT]({info.get('dot_url','#')}) · [Permits]({info.get('permit_url','#')})")
