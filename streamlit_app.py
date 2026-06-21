
import streamlit as st
import json, os, random, uuid, re
from pathlib import Path
from datetime import datetime, timezone

st.set_page_config(page_title="NYC CDL Pro Accessible Manual", page_icon="🛣️", layout="wide")
BASE = Path(__file__).parent
DATA_PATH = BASE / "data" / "cdl_manual_data.json"
USER_DIR = BASE / "user_data"
HIGHLIGHT_DIR = USER_DIR / "highlights"
QUIZ_LOG_DIR = USER_DIR / "quiz_logs"
SETTINGS_DIR = USER_DIR / "settings"
for d in (HIGHLIGHT_DIR, QUIZ_LOG_DIR, SETTINGS_DIR):
    d.mkdir(parents=True, exist_ok=True)

with open(BASE / "styles" / "cdl_pro.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()
items = data["items"]
facts = data["facts"]
questions = data["questions"]

# ───────────────────────── Session / device identity ─────────────────────────
def init_state():
    defaults = {
        "reader_size": 22,
        "session_id": uuid.uuid4().hex[:12],
        "device_id": None,
        "device_name": "My Device",
        "quiz": [],
        "answers": {},
        "quiz_started_at": None,
        "quiz_submitted_at": None,
        "quiz_elapsed_seconds": 0,
        "quiz_topic": "All Topics",
        "highlight_color": "#fff2a8",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# Keep one local device id on the server. In deployed Streamlit this is still server-side JSON,
# but it creates stable, separate logs/highlights for each chosen device profile.
def set_device_profile(name: str):
    safe = re.sub(r"[^a-zA-Z0-9_-]+", "_", (name or "device").strip())[:40] or "device"
    st.session_state.device_name = name.strip() or "My Device"
    st.session_state.device_id = safe.lower()
    save_settings()

def settings_file():
    did = st.session_state.device_id or st.session_state.session_id
    return SETTINGS_DIR / f"settings_{did}.json"

def save_settings():
    payload = {
        "device_id": st.session_state.device_id,
        "device_name": st.session_state.device_name,
        "highlight_color": st.session_state.highlight_color,
        "reader_size": st.session_state.reader_size,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
    }
    settings_file().write_text(json.dumps(payload, indent=2), encoding="utf-8")

def owner_id():
    return st.session_state.device_id or st.session_state.session_id

def hfile():
    return HIGHLIGHT_DIR / f"highlights_{owner_id()}.json"

def quiz_log_file():
    return QUIZ_LOG_DIR / f"quiz_log_{owner_id()}.json"

def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def write_json(path: Path, payload):
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

def load_highlights():
    return load_json(hfile(), [])

def save_highlight(card, text, note=""):
    hs = load_highlights()
    hs.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "session_id": st.session_state.session_id,
        "device_id": owner_id(),
        "device_name": st.session_state.device_name,
        "card_id": card["id"],
        "title": card["title"],
        "topic": card["topic"],
        "source": card["source"],
        "page": card["page"],
        "color": st.session_state.highlight_color,
        "text": text.strip(),
        "note": note.strip(),
    })
    write_json(hfile(), hs)

def clear_highlights():
    write_json(hfile(), [])

def load_quiz_logs():
    return load_json(quiz_log_file(), [])

def save_quiz_log(score, total, pct, topic, elapsed_seconds, review):
    logs = load_quiz_logs()
    logs.append({
        "time_started": st.session_state.quiz_started_at,
        "time_submitted": datetime.now().isoformat(timespec="seconds"),
        "session_id": st.session_state.session_id,
        "device_id": owner_id(),
        "device_name": st.session_state.device_name,
        "topic": topic,
        "score": score,
        "total": total,
        "percent": pct,
        "elapsed_seconds": elapsed_seconds,
        "elapsed_label": format_seconds(elapsed_seconds),
        "review": review,
    })
    write_json(quiz_log_file(), logs)

