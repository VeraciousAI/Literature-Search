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
        print("================================================================================================================================")

def search_and_print_papers(resource_func, query):
    titles, authors, years, links, abstracts, journals, dois = resource_func(query)
    print_papers(titles, authors, years, links, abstracts, journals, dois)

def search_and_print_papers_page2(resource_func, query, start_index, end_index):
    titles, authors, years, links, abstracts, journals, dois = resource_func(query)
    for i in range(start_index, min(end_index, len(titles))):
        print_papers([titles[i]], [authors[i]], [years[i]], [links[i]], [abstracts[i]], [journals[i]], [dois[i]])

def Search(query, SS_key):
    # Print 12 papers on first page
    search_and_print_papers(search_arxiv, query)

    search_and_print_papers(search_springer, query)

    search_and_print_papers(lambda q: SemanticScholarLoader(SS_key).search_semantic(q), query)

    search_and_print_papers(search_discovery, query)

    # Print next 12 papers on second page
    search_and_print_papers_page2(search_arxiv_page2, query, 3, 6)
    
    search_and_print_papers_page2(search_springer_page2, query, 3, 6)

    search_and_print_papers_page2(lambda q: SemanticScholarLoader(SS_key).search_semantic_page2(q), query, 3, 6)

    search_and_print_papers_page2(search_discovery_page2, query, 3, 6)

    # For page 3 to page 10
    start_index = 6  # 0-based index, so 6 represents the 7th paper
    end_index = 29   # 0-based index, so 29 represents the 30th paper

    semantic_titles, semantic_authors, semantic_years, semantic_links, semantic_abstracts, semantic_journals, semantic_dois = SemanticScholarLoader(SS_key).search_semantic_page10(query)
    
    # Slice the lists to save the desired papers
    semantic_titles = semantic_titles[start_index:end_index+1]
    semantic_authors = semantic_authors[start_index:end_index+1]
    semantic_years = semantic_years[start_index:end_index+1]
    semantic_links = semantic_links[start_index:end_index+1]
    semantic_abstracts = semantic_abstracts[start_index:end_index+1]
    semantic_journals = semantic_journals[start_index:end_index+1]
    semantic_dois = semantic_dois[start_index:end_index+1]
    
    ucl_titles, ucl_authors, ucl_years, ucl_links, ucl_abstracts, ucl_journals, ucl_dois = search_discovery_page10(query)

    # Slice the lists to save the desired papers
    ucl_titles = ucl_titles[start_index:end_index+1]
    ucl_authors = ucl_authors[start_index:end_index+1]
    ucl_years = ucl_years[start_index:end_index+1]
    ucl_links = ucl_links[start_index:end_index+1]
    ucl_abstracts = ucl_abstracts[start_index:end_index+1]
    ucl_journals = ucl_journals[start_index:end_index+1]
    ucl_dois = ucl_dois[start_index:end_index+1]
    
    arxiv_titles, arxiv_authors, arxiv_years, arxiv_links, arxiv_abstracts, arxiv_journals, arxiv_dois = search_arxiv_page10(query)

    # Slice the lists to save the desired papers
    arxiv_titles = arxiv_titles[start_index:end_index+1]
    arxiv_authors = arxiv_authors[start_index:end_index+1]
    arxiv_years = arxiv_years[start_index:end_index+1]
    arxiv_links = arxiv_links[start_index:end_index+1]
    arxiv_abstracts = arxiv_abstracts[start_index:end_index+1]
    arxiv_journals = arxiv_journals[start_index:end_index+1]
    arxiv_dois = arxiv_dois[start_index:end_index+1]
    
    springer_titles, springer_authors, springer_years, springer_links, springer_abstracts, springer_journals, springer_dois = search_springer_page10(query)
    
    # Slice the lists to save the desired papers
    springer_titles = springer_titles[start_index:end_index+1]
    springer_authors = springer_authors[start_index:end_index+1]
    springer_years = springer_years[start_index:end_index+1]
    springer_links = springer_links[start_index:end_index+1]
    springer_abstracts = springer_abstracts[start_index:end_index+1]
    springer_journals = springer_journals[start_index:end_index+1]
    springer_dois = springer_dois[start_index:end_index+1]
    
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
SS_key = "vl00ouBjD66ZR2x3qpBKO2kr3gGvm46q7fUae6xR"
Search(query, SS_key)
