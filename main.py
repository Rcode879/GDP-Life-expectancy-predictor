# Import necessary libraries
import matplotlib.pyplot as plt  # For plotting graphs
import numpy as np  # For numerical computations
import pandas as pd  # For handling dataframes
from sklearn.metrics import mean_squared_error, r2_score  # For evaluating model performance

# Load dataset
df = pd.read_csv("life-expectancy-vs-gdp-per-capita.csv")  # Read the CSV file into a DataFrame

# Drop unnecessary columns that are not useful for modeling
df.drop(["417485-annotations", "Entity", "Code", "Year", "Population (historical estimates)", "Continent"], axis=1, inplace=True)

# Remove rows with missing values to ensure clean data
df.dropna(inplace=True)

# Extract the "GDP per capita" column as a NumPy array
gdp = (np.array(df[["GDP per capita"]]))
gdp = gdp.flatten()  # Convert to a 1D array

# Extract the "Life expectancy" column as a NumPy array
expectancy = (np.array(df[["Life expectancy"]]))
expectancy = expectancy.flatten()  # Convert to a 1D array

# Apply logarithm transformation to GDP to linearize the relationship with life expectancy
log_gdp = np.log(gdp)

# Fit a 7th-degree polynomial model to the log-transformed GDP and life expectancy data
mymodel = np.poly1d(np.polyfit(log_gdp, expectancy, 7))

# Generate a smooth range of GDP values for plotting the model's curve
myline = np.linspace(min(gdp), max(gdp), 100)  # 100 points between min and max GDP

# Predict life expectancy for the generated GDP values using the fitted model
expectancy_fit = mymodel(np.log(myline))

# Create a large figure for better visibility
plt.figure(figsize=(20, 10))

# Scatter plot of actual GDP vs. Life Expectancy
plt.scatter(gdp, expectancy)

# Label the x-axis and y-axis
plt.xlabel("GDP per Capita")
plt.ylabel("Life Expectancy")

# Set x-axis to logarithmic scale for better visualization
plt.xscale("log")

# Plot the polynomial regression model as a red line
plt.plot(myline, expectancy_fit, color="red")

# --- Console-based menu system ---
quit = False  # Variable to control the menu loop

while quit == False:
    # Prompt user for input
    choice = input("Enter 'p' to make a prediction, enter 'q' to quit, enter 't' to view the model's r2 error, enter 'g' to view the graph: ")
    choice = choice.lower()  # Convert input to lowercase for consistency

    # Exit the loop if user chooses to quit
    if choice == "q":
        quit = True

    # Predict life expectancy for a user-specified GDP per capita
    elif choice == "p":
        while True:
            try:
                user_gdp = float(input("Enter the GDP per Capita:"))  # Get GDP input from user
                break  # Exit loop if input is valid
            except ValueError:
                print("Please enter only numbers!")  # Handle invalid input

        # Predict life expectancy using the model and log-transformed GDP
        print(f"The estimated life expectancy of a country with {user_gdp} GDP per capita is {mymodel(np.log(user_gdp))} ")

    # Display the R² error of the model (performance evaluation)
    elif choice == "t":
        print(f"The model's R² error is {r2_score(expectancy, mymodel(log_gdp))}")

    # Show the graph if the user chooses 'g'
    elif choice == "g":
        plt.show()  # Display the graph
