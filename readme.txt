# AUPE RiskMonitor

![AUPE RiskMonitor Logo](path/to/logo.png)

**Version:** 1.0.0  
**Release Date:** July 1, 2024

---

## Overview
The AUPE RiskMonitor 1.0.0 is the inaugural release of this application, designed to provide robust data visualization tools for analyzing landslide risks in the Lombardy region of Italy at the provincial level using data provided by Italy’s ISPRA IdroGEO platform. This document outlines the features, installation instructions, known limitations, and other relevant details to help users and developers get started with the software.

---

## Features

### Dynamic Data Visualization
- **Bar and Pie Charts:**
  - Dynamic bar and pie charts for visualizing landslide risk data. Users can select risk types and levels to compare data across different regions.
- **Landslide Risk Data at Different Levels:**
  - Visualize landslide risk data categorized by various risk levels such as low, medium, and high.
- **Geographic Visualization of Risks at Provincial Levels:**
  - Provides a clear comparison of landslide risks across different provinces.
- **Interactive Choropleth Map:**
  - Interactive map using Folium to display geographical data of landslide risks, allowing users to explore risk areas visually.

### Key Capabilities
- **Efficient Data Fetching:**
  - Optimized data fetching from the Flask API to enhance performance and reduce loading times, ensuring a smoother user experience.
- **User-Friendly Interface:**
  - Intuitive user interface, including tab navigation and dropdown filters for easy data selection and comparison.
  - Responsive layout for compatibility across different screen sizes and devices.

---

## Installation Instructions

### Prerequisites
- Windows (10 and above)
- Internet connection
- Python 3.8 or later

### Installation Steps
1. **Download the Software:**
   - Obtain the software package from the provided [download link](https://github.com/Black-Lights/AUPE.git).
   - Download the ZIP file and extract it.
2. **Run the Installer:**
   - Navigate to the software directory.
   - Execute the `install.bat` file to begin the installation process.
   - This will automatically create a virtual environment and install the necessary dependencies.
   - The installation process may take approximately 10-12 minutes, depending on your device specifications. Please be patient.
3. **Start the Application:**
   - Once the installation is complete, you can start the application.
   - Open the `AUPE_RiskMonitor.bat` file located in the current directory to access the application.

---

## Known Limitations

### Loading Time
- **Initial Data Loading:**
  - Initial data loading might take a few seconds due to the access of data on the cloud database (AWS-RDS PostgreSQL). Users are advised to be patient during this period.

### Browser Compatibility
- **Compatibility Issues:**
  - Some visualizations may not render correctly on older versions of Internet Explorer. It is recommended to use modern browsers like Chrome, Firefox, or Safari for the best experience.

### Hardware Requirements
- **Minimum Specifications:**
  - The application requires a minimum of 2GB RAM and a 1GHz processor for optimal performance. Running the software on lower-spec hardware may result in slower performance.

---

## Configuration

### Database Connection
- The database configuration is set in the `config.py` file. Ensure the following settings are correct:
  ```python
  db_name = "se4g_proj"
  user = "gis_admin"
  password = "se4guser"
  host = "http://database-test1.cnuw2qoiq9mr.eu-north-1.rds.amazonaws.com"
  port = 5432


## Support
- For technical support or questions related to this release, please contact our support team at teamaupe@gmail.com.

## Legal Notices
- This software is provided under the terms of the [Team AUPE]. Please read the license agreement before using the software.
