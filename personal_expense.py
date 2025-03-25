import streamlit as st
import mysql.connector
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

connection = mysql.connector.connect(
host="localhost",
user="root",
password="Devi!1990",
database="expense"
)
cursor=connection.cursor()

#image = Image.open('C:\\Users\\Devipriya\\Desktop\\Devi_Learning\\Personal_expense_Proj1\\Personal_Expenses.jpg')
#st.title('Analyzing Personal Expenses')
# Set up the home page
def home():
    st.title("Analyzing Personal Expenses")
    from PIL import Image
    image= Image.open('C:\\Users\\Devipriya\\Desktop\\Devi_Learning\\Personal_expense_Proj1\\Personal_Expenses.jpg')
    st.image(image, caption='Personal Expense', use_container_width=True)
    st.write("This project is about a detailed analysis of our personal expenses for a year. It will be very useful for all of us to estimate and plan our expenses for the future accordingly. ")

# Set up the queries page
def queries():
    option = st.selectbox('Select an option:',('Option 1', 'Option 2', 'Option 3','Option 4','Option 5','Option 6','Option 7','Option 8','Option 9','Option 10','Option 11','Option 12','Option 13','Option 14','Option 15','Option 16','Option 17'))

# Function to fetch data based on the selected option
    def fetch_data(query):
        return pd.read_sql_query(query, connection)
    if option == 'Option 1':
        query1 = "select sum(amount) as total_amount_Shopping from expense_year where category = 'Shopping';"
        query2 = "select sum(amount) as total_amount_Subscription from expense_year where category = 'Subscription';"
        query3 = "select sum(amount) as total_amount_Groceries from expense_year where category = 'Groceries';"
        query4= "select sum(amount) as total_amount_HealthMedicine from expense_year where category = 'Health and Medicine';"
        query5 = "select sum(amount) as total_amount_Investment from expense_year where category = 'Investment';"
        query6 = "select sum(amount) as total_amount_Loanamount from expense_year where category = 'Loan amount';"
        query7 = "select sum(amount) as total_amount_Schoolfees from expense_year where category = 'School fees';"
# Fetch data from the database
        df1 = pd.read_sql_query(query1, connection)
        df2 = pd.read_sql_query(query2, connection)
        df3 = pd.read_sql_query(query3, connection)
        df4 = pd.read_sql_query(query4, connection)
        df5 = pd.read_sql_query(query5, connection)
        df6 = pd.read_sql_query(query6, connection)
        df7 = pd.read_sql_query(query7, connection)

        st.write("Total amount spent in each category for over all 2024")

# Example: Plotting data from the first dataframe
        fig, ax = plt.subplots()
        ax.bar(['Shopping', 'Subscription', 'Groceries', 'Health and Medicine', 'Investment', 'Loan amount', 'School fees'],
        [df1['total_amount_Shopping'].item(), df2['total_amount_Subscription'].item(), df3['total_amount_Groceries'].item(),
        df4['total_amount_HealthMedicine'].item(), df5['total_amount_Investment'].item(), df6['total_amount_Loanamount'].item(),
        df7['total_amount_Schoolfees'].item()],
        color=['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black'])

        ax.set_title('Total amount spent in each category for 2024')
        ax.set_ylabel('Total Amount')
        ax.set_xlabel('Categories')
        plt.xticks(rotation=45)

        st.pyplot(fig)

    elif option == 'Option 2':
        query1 = "select sum(amount) as total_amount_Cash from expense_year where Payment_Mode = 'Cash';"
        query2 = "select sum(amount) as total_amount_Creditcard from expense_year where Payment_Mode = 'Credit card';"
        query3 = "select sum(amount) as total_amount_Debitcard from expense_year where Payment_Mode = 'Debit card';"
        query4= "select sum(amount) as total_amount_Netbanking from expense_year where Payment_Mode = 'Netbanking';"
        query5 = "select sum(amount) as total_amount_UPI from expense_year where Payment_Mode = 'UPI';"
        query6 = "select sum(amount) as total_amount_Wallet from expense_year where Payment_Mode = 'Wallet';"

