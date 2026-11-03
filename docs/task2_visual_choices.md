# Task 2: Choosing the Right Visuals — Dashboard Architecture
**Company:** Tata Insights and Quants (Tata iQ)
**Project:** Data Visualisation: Empowering Business with Effective Insights

---

## 🎯 Design Principle
Each visual was chosen so that a senior leader can understand the insight in a few seconds. The chart type strictly follows the type of question: trend, comparison, ranking, relationship, or geography.

---

## 👔 1. CEO Dashboard Visual Mapping Matrix

| Question | Visual | Reason |
|---|---|---|
| **Sales, profit, margin trend** | KPI cards + Line chart | Shows operational headline numbers plus changes over time. |
| **Regional profitability** | Map + Sorted bar chart | Connects geographic locations directly with top-to-bottom performance rankings. |
| **Loss-making categories** | Bar chart (Negative margins highlighted in red) | Operational losses stand out instantly to protect company cash flow. |
| **Discount vs profit** | Scatter plot | Visualizes correlation and distribution dense points between two raw measures. |
| **Invest or cut** | Sales vs Profit quadrant scatter | Separates strategic categories explicitly into growth, fix, and cut zones. |

---

## 📢 2. CMO Dashboard Visual Mapping Matrix

| Question | Visual | Reason |
|---|---|---|
| **Top segments** | Grouped bar chart | Compares a small number of core business categories side-by-side. |
| **Top 10 customers** | Sorted horizontal bar chart | Clear ranking structure where long corporate account names fit perfectly without being cut off. |
| **Category by region** | Heat map | Compares two distinct dimensions at once, using color density to reveal product intensity. |
| **Seasonality** | Monthly line chart | Tracks recurring transactional peaks and dips over time to plan ad campaigns. |
| **Shipping preference** | Bar chart (or Donut for 3-4 slices) | Offers a clean, rapid visual comparison of customer delivery choices. |
| **Repeat customers** | KPI card + Bar breakdown | Places a primary retention percentage metric next to minor contextual trends. |

---

## 🚫 3. Chart Types & Clean Design Rules to Avoid

To maintain professional visualization standards, the following guidelines are strictly enforced across our dashboard systems:
* **No 3D Charts:** Three-dimensional effects distort the scale of values, making true analytical reading difficult.
* **No Multi-Slice Pie Charts:** Pie charts containing more than 4 slices are difficult to read; horizontal bars are used instead.
* **No Raw Tables for Trends:** The human eye cannot spot multi-month patterns inside dense grids of text; charts replace raw tracking lists.
* **Color Palette Constraint:** Restriced to a maximum of 3–4 solid colors, used consistently across all sheets. 

---

## 🎛️ 4. Dynamic Dashboard Control Filters
To allow both the CEO and CMO to customize their views, all dashboards feature global top-level interactive filters for:
1. `Year` (Chronological slicing)
2. `Region` (Geographical slicing)
3. `Category` (Product segment slicing)

