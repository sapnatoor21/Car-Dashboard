

# Car Dashboard

This repository provides an interactive **Car Dashboard** application built using **Streamlit** and **Plotly**. The dashboard displays key vehicle metrics, performance indicators, and simulated route information, offering an easy-to-use control interface. 

### Features

1. **Metrics Display**:
   - **Speed**: Displays the current speed in miles per hour (e.g., "60 mph").
   - **Fuel Level**: Shows fuel level as a percentage with a change indicator (delta).
   - **Distance**: Displays the distance traveled in miles with a delta change.

2. **Real-time Data Visualization**:
   - **Speed and RPM over Time**: Line chart of speed and RPM values over a 10-second period, visualized with Plotly for dynamic interactivity.

3. **Performance Indicators**:
   - **Oil Pressure and Temperature Gauges**: Visual representations of oil pressure and engine temperature using Streamlit's `progress` bar as gauges.

4. **Route Mapping**:
   - A simple route map indicating two locations in San Francisco using Streamlit’s built-in map function.

5. **Engine Control**:
   - Buttons to **Start** and **Turn Off** the engine, providing an interactive control feature.

### How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd car-dashboard
   ```
3. Install required dependencies:
   ```bash
   pip install streamlit plotly pandas numpy
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Screenshots

- **Main Dashboard**: Metrics and line chart of Speed and RPM.
- **Performance Gauges**: Oil pressure and temperature gauges.
- **Route Map**: Basic route visualization.
- **Control Panel**: Engine control buttons for simulation.

### Technologies Used

- **Streamlit**: For creating the web interface.
- **Plotly**: For interactive and dynamic charting.
- **Pandas** and **NumPy**: For data handling and generation of sample metrics.

### Future Enhancements

- Add more interactive controls for real-time adjustments.
- Integrate live data streaming for metrics.
- Improve map integration with additional route features.

---

This description provides an overview of the Car Dashboard project, including setup instructions, features, and future enhancement ideas.
