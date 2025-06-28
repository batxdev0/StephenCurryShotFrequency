import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import matplotlib.cm as cm
import seaborn as sns

curry_df = pd.read_csv("/Users/batutaskan/Desktop/nbaHeatMAp/3_stephen_curry_shot_chart_2023.csv")

curry_df['shot_type'] = curry_df['shot_type'].replace({2: '2-point_shot', 3:'3-point_shot'})

curry_df['result'] = curry_df['result'].replace({True:'Made',False:'Missed'})

print(curry_df.head())

plt.figure(figsize=(8,5))
sns.countplot(x='shot_type',data=curry_df,palette='viridis')
plt.title("Frequency of each shot type made by Stephen Curry")
plt.xlabel("Shot Type")
plt.ylabel("Count")
#plt.show()

accuracy_by_type = curry_df.groupby('shot_type')['result'].value_counts(normalize=True).unstack().fillna(0)


accuracy_by_type[['Made','Missed']].plot(kind='bar',stacked=True,color=['green','red'],figsize=(8,5))

plt.title("Shooting Accuracy by Shot Type")
plt.xlabel("Shot Type")
plt.ylabel("Accuracy (%)")
plt.xticks(rotation= 0)
#plt.show()

def convert_cordinates(df):
    
    df['court_x'] = df['left'] -240
    df['court_y'] = df['top']
    
    return df

curry_df = convert_cordinates(curry_df)

def draw_nba_court(axis=None):
    """
    Draws an NBA halfcourt using matplotlib primitives.

    Args:
        axis (matplotlib axis): Optional axis to draw on. Creates one if not provided.

    Returns:
        fig, axis: Figure and axis with the court drawn
    """
    if axis is None:
        fig = plt.figure(figsize=(9, 9))
        axis = fig.add_subplot(111, aspect='auto')
    else:
        fig = None

    # --- Court Outline (Baseline, Sidelines, Halfcourt Line) ---
    axis.plot([-250, 250], [-47.5, -47.5], 'k-')     # Baseline
    axis.plot([-250, -250], [-47.5, 422.5], 'k-')    # Left sideline
    axis.plot([250, 250], [-47.5, 422.5], 'k-')      # Right sideline
    axis.plot([-250, 250], [422.5, 422.5], 'k-')     # Halfcourt line
    
    # --- Backboard ---
    axis.plot([-30, 30], [-10, -10], 'k-', lw=2)

    # --- Paint / Lane ---
    axis.plot([-80, -80], [-47.5, 142.5], 'k-')
    axis.plot([80, 80], [-47.5, 142.5], 'k-')
    axis.plot([-60, -60], [-47.5, 142.5], 'k-')
    axis.plot([60, 60], [-47.5, 142.5], 'k-')
    axis.plot([-80, 80], [142.5, 142.5], 'k-')     # Free throw line

    # --- Hoop and Restricted Area ---
    hoop = Arc((0, 0), 15, 15, theta1=0, theta2=360, lw=1.5, color='black')
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, lw=1.5, color='black')
    axis.add_patch(hoop)
    axis.add_patch(restricted)

    # --- Free Throw Circle ---
    axis.add_patch(Arc((0, 142.5), 120, 120, theta1=0, theta2=180, lw=1.5, color='black'))     # Top half
    axis.add_patch(Arc((0, 142.5), 120, 120, theta1=180, theta2=360, lw=1.5, linestyle='--', color='black'))  # Bottom half (dashed)

    # --- 3-Point Lines ---
    axis.plot([-220, -220], [-47.5, 92.5], 'k-')     # Left corner 3
    axis.plot([220, 220], [-47.5, 92.5], 'k-')       # Right corner 3
    axis.add_patch(Arc((0, 0), 475, 475, theta1=22, theta2=158, lw=1.5, color='black'))   # 3-pt arc

    # --- Halfcourt Circle ---
    axis.add_patch(Arc((0, 422.5), 122, 122, theta1=180, theta2=360, lw=1.5, color='black'))

    # --- Axis Settings ---
    axis.set_xlim(-250, 250)
    axis.set_ylim(-47.5, 470)
    axis.set_aspect(1)     # Equal aspect ratio
    axis.axis('off')       # Hide axes

    return fig, axis


#heatmap-visualation

fig,ax = plt.subplots(figsize=(9,9))

draw_nba_court(ax)

kde = sns.kdeplot(
    x = curry_df['court_x'],
    y = curry_df['court_y'],
    fill = True,
    cmap = 'Reds',
    bw_adjust = 0.8,
    alpha = 0.6,
    levels = 100,
    thresh = 0.05,
    ax = ax
    
    
    
)

plt.show()
 



#source venv/bin/activate