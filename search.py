import sys
from termcolor import colored
from semantic_scholar_loader import SemanticScholarLoader
from ucl_discovery import search_discovery, search_discovery_page2, search_discovery_page10
from arxiv_loader import search_arxiv, search_arxiv_page2, search_arxiv_page10
from springer import search_springer, search_springer_page2, search_springer_page10

def print_papers(titles, authors, years, links, abstracts, journals, dois):
    for i in range(min(len(titles), len(authors), len(years), len(links), len(abstracts), len(journals), len(dois))):
        print(colored(titles[i], "yellow"))
        print(colored(authors[i], "green"))
        print(colored(years[i], "red"))
        print(colored(links[i], "blue"))
        print(colored(abstracts[i], "white"))
        print(colored(journals[i], "magenta"))
        print(colored(dois[i], "cyan"))
        print("=====================================================================================================")

def Search(query, SS_key):
    semantic_titles, semantic_authors, semantic_years, semantic_links, semantic_abstracts, semantic_journals, semantic_dois = SemanticScholarLoader(SS_key).search_semantic_page10(query)
    
    ucl_titles, ucl_authors, ucl_years, ucl_links, ucl_abstracts, ucl_journals, ucl_dois = search_discovery_page10(query)
    
    arxiv_titles, arxiv_authors, arxiv_years, arxiv_links, arxiv_abstracts, arxiv_journals, arxiv_dois = search_arxiv_page10(query)

    springer_titles, springer_authors, springer_years, springer_links, springer_abstracts, springer_journals, springer_dois = search_springer_page10(query)
    
    # Combine all the lists into a single list
    all_titles = [semantic_titles, ucl_titles, arxiv_titles, springer_titles]
    all_authors = [semantic_authors, ucl_authors, arxiv_authors, springer_authors]
    all_years = [semantic_years, ucl_years, arxiv_years, springer_years]
    all_links = [semantic_links, ucl_links, arxiv_links, springer_links]
    all_abs = [semantic_abstracts, ucl_abstracts, arxiv_abstracts, springer_abstracts]
    all_journals = [semantic_journals, ucl_journals, arxiv_journals, springer_journals]
    all_dois = [semantic_dois, ucl_dois, arxiv_dois, springer_dois]
    
    num_papers_per_list = min(len(titles) for titles in all_titles)
    batch_size = 3  # Number of papers to fetch in each batch
    
    for i in range(0, num_papers_per_list, batch_size):
        batch_titles = [titles[i:i+batch_size] for titles in all_titles]
        batch_authors = [data[i:i+batch_size] for data in all_authors]
        batch_years = [data[i:i+batch_size] for data in all_years]
        batch_links = [data[i:i+batch_size] for data in all_links]
        batch_abs = [data[i:i+batch_size] for data in all_abs]
        batch_journals = [data[i:i+batch_size] for data in all_journals]
        batch_dois = [data[i:i+batch_size] for data in all_dois]
        
        for titles, authors, years, links, abstracts, journals, dois in zip(batch_titles, batch_authors, batch_years, batch_links, batch_abs, batch_journals, batch_dois):
            print_papers(titles, authors, years, links, abstracts, journals, dois)

query = sys.argv[1]
SS_key = "Enter_your_key_here"
Search(query, SS_key)
