import streamlit as st

# Sidebar navigation
st.sidebar.title("Fitness Studio POS")
page = st.sidebar.radio("Navigate", ["Home", "Services", "Customers", "Sales", "Reports", "Shift Closure"])

# Home Page
if page == "Home":
    st.title("Fitness Studio POS")
    st.write("Welcome to the Fitness Studio POS System!")

# Services Page
elif page == "Services":
    st.title("Services")
    st.write("Manage your services here.")
    # Add form to create new service
    with st.form("Add Service"):
        service_name = st.text_input("Service Name")
        service_description = st.text_area("Service Description")
        service_price = st.number_input("Service Price", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Add Service")
        if submitted:
            st.write(f"Service Added: {service_name}, {service_description}, {service_price}")

# Customers Page
elif page == "Customers":
    st.title("Customers")
    st.write("Manage your customers here.")
    # Add form to create new customer
    with st.form("Add Customer"):
        customer_name = st.text_input("Customer Name")
        customer_contact = st.text_input("Contact Information")
        submitted = st.form_submit_button("Add Customer")
        if submitted:
            st.write(f"Customer Added: {customer_name}, {customer_contact}")

# Sales Page
elif page == "Sales":
    st.title("Sales")
    st.write("Record a new sale.")
    # Add form to record new sale
    with st.form("Record Sale"):
        sale_service = st.text_input("Service")
        sale_customer = st.text_input("Customer")
        sale_payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Other"])
        sale_amount = st.number_input("Sale Amount", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Record Sale")
        if submitted:
            st.write(f"Sale Recorded: {sale_service}, {sale_customer}, {sale_payment_method}, {sale_amount}")

# Reports Page
elif page == "Reports":
    st.title("Reports")
    st.write("View reports here.")
    # Dummy data for reports
    st.write("Report data will be displayed here.")

# Shift Closure Page
elif page == "Shift Closure":
    st.title("Shift Closure")
    st.write("Close the shift and verify transactions.")
    # Add form to close shift
    with st.form("Close Shift"):
        shift_operator = st.text_input("Operator Name")
        shift_cash_start = st.number_input("Starting Cash", min_value=0.0, step=0.01)
        shift_cash_end = st.number_input("Ending Cash", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Close Shift")
        if submitted:
            st.write(f"Shift Closed by {shift_operator}. Starting Cash: {shift_cash_start}, Ending Cash: {shift_cash_end}")
