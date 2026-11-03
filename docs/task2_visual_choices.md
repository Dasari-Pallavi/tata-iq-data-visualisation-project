# Task 2: Visual Mapping Strategy — Executive Dashboards
**Company:** Tata Insights and Quants (Tata iQ)
**Project:** Data Visualisation: Empowering Business with Effective Insights

---

## 👔 Executive Vision: CEO Dashboard Architecture

### 1. Monthly Revenue Trajectory
* **Selected Visual:** Line Chart
* **Data Field Mapping:** X-Axis: `InvoiceDate` (Grouped by Month) | Y-Axis: `Sum(Revenue)`
* **Business Value:** Provides the CEO with a macro-view of revenue stability and seasonal growth trajectories over time.

### 2. Top 10 High-Yield Global Territories
* **Selected Visual:** Horizontal Bar Chart
* **Data Field Mapping:** Y-Axis: `Country` (Top 10 Filter) | X-Axis: `Sum(Revenue)` & `Sum(Quantity)`
* **Business Value:** Prevents text truncation of country labels and naturally orders external expansion targets outside the UK.

### 3. Product Inventory Demand Matrix
* **Selected Visual:** Stacked Column Chart
* **Data Field Mapping:** X-Axis: `StockCode` | Y-Axis: `Sum(Quantity)` | Color Legend: `Product Category`
* **Business Value:** Highlights critical operational inventory stock lines driving the largest shipment volumes.

### 4. Discount Yield Impacts
* **Selected Visual:** Scatter Plot
* **Data Field Mapping:** X-Axis: `Discount Percentage` | Y-Axis: `Profit Margin` | Detail: `Transaction ID`
* **Business Value:** Proves visually the exact threshold where excessive promotions destroy net transaction profitability.

---

## 📢 Marketing Operations: CMO Dashboard Architecture

### 1. Top 10 High-Value Key VIP Accounts
* **Selected Visual:** Sorted Vertical Column Chart
* **Data Field Mapping:** X-Axis: `CustomerID` | Y-Axis: `Sum(Revenue)`
* **Business Value:** Isolates the top corporate accounts to feed high-tier VIP retention plans.

### 2. Regional Under-Penetration Map
* **Selected Visual:** Filled Geospatial Map (Choropleth)
* **Data Field Mapping:** Location: `Country` | Color Intensity: `Sum(Revenue)` (Low Value Filter)
* **Business Value:** Provides immediate spatial visibility into zero or low-performance markets to redirect ad spending.

### 3. Seasonal Campaign Timings
* **Selected Visual:** Area Chart
* **Data Field Mapping:** X-Axis: `InvoiceDate` (Weeks/Months) | Y-Axis: `Sum(Order Volume)`
* **Business Value:** Identifies historical peak demand periods to optimize multi-channel marketing campaigns weeks ahead.
