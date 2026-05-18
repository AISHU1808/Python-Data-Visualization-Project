import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# SECTION 1: BASIC CHARTS (Single Window)
# ==========================================

# 1. Simple Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.figure()
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.show()

# 2. Bar Chart Using Numpy
names = np.array(["a", "b", "c", "d"])
marks = np.array([10, 20, 30, 40])
plt.figure()
plt.bar(names, marks)
plt.title("Basic Bar Chart")
plt.show()

# 3. Pie Chart
names = np.array(["a", "b", "c", "d"])
data = np.array([10, 20, 30, 40])
plt.figure()
plt.pie(data, labels=names)
plt.title("Basic Pie Chart")
plt.show()

# 4. Histogram
data = np.array([10, 20, 30, 40])
plt.figure()
plt.hist(data)
plt.title("Basic Histogram")
plt.show()

# 5. Scatter Plot
data = np.array([10, 20, 30, 40])
data1 = np.array([1, 2, 3, 4])
plt.figure()
plt.scatter(data, data1)
plt.title("Basic Scatter Plot")
plt.show()


# ==========================================
# SECTION 2: STYLED & LABELED CHARTS
# ==========================================

# 6. Sales Chart (Styled Line)
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
plt.figure()
plt.plot(x, y, marker="o", color="r")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.title("Sales Chart")
plt.show()

# 7. Green Bar Chart
names = np.array(["A", "B", "C", "D"])
marks = np.array([50, 70, 60, 90])
plt.figure()
plt.bar(names, marks, color="green")
plt.title("Styled Bar Chart")
plt.show()

# 8. Budget Expenses Pie Chart
data = np.array([40, 30, 20, 10])
labels = np.array(["food", "rent", "travel", "other"])
plt.figure()
plt.pie(data, labels=labels)
plt.title("Expenses Pie Chart")
plt.show()

# 9. Histogram with Sample Distribution
data = np.array([10, 20, 20, 30, 40, 40, 50])
plt.figure()
plt.hist(data)
plt.title("Distribution Histogram")
plt.show()

# 10. Multi-point Scatter Plot
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 15, 20, 30, 50])
plt.figure()
plt.scatter(x, y)
plt.title("Linear/Exponential Scatter")
plt.show()


# ==========================================
# SECTION 3: REFINED & MULTI-LINE VISUALS
# ==========================================

# 11. Performance Line Style Shortcodes
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 15, 25, 35, 45])
plt.figure()
plt.plot(x, y, "b--o")  # Blue, dashed line, circle marker
plt.title("Performance Chart")
plt.show()

# 12. Multiple Lines on One Graph (Sales vs Profit)
x = np.array([1, 2, 3, 4])
sales = np.array([10, 20, 30, 40])
profit = np.array([5, 10, 15, 20])  # Fixed syntax here
plt.figure()
plt.plot(x, sales, label="Sales", color="hotpink")
plt.plot(x, profit, label="Profit", color="green")
plt.legend()
plt.title("Sales vs Profit Trends")
plt.show()

# 13. Student Marks Bar Chart with Labels
names = np.array(["ram", "ravi", "anu", "kiran"])
marks = np.array([80, 70, 90, 85])  # Fixed array initialization
plt.figure()
plt.bar(names, marks)
plt.title("Student Performance")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()

# 14. Percentage-based Pie Chart
data = np.array([10, 20, 30])
labels = np.array(["good", "travel", "shopping"])
plt.figure()
# FIXED: changed %1.1F%% to lowercase %1.1f%% to avoid string runtime formatting crashes
plt.pie(data, labels=labels, autopct="%1.1f%%")
plt.title("Activity Split")
plt.show()


# ==========================================
# SECTION 4: SUBPLOTS & FIGURE SIZES
# ==========================================

# 15. Clean Side-by-Side Subplot (Line + Bar)
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x, y, "g:*")
plt.title("Line Subplot")

name = np.array(["a", "b", "c", "d"])
data = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.bar(name, data)
plt.title("Bar Subplot")
plt.tight_layout()
plt.show()

# 16. Two Line Charts (Comparison)
plt.figure(figsize=(10, 4))
x1 = np.array([1, 2, 4, 6])
y1 = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("Sales Dynamic")

x2 = np.array([9, 7, 5, 3])
y2 = np.array([90, 60, 40, 20])
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("Profit Dynamic")
plt.tight_layout()
plt.show()


# 17. The Comprehensive 4-Chart Dashboard Window
plt.figure(figsize=(10, 8))

# Subplot 1: Line Chart
Months = np.array([1, 2, 3, 4, 5])
Sales = np.array([10, 20, 30, 25, 35])
plt.subplot(2, 2, 1)
plt.plot(Months, Sales)
plt.title("Monthly Sales")

# Subplot 2: Bar Chart
Names = np.array(["Ram", "Ravi", "Anu", "Kiran"])
Marks = np.array([80, 70, 90, 85])
plt.subplot(2, 2, 2)
plt.bar(Names, Marks)
plt.title("Student Marks")

# Subplot 3: Pie Chart
Data = np.array([40, 30, 20, 10])
Labels = np.array(["Food", "Rent", "Travel", "Other"])
plt.subplot(2, 2, 3)
plt.pie(Data, labels=Labels)
plt.title("Expense Breakdown")

# Subplot 4: Scatter Plot
Hours = np.array([1, 2, 3, 4, 5])
Marks_Scatter = np.array([50, 55, 65, 70, 80])
plt.subplot(2, 2, 4)
plt.scatter(Hours, Marks_Scatter)
plt.title("Study Hours vs Marks")

# CRITICAL: Automatically adjusts chart subplots so titles do not clip into graphs
plt.tight_layout()
plt.show()


# ==========================================
# SECTION 5: GRIDDING & DIMENSIONALITY
# ==========================================

# 18. Large Gridded Plot
x = np.array([1, 2, 4, 6])
y = np.array([10, 20, 40, 30])
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title("Gridded Performance Layout")
plt.grid(True)
plt.show()

# 19. Large Gridded Bar Chart
names = np.array(["aa", "bb", "cc"])
marks = np.array([10, 20, 30])
plt.figure(figsize=(8, 6))
plt.bar(names, marks)
plt.title("Gridded Bar Analytics")
plt.grid(axis="y")  # Gridding just the Y-axis looks cleaner for bar charts
plt.show()
