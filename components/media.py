import base64
from pathlib import Path

import streamlit as st

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


def show_image(filename, caption=None, width=None):
    """Display an image from assets/images/."""
    path = ASSETS_DIR / "images" / filename
    if not path.exists():
        st.warning(f"Image not found: {filename}")
        return
    kwargs = {}
    if caption:
        kwargs["caption"] = caption
    if width:
        kwargs["width"] = width
    st.image(str(path), **kwargs)


def show_video(filename):
    """Display a video from assets/videos/. Show info message if missing."""
    path = ASSETS_DIR / "videos" / filename
    if not path.exists():
        st.info(f"Video file not found: {filename}")
        return
    st.video(str(path))


def image_to_base64(filename):
    """Convert an image from assets/images/ to a base64 data-URI string."""
    path = ASSETS_DIR / "images" / filename
    if not path.exists():
        return ""
    data = path.read_bytes()
    encoded = base64.b64encode(data).decode()
    suffix = path.suffix.lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "svg": "image/svg+xml", "gif": "image/gif"}.get(suffix, "image/png")
    return f"data:{mime};base64,{encoded}"


def logo_header():
    """Render K-forma logo on the left and LBPA text on the right."""
    col_logo, col_spacer, col_text = st.columns([1, 0.3, 2])

    with col_logo:
        logo_path = ASSETS_DIR / "images" / "kforma_logo.png"
        if logo_path.exists():
            st.image(str(logo_path), width=180)

    with col_text:
        st.markdown(
            """
            <div style="display:flex; align-items:center; height:100%;">
                <div>
                    <span style="font-size:1.4rem; font-weight:600; color:#00BCD4;">
                        LBPA 2026
                    </span><br>
                    <span style="font-size:0.95rem; color:#b0b8c8;">
                        AI un Python Būvkonstrukciju Projektēšanā
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
