# Review Insights Engine 🎬

Review Insights Engine is an Aspect-Based Sentiment Analysis (ABSA) tool that analyzes movie reviews using Natural Language Processing (NLP). 

Instead of just assigning a single positive or negative score to an entire review, this system extracts specific aspects (like *acting*, *story*, *cinematography*, or *soundtrack*) and evaluates the sentiment for each individual component using a custom lexicon-based approach.

## 🚀 Features
* **Aspect Extraction:** Automatically identifies key elements discussed in the text.
* **Granular Sentiment Scoring:** Assigns sentiment scores to individual aspects rather than the overall text.
* **Insight Generation:** Ranks aspects and generates a comprehensive breakdown of the review's strengths and weaknesses.

## 🛠️ Technologies Used
* **Python** - Core programming language
* **spaCy** - Industrial-strength NLP for tokenization, POS tagging, and dependency parsing
* **NLTK** - Used for the custom lexicon-based sentiment scoring
* **Pandas** - Data manipulation, filtering, and aggregation

## ⚙️ The NLP Pipeline



The data flows through the following sequential process:

1. **Input:** `reviews.csv` (Raw review text data)
2. **Preprocessing:** Text cleaning, tokenization, and stop-word removal.
3. **Aspect Extraction:** Identifying nouns and noun phrases representing movie aspects.
4. **Aspect Filtering:** Removing irrelevant or low-frequency terms.
5. **Sentiment Scoring:** Calculating polarity scores for adjectives/adverbs modifying the extracted aspects.
6. **Aspect Normalization:** Grouping similar terms (e.g., *storyline*, *plot*, *narrative*).
7. **Aspect Ranking:** Sorting aspects by frequency and overall sentiment impact.
8. **Insight Generation:** Outputting the final aspect-based summary.

<!-- ## 💻 Installation & Setup
*(Provide instructions on how to clone the repository and install dependencies)*

```bash
git clone [https://github.com/yourusername/review-insights-engine.git](https://github.com/yourusername/review-insights-engine.git)
cd review-insights-engine
pip install -r requirements.txt
python -m spacy download en_core_web_sm -->