from citeas_api import get_citation_by_doi
from base_web_api_data import BaseWebAPIDataLoader

class SemanticScholarLoader(BaseWebAPIDataLoader):
    SS_key = None
    def __init__(self,SS_key):
        self.SS_key = SS_key
        super().__init__("https://api.semanticscholar.org/graph/v1/paper/search")
    def search_semantic(self, query, limit=15):
        # Lists to append research papers data separately
        titles = []
        authors = []
        years = []
        source_links = []
        abstracts = []
        citation_count = []
        journals = []
        dois = []
        
        headers = {
            "x-api-key": self.SS_key #Enter your SS_key here
        }
        params = {
            "query": query,
            "limit": limit, #by set limit you can retreive as much results as you want
            #Required fields
            "fields": "title,url,abstract,authors,citationStyles,journal,citationCount,year,externalIds",
        }

        data = self.make_request("", params=params, headers=headers)
        papers = data.get("data", [])
        
        # Extract data from each paper
        for paper in papers:
          titles.append(paper["title"])
          
          author = ", ".join(author["name"] for author in paper["authors"])
          authors.append(author)
          
          years.append(paper["year"])
          
          source_links.append(paper["url"])
          
          journal = paper["journal"] # API gives websites names as journals
          if journal and "name" in journal: # There is also (pages and volume) of journals and we want only names of journals
            journal_name = journal["name"]
            journals.append(journal_name) 
          else:
            # Sometimes there is no journal name present. So, In that case we store Journal name as Semantic
            journals.append("Semantic")
          
          citation_count.append(paper["citationCount"]) # Number of times the research paper cited
          
          abstract = paper["abstract"]
          
          external_ids = paper.get("externalIds", {}) # There are more Id's in "externalIds" but we only get DOI
          doi = external_ids.get("DOI")
          dois.append(doi)

          # To get citations we used "Citeas" API because by Semantic scholar API we don't get the citations of the research papers
          citation = get_citation_by_doi(doi) 
          answer_with_citation = f"{abstract} SOURCE: {citation}" # Combine abstracts with citations
          abstracts.append(answer_with_citation)

        return titles, authors, years, source_links, abstracts, journals, dois
