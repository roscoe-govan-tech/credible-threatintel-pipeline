import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "data/threatintel.db"


# =========================
# LOAD DATA (UPDATED TO INCLUDE TL;DR)
# =========================
def load_data():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query("""
        SELECT 
            source_name,
            category,
            title,
            url,
            published_at,
            collected_at,
            tldr
        FROM raw_items
        ORDER BY collected_at DESC
    """, conn)

    conn.close()

    # Fill missing TL;DR safely
    df["tldr"] = df["tldr"].fillna("No TL;DR available")

    return df


# =========================
# THREAT SCORING ENGINE
# =========================
def score_intel(row):
    score = 0

    if "CISA" in row["source_name"]:
        score += 5

    if "KEV" in row["category"] or "exploit" in row["category"]:
        score += 4

    if "ransomware" in row["title"].lower():
        score += 3

    if "Microsoft" in row["source_name"]:
        score += 2

    return score


def get_color(score):
    if score >= 7:
        return "#ff4d4d"  # high risk (red)
    elif score >= 4:
        return "#ffa500"  # medium risk (orange)
    else:
        return "#4caf50"  # low risk (green)


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Threat Intel Dashboard", layout="wide")

st.title("🛡️ Credible Threat Intelligence Feed")


# =========================
# LOAD DATA
# =========================
df = load_data()

# Apply scoring
df["priority_score"] = df.apply(score_intel, axis=1)


# =========================
# KPI CARDS
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Total Intel Items", len(df))
col2.metric("Sources", df["source_name"].nunique())
col3.metric("Categories", df["category"].nunique())


# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("🎛️ Filters")

selected_sources = st.sidebar.multiselect(
    "Sources",
    options=df["source_name"].unique(),
    default=list(df["source_name"].unique())
)

selected_categories = st.sidebar.multiselect(
    "Categories",
    options=df["category"].unique(),
    default=list(df["category"].unique())
)

min_score = st.sidebar.slider(
    "Minimum Threat Score",
    0, 10, 0
)


# =========================
# FILTER DATA
# =========================
filtered = df[
    (df["source_name"].isin(selected_sources)) &
    (df["category"].isin(selected_categories)) &
    (df["priority_score"] >= min_score)
]


# =========================
# TOP THREATS PANEL
# =========================
st.subheader("🚨 Top Threats Today")

top = filtered.sort_values("priority_score", ascending=False).head(5)

for _, row in top.iterrows():
    st.markdown(f"""
- **[{row['title']}]({row['url']})**  
  Score: `{row['priority_score']}` | Source: `{row['source_name']}`
""")


# =========================
# TABLE VIEW (NOW INCLUDES TL;DR)
# =========================
st.subheader("📊 Raw Intelligence Feed")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)


# =========================
# INTELLIGENCE FEED (SOC CARDS + TL;DR)
# =========================
st.subheader("🔎 Intelligence Feed")

for _, row in filtered.head(15).iterrows():

    color = get_color(row["priority_score"])

    st.markdown(f"""
<div style="
    padding: 12px;
    border-radius: 8px;
    border-left: 6px solid {color};
    background-color: #0e1117;
    margin-bottom: 10px;
">

### 🧠 {row['title']}

**Source:** `{row['source_name']}`  
**Category:** `{row['category']}`  
**Score:** `{row['priority_score']}`  

**TL;DR:** {row['tldr']}

**Published:** `{row['published_at']}`  

🔗 [Open Original Report]({row['url']})

</div>
""", unsafe_allow_html=True)