
import streamlit as st

st.set_page_config(page_title="Futures Trade Calculator", layout="wide")

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

st.title("Futures Trade Calculator")

col1, col2 = st.columns(2)

with col1:
    st.header("Trade Profit & ROI Calculator")
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
        st.markdown(f"**Total Position Size:** {pos_size:,.2f}")
        st.markdown(f"**Take Profit Price:** {tp_price:,.3f} | Quantity: {qty:,.2f}")
        st.markdown(f"**Estimated Profit:** ${profit:,.2f}")
        st.markdown(f"**ROI based on margin:** {roi:.1f}%")
        st.markdown(f"**Profit % on position:** {profit_pct:.2f}%")
        if profit >= 400:
            st.success("Profit is above $400 threshold.")

with col2:
    st.header("Trade TP Value Calculator")
    trading_pair2 = st.text_input("Trading Pair (for storage)", "LINK/USDT")
    margin2 = st.number_input("Margin (USDT)", value=364.62)
    margin_mode2 = st.selectbox("Margin Mode", ["Isolated", "Cross"], key="mode2")
    leverage2 = st.slider("Leverage", 10, 150, 30)
    entry_price2 = st.number_input("Entry Price ($)", value=12.020)
    target_profit = st.number_input("Desired Profit ($)", value=400.0)

    if st.button("Calculate TP", key="tp"):
        pos_size2, qty2, tp_price2, tp_value2, roi2 = calculate_tp_value(
            entry_price2, leverage2, margin2, target_profit
        )
        st.markdown(f"**Position Size:** {pos_size2:,.2f}")
        st.markdown(f"**Quantity:** {qty2:,.2f}")
        st.markdown(f"**TP Price:** {tp_price2:.5f}")
        st.markdown(f"**Profit:** ${target_profit:,.2f}")
        st.markdown(f"**ROI:** {roi2:.1f}%")
        st.markdown(f"**Take Profit Value:** ${tp_value2:,.3f}")
