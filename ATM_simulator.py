import streamlit as st

if "balance" not in st.session_state:
    st.session_state.balance = 100  # Initial balance for demo

st.title("ATM Simulator")

st.write("""
This ATM simulator allows you to:
- Check your account balance  
- Deposit funds  
- Withdraw funds  

**Initial balance is set to $100 for demonstration purposes.**
""")

option = st.radio(
    "Select an action:",
    ("Check Balance", "Deposit", "Withdraw")
)

if option == "Check Balance":
    st.subheader("Account Balance")
    st.success(f"Your current balance is: **${st.session_state.balance:.2f}**")

elif option == "Deposit":
    st.subheader("Deposit Funds")
    amount = st.number_input("Enter amount to deposit:", min_value=0.0, step=10.0)
    if st.button("Deposit"):
        if amount > 0:
            st.session_state.balance += amount
            st.success(f"${amount:.2f} deposited successfully!")
        else:
            st.error("Please enter a valid deposit amount.")

elif option == "Withdraw":
    st.subheader("Withdraw Funds")
    amount = st.number_input("Enter amount to withdraw:", min_value=0.0, step=10.0)
    if st.button("Withdraw"):
        if amount <= 0:
            st.error("Please enter a valid withdrawal amount.")
        elif amount > st.session_state.balance:
            st.error("Insufficient balance!")
        else:
            st.session_state.balance -= amount
            st.success(f"${amount:.2f} withdrawn successfully!")

st.write("---")
st.info(f"Current Balance: **${st.session_state.balance:.2f}**")