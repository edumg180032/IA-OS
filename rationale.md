# RATIONALE.MD
## Dependencies
The following libraries are required to run the script:

os
requests
xml.etree.ElementTree
matplotlib.pyplot
collections.Counter
wordcloud.WordCloud
nltk
nltk.corpus.stopwords
fitz
re

## 

The code is designed to analyze a set of PDF files in a specific directory and obtain information from them. The script begins by importing several libraries, including os, requests, xml.etree.ElementTree, matplotlib.pyplot, collections, wordcloud, nltk, and fitz.

Next, the script defines the directory in which the PDFs are located and sets up several lists to store the number of URLs, images, and abstract words found in each PDF. The script then defines a function to send a request to Grobid, a tool for extracting information from PDFs. Another function is also defined to create a word cloud from the abstracts of all the PDFs.

The script then iterates through each PDF file in the directory and sends a request to Grobid to extract information. The script then counts the number of images in each PDF using fitz. Additionally, the script searches each PDF for URLs using regular expressions and creates a list of URLs for each PDF. The script also extracts the abstract of each PDF using ElementTree and filters out any stop words using nltk.

After analyzing all the PDFs in the directory, the script combines all the abstracts into a single string and creates a word cloud from the word frequencies. Finally, the script creates a bar chart to show the number of images found in each PDF. The chart and the word cloud are saved in the same directory as the PDFs.

In conclusion, this script is useful for obtaining information about multiple PDFs in a directory, including the number of images, URLs, and abstract words. The script also provides visualizations in the form of a word cloud and a bar chart.
