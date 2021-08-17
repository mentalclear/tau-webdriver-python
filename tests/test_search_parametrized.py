"""
These tests cover DuckDuckGo searches
"""
import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser) 

  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "panda"
  search_page.search(phrase)

  # And the search result query is "panda"
  assert phrase == result_page.search_input_value()

  # And the search result links pertain to "panda"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  # Then the search result title contains "panda" 
  # Move to be the last to avoid race conditions.
  assert phrase in result_page.title()

  # raise Exception("Incomplete Test")
  