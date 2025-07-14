import streamlit as st

from src.config import config
from src.routes import banner

# Set page layout
st.set_page_config(layout=config.page_layout)

# Initialise session states
if "runtime" not in st.session_state:
    with open("src/resources/session_states.txt", "r") as file_states:
        states = [
            tuple(line.strip().split("=="))
            for line in file_states.readlines()
        ]
    for state in states:
        st.session_state[state[0]] = state[1]

# Initialise page state and pages
st.session_state["page"] = "Welcome"
with open("src/resources/pages.txt", "r") as file_pages:
    pages = {
        page_parts[0]: {
            "path": f"src/components/{page_parts[0]}.py",
            "title": page_parts[1],
            "icon": page_parts[2]
        }
        for page in file_pages.readlines()
        if (page_parts := page.strip().split(","))
    }

# Initialise page navigation
page_nav = {
    "Navigation": [
        st.Page(
            page["path"],
            title=page["title"],
            icon=page["icon"]
        )
        for key, page in pages.items()
    ]
}

# Runtime
banner.banner(pages)
runtime = st.navigation(
    page_nav,
    position=config.nav_bar_pos,
    expanded=True
)
runtime.run()