# 🎵 Musical Habits Dashboard: Analyzing Springfield and Shelbyville 🎧
## 📖 Project Overview
This project dives into the musical preferences and behaviors of users in Springfield and Shelbyville. Using a dataset of online music streaming activity, the goal was to validate the hypothesis:

"User activity differs depending on the day of the week and the city."

The analysis was conducted using Python for data preprocessing and hypothesis testing. The findings were summarized in a step-by-step process, providing insights into user behavior across the two cities.

🛠 Step-by-Step Implementation
1. Data Description
The dataset contained 65,079 entries and included the following columns:

user_id: Unique identifier for the user.
track: Title of the song.
artist: Name of the artist.
genre: Genre of the song.
city: City where the user resides.
time: Exact time the song was played.
day: Day of the week the song was played.
Key Observations:
There were missing values in track, artist, and genre.
The time and day columns were stored as strings and required conversion for accurate analysis.
Implicit duplicates were found in the genre column.
2. Data Preprocessing
2.1 Header Formatting
Converted all column names to lowercase.
Removed spaces and applied snake_case for consistency.
2.2 Handling Missing Values
Replaced missing values in track, artist, and genre with "unknown."
2.3 Removing Duplicates
Explicit duplicates: Removed using the drop_duplicates() method.
Implicit duplicates in genre: Corrected variations like "hip," "hop," and "hip-hop" into "hiphop."
3. Hypothesis Testing
3.1 Total Songs Played per City
Springfield had over twice as many plays as Shelbyville:

Springfield: 42,741 plays
Shelbyville: 18,512 plays
3.2 Total Songs Played by Day
Analyzed activity for Monday, Wednesday, and Friday:

Friday had the highest activity, closely followed by Monday.
Wednesday had the least activity.
3.3 Daily City-Specific Analysis
Created a function, number_tracks(day, city), to calculate the number of plays for a specific day and city. Results:

City	Monday	Wednesday	Friday
Springfield	15,740	11,056	15,945
Shelbyville	5,614	7,003	5,895
## 🔍 Conclusions
The hypothesis was validated. Significant differences were observed in user activity between the cities and across days of the week:

Springfield had consistently higher activity across all days.
Shelbyville had its highest activity on Wednesday, while this was Springfield's least active day.
## 🚀 Learnings and Next Steps
Data Quality: Ensuring consistent formatting and handling missing values were key to accurate analysis.
Future Enhancements:
Incorporate additional datasets for broader insights.
Apply statistical hypothesis testing for more robust conclusions.
This project highlighted the importance of understanding user behavior through data analysis, paving the way for informed decision-making in music streaming services.
