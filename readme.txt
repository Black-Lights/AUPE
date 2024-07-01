Software Release Document
Software Name: AUPE RiskMonitor
Version: 1.0.0
Release Date: July 1, 2024
________________________________________
Overview
The AUPE Risk Monitor 1.0.0 is the inaugural release of this application, designed to provide robust data visualization tools for analyzing landslide risks in the Lombardy region of Italy at provincial level using the data provided by Italy’s ISPRA IdroGEO platform. This document outlines the features, installation instructions, known limitations, and other relevant details to help users and developers get started with the software.
Features
Dynamic Data Visualization
•	Bar and Pie Charts:
o	The application includes dynamic bar and pie charts for visualizing landslide risk data. Users can select risk types and levels to compare data across different regions.
•	Landslide Risk Data at Different Levels:
o	Visualize landslide risk data categorized by various risk levels such as low, medium, and high.
•	Geographic Visualization of Risks at Provincial Levels:
o	Provides a clear comparison of landslide risks across different provinces.
•	Interactive Choropleth Map:
o	Features an interactive map using Folium to display geographical data of landslide risks, allowing users to explore risk areas visually.

Key Capabilities
Efficient Data Fetching
•	Optimized data fetching from the Flask API to enhance performance and reduce loading times, ensuring a smoother user experience.
User-Friendly Interface
•	Designed with an intuitive user interface, including tab navigation and dropdown filters for easy data selection and comparison.
•	Responsive layout for compatibility across different screen sizes and devices.
Installation Instructions
Prerequisites
•	Windows (10 and above)
•	Internet connection
•	Ensure that Python 3.8 or later is installed on your system.
Installation Steps
1.	Download the Software:
o	Obtain the software package from the provided download link.
	Download link for AUPE RiskMonitor
Download ZIP file and extract it.
2.	Run the Installer: 
o	Navigate to the software directory.
o	Execute the install.bat file to begin the installation process.
o	This will automatically create a virtual environment and install the necessary dependencies.
o	The installation process may take approximately 10-12 minutes, depending on your device specifications. Please be patient.
3.	Start the Application: 
o	Once the installation is complete, you can start the application.
o	Open the AUPE_RiskMonitor.bat file located in the current directory to access the application.
Known Limitations
Loading Time
•	Initial Data Loading:
o	Initial data loading might take a few seconds due to the access of data on the cloud database (AWS- RDS PostgreSQL). Users are advised to be patient during this period.
Browser Compatibility
•	Compatibility Issues:
o	Some visualizations may not render correctly on older versions of Internet Explorer. It is recommended to use modern browsers like Chrome, Firefox, or Safari for the best experience.
Hardware Requirements
•	Minimum Specifications:
o	The application requires a minimum of 2GB RAM and a 1GHz processor for optimal performance. Running the software on lower-spec hardware may result in slower performance.
Configuration
Database Connection
•	The database configuration is set in the config.py file. Ensure the following settings are correct:
db_name = "se4g_proj"
user = "gis_admin"
password = "se4guser"
host = http://database-test1.cnuw2qoiq9mr.eu-north-1.rds.amazonaws.com
port = 5432
Support
For technical support or questions related to this release, please contact our support team at teamaupe@gmail.com.
Legal Notices
This software is provided under the terms of the [Team AUPE]. Please read the license agreement before using the software.
________________________________________
This document outlines the key details of the 1.0.0 release, providing a comprehensive overview of new features, enhancements, and other relevant information for users and developers.