# Fetch data from the database
        df1 = pd.read_sql_query(query1, connection)
        df2 = pd.read_sql_query(query2, connection)
        df3 = pd.read_sql_query(query3, connection)
        df4 = pd.read_sql_query(query4, connection)
        df5 = pd.read_sql_query(query5, connection)
        df6 = pd.read_sql_query(query6, connection)

        st.write("Total amount spent using each payment mode")

        fig, ax = plt.subplots()
        ax.bar(['Cash', 'Credit card', 'Debit card', 'Netbanking', 'UPI', 'Wallet'],
        [df1['total_amount_Cash'].item(), df2['total_amount_Creditcard'].item(), df3['total_amount_Debitcard'].item(),
        df4['total_amount_Netbanking'].item(), df5['total_amount_UPI'].item(), df6['total_amount_Wallet'].item()],
        color=['blue', 'green', 'red', 'magenta', 'yellow', 'black'])

        ax.set_title('Total amount spent using each payment mode')
        ax.set_ylabel('Total Amount')
        ax.set_xlabel('Payment_Mode')
        plt.xticks(rotation=45)

        st.pyplot(fig)
    
    elif option == 'Option 3':
        query = "select sum(cashback) as total_amount_cashback from expense_year;"
        df = pd.read_sql_query(query, connection)
        st.write("Total cashback received across all transactions")
        fig, ax = plt.subplots()
        ax.plot(df['total_amount_cashback'],marker='o')
        ax.set_title('Total cashback received across all transactions')
        ax.set_xlabel('total_amount_cashback')
        st.pyplot(fig)

    elif option == 'Option 4':
        query = "select category,sum(amount) as total_amount from expense_year group by category order by total_amount desc limit 5;"
        df = pd.read_sql_query(query, connection)
        st.write("Top 5 most expensive categories in terms of spending")
        fig, ax = plt.subplots()
        ax.plot(df['category'], df['total_amount'], marker='o')
        ax.set_title('Top 5 most expensive categories in terms of spending')
        ax.set_xlabel('category')
        ax.set_ylabel('total_amount')
        st.pyplot(fig)
    
    elif option == 'Option 5':
        query1 = "select sum(amount) as amount_UPI from expense_year where payment_mode='UPI' and discription='Transportation';"
        query2 = "select sum(amount) as amount_Creditcard from expense_year where payment_mode='Credit card' and discription='Transportation';"
        query3 = "select sum(amount) as amount_Netbanking from expense_year where payment_mode='Netbanking' and discription='Transportation';"
        query4= "select sum(amount) as amount_Wallet from expense_year where payment_mode='Wallet' and discription='Transportation';"
        query5 = "select sum(amount) as amount_Cash from expense_year where payment_mode='Cash' and discription='Transportation';"
        df1 = pd.read_sql_query(query1, connection)
        df2 = pd.read_sql_query(query2, connection)
        df3 = pd.read_sql_query(query3, connection)
        df4 = pd.read_sql_query(query4, connection)
        df5 = pd.read_sql_query(query5, connection)
        st.write("Total amount spent on transportation using different payment modes")
        fig, ax = plt.subplots()
        ax.bar(['UPI', 'Credit card','Netbanking','Wallet','Cash'],
        [df1['amount_UPI'].item(), df2['amount_Creditcard'].item(), df3['amount_Netbanking'].item(),
        df4['amount_Wallet'].item(), df5['amount_Cash'].item()],
        color=['blue', 'green', 'red', 'magenta', 'yellow'])

        ax.set_title('Total amount spent on transportation using different payment modes')
        ax.set_ylabel('Total Amount')
        ax.set_xlabel('Payment_Mode')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    elif option == 'Option 6':
        query = "select distinct payment_mode as transaction from expense_year where cashback > 0;"
        df = pd.read_sql_query(query, connection)
        st.write("Cashbacks are received only through below payment mode")
        fig, ax = plt.subplots()
        ax.plot(df['transaction'],marker='o')
        ax.set_title('transactions resulted in cashback')
        ax.set_xlabel('transaction')
        st.pyplot(fig)

    elif option == 'Option 7':
        query1 = "select sum(amount)as Jan_spending from expense_year where months='Jan';"
        query2 = "select sum(amount)as Feb_spending from expense_year where months='Feb';"
        query3 = "select sum(amount)as March_spending from expense_year where months='March';"
        query4= "select sum(amount)as April_spending from expense_year where months='April';"
        query5 = "select sum(amount)as May_spending from expense_year where months='May';"
        query6 = "select sum(amount)as June_spending from expense_year where months='June';"
        query7 = "select sum(amount)as July_spending from expense_year where months='July';"
        query8 = "select sum(amount)as Aug_spending from expense_year where months='Aug';"
        query9 = "select sum(amount)as Sep_spending from expense_year where months='Sep';"
        query10 = "select sum(amount)as Oct_spending from expense_year where months='Oct';"
        query11 = "select sum(amount)as Nov_spending from expense_year where months='Nov';"
        query12 = "select sum(amount)as Dec_spending from expense_year where months='Dec';" 
        df1 = pd.read_sql_query(query1, connection)
        df2 = pd.read_sql_query(query2, connection)
        df3 = pd.read_sql_query(query3, connection)
        df4 = pd.read_sql_query(query4, connection)
        df5 = pd.read_sql_query(query5, connection)
        df6 = pd.read_sql_query(query6, connection)
        df7 = pd.read_sql_query(query7, connection)
        df8 = pd.read_sql_query(query8, connection)
        df9 = pd.read_sql_query(query9, connection)
        df10 = pd.read_sql_query(query10, connection)
        df11 = pd.read_sql_query(query11, connection)
        df12 = pd.read_sql_query(query12, connection)
        st.write("Total spending on each month over year 2024")

        fig, ax = plt.subplots()
        ax.bar(['Jan', 'Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec'],
        [df1['Jan_spending'].item(), df2['Feb_spending'].item(), df3['March_spending'].item(),
        df4['April_spending'].item(), df5['May_spending'].item(),df6['June_spending'].item(),df7['July_spending'].item(),df8['Aug_spending'].item(),df9['Sep_spending'].item(),df10['Oct_spending'].item(),df11['Nov_spending'].item(),df12['Dec_spending'].item()],
        color=['blue', 'green','red','yellow','black','magenta','red','magenta','cyan','blue','green','red'])

        ax.set_title('Total spending in each month of the year')
        ax.set_ylabel('Total Amount')
        ax.set_xlabel('Month')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif option == 'Option 8':
        query = "select months,Discription,sum(amount) as total_spending from expense_year where discription in('Toys/Gifts Purchase','Transportation','Movie charge','Subscription for Hotstar','Subscription for Netflix') group by months,discription order by total_spending desc limit 1;"
        df = pd.read_sql_query(query, connection)
        st.write("November month is the highest spending month in categories like Travel,Entertainment or Gifts with Rs.12758.92")
        fig = px.scatter_3d(df, x='months', y='Discription', z='total_spending')
        st.plotly_chart(fig)  

    elif option == 'Option 9':
        query = "select category,months,count(amount)as recurrence_count from expense_year group by months,category having recurrence_count > 1 order by months,category;"
        df = pd.read_sql_query(query, connection)
        st.write("Recurring expenses that occur during specific months of the year")
        # Plotting the 3D graph
        fig = px.scatter_3d(df, x='category', y='months', z='recurrence_count')
        # Display the plot in Streamlit
        st.plotly_chart(fig)

    elif option == 'Option 10':
        query = "select months,sum(cashback)as cashback from expense_year where cashback>0 group by months;"
        df = pd.read_sql_query(query, connection)
        st.write("Cashback or rewards earned in each month")
        # Plot the data
        fig,ax = plt.subplots()
        ax.plot(df['months'], df['cashback'], marker='*')
        ax.set_title('Cashback or rewards were earned in each month')
        ax.set_xlabel('months')
        ax.set_ylabel('cashback')
        st.pyplot(fig)

    elif option == 'Option 11':
        query = "WITH monthly_spending AS (SELECT months,SUM(amount) AS total_spending FROM expense_year GROUP BY months),spending_change AS (SELECT months,total_spending,LAG(total_spending) OVER (ORDER BY CASE WHEN months = 'Jan' THEN 1 WHEN months = 'Feb' THEN 2 WHEN months = 'March' THEN 3 WHEN months = 'April' THEN 4 WHEN months = 'May' THEN 5 WHEN months = 'June' THEN 6 WHEN months = 'July' THEN 7 WHEN months = 'Aug' THEN 8 WHEN months = 'Sep' THEN 9 WHEN months = 'Oct' THEN 10 WHEN months = 'Nov' THEN 11 WHEN months = 'Dec' THEN 12 ELSE 13 END ASC) AS previous_month_spending FROM monthly_spending)SELECT months,total_spending,previous_month_spending,(total_spending - previous_month_spending) AS change_in_spending FROM spending_change GROUP BY months ORDER BY CASE WHEN months = 'Jan' THEN 1 WHEN months = 'Feb' THEN 2 WHEN months = 'March' THEN 3 WHEN months = 'April' THEN 4 WHEN months = 'May' THEN 5 WHEN months = 'June' THEN 6 WHEN months = 'July' THEN 7 WHEN months = 'Aug' THEN 8 WHEN months = 'Sep' THEN 9 WHEN months = 'Oct' THEN 10 WHEN months = 'Nov' THEN 11 WHEN months = 'Dec' THEN 12 ELSE 13 END ASC;"

        # Execute the query and load the data into a DataFrame
        df = pd.read_sql_query(query, connection)
        st.write("overall spending changed over time")

        # Plotting the 3D graph
        fig = px.scatter_3d(df, x='months', y='total_spending', z='change_in_spending')

        # Display the plot in Streamlit
        st.plotly_chart(fig)

    elif option == 'Option 12':
        query = "select Avg(amount),discription from expense_year where discription='Transportation';"
        df = pd.read_sql_query(query, connection)
        st.write("Typical costs associated with different types of travel",df)
        fig, ax = plt.subplots()
        ax.plot(df['Avg(amount)'], df['discription'], marker='o')
        ax.set_title('Typical costs associated with different types of travel')
        ax.set_xlabel('Avg(amount)')
        ax.set_ylabel('discription')
        st.pyplot(fig)

    elif option == 'Option 13':
        query1 = "select months,category,sum(amount)as Grocery_amount from expense_year where category= 'Groceries' group by months,category order by grocery_amount desc;"
        query2 = "select DAYNAME(date) as DayName,category,sum(amount)as Grocery_amount from expense_year where category= 'Groceries' group by DayName,category order by grocery_amount desc;"
        df1 = pd.read_sql_query(query1, connection)
        df2 = pd.read_sql_query(query2, connection)
        st.write("For seasonal spending like Diwali and New year it is high",df1)
        st.write("For weekdays(Sunday was spent a lot)",df2)
        fig1 = px.scatter_3d(df1, x='months', y='category', z='Grocery_amount')
        fig1.update_layout(title='For seasonal spending like Diwali and New year it is high')
        fig2 = px.scatter_3d(df2, x='DayName', y='category', z='Grocery_amount')
        fig2.update_layout(title='For weekdays,Sunday was spent a lot')
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)

    elif option == 'Option 14':
        query = "select category,sum(amount)as total_spent from expense_year group by category order by total_spent desc;"
        df = pd.read_sql_query(query, connection)
        st.write("Here high priority on Health & Medicine where as low priority on Loan amount.",df)
        fig, ax = plt.subplots()
        ax.plot(df['category'], df['total_spent'], marker='*')
        ax.set_title('High and Low Priority Categories')
        ax.set_xlabel('category')
        ax.set_ylabel('total_spent')
        st.pyplot(fig)

    elif option == 'Option 15':
        query = "SELECT category, (SUM(amount) / (SELECT SUM(amount) FROM expense_year)) * 100 AS Percentage_of_total FROM expense_year GROUP BY category ORDER BY Percentage_of_total DESC LIMIT 1;"
        df = pd.read_sql_query(query, connection)
        st.write("Category that contributes the highest percentage of the total spending",df)
        fig, ax = plt.subplots()
        ax.plot(df['category'], df['Percentage_of_total'], marker='o')
        ax.set_title('highest percentage of the total spending')
        ax.set_xlabel('category')
        ax.set_ylabel('Percentage_of_total')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    elif option == 'Option 16':
        query = "select sum(amount)as Saving_amount from expense_year where Category in('Loan amount','Investment');"
        df = pd.read_sql_query(query, connection)
        st.write("total amount saved overall year",df)
        fig, ax = plt.subplots()
        ax.plot(df['Saving_amount'],marker='*')
        ax.set_title('Amount saved')
        ax.set_xlabel('Saving_amount')
        st.pyplot(fig)

    elif option == 'Option 17':
        query = "SELECT SUM(amount) / 12 AS Avg_per_month FROM expense_year;"
        df = pd.read_sql_query(query, connection)
        st.write("Average amount spent per month",df)
        fig, ax = plt.subplots()
        ax.plot(df['Avg_per_month'],marker='*')
        ax.set_title('Average amount spent per month')
        ax.set_xlabel('Avg_per_month')
        st.pyplot(fig)


# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Queries"])

# Display the selected page
if page == "Home":
    home()
elif page == "Queries":
    queries()
connection.commit()
connection.close()