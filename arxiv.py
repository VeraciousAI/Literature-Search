import arxiv
import urllib.request
from bs4 import BeautifulSoup
from citeas_api import get_citation_by_doi

def search_arxiv(query):
  # Lists to append research papers data separately
  titles = []
  authors = []
  years = []
  abstracts = []
  dois = []
  journals = []
  source_links = []
  
  search = arxiv.Search(
  query = query,
  max_results = 30,
  sort_by = arxiv.SortCriterion.Relevance, # Sort by Relevance
  sort_order = arxiv.SortOrder.Descending
  )
  arxiv_papers = list(search.results())

  # Extract data from each paper
  for result in arxiv_papers:
    title = result.title
    titles.append(title)
    
    author = ", ".join([author.name for author in result.authors])
    authors.append(author)
    
    published_date = result.published.strftime("%Y")
    years.append(published_date)
    
    url = result.links
    links = next(link for link in url if link.rel == 'alternate').href
    source_links.append(links)
    
    journal = result.journal_ref
    if journal:
      # For some papers there is no journal name. In that case we store journal name as "arxiv.org"
     journals.append(journal)
    else:
      journals.append("arxiv.org")
  
  # Now, we scrape the arxiv.org to fetch the DOI and abstracts from the links because Arxiv API not able to fetch the DOI of papers
  for url in source_links:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req).read()
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        try:
            # We also get abstracts by Arxiv API but we want to combine them with citations thats why, we also scrape them
            abstract = soup.find('blockquote', {'class': 'abstract'}).text.strip()
            doi_link = soup.find("a", href=lambda href: href and "doi.org" in href)
            if doi_link:
                doi = doi_link.get("href")
                doi_identifier = doi.replace("https://doi.org/", "")
                dois.append(doi_identifier)
                # To get citations we used "Citeas" API because by Arxiv API don't get the citations of the papers
                citation = get_citation_by_doi(doi_identifier)
            else:
                citation = url
                print("DOI link not found.")
            
            if abstract != "":
                answer_with_citation = f"{abstract} SOURCE: {citation}" # Combine abstracts with citations
                abstracts.append(answer_with_citation)
        except:
          pass
    #to avoid HTTP and URL Errors
    except urllib.error.HTTPError:
        pass
    except urllib.error.URLError:
        pass
  
  return titles, authors, years, source_links, abstracts, journals, dois
