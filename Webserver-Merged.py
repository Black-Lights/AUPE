#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
from flask import Flask, jsonify, send_file
import psycopg2
from psycopg2.extras import RealDictCursor
from config import db_name, user, password, host

# Initialize Flask application
app = Flask(__name__)

# Function to get database connection
def get_db_connection():
    try:
        # Establish connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host
        )
        return conn
    except psycopg2.Error as e:
        # Log error if connection fails
        app.logger.error(f"Error connecting to database: {e}")
        return None

# Define route to get landslide data for the map
@app.route('/map', methods=['GET'])
def get_landslide_data():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('''
        SELECT
            cod_reg,
            cod_rip,
            COD_PROV,
            ar_kmq,
            nome,
            uid,
            ar_fr_p3p4,
            ar_fr_p4,
            ar_fr_p3,
            ar_fr_p2,
            pop_fr_p4,
            pop_fr_p3,
            pop_fr_p2,
            ed_fr_p4,
            ed_fr_p3,
            ed_fr_p2,
            ar_frp3p4p,
            popfrp3p4p,
            ed_fr_p3p4,
            edfrp3p4p,
            ST_AsText(ST_SnapToGrid(geometry, 0.001)) as geom_wkt  -- Adjust 0.001 for your desired precision
        FROM dataset
    ''')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

# Define route to get landslide data with surface information
@app.route('/landslides/surface', methods=['GET'])
def get_landslides():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection error"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT ar_kmq, nome, ar_fr_p3p4, ar_fr_p2, ar_fr_p1, ar_fr_p3, ar_fr_p4, ar_fr_aa, ar_frp4_p, ar_frp3_p, ar_frp2_p,ar_frp1_p, ar_fraa_p, ar_frp3p4p FROM dataset;")
        landslides = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(landslides)
    except psycopg2.Error as e:
        # Log error if SQL query fails
        app.logger.error(f"Error executing SQL query: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Define route to get landslide data for map visualization
@app.route('/landslides/map', methods=['GET'])
def get_landslides_map():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection error"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT ar_kmq, nome, ar_fr_p3p4, ar_fr_p2, ar_fr_p1, ar_fr_p3, ar_fr_p4, ar_fr_aa, ar_frp4_p, ar_frp3_p, ar_frp2_p, ar_frp1_p, ar_fraa_p, ar_frp3p4p, pop_fr_p2, pop_fr_p1, pop_fr_p3, pop_fr_p4, pop_fr_aa, popfrp4_p, popfrp3_p, popfrp2_p, popfrp1_p, popfrp3p4p, popfr_p3p4, popfraa_p, ST_AsText(geometry) AS geometry_wkt FROM dataset;")
        landslides_map = cursor.fetchall()
        
        # Process each row to handle WKT geometry data
        for row in landslides_map:
            wkt_data = row['geometry_wkt']
            try:
                row['geometry'] = wkt_data  # Directly assign the WKT data
            except Exception as e:
                # Log error if processing WKT data fails
                app.logger.error(f"Error processing WKT data: {e}")
                row['geometry'] = None  # Handle or log this error as needed
            del row['geometry_wkt']

        cursor.close()
        conn.close()
        return jsonify(landslides_map)
    except psycopg2.Error as e:
        # Log error if SQL query fails
        app.logger.error(f"Error executing SQL query: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Define route to get landslide data with population information
@app.route('/landslides/population', methods=['GET'])
def get_landslides_population():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection error"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT ar_kmq,pop_fr_p2, pop_fr_p1, pop_fr_p3, pop_fr_p4, pop_fr_aa, popfrp4_p, popfrp3_p, popfrp2_p, popfrp1_p, popfrp3p4p, popfr_p3p4, popfraa_p, nome FROM dataset;")
        landslides_population = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(landslides_population)
    except psycopg2.Error as e:
        # Log error if SQL query fails
        app.logger.error(f"Error executing SQL query: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

# Main block to run the Flask application
if __name__ == '__main__':
    # Run the app with debugging enabled, on localhost and port 5000
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)


# In[ ]:





# In[ ]:




