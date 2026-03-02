# SearchEngine_&_InformationRetrieval

## Topic -- Web Page Scraper

This project scrapes a web page using web scraping techniques and extracts useful information from a given URL.

---

##  Project Description

The program:

- Accepts a single URL as a command-line argument
- Fetches webpage content using an HTTP request
- Extracts the page title
- Extracts complete body text
- Extracts all unique hyperlinks from the page
- Handles errors gracefully if the URL is invalid

---

## Concepts Used

- Web Scraping (BeautifulSoup, requests)
- HTML Parsing
- Command Line Arguments (`sys`)
- Exception Handling
- Sets (for storing unique links)
- Basic String Handling

---

## Libraries Used

```python
from bs4 import BeautifulSoup
import requests
import sys
import re
