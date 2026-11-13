"""Green -> blue palette map (Nov 2026 colour refresh). Applied to pages, generators and scripts.
FONT_LINK / FONT_NAMES swap the old DM Sans / PT Serif / Hanken Grotesk faces for Inter."""
MAP = [
    ("#175233", "#1b315e"), ("#1e6040", "#294b8e"), ("#2d7a4a", "#294b8e"), ("#4a9e6a", "#3f6fc4"),
    ("#a8c89f", "#8fb3ef"), ("#a8ccb4", "#8fb3ef"), ("#e4f2e4", "#eaf1fc"), ("#eaf3ea", "#f0f5fd"),
    ("#f7faf7", "#f5f9ff"), ("#f1f5f1", "#ffffff"), ("#0d2218", "#1b315e"), ("#3d5248", "#4a4f5a"),
    ("#d8ead9", "#e6eefb"), ("#e3ece4", "#eaf1fc"), ("#174d33", "#1b315e"), ("#c8e6c9", "#d6e4fb"),
    ("rgba(168,200,159", "rgba(143,179,239"), ("rgba(216,234,217", "rgba(214,227,248"),
    ("rgba(30,60,40", "rgba(27,49,94"), ("rgba(30,96,64", "rgba(41,75,142"),
    ("rgba(247,250,247", "rgba(245,249,255"), ("rgba(13,34,24", "rgba(27,49,94"),
    ("rgba(90,113,89", "rgba(74,95,140"),
]
def apply(s):
    for a, b in MAP:
        s = s.replace(a, b).replace(a.upper(), b)
    return s

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
