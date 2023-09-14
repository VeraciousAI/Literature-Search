import requests
from bs4 import BeautifulSoup

def search_discovery(query,answersCount=1,papersCount=15):
    # Lists to append research papers data separately
    titles = []
    authors = []
    years = []
    abstracts = []
    journals = []
    dois = []
    source_links = []

    # Set range as how many pages you want to scrape
    for page_num in range(1,3):
        search_url = f"https://search2.ucl.ac.uk/s/search.html?query={query}&collection=ucl-discovery&f.Type%7CT=Article&page={page_num}"

        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            ul_tag = soup.find('ul', id='fb-results')

            if ul_tag:
                li_tags = ul_tag.find_all('li')
                for li_tag in li_tags:
                    anchor_tag = li_tag.find('a', title=True)
                    if anchor_tag:
                        url = anchor_tag['title']
                        source_links.append(url)
                        
                        title = anchor_tag.get_text(strip=True)
                        titles.append(title)
                        
                        author_names = li_tag.find(text=True, recursive=False).strip()
                        author_names = ' '.join(author_names.split()[:-1])
                        authors.append(author_names)
                        
                        span_tag = li_tag.find('span', style='font-style:italic')
                        year = span_tag.get_text(strip=True)[-5:-1]
                        years.append(year)
                        
                        journal = span_tag.get_text(strip=True).split(',')[0]
                        journals.append(journal)
                        
                        citation = li_tag.get_text(strip=True)
                        citation = ' '.join(citation.split())
                        full_citation = author.replace("Full text available", "")
                        
                        answersCount+=1
                        if answersCount >= papersCount:  # Extract certain numbers of papers only
                            break

                        response = requests.get(url)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.content, "html.parser")
                            div = soup.find('div', class_='ep_summary_content_main')
                            if div:
                                a_tag = div.find('a')
                                doi = a_tag.get_text(strip=True)
                                dois.append(doi)
                            
                            abstract_tag = soup.find('h2', class_='ep_block', string='Abstract')
                            if abstract_tag:
                                abstract = abstract_tag.find_next('p').get_text()
                                if abstract != "":
                                    answer_with_citation = f"{abstract} SOURCE: {full_citation}" # Combine abstracts with citations
                                    abstracts.append(answer_with_citation)                               

    return titles, authors, years, source_links, abstracts, journals, dois
