import streamlit as st
import pandas as pd
import plotly.express as px

# Load the generated data
df = pd.read_csv("onboarding_large_dummy_data.csv")

# Page Configuration
st.set_page_config(page_title="Onboarding Analysis", layout="wide")

# Sidebar Navigation
st.sidebar.title('Navigation')
sections = ["Executive Summary", "Introduction", "Business Problem", "Proposed Solution with Ziplyne", 
            "Implementation Plan", "Expected Outcomes", "Conclusion", "Appendices", "Analysis"]
selection = st.sidebar.radio("Go to", sections)

# Function to display content for each section
def display_section(section):
    if section == "Executive Summary":
        st.header("Executive Summary")
        st.write("""
        The onboarding process is a critical touchpoint for new users, yet many businesses struggle with high drop-off rates and inconsistent user experiences. 
        This case study explores how Ziplyne, a digital adoption platform, can revolutionize the onboarding experience by providing interactive, personalized, and engaging walkthroughs. 
        By implementing Ziplyne, businesses can expect to see improved user engagement, faster time-to-value, and increased customer satisfaction.
        """)
    elif section == "Introduction":
        st.header("Introduction")
        st.write("""
        Introduction to the company and the importance of onboarding.
        Brief description of Ziplyne and its functionalities as a digital adoption platform.
        """)
    elif section == "Business Problem":
        st.header("Business Problem")
        st.write("""
        Detailed explanation of the current onboarding challenges.
        - High drop-off rates during onboarding.
        - Inconsistent onboarding experiences.
        - Lack of user engagement and understanding of product features.
        - Delays in time-to-value for new users.
        Impact of these challenges on business metrics (e.g., user retention, customer satisfaction, revenue).
        """)
    elif section == "Proposed Solution with Ziplyne":
        st.header("Proposed Solution with Ziplyne")
        st.write("""
        **Solution Overview**: How Ziplyne can address the onboarding challenges.
        - Interactive walkthroughs and guided tours.
        - In-app help and support features.
        - Personalized onboarding experiences based on user roles.
        - Real-time analytics and feedback collection.
        """)
    elif section == "Implementation Plan":
        st.header("Implementation Plan")
        st.write("""
        **Step 1: Needs Assessment**
        - Conduct user research to understand different user personas and their onboarding needs.
        - Define success metrics for the onboarding process.

        **Step 2: Design and Customization**
        - Design interactive walkthroughs for key features.
        - Customize onboarding flows for different user roles and levels of expertise.
        - Integrate multimedia elements (videos, images, tooltips) to enhance engagement.

        **Step 3: Integration with Existing Systems**
        - Ensure seamless integration of Ziplyne with the current product infrastructure.
        - Set up user tracking and analytics to monitor onboarding progress.

        **Step 4: Testing and Feedback**
        - Conduct beta testing with a small group of new users.
        - Collect feedback and make necessary adjustments.

        **Step 5: Full-Scale Rollout**
        - Launch the new onboarding process for all new users.
        - Provide training for support and customer success teams.

        **Step 6: Continuous Improvement**
        - Monitor onboarding metrics and user feedback.
        - Continuously update and improve onboarding content and flows based on data insights.
        """)
    elif section == "Expected Outcomes":
        st.header("Expected Outcomes")
        st.write("""
        - Improved user engagement and reduced drop-off rates during onboarding.
        - Faster time-to-value for new users.
        - Increased user satisfaction and retention.
        - Enhanced ability to gather user insights and improve product features.
        """)
    elif section == "Conclusion":
        st.header("Conclusion")
        st.write("""
        Recap of the business problem and the proposed solution.
        Final thoughts on the impact of an improved onboarding process on overall business success.
        """)
    elif section == "Appendices":
        st.header("Appendices")
        st.write("""
        - Detailed user research findings.
        - Screenshots or mockups of the proposed onboarding flows.
        - Technical documentation for integration.
        """)
    elif section == "Analysis":
        st.header("Analysis of Onboarding Process")

        # Visualization: Completion Time by Step
        st.subheader("Completion Time by Step")
        fig1 = px.box(df, x="Step", y="Completion_Time", color="Completion_Status",
                      title="Completion Time Distribution by Onboarding Step",
                      labels={"Step": "Onboarding Step", "Completion_Time": "Completion Time (minutes)",
                              "Completion_Status": "Completion Status"})
        st.plotly_chart(fig1)

        # Visualization: Completion Status Distribution
        st.subheader("Completion Status Distribution")
        fig2 = px.histogram(df, x="Step", color="Completion_Status", barmode="group",
                            title="Completion Status Distribution by Onboarding Step",
                            labels={"Step": "Onboarding Step", "Completion_Status": "Completion Status"})
        st.plotly_chart(fig2)

        # Visualization: Role and Experience Level Impact
        st.subheader("Impact of User Role and Experience Level")
        fig3 = px.histogram(df, x="User_Role", color="Completion_Status", barmode="group",
                            title="Completion Status by User Role",
                            labels={"User_Role": "User Role", "Completion_Status": "Completion Status"})
        fig4 = px.histogram(df, x="Experience_Level", color="Completion_Status", barmode="group",
                            title="Completion Status by Experience Level",
                            labels={"Experience_Level": "Experience Level", "Completion_Status": "Completion Status"})

        st.plotly_chart(fig3)
        st.plotly_chart(fig4)

# Display the selected section
display_section(selection)
