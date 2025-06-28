# NBA Heat Map Visualization - Stephen Curry Shot Analysis

A Python-based data visualization project that analyzes Stephen Curry's shooting patterns from the 2023 NBA season. This project creates detailed heat maps and statistical visualizations of Curry's shot distribution and accuracy across different areas of the basketball court.

## 🏀 Features

- **NBA Court Visualization**: Custom-drawn NBA halfcourt with accurate dimensions and markings
- **Shot Distribution Heat Map**: Kernel density estimation (KDE) visualization showing Curry's shooting hotspots
- **Shot Type Analysis**: Bar charts showing frequency and accuracy of 2-point vs 3-point shots
- **Data Processing**: Automated coordinate conversion and shot result categorization

## 📊 Visualizations Included

1. **Shot Type Frequency**: Bar chart showing the distribution of 2-point vs 3-point shot attempts
2. **Shooting Accuracy**: Stacked bar chart displaying made vs missed shots by shot type
3. **Court Heat Map**: Red-tinted density plot overlaid on an NBA court showing shooting hotspots

## 🛠️ Prerequisites

- Python 3.x
- Required packages (see requirements.txt):
  - pandas
  - numpy
  - matplotlib
  - seaborn

## 🚀 Installation & Setup

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd nbaHeatMAp
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the analysis**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
nbaHeatMAp/
├── main.py                              # Main analysis script
├── requirements.txt                     # Python dependencies
├── 3_stephen_curry_shot_chart_2023.csv # Stephen Curry's 2023 shot data
├── README.md                           # This file
└── venv/                               # Virtual environment (created during setup)
```

## 📈 Data Analysis

The script performs the following analyses:

1. **Data Preprocessing**:
   - Converts shot type codes (2 → 2-point shot, 3 → 3-point shot)
   - Converts result codes (True → Made, False → Missed)
   - Transforms court coordinates for proper visualization

2. **Statistical Analysis**:
   - Shot type frequency distribution
   - Shooting accuracy by shot type
   - Spatial shot distribution using kernel density estimation

3. **Visualization**:
   - Custom NBA court drawing with all standard markings
   - Heat map overlay showing shooting density
   - Statistical charts for shot analysis

## 🎯 Key Functions

- `convert_cordinates()`: Transforms raw coordinate data to court-relative positions
- `draw_nba_court()`: Creates a detailed NBA halfcourt visualization with all standard markings
- Kernel density estimation for shot distribution analysis

## 📊 Expected Output

When you run the script, you'll see:
1. A summary of the processed data (first 5 rows)
2. A shot type frequency bar chart
3. A shooting accuracy stacked bar chart
4. A comprehensive heat map showing Curry's shooting patterns on an NBA court

## 🔧 Customization

You can modify the script to:
- Analyze different players by changing the CSV file
- Adjust heat map parameters (bw_adjust, alpha, levels)
- Change color schemes and visualization styles
- Add additional statistical analyses

## 📝 Data Format

The CSV file should contain columns for:
- `shot_type`: 2 for 2-point shots, 3 for 3-point shots
- `result`: True for made shots, False for missed shots
- `left`: X-coordinate of shot location
- `top`: Y-coordinate of shot location

## 🤝 Contributing

Feel free to contribute by:
- Adding new visualization types
- Improving the court drawing accuracy
- Adding support for different data formats
- Enhancing the statistical analysis

## 📄 License

This project is open source and available under the [LICENSE](LICENSE) file.

---

*Note: This project is for educational and analytical purposes. The shot data represents Stephen Curry's 2023 NBA season performance.*
