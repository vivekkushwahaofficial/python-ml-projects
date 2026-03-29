# Python ML Projects Collection

A beginner-friendly, portfolio-ready collection of Python mini-projects covering machine learning basics, sentiment analysis, computer vision, data exploration, and web scraping.

## Overview

This repository demonstrates practical data and automation workflows using real datasets and public websites:

- Face detection in images with OpenCV.
- Rule-based sentiment analysis for text and stock-related tweets using NLTK VADER.
- Data loading, cleaning, and visualization with pandas, seaborn, and matplotlib.
- Web scraping of article and product metadata using requests and BeautifulSoup.

It is designed as a learning repository where each folder focuses on one applied topic.

## Features

- Image face detection using Haar cascades.
- Interactive sentiment classification from user input.
- Notebook-driven sentiment analysis of stock tweet data.
- Data exploration for a global education dataset.
- Web scraping examples for news headlines and book metadata.
- Notebook demos for plotting and visualization basics.

## Tech Stack

- Language: Python 3.x
- Core libraries:
  - OpenCV (cv2)
  - NLTK (VADER SentimentIntensityAnalyzer)
  - pandas
  - matplotlib
  - seaborn
  - requests
  - BeautifulSoup4
  - html5lib parser
- Format: Python scripts (.py), Jupyter notebooks (.ipynb), CSV datasets

## Project Structure

```text
python-ml-projects/
├── README.md
├── Notebook-demo.ipynb
├── Untitled.ipynb
├── Image Recognition/
│   └── face-detection.py
├── Manipulate and Visualize Data/
│   ├── Global_Education.csv
│   └── Load-Data.ipynb
├── ML-Python/
│   └── customer-service.py
├── Sentiment Analysis/
│   ├── stockerbot-export.csv
│   ├── stocks.ipynb
│   ├── Untitled.ipynb
│   └── Untitled1.ipynb
└── Web-Scraping/
    ├── book-site.py
    ├── scraping-basics.py
    └── scraping.py
```

## Key Scripts and Notebooks

- `Image Recognition/face-detection.py`
  - Loads an image, detects faces, draws rectangles, and displays results.
- `ML-Python/customer-service.py`
  - Runs a command-line loop that labels messages as Positive, Negative, or Neutral.
- `Web-Scraping/scraping-basics.py`
  - Extracts and prints Hacker News titles.
- `Web-Scraping/scraping.py`
  - Extracts title, link, and upvotes from Hacker News posts.
- `Web-Scraping/book-site.py`
  - Scrapes travel books (title, price, rating) from books.toscrape.com.
- `Manipulate and Visualize Data/Load-Data.ipynb`
  - Loads and explores global education data with summary stats and visualizations.
- `Sentiment Analysis/stocks.ipynb`
  - Loads stock tweet data, computes sentiment scores, and plots sentiment trends.

## Installation

1. Clone the repository.
2. Open the project in VS Code or Jupyter.
3. Create a virtual environment.
4. Install dependencies.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install opencv-python nltk pandas matplotlib seaborn requests beautifulsoup4 html5lib jupyter
```

5. Download required NLTK resources once:

```python
import nltk
nltk.download("vader_lexicon")
nltk.download("subjectivity")
nltk.download("movie_reviews")
```

## How to Run

### 1) Face Detection

```bash
python "Image Recognition/face-detection.py"
```

Notes:
- Keep an input image named `group-photo.webp` in the same working directory used by the script.
- Press any key in the image window to close.

### 2) Customer Sentiment CLI

```bash
python "ML-Python/customer-service.py"
```

Type messages in the console and receive sentiment labels.

### 3) Web Scraping Scripts

```bash
python "Web-Scraping/scraping-basics.py"
python "Web-Scraping/scraping.py"
python "Web-Scraping/book-site.py"
```

### 4) Jupyter Notebooks

```bash
jupyter notebook
```

Then open and run:
- `Manipulate and Visualize Data/Load-Data.ipynb`
- `Sentiment Analysis/stocks.ipynb`
- `Notebook-demo.ipynb`

## Example Output

### Customer Sentiment CLI

```text
Message: I really love this product
Positive Comment!

Message: This service is terrible
Negative Comound!

Message: It is okay
Neutral Comment
```

### Web Scraping

`scraping.py` prints a Python list of dictionaries similar to:

```text
[
  {'title': 'Example post title', 'link': 'https://example.com', 'upvotes': '123 points'},
  {'title': 'Another post', 'link': 'https://example.org', 'upvotes': '45 points'}
]
```

### Face Detection

A window displays the input group photo with blue rectangular boxes around detected faces.

## Future Improvements

- Add a `requirements.txt` for reproducible setup.
- Add command-line arguments for input/output paths in scripts.
- Standardize spelling and output labels in sentiment scripts.
- Save results to CSV/JSON for scraping and analysis workflows.
- Add unit tests for sentiment and scraping logic.
- Add notebook markdown explanations and final insights per analysis.
- Add Docker support for environment consistency.

## Author

Vivek Kushwaha (update this section with your preferred GitHub profile link and contact details).
