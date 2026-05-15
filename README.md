# ComProg-Final-Project

Detection of Thermal Efficiency Degradation in Grid-Tied Inverters: A Comparative Study under Peak Irradiation Windows
Course: Computer Programming 1

Engineering Pillar: Inverter Efficiency Drops (REN-05)

Institution: Technological University of the Philippines – Manila

Student Information
Name: Ma. Rica Lianne P. Villarta

Student ID: TUPM-25-3364

Course/Section: BSECE 1-C

Professor: Engr. Gilfred Allen Madrigal

Project Overview
This project implements a robust Engineering Data Systems Pipeline to analyze and predict Anoxic Events (critical low-oxygen conditions) in aquaculture environments. By leveraging sensor telemetry, the system identifies correlations between rising temperatures and declining Dissolved Oxygen (DO) levels, which are vital for maintaining aquatic life.

Dataset Description
The analysis utilizes high-frequency sensor data from aquaculture ponds. The primary telemetry parameters include:

TEMP: Water Temperature (Celsius)

DO: Dissolved Oxygen (mg/L)

pH: Potential of Hydrogen

Ammonia/Nitrate: Chemical nutrient concentrations

Turbidity: Water clarity/suspended solids

Unique Filter Logic (Non-Duplicate Submission)
To satisfy the project’s integrity requirements, the data is programmatically sliced using the following unique engineering constraints:

Station Isolation: Data is strictly limited to Station 1 sensor nodes.

Temporal Constraint: Analysis is focused on the Month of June, representing the peak thermal stress period.

Critical Threshold: A filter is applied where DO < 6.5 mg/L to isolate pre-anoxic and anoxic conditions.

Engineering Justification: June exhibits the highest average temperatures; according to Henry's Law, as temperature increases, the solubility of oxygen in water decreases, making this the most critical period for electronics-based environmental monitoring.

 Software Architecture
The pipeline is built using Python 3.x and follows a modular Object-Oriented Programming (OOP) approach:

Ingestion Module: Robust CSV loading with try-except error handling.

Cleaning Module: Automated handling of sensor drift, null values, and duplicates.

Analysis Module: Statistical computation (Mean, Median, StdDev) using NumPy.

Visualization Module: Generation of 5 Static Graphs (.png) and 4 Animated Graphs (.gif) to track real-time oxygen decay.

 Project Purpose
The final output provides a decision-support system for aquaculture management, utilizing data-driven insights to prevent mass mortality in ponds due to oxygen depletion.

Developed as a Final Project requirement for Computer Programming 1 (2026)
