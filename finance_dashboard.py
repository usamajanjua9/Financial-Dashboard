import streamlit as st  # Streamlit for UI
import pandas as pd  # Pandas for data handling
import yfinance as yf  # Yahoo Finance API for stock data
import plotly.express as px  # Plotly for interactive charts
import random  # For random selection of finance quotes

# 🎨 Set up Streamlit page layout and title
st.set_page_config(page_title="💰 Ultimate Financial Dashboard", layout="wide")

# Hide Streamlit's extra UI elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 🌟 Main Title
st.title("💰 Ultimate Financial Dashboard 📊")
st.write("🔥 Track your money, investments, and goals all in one place! 🚀")

# 🖼️ Add a fun header GIF for an engaging UI
st.image("https://i.gifer.com/J4o.gif", use_container_width=True)

# 📅 Sidebar - User Inputs for Finance Tracking
st.sidebar.header("💡 Financial Overview")

# User input for monthly income
income = st.sidebar.number_input("Monthly Income 💵", min_value=0, value=5000)

# User input for monthly expenses
expenses = st.sidebar.number_input("Monthly Expenses 🛍️", min_value=0, value=3000)

# User input for savings goal in percentage
savings_percentage = st.sidebar.slider("💰 Savings Goal (%)", 0, 100, 20)

# 📈 Sidebar - Investment Portfolio Tracking
st.sidebar.header("📈 Investment Portfolio")

# User input for stock symbol to fetch live stock data
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g. AAPL) 📊", "AAPL")

# ---------------------------- BUDGET ANALYSIS ---------------------------- #

# 🏦 Display Budget Summary
st.header("📊 Budget Summary")

# Calculate Remaining Budget & Savings Amount
remaining_budget = income - expenses
savings_amount = (savings_percentage / 100) * income

# Create a DataFrame for visualization
budget_df = pd.DataFrame({
    "Category": ["Income", "Expenses", "Savings", "Remaining Budget"],
    "Amount": [income, expenses, savings_amount, remaining_budget]
})

# 📊 Create a Pie Chart for Budget Breakdown
fig_budget = px.pie(
    budget_df, 
    names="Category", 
    values="Amount", 
    title="💰 Budget Distribution",
    color_discrete_sequence=px.colors.qualitative.Pastel  # Using pastel colors for better visuals
)

# Show the pie chart
st.plotly_chart(fig_budget, use_container_width=True)

# ---------------------------- LIVE STOCK DATA ---------------------------- #

# 📉 Fetch and Display Live Stock Data
st.header("📈 Live Stock Market Data")

try:
    # Fetch stock data for the past month using Yahoo Finance API
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period="1mo")

    # Create an interactive line chart for stock prices
    fig_stock = px.line(
        stock_data, 
        x=stock_data.index, 
        y="Close", 
        title=f"📉 {stock_symbol} Stock Price Trend", 
        markers=True
    )

    # Display the stock chart
    st.plotly_chart(fig_stock, use_container_width=True)

except Exception as e:
    st.error("⚠️ Invalid stock symbol. Please enter a valid stock.")

# ---------------------------- FINANCIAL GOALS TRACKER ---------------------------- #

# 🎯 Financial Goal Tracking
st.header("🎯 Financial Goals")

# User input for setting a financial goal
goal = st.text_input("Set Your Financial Goal (e.g., Buy a Car, Save $10,000) 🚗", "Save $10,000")

# User input for goal amount
goal_amount = st.number_input("Goal Amount ($) 🎯", min_value=0, value=10000)

# User input for current savings
current_savings = st.number_input("Current Savings ($) 💰", min_value=0, value=2000)

# Calculate progress percentage
progress = (current_savings / goal_amount) * 100

# Display progress bar
st.progress(progress / 100)

# Show progress status
st.subheader(f"🚀 Progress: {progress:.2f}% towards {goal}")

# ---------------------------- FINANCE QUOTES ---------------------------- #

# 🎭 Display Random Finance Quote
st.header("💡 Finance Tip of the Day 🎭")

# List of finance quotes
finance_quotes = [
    "💰 'Do not save what is left after spending, but spend what is left after saving.' - Warren Buffett",
    "📈 'The stock market is filled with individuals who know the price of everything, but the value of nothing.' - Philip Fisher",
    "🏦 'A budget tells your money where to go instead of wondering where it went.' - Dave Ramsey",
    "🛍️ 'Too many people spend money they haven't earned to buy things they don’t want to impress people they don’t like.' - Will Rogers",
]

# Display a randomly chosen quote
st.write(random.choice(finance_quotes))

# ---------------------------- FOOTER GIF ---------------------------- #

# 🌟 Add a fun GIF footer to keep users engaged
st.image("https://i2.wp.com/frugaling.org/wp-content/uploads/2013/11/giphy-3.gif?resize=500%2C274", use_container_width=True)

# 🚀 Motivational closing statement
st.write("🔥 *Stay financially fit and reach your money goals!* 🚀💰")
