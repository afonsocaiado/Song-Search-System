# 🎵 Lyrics and Music Information Retrieval System

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Solr](https://img.shields.io/badge/Solr-8.10-orange.svg)](https://solr.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Powered-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

An advanced information retrieval system built using Apache Solr for searching and retrieving song information and lyrics, with features for intelligent ranking, filtering, and recommendation.

## 🔍 Project Description

This repository implements a complete music information retrieval system that enables users to:

- Search for songs based on lyrics, artist, album, genre, and other metadata
- Get ranked results using advanced text analysis techniques
- Filter search results by various song attributes
- Explore music with intelligent query expansion and suggestions

The system includes data processing pipelines, a Solr-based search engine, and evaluation tools for measuring search quality.

### 🚀 Key Features

- **Advanced Text Processing**: Tokenization, stemming, and stopword removal optimized for lyrics
- **Query Expansion**: Automatic expansion of queries to improve recall
- **Intelligent Ranking**: Custom scoring model for relevance-based result ordering
- **Faceted Search**: Dynamic filtering of results by artist, genre, and year
- **Performance Evaluation**: Comprehensive evaluation of search quality using precision, recall, and other metrics

## 🧑‍💻 Project Team

- Afonso Caiado de Sousa
- Jose Miguel Macaes

## 🔧 Technologies

- **Apache Solr**: Core search platform with text analysis capabilities
- **Python**: Data processing, cleaning, and integration with external APIs
- **Docker**: Containerization for easy deployment and reproducibility
- **Spotify API**: Integration for enhanced music metadata

## 🗂️ Repository Structure

```
.
├── src/                  # Source code for data processing
│   ├── clean.py          # Data cleaning scripts
│   ├── combine.py        # Dataset combination utilities
│   ├── createSpotify.py  # Spotify API integration
│   └── extend.py         # Data enrichment tools
│
├── solr/                 # Solr configuration and deployment
│   ├── Dockerfile        # Docker configuration
│   ├── startup.sh        # Initialization script
│   ├── evaluation.py     # Search quality evaluation
│   └── queries/          # Sample queries for testing
│
├── docs/                 # Documentation
│   ├── milestone1/       # Initial project documentation
│   └── milestone3/       # Final project report and presentation
│
├── dataset/              # Raw dataset files
├── Makefile              # Build automation
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Docker
- Make (optional, for automated build)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lyrics-search-engine.git
   cd lyrics-search-engine
   ```

2. Build the dataset:
   ```bash
   make
   ```
   This will:
   - Combine the raw data sources
   - Clean and process the data
   - Extend the dataset with additional metadata

3. Build and run the Solr container:
   ```bash
   cd solr
   chmod +x startup.sh
   docker build . -t lyrics-search-engine
   docker run --name music_lyrics -p 8983:8983 -v ${PWD}/data:/data --rm lyrics-search-engine
   ```

4. Access the Solr interface:
   ```
   http://localhost:8983/solr/
   ```

## 📚 How to use

### Basic Search

1. Navigate to the Solr Query interface at `http://localhost:8983/solr/#/music/query`
2. Enter your search query in the "q" field
3. Specify additional parameters as needed
4. Click "Execute Query"

### Advanced Features

- **Field-Specific Search**: Use `lyrics:love` to search only in lyrics
- **Faceted Search**: Enable faceting for dynamic filtering
- **Boosting Fields**: Use `qf=title^2.0 lyrics^1.0` to prioritize title matches
- **Query Expansion**: Enable automatic query expansion for better recall

### Evaluation

Run the evaluation script to measure search quality:

```bash
cd solr
python evaluation.py
```

## 📊 Performance

The system has been evaluated using standard information retrieval metrics:

- Mean Average Precision (MAP): 0.85
- Mean Reciprocal Rank (MRR): 0.92
- Normalized Discounted Cumulative Gain (NDCG): 0.89

Detailed evaluation results are available in the [final project report](docs/milestone3/report-72.pdf).

## 🔗 References & Acknowledgements

- Comprehensive documentation in the [project report](docs/milestone3/report-72.pdf)
- Based on techniques from Information Retrieval course at FEUP
- Uses the [Million Song Dataset](http://millionsongdataset.com/) and [Genius Lyrics API](https://genius.com/api)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.