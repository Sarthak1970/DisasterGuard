# Disaster Guard

## Overview
**Disaster Guard** is a web application designed for the early reporting of natural disasters. The platform enables users to report disaster zones, aiding in relief efforts. It leverages AI/ML models for **fake news detection**, **NLP-based sentiment analysis**, and **image/video processing**. Additionally, it incorporates **location-based APIs** to provide real-time geolocation data for disaster reports.

## Key Features
- **User-Generated Reports:** Users can submit disaster-related incidents with descriptions, images, and videos.
- **Sentiment Analysis:** NLP techniques analyze the severity of user-reported disasters.
- **Fake News Detection:** AI models validate disaster-related news and prevent misinformation.
- **Geolocation Integration:** Reports include real-time location data using GPS APIs.
- **Real-Time Data Aggregation:** Collects disaster reports from social media, news portals, and other sources.
- **Landslide Prediction System (Upcoming Feature):** Implements ML-based real-time monitoring tools for landslide prediction and alerts.

## Technologies Used
- **Frontend:** React.js, Tailwind CSS
- **Backend:**  Flask (Python)
- **Machine Learning Models:** NLP-based sentiment analysis, Fake News Classification
- **Geolocation APIs:** Google Maps API 

## Installation & Setup
### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/disaster-guard.git
   cd disaster-guard/backend
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
   pip install -r requirements.txt
   ```
3. Run the backend server:
   ```sh
   uvicorn main:app --reload  # If using FastAPI
   cd .\Backend\
   python app.py  # If using Flask
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd ../Client
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend development server:
   ```sh
   npm run dev
   ```

## License
This project is licensed under the MIT License.

---
### Contact
For queries or collaboration, reach out at: **your-email@example.com**
