# python-ml-projects

This repository contains hands-on projects in machine learning, data science, web scraping, and image processing using Python. It is built as a practical learning portfolio with script-based and notebook-based workflows.

## Features

- Data analysis and visualization on real-world datasets
- Sentiment analysis using rule-based NLP
- Image recognition with face detection
- Web scraping from public websites

## Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- OpenCV
- BeautifulSoup, Requests
- Jupyter Notebook

## Project Structure

```text
python-ml-projects/
├── README.md
├── .gitignore
├── Notebook-demo.ipynb
├── Untitled.ipynb
├── Image Recognition/
│   ├── face-detection.py          # Face detection on a group image using OpenCV
│   ├── group-photo.webp
│   └── group-photo-copy.webp
├── Manipulate and Visualize Data/
│   ├── Global_Education.csv       # Dataset for exploratory data analysis
│   └── Load-Data.ipynb            # Data loading, cleaning, stats, and plots
├── ML-Python/
│   └── customer-service.py        # Interactive sentiment classification CLI
├── Sentiment Analysis/
│   ├── stockerbot-export.csv      # Stock tweet dataset
│   ├── stocks.ipynb               # Sentiment trend analysis notebook
│   ├── Untitled.ipynb
│   └── Untitled1.ipynb
└── Web-Scraping/
    ├── scraping-basics.py         # Basic Hacker News title scraping
    ├── scraping.py                # HN title + link + upvote extraction
    └── book-site.py               # Books-to-Scrape product extraction
```

## Setup Instructions

1. Clone the repository.

```bash
git clone https://github.com/vivekkushwahaofficial/python-ml-projects.git
cd python-ml-projects
```

2. Create and activate a virtual environment.

```bash
python -m venv .venv
# Windows (Git Bash)
source .venv/Scripts/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

3. Install required packages.

```bash
pip install pandas numpy matplotlib seaborn scikit-learn opencv-python requests beautifulsoup4 html5lib nltk jupyter
```

4. Download required NLTK resources once.

```bash
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('subjectivity'); nltk.download('movie_reviews')"
```

## How to Run

### Run Python Scripts

```bash
python "Image Recognition/face-detection.py"
python "ML-Python/customer-service.py"
python "Web-Scraping/scraping-basics.py"
python "Web-Scraping/scraping.py"
python "Web-Scraping/book-site.py"
```

### Run Jupyter Notebooks

```bash
jupyter notebook
```

Open and run notebooks from:

- Manipulate and Visualize Data
- Sentiment Analysis
- Root demo notebooks

## Future Improvements

- Add more ML models and experiments
- Improve UI for interactive workflows where relevant
- Deploy selected projects as web apps or APIs

## Author

- Name: Vivek Kumar
- GitHub: https://github.com/vivekkushwahaofficial