def format_seconds(seconds):
    seconds = int(seconds or 0)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h {m}m {s}s"
    return f"{m}m {s}s"

def current_elapsed():
    if not st.session_state.quiz_started_at:
        return 0
    try:
        start = datetime.fromisoformat(st.session_state.quiz_started_at)
        return int((datetime.now() - start).total_seconds())
    except Exception:
        return 0

# ───────────────────────── Data helpers ─────────────────────────
def topic_list():
    return sorted(set(i["topic"] for i in items))

def filter_items(topic, search):
    arr = [i for i in items if topic == "All Topics" or i["topic"] == topic]
    if search:
        s = search.lower()
        arr = [i for i in arr if s in i["title"].lower() or s in i["body"].lower() or s in i["topic"].lower()]
    return arr

def all_sources():
    return sorted(set(i["source"] for i in items))

# ───────────────────────── Render helpers ─────────────────────────
def render_card(card):
    st.markdown(f"""
    <div class='reader-card'>
      <span class='topic-chip'>{card['topic']}</span>
      <span class='source-chip'>{card['source']} · page {card['page']}</span>
      <h2>{card['title']}</h2>
      <div class='reader-text'>{card['body']}</div>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("⭐ Highlight a favorite part from this card"):
        st.caption("Copy/paste the exact sentence or paragraph you want to save. It saves only to this device/session JSON file.")
        txt = st.text_area("Text to highlight", key=f"hl_txt_{card['id']}", height=110)
        note = st.text_input("Optional note", key=f"hl_note_{card['id']}")
        st.markdown(f"<div class='highlight-preview' style='background:{st.session_state.highlight_color};'>Preview highlight color</div>", unsafe_allow_html=True)
        if st.button("Save highlight", key=f"save_{card['id']}"):
            if txt.strip():
                save_highlight(card, txt, note)
                st.success("Highlight saved to JSON for this device/session.")
            else:
                st.warning("Paste the text you want to highlight first.")

def render_timer_box():
    elapsed = current_elapsed()
    st.markdown(f"""
    <div class='timer-box'>
      <div class='timer-label'>Quiz Timer</div>
      <div class='timer-time'>{format_seconds(elapsed)}</div>
      <div class='timer-note'>Timer starts when you build a quiz and saves to JSON when you submit.</div>
    </div>
    """, unsafe_allow_html=True)

# ───────────────────────── Header / Sidebar ─────────────────────────
st.markdown("""
<div class='big-hero'>
  <div class='eyebrow'>NYC CDL PRO · ACCESSIBLE MANUAL</div>
  <h1>Complete CDL PDF Study Reader</h1>
  <p>Every extracted CDL manual page is broken into large, clean study cards. Use bigger text, search every topic, save colored highlights to JSON, and take timed quizzes built from the real manual facts, numbers, ages, pressures, distances, and CDL rules.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("CDL Pro")
page = st.sidebar.radio("Open", ["Dashboard", "Accessible Reader", "Facts & Numbers", "Practice Quizzes", "My Highlights", "Quiz History", "Source Coverage"])
st.sidebar.markdown("---")
with st.sidebar.expander("⚙️ Reading + highlight settings", expanded=True):
    name = st.text_input("Device / user log name", value=st.session_state.device_name, help="This name becomes the JSON owner for highlights and quiz logs on this machine/server.")
    if st.button("Use this device name"):
        set_device_profile(name)
        st.success("Device profile saved.")
    st.session_state.reader_size = st.slider("Reader text size", 18, 38, st.session_state.reader_size)
    st.session_state.highlight_color = st.color_picker("Highlight color", st.session_state.highlight_color)
    if st.button("Save reading settings"):
        save_settings()
        st.success("Settings saved.")
    st.markdown(f"<div class='highlight-preview' style='background:{st.session_state.highlight_color};'>Highlight preview</div>", unsafe_allow_html=True)

st.markdown(f"<style>.reader-text{{--reader-size:{st.session_state.reader_size}px;}}</style>", unsafe_allow_html=True)
st.sidebar.caption(f"Session ID: {st.session_state.session_id}")
st.sidebar.caption(f"JSON owner: {owner_id()}")

# ───────────────────────── Pages ─────────────────────────
if page == "Dashboard":
    m = data['meta']
    st.markdown("<div class='metric-grid'>" + "".join([
        f"<div class='metric'><strong>{len(topic_list())}</strong><span>Manual topics</span></div>",
        f"<div class='metric'><strong>{m['unique_cards']}</strong><span>Readable study cards</span></div>",
        f"<div class='metric'><strong>{m['fact_count']}</strong><span>Extracted rule facts</span></div>",
        f"<div class='metric'><strong>{m['question_count']}</strong><span>Practice questions</span></div>",
    ]) + "</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='reader-card'><h2>Built for visual accessibility</h2>
    <div class='reader-text'>The original CDL PDFs are packed into small columns. This app converts the material into large, high-contrast cards with adjustable text size, bigger spacing, search, topic filters, and separate fact/number study mode. Highlights and quiz timing save to JSON so each device profile can keep its own progress.</div></div>
    """, unsafe_allow_html=True)

elif page == "Accessible Reader":
    st.subheader("Accessible Reader")
    c1, c2, c3 = st.columns([2,2,1])
    with c1:
        topic = st.selectbox("Topic", ["All Topics"] + topic_list())
    with c2:
        search = st.text_input("Search manual text", placeholder="air pressure, age, hazmat, 4/32, passengers...")
    with c3:
        limit = st.number_input("Cards", 5, 500, 25)
    arr = filter_items(topic, search)
    st.caption(f"Showing {min(len(arr), limit)} of {len(arr)} matching cards")
    for card in arr[:limit]:
        render_card(card)

elif page == "Facts & Numbers":
    st.subheader("Rules, numbers, ages, pressures, distances, and key facts")
    topic = st.selectbox("Filter topic", ["All Topics"] + topic_list(), key="fact_topic")
    s = st.text_input("Search facts", key="fact_search")
    arr = [f for f in facts if topic == "All Topics" or f['topic'] == topic]
    if s:
        arr = [f for f in arr if s.lower() in f['fact'].lower()]
    st.caption(f"{len(arr)} matching facts")
    for f in arr[:600]:
        st.markdown(f"<div class='fact-box'><b>{f['topic']}</b><br>{f['fact']}<br><span class='small-note'>{f['source']} · page {f['page']}</span></div>", unsafe_allow_html=True)

elif page == "Practice Quizzes":
    st.subheader("Timed Practice Quizzes")
    c1, c2 = st.columns([2,1])
    with c1:
        topic = st.selectbox("Quiz category", ["All Topics"] + topic_list())
    with c2:
        count = st.slider("Questions", 5, 50, 15)

    if st.button("Build new timed quiz", type="primary"):
        pool = [q for q in questions if topic == "All Topics" or q['topic'] == topic]
        random.shuffle(pool)
        st.session_state.quiz = pool[:count]
        st.session_state.answers = {}
        st.session_state.quiz_started_at = datetime.now().isoformat(timespec="seconds")
        st.session_state.quiz_submitted_at = None
        st.session_state.quiz_elapsed_seconds = 0
        st.session_state.quiz_topic = topic
        st.rerun()

    if not st.session_state.quiz:
        st.info("Click Build new timed quiz to start the timer.")
    else:
        render_timer_box()
        st.caption(f"Quiz started: {st.session_state.quiz_started_at} · Topic: {st.session_state.quiz_topic}")
        with st.form("quiz_form"):
            answers = []
            for idx, q in enumerate(st.session_state.quiz):
                st.markdown(f"<div class='quiz-card'><b>Q{idx+1}. {q['topic']}</b><br><br>{q['q']}</div>", unsafe_allow_html=True)
                choice = st.radio("Answer", q['choices'], key=f"qa_{st.session_state.quiz_started_at}_{idx}", label_visibility="collapsed")
                answers.append(q['choices'].index(choice))
            submitted = st.form_submit_button("Submit Quiz + Save Time")

        if submitted:
            elapsed = current_elapsed()
            st.session_state.quiz_elapsed_seconds = elapsed
            score = sum(1 for i, q in enumerate(st.session_state.quiz) if answers[i] == q['a'])
            total = len(st.session_state.quiz)
            pct = round(score / total * 100) if total else 0
            review = []
            for i, q in enumerate(st.session_state.quiz):
                review.append({
                    "question": q['q'],
                    "topic": q['topic'],
                    "selected": q['choices'][answers[i]],
                    "correct": q['choices'][q['a']],
                    "is_correct": answers[i] == q['a'],
                    "manual_fact": q.get('explain', ''),
                    "source": q.get('source', ''),
                    "page": q.get('page', ''),
                })
            save_quiz_log(score, total, pct, st.session_state.quiz_topic, elapsed, review)
            st.success(f"Score: {score}/{total} — {pct}% · Time: {format_seconds(elapsed)} · Saved to JSON")
            for i, q in enumerate(st.session_state.quiz):
                right = answers[i] == q['a']
                cls = 'correct' if right else 'wrong'
                st.markdown(f"<div class='quiz-card {cls}'><b>{'Correct' if right else 'Missed'} — Q{i+1}</b><br>{q['q']}<br><br><b>Your answer:</b> {q['choices'][answers[i]]}<br><b>Correct answer:</b> {q['choices'][q['a']]}<br><b>Manual fact:</b> {q.get('explain','')}<br><span class='small-note'>{q.get('source','')} · page {q.get('page','')}</span></div>", unsafe_allow_html=True)

elif page == "My Highlights":
    st.subheader("My Colored Highlights")
    hs = load_highlights()
    c1, c2 = st.columns(2)
    with c1:
        st.download_button("Download highlights JSON", json.dumps(hs, indent=2), file_name=f"cdl_highlights_{owner_id()}.json", mime="application/json")
    with c2:
        if st.button("Clear this device/session's highlights"):
            clear_highlights(); st.rerun()
    if not hs:
        st.info("No highlights saved yet.")
    for h in reversed(hs):
        color = h.get('color', '#fff2a8')
        st.markdown(f"<div class='highlight-card' style='background:{color};'><b>{h['title']}</b><br><span class='small-note'>{h['topic']} · {h['source']} page {h['page']} · {h['time']}</span><br><br>{h['text']}<br><br><i>{h.get('note','')}</i></div>", unsafe_allow_html=True)

elif page == "Quiz History":
    st.subheader("Quiz History JSON")
    logs = load_quiz_logs()
    st.download_button("Download quiz history JSON", json.dumps(logs, indent=2), file_name=f"cdl_quiz_history_{owner_id()}.json", mime="application/json")
    if not logs:
        st.info("No quiz attempts saved yet.")
    for log in reversed(logs[-50:]):
        st.markdown(f"""
        <div class='quiz-log-card'>
          <b>{log['topic']}</b> — {log['score']}/{log['total']} ({log['percent']}%)<br>
          <span class='small-note'>Time: {log['elapsed_label']} · Started: {log['time_started']} · Saved for {log.get('device_name','device')}</span>
        </div>
        """, unsafe_allow_html=True)

elif page == "Source Coverage":
    st.subheader("Source Coverage")
    st.write("This app includes extracted, readable cards from the New York CDL handbook, hazardous materials manual, and current section PDFs, with duplicate text removed where possible.")
    by = {}
    for i in items:
        by.setdefault(i['source'], 0)
        by[i['source']] += 1
    for k, v in by.items():
        st.markdown(f"- **{k}** — {v} readable cards")
    st.markdown("---")
    st.caption("Use Accessible Reader search when you need exact rules, ages, numbers, pressures, distances, or definitions from the manuals.")
