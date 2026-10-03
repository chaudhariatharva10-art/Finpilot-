"""Main Streamlit entry point for FinPilot."""

import streamlit as st


def main() -> None:
    """Render the initial FinPilot landing page."""
    st.title("FinPilot")
    st.write("")
    st.subheader("Personal Financial Health & Planning")


if __name__ == "__main__":
    main()
