# Workout Tracker
## About
This Exercise Tracker application automates the process of logging your daily workouts. It uses the Nutritionix API to recognize and quantify the exercises you perform and then records the results into a Google Sheets document via the Sheety API. This allows users to keep an organized and easily accessible log of their workouts, including details like the type of exercise, duration, and calories burned. Ideal for fitness enthusiasts who want to keep a close eye on their training and progress.

## Features
- Exercise Recognition: Leverages the power of the Nutritionix API to identify numerous types of physical activities from natural language input.-
- Data Logging: Automatically records each exercise session's details, including date, time, type, duration, and calories burned into a Google Sheets spreadsheet.
- Secure Authentication: Uses basic HTTP authentication to ensure secure access to the Sheety API.
- Environmental Configuration: API keys and endpoint URLs are securely stored using environment variables to protect sensitive information.

## How to Set Up and Use
### Prerequisites
- Python 3.6 or higher
- requests library installed
- An account and API credentials for Nutritionix
- An account and setup on Sheety for accessing Google Sheets
- Environment variables set for API_ID, API_KEY, and SHEETY_ENDPOINT

## Clone the Repository
Start by cloning the repository to your local machine. You can do this using the following command:

```bash
git clone https://github.com/yourusername/exercise-tracker.git
cd exercise-tracker
```

# Install Dependencies
Install the required Python packages by running:
```bash
pip install requests
```
## Set Environment Variables
You need to set up the following environment variables in your system:

- API_ID: Your Nutritionix application ID.
- API_KEY: Your Nutritionix application key.
- SHEETY_ENDPOINT: The endpoint URL of your Sheety API for updating your Google Sheets.

## Running the Application
Once all the setup is done, you can run the application by executing:
```bash
python exercise_tracker.py
```

Follow the on-screen prompts to input your exercises and the application will handle logging them into your Google Sheets.

## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

