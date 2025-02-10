# GDP-Life-expectancy-predictor
# Life Expectancy vs GDP Prediction Model

## 📌 Overview

This project analyzes the relationship between **GDP per Capita** and **Life Expectancy** using **Polynomial Regression**. The model fits a **7th-degree polynomial** to predict life expectancy based on GDP per capita. The project includes:

- Data preprocessing (cleaning and transformation)
- Polynomial regression model training
- Data visualization using Matplotlib
- Interactive **console-based predictions**
- **R² error evaluation** to measure model accuracy

## 🚀 Features

✅ Reads data from a CSV file ✅ Cleans and preprocesses the dataset ✅ Applies **log transformation** to GDP for better model fit ✅ Fits a **7th-degree polynomial regression model** ✅ Plots **actual vs predicted values** with a logarithmic scale ✅ Allows **user input to predict life expectancy** ✅ Displays **R² score** to assess model accuracy ✅ Interactive **menu for user interaction**

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**

```sh
git clone 
cd GDP-Life-expectancy-predictor
```

### **2️⃣ Install Dependencies**

Ensure you have Python installed. Then, install the required libraries:

```sh
pip install numpy pandas matplotlib scikit-learn
```

### **3️⃣ Run the Script**

```sh
python main.py
```

---

## 📊 How It Works

1. **Load & Clean Data**

   - Reads the dataset from `life-expectancy-vs-gdp-per-capita.csv`
   - Drops unnecessary columns and handles missing values

2. **Apply Log Transformation**

   - GDP is **log-transformed** to make the relationship more linear

3. **Train Polynomial Regression Model**

   - Fits a **7th-degree polynomial** using `np.polyfit()`

4. **Plot the Model**

   - Scatter plot of GDP vs. Life Expectancy
   - Polynomial regression curve (red line) overlayed
   - **Logarithmic x-axis** for better visualization

5. **Interactive Console Menu**

   - `p` → Predict life expectancy for a user-input GDP value
   - `t` → Display the **R² error** of the model
   - `g` → Show the **graph** of the model
   - `q` → Quit the program

---

## 📈 Example Usage

```
Enter 'p' to make a prediction, 't' to view R² error, 'g' to view graph, 'q' to quit: p
Enter the GDP per Capita: 65020.35
The estimated life expectancy of a country with 65020.35 GDP per capita is 77.7771393826115 years
```


## 📜 License

This project is open-source and available under the **MIT License**.



