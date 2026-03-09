
# Review Insights Engine 🎬

Review Insights Engine is an **Aspect-Based Sentiment Analysis (ABSA)** system that analyzes movie reviews using **Natural Language Processing (NLP)**.

Instead of assigning a single sentiment score to an entire review, the system extracts **specific aspects** (such as *acting*, *story*, *visuals*, or *music*) and determines the sentiment associated with each one.

This allows the system to generate **structured insights about what audiences liked and disliked in a movie.**

---

## 🚀 Features

### Aspect Extraction
Automatically identifies important elements discussed in reviews such as acting, story, visuals, and music.

### Aspect-Level Sentiment Analysis
Calculates sentiment for **each aspect individually**, instead of scoring the entire review as a single sentiment.

### Insight Generation
Produces human-readable insights summarizing audience opinions about the movie.

### Visual Analysis
Generates charts showing sentiment distribution and top positive/negative aspects.

### Automated Report
Creates a complete **HTML report** summarizing the analysis results.

---

## 🛠️ Technologies Used

* **Python** – Core programming language
* **spaCy** – Tokenization, POS tagging, and dependency parsing
* **NLTK** – Lexicon-based sentiment scoring
* **Pandas** – Data processing and aggregation
* **Matplotlib** – Visualization and charts

---

## ⚙️ NLP Pipeline

The system processes reviews through the following pipeline:

```text
reviews.csv
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

## 💻 Installation

1. Clone the repository:
```bash
git clone [https://github.com/mohanv2005/Review-insight-engine.git](https://github.com/mohanv2005/Review-insight-engine.git)
cd Review-insight-engine

```


2. Install the required dependencies:
```bash
pip install -r requirements.txt

```


3. Download the spaCy English language model:
```bash
python -m spacy download en_core_web_sm

```



---

## 💡 Usage

To run the pipeline on the default dataset (`data/movies_reviews.csv`) and generate the HTML report in the default `outputs/` folder, execute the main script:

```bash
python main.py

```

You can also specify custom input files and output directories using command-line arguments:

```bash
python main.py --input data/movies_reviews.csv --output custom_results_folder

```

---

## 📌 Future Improvements

Potential improvements for the system include:

* Handling sarcasm and irony in reviews.
* Improving aspect detection with advanced dependency parsing.
* Spelling correction for noisy user reviews.
* Integrating machine learning models for sentiment prediction.

