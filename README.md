# Review Insights Engine

Review Insights Engine is an **Aspect-Based Sentiment Analysis (ABSA)** system that analyzes movie reviews using **Natural Language Processing (NLP)**.

Instead of assigning one sentiment score to an entire review, the system identifies specific aspects such as *acting*, *story*, *visuals*, and *music*, then determines sentiment for each aspect individually.

The project includes a **Flask-powered web interface**, allowing users to upload custom CSV review files directly through the browser and instantly generate interactive sentiment reports.

---

## Project Highlights

* Aspect-Based Sentiment Analysis for movie reviews
* Aspect-level sentiment scoring
* Automatic insight generation
* Interactive HTML report generation
* Dynamic chart visualization
* CSV upload through web interface
* Professional themed UI for upload and report pages

---

## Features

### Aspect Extraction

Automatically identifies meaningful movie-related aspects such as acting, story, visuals, music, dialogue, and screenplay.

### Aspect-Level Sentiment Analysis

Scores each extracted aspect independently instead of assigning one sentiment label to the entire review.

### Insight Generation

Generates human-readable textual insights summarizing audience opinions.

### Visual Analysis

Creates sentiment charts including:

* Aspect Sentiment Distribution
* Top Positive vs Negative Aspects

### Automated HTML Report

Generates structured styled report pages containing:

* Movie summary
* Key insights
* Sentiment tables
* Visual charts

### Web CSV Upload Interface

Users can upload custom CSV files directly through browser UI without using terminal commands.

---

## Technologies Used

* Python
* Flask
* spaCy
* NLTK
* Pandas
* Matplotlib
* HTML/CSS

---

## NLP Pipeline

```text
CSV Input
   ↓
Preprocessing
   ↓
Aspect Extraction
   ↓
Aspect Filtering
   ↓
Sentiment Scoring
   ↓
Aspect Normalization
   ↓
Aspect Ranking
   ↓
Insight Generation
   ↓
Visualization & Report Generation
```

---

## Web Application Workflow

```text
Upload CSV File
      ↓
Flask Receives File
      ↓
Run NLP Pipeline
      ↓
Generate Charts + Report
      ↓
Display HTML Report in Browser
```

---

## Project Structure

```plaintext
Review Insights Engine/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── movies_reviews.csv
│   └── simple_review.csv
│
├── uploads/
├── outputs/
├── lexicons/
│
├── static/
│   ├── aspect_sentiment_chart.png
│   ├── top_aspects_chart.png
│   └── css/
│       └── theme.css
│
├── templates/
│   └── upload.html
│
├── src/
│   ├── preprocessing.py
│   ├── aspect_extraction.py
│   ├── aspect_filter.py
│   ├── sentiment_analysis.py
│   ├── aspect_normalizer.py
│   ├── aspect_ranking.py
│   ├── insight_generator.py
│   └── export_results.py
│
└── lexicons/
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/mohanv2005/Review-insight-engine.git
cd Review-insight-engine
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## Usage

### Run Web Application Version

```bash
python app.py
```

Then open browser:

```plaintext
http://127.0.0.1:5000
```

Upload your CSV file directly through the website interface.

---

### Run Command-Line Version

```bash
python main.py
```

Custom input/output:

```bash
python main.py --input data/movies_reviews.csv --output custom_results_folder
```

---

## Sample Data

Sample datasets are included in the `data/` folder:

* movies_reviews.csv
* simple_review.csv

These can be used directly for testing both the web and command-line versions.

---

## CSV Input Format

Your CSV file should follow this format:

```csv
movie,review_id,review_text
Inception,01,Great acting and amazing visuals
Inception,02,Story was confusing but music was excellent
```

Required columns:

* movie
* review_id
* review_text

---

## Output Generated

### In outputs/

* report.html
* aspect_scores.csv
* insights.txt

### In static/

* aspect_sentiment_chart.png
* top_aspects_chart.png

---

## Example Output Includes

* Movie title
* Summary paragraph
* Key insights
* Aspect sentiment table
* Sentiment charts
* Upload another CSV option

---

## Future Improvements

* Sarcasm and irony detection
* Transformer/BERT sentiment models
* Smarter aspect clustering
* Real-time review scraping from IMDb / Rotten Tomatoes
* Dashboard analytics with filters
* Download report as PDF

---

## License

This project is for academic and educational purposes.
