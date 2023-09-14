# Research-Sources-Search
## Description:
The Research Paper Search Script is a Python program designed to help users search for academic research papers based on a given query. It utilizes multiple sources, including Semantic Scholar, UCL Discovery, ArXiv, and Springer, to provide a comprehensive list of relevant research papers. This script allows users to quickly find academic papers related to their research interests, helping them stay up-to-date with the latest scholarly work in their field. There are 120 research papers fetched against one query, 30 research papers from each resource.

## Usage Instructions:

### 1. Prerequisites:
  - Ensure you have Python installed on your system.
  - Run the *requirements.text* file by command **pip install -r requirements.txt**

### 2. Semantic Scholar API Key (Required):
  - To use the script, you need a Semantic Scholar API key. You can obtain one from the Semantic Scholar website https://www.semanticscholar.org/api/

### 3. Springer API Key (Required):
  - To use the script, you need a Springer API key. You can obtain one from the Springer Nature website https://dev.springernature.com/signup

### 4. Running the Script:
  - Open your terminal or command prompt.
  - Navigate to the directory where the script is located.
  - Run the script with the command: **script_name.py "*your_query_here*"**.
  - Replace *"your_query_here"* with your research topic or query.

### 5. Script Execution:
  - The script will execute and start searching for research papers based on your query across various sources.
  - It will fetch paper information, including titles, authors, publication years, links, abstracts, journals, and DOIs.
  - The script will display the retrieved paper information in a formatted manner with different colors to make it more readable.

### 6.Customization (Optional):
  - You can customize the script to include or exclude specific data sources by commenting or uncommenting the corresponding lines in the script.

### 7. Batch Processing:
  - The script processes papers in batches to ensure efficient handling of large search results.
  - The default batch size is 3.
  - We display the first three research papers from each resource, then second three from all resources and so on.
  - You can modify the batch_size variable to control the number of papers processed in each batch.

## Notes:
  - Ensure that you have a reliable internet connection while running the script, as it fetches data from external sources.
  - You can adjust the script to fit your specific requirements or integrate it into larger projects as needed.
  - Please replace "script_name.py" with the actual name of the script you are using.

## Limitations:
  - Semantic Scholar API not fetching abstracts of all research papers. It returns abstracts as None for some reasearch papers. While on their website, the abstract is available.
  - Springer API gives constant valye of year for all research papers in *"publicationDate"* and that is "2024".

## Guidance:
  - Need guidance to overcome the response time. The response time of a Research Paper Search Script is 3 mins 30 secs approximately.

## Disclaimer:
**The Research Paper Search Script is a powerful tool for researchers, students, and anyone interested in accessing academic research papers quickly and efficiently. It streamlines the process of finding relevant scholarly content across multiple sources, making it an invaluable resource for staying informed and conducting in-depth research.**
