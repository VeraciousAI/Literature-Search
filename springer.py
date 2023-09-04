import requests
from termcolor import colored

def search_springer(query):
  # Lists to append research papers data separately
  titles = []
  authors = []
  years = []
  abstracts = []
  dois = []
  journals = []
  source_links = []

  API_key = "enter_your_key"
  url = "http://api.springernature.com/"
  endpoint = "metadata/json"
  params = {
      "q": query,
      "api_key": API_key,
      "hl": "en", #language
      "p": 30  # Number of records
  }

  response = requests.get(url + endpoint, params=params)

  if response.status_code == 200:
      data = response.json()

  # Extract data from each paper
  for record in data["records"]:  
    title = record.get("title")
    titles.append(title)
  
    publicationName = record.get("publicationName") #journal names
    journals.append(publicationName)
  
    author = record.get("creators")
    author_names = ", ".join([a.get("creator") for a in author])
    authors.append(author_names)
  
    publicationDate = record.get("publicationDate") # The Springer API fetch wrong year (It fetch 2024 always)
    year = publicationDate.split("-")[0] # to skip (day, month) and get year only
    years.append(publicationDate)
  
    volume = record.get("volume")
    number = record.get("number")
  
    startingPage = record.get("startingPage")
    endingPage = record.get("endingPage")
    
    doi = record.get("identifier")
    dois.append(doi)
    
    url = record.get("url")[0]['value']
    source_links.append(url)
    
    abstract = record.get("abstract")

    # By Springer API we don't get the citations of the research papers. So, we create citations in harvard style by combining the data
    citation_parts = []
    if author_names:
      citation_parts.append(author_names)
    
    if publicationDate:
      citation_parts.append(str(publicationDate))
    
    if title:
      citation_parts.append(f"'{title}'")
    
    if publicationName:
      citation_parts.append(publicationName)
    
    if volume:
      citation_parts.append(f"vol. {volume}")
    
    if number:
      citation_parts.append(f"no. {number}")
    
    if startingPage and endingPage:
      citation_parts.append(f"pp. {startingPage}-{endingPage}")
    
    #Combine the abstracts with their citations
    citation = ", ".join(citation_parts)
    answer_with_citation = f"{abstract} SOURCE: {citation}"
    abstracts.append(answer_with_citation)
  
return titles, authors, years, source_links, abstracts, journals, dois
