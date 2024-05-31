import streamlit as st
import pandas as pd
from supabase_client import supabase

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
        service_price = st.number_input("Service Price", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Add Service")
        if submitted:
            data = {
                "name": service_name,
                "price": service_price
            }
            response = supabase.table('services').insert(data).execute()
            if response.error:
                st.error(f"Error adding service: {response.error.message}")
            else:
                st.success(f"Service Added: {service_name}, {service_price}")
    
    # Display list of services
    response = supabase.table('services').select('*').execute()
    services = response.data
    if services:
        st.subheader("Existing Services")
        df_services = pd.DataFrame(services)
        st.table(df_services)

# Customers Page
elif page == "Customers":
    st.title("Customers")
    st.write("Manage your customers here.")
    
    # Add form to create new customer
    with st.form("Add Customer"):
        customer_name = st.text_input("Customer Name")
        customer_email = st.text_input("Customer Email")
        customer_tel = st.text_input("Customer Telephone")
        submitted = st.form_submit_button("Add Customer")
        if submitted:
            data = {
                "name": customer_name,
                "email": customer_email,
                "tel": customer_tel
            }
            response = supabase.table('customers').insert(data).execute()
            if response.error:
                st.error(f"Error adding customer: {response.error.message}")
            else:
                st.success(f"Customer Added: {customer_name}, {customer_email}, {customer_tel}")
    
    # Display list of customers
    response = supabase.table('customers').select('*').execute()
    customers = response.data
    if customers:
        st.subheader("Existing Customers")
        df_customers = pd.DataFrame(customers)
        st.table(df_customers)

# Sales Page
elif page == "Sales":
    st.title("Sales")
    st.write("Record a new sale.")
    
    # Fetch services and customers for selection
    services = supabase.table('services').select('*').execute().data
    customers = supabase.table('customers').select('*').execute().data
    
    if services and customers:
        with st.form("Record Sale"):
            sale_service = st.selectbox("Service", [s['name'] for s in services])
            sale_customer = st.selectbox("Customer", [c['name'] for c in customers])
            sale_payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Other"])
            sale_amount = st.number_input("Sale Amount", min_value=0.0, step=0.01)
            submitted = st.form_submit_button("Record Sale")
            if submitted:
                data = {
                    "service": sale_service,
                    "customer": sale_customer,
                    "payment_method": sale_payment_method,
                    "amount": sale_amount
                }
                response = supabase.table('sales').insert(data).execute()
                if response.error:
                    st.error(f"Error recording sale: {response.error.message}")
                else:
                    st.success(f"Sale Recorded: {sale_service}, {sale_customer}, {sale_payment_method}, {sale_amount}")
    
    # Display list of sales
    response = supabase.table('sales').select('*').execute()
    sales = response.data
    if sales:
        st.subheader("Sales Records")
        df_sales = pd.DataFrame(sales)
        st.table(df_sales)

# Reports Page
elif page == "Reports":
    st.title("Reports")
    st.write("View reports here.")
    
    # Example report: Total Sales Amount
    response = supabase.table('sales').select('*').execute()
    sales = response.data
    if sales:
        total_sales = sum(s['amount'] for s in sales)
        st.write(f"Total Sales Amount: {total_sales}")

# Shift Closure Page
elif page == "Shift Closure":
    st.title("Shift Closure")
    st.write("Close the shift and verify transactions.")
    
    # Add form to close shift
    with st.form("Close Shift"):
        shift_instructor = st.text_input("Instructor Name")
        shift_cash_start = st.number_input("Starting Cash", min_value=0.0, step=0.01)
        shift_cash_end = st.number_input("Ending Cash", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Close Shift")
        if submitted:
            data = {
                "instructor": shift_instructor,
                "cash_start": shift_cash_start,
                "cash_end": shift_cash_end
            }
            response = supabase.table('shifts').insert(data).execute()
            if response.error:
                st.error(f"Error closing shift: {response.error.message}")
            else:
                st.success(f"Shift Closed by {shift_instructor}. Starting Cash: {shift_cash_start}, Ending Cash: {shift_cash_end}")
    
    # Display list of shifts
    response = supabase.table('shifts').select('*').execute()
    shifts = response.data
    if shifts:
        st.subheader("Shift Records")
        df_shifts = pd.DataFrame(shifts)
        st.table(df_shifts)
