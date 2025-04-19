
import streamlit as st

# Page config
st.set_page_config(page_title="Futures Trade Calculator", layout="wide")

# Initialize theme state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Toggle switch
dark_mode = st.toggle("Dark Mode", value=st.session_state.dark_mode)

# Update session state
st.session_state.dark_mode = dark_mode

# Apply the theme
if dark_mode:
    bg_color = "#0f172a"
    card_bg = "#1e293b"
    text_color = "#f1f5f9"
    accent_color = "#22d3ee"
else:
    bg_color = "#f5f7fa"
    card_bg = "#ffffff"
    text_color = "#1f2937"
    accent_color = "#ff9900"

# Custom styles
st.markdown(f"""
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: {bg_color};
            color: {text_color};
        }}
        .main {{
            padding: 2rem;
            background-color: {card_bg};
            border-radius: 12px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
        }}
        .stButton>button {{
            background-color: {accent_color};
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.5rem 1.5rem;
        }}
        .metric-box {{
            background-color: {card_bg};
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            border: 1px solid #334155;
        }}
        .stMarkdown h2 {{
            color: {text_color};
        }}
        .header-text {{
            font-size: 32px;
            font-weight: 700;
            color: {text_color};
            margin-bottom: 1rem;
        }}
        .subheader-text {{
            font-size: 20px;
            font-weight: 500;
            color: {text_color};
            margin-bottom: 2rem;
        }}
    </style>
""", unsafe_allow_html=True)

def metric(label, value):
    st.markdown(f"<div class='metric-box'>{label}: <span style='color:{accent_color}'>{value}</span></div>", unsafe_allow_html=True)

def calculate_profit_and_roi(entry_price, leverage, margin, tp_value):
    position_size = margin * leverage
    quantity = position_size / entry_price
    tp_price = tp_value / quantity
    profit = tp_value - position_size
    roi = (profit / margin) * 100
    profit_percent = (profit / position_size) * 100
    return position_size, quantity, tp_price, profit, roi, profit_percent

def calculate_tp_value(entry_price, leverage, margin, target_profit):
    position_size = margin * leverage
    quantity = position_size / entry_price
    tp_price = entry_price + (target_profit / quantity)
    tp_value = tp_price * quantity
    roi = (target_profit / margin) * 100
    return position_size, quantity, tp_price, tp_value, roi

st.markdown("<div class='header-text'>Futures Trade Calculator</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader-text'>Calculate profit, ROI, and ideal TP Value like a pro trader.</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Trade Profit & ROI Calculator")
    trading_pair1 = st.text_input("Trading Pair", "LINK/USDT")
    entry_price1 = st.number_input("Entry Price ($)", value=12.650)
    leverage1 = st.number_input("Leverage (x)", value=30)
    margin1 = st.number_input("Margin Used ($)", value=364.62)
    tp_value1 = st.number_input("Take Profit Value ($)", value=11139.980)
    margin_mode1 = st.selectbox("Margin Mode", ["Cross", "Isolated"])

    if st.button("Calculate ROI", key="roi"):
        pos_size, qty, tp_price, profit, roi, profit_pct = calculate_profit_and_roi(
            entry_price1, leverage1, margin1, tp_value1
        )
        metric("Total Position Size", f"{pos_size:,.2f} USDT")
        metric("Take Profit Price", f"{tp_price:,.3f} USDT")
        metric("Quantity", f"{qty:,.2f}")
        metric("Estimated Profit", f"${profit:,.2f}")
        metric("ROI (on Margin)", f"{roi:.2f}%")
        metric("Profit % on Position", f"{profit_pct:.2f}%")
        if profit >= 400:
            st.success("Profit is above $400 threshold!")

with col2:
    st.subheader("Trade TP Value Calculator")
    trading_pair2 = st.text_input("Trading Pair (for Storage)", "LINK/USDT")
    margin2 = st.number_input("Margin (USDT)", value=364.62)
    margin_mode2 = st.selectbox("Margin Mode", ["Isolated", "Cross"], key="mode2")
    leverage2 = st.slider("Leverage", 10, 150, 30)
    entry_price2 = st.number_input("Entry Price ($)", value=12.020)
    target_profit = st.number_input("Desired Profit ($)", value=400.0)

    if st.button("Calculate TP", key="tp"):
        pos_size2, qty2, tp_price2, tp_value2, roi2 = calculate_tp_value(
            entry_price2, leverage2, margin2, target_profit
        )
        metric("Position Size", f"{pos_size2:,.2f} USDT")
        metric("Quantity", f"{qty2:,.2f}")
        metric("TP Price", f"{tp_price2:.5f}")
        metric("Estimated Profit", f"${target_profit:,.2f}")
        metric("ROI (on Margin)", f"{roi2:.2f}%")
        metric("Take Profit Value", f"${tp_value2:,.3f}")
