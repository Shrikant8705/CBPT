import streamlit as st
import pandas as pd
import numpy as np
import time

def app():
    page_bg_img="""

        <style>
        [data-testid="stAppViewContainer"]
           {
                background-image: url('https://c1.wallpaperflare.com/preview/906/249/93/forward-landscape-weather-nature.jpg');
                background-size: cover;
            }
        </style>
        """
    
    st.markdown(page_bg_img,unsafe_allow_html=True)

    st.header("What is a CloudBurst? ⛈️",divider='blue')
    expander= st.expander("See explanation")
    expander.write
    (
    "A cloudburst is an extreme weather phenomenon characterized by intense and sudden rainfall over a short duration within a localized area. These intense downpours often result in flash floods, landslides, and other hazardous conditions, posing significant risks to life, property, and the environment"
             )
    expander.image("https://mc.webpcache.epapr.in/mcms.php?size=large&in=https://mcmscache.epapr.in/post_images/website_326/post_28895076/full.jpeg")
    st.header("_Introduction_:")
    st.write("A cloudburst is an extreme weather phenomenon characterized by intense and sudden rainfall over a short duration within a localized area. These intense downpours often result in flash floods, landslides, and other hazardous conditions, posing significant risks to life, property, and the environment")
    st.header("_Causes_")
    st.write("Cloudbursts typically occur when warm, moisture-laden air rises rapidly into the atmosphere and encounters cooler air at higher altitudes. This rapid upward motion causes the moisture to condense rapidly, leading to the formation of towering cumulonimbus clouds. When these clouds become saturated with moisture, they release it in the form of heavy rainfall, often accompanied by thunder and lightning.")
    st.header('_Mitigation and Preparedness_:')
    st.write("Mitigating the impacts of cloudbursts requires a combination of proactive measures, including improved urban planning, implementation of early warning systems, construction of flood control infrastructure, and community-based disaster preparedness initiatives. By enhancing resilience and preparedness, communities can reduce the risk of loss of life and property during cloudburst events.")
    st.header("_Conclusion_:")
    st.write("Cloudbursts are powerful and unpredictable natural phenomena that can have devastating consequences for human communities and the environment. Understanding the causes, effects, and impacts of cloudbursts is essential for effective disaster risk management and climate adaptation efforts in vulnerable regions.")
    st.write("ThankYou!")
    st.write("Another Example Line")