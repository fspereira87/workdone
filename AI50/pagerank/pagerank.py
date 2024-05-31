import os
import random
import re
import sys
from collections import Counter

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    transition_probabilities = {}

    # If the current page has outgoing links
    if corpus[page]:
        prob_link = damping_factor / len(corpus[page])
        prob_random = (1 - damping_factor) / len(corpus)

        for p in corpus:
            transition_probabilities[p] = prob_random

        for link in corpus[page]:
            transition_probabilities[link] += prob_link

    # If the current page has no outgoing links
    else:
        prob_random = 1 / len(corpus)
        for p in corpus:
            transition_probabilities[p] = prob_random

    return transition_probabilities




def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_counts = Counter()

    # Generate sample by choosing a random page
    current_page = random.choice(list(corpus.keys()))
    page_counts[current_page] += 1

    # Generate the remaining samples
    for _ in range(n - 1):
        probability_transition = transition_model(corpus, current_page, damping_factor)
        next_page = random.choices(list(probability_transition.keys()), weights=list(probability_transition.values()))[0]
        page_counts[next_page] += 1
        current_page = next_page

    # Normalize the PageRank values
    page_ranks = {page: count / n for page, count in page_counts.items()}

    return page_ranks

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n = len(corpus)

    page_ranks = {page: 1 / n for page in corpus}

    # Define a function to calculate the PageRank for a single page based on the PageRank formula
    def calculate_pagerank(page):
        base_rank = (1 - damping_factor) / n
        return base_rank + damping_factor * sum((page_ranks[link] / len(corpus[link])) for link in corpus if page in corpus[link])

    while True:
        new_page_ranks = {page: calculate_pagerank(page) for page in corpus}


        if all(abs(new_page_ranks[page] - page_ranks[page]) < 0.001 for page in corpus):
            break

        page_ranks = new_page_ranks

    return page_ranks

if __name__ == "__main__":
    main()
