import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="Ziplyne Onboarding Case Study", layout="wide")

# Header
st.title("Ziplyne Onboarding Case Study")
st.markdown("""
This case study demonstrates how Ziplyne can improve the onboarding process by addressing common challenges and implementing effective solutions. Below is a visualization of the dummy data supporting the case study.
""")

# Dummy Data Generation
np.random.seed(42)
data = {
    "Step": np.tile(["Signup", "First Login", "Profile Setup", "Feature Tour", "First Task", "Feedback"], 100),
    "Completion_Time": np.random.exponential(scale=5, size=600),
    "User_Role": np.random.choice(["Admin", "Editor", "Viewer"], 600),
    "Experience_Level": np.random.choice(["Beginner", "Intermediate", "Advanced"], 600),
    "Completion_Status": np.random.choice(["Completed", "Abandoned"], 600, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# Filter Data for Visualization
completed_steps = df[df["Completion_Status"] == "Completed"]
abandoned_steps = df[df["Completion_Status"] == "Abandoned"]

# Visualization: Completion Time by Step
st.subheader("Completion Time by Step")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x="Step", y="Completion_Time", data=completed_steps, ax=ax)
ax.set_title("Completion Time by Onboarding Step")
ax.set_xlabel("Onboarding Step")
ax.set_ylabel("Completion Time (minutes)")
st.pyplot(fig)

# Visualization: Completion Status Distribution
st.subheader("Completion Status Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x="Step", hue="Completion_Status", data=df, ax=ax)
ax.set_title("Completion Status Distribution by Onboarding Step")
ax.set_xlabel("Onboarding Step")
ax.set_ylabel("Count")
st.pyplot(fig)

# Visualization: Role and Experience Level Impact
st.subheader("Impact of User Role and Experience Level")
fig, ax = plt.subplots(1, 2, figsize=(15, 6))
sns.countplot(x="User_Role", hue="Completion_Status", data=df, ax=ax[0])
ax[0].set_title("Completion Status by User Role")
ax[0].set_xlabel("User Role")
ax[0].set_ylabel("Count")

sns.countplot(x="Experience_Level", hue="Completion_Status", data=df, ax=ax[1])
ax[1].set_title("Completion Status by Experience Level")
ax[1].set_xlabel("Experience Level")
ax[1].set_ylabel("Count")

st.pyplot(fig)

# Conclusion
st.markdown("""
### Conclusion
The visualizations above highlight the potential challenges in the onboarding process, such as high abandonment rates at specific steps and differences in completion rates across user roles and experience levels. By leveraging Ziplyne's capabilities, these issues can be addressed to improve user retention and satisfaction.
""")
