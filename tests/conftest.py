"""
This module contains shared fixtures.
"""
import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
  # Read the config file
  with open('config.json') as config_file:
    config = json.load(config_file)

  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']  
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config settings
  return config

@pytest.fixture
def browser(config):

  # Initialize the WebDriver instance, in my case a path to a webdriver must be provided everywhere
  if config['browser'] == 'Firefox':
    # Correct way to add the path to Firefox driver executable:
    b = selenium.webdriver.Firefox(executable_path='./bin/geckodriver.exe')
  elif config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome('./bin/chromedriver.exe')
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome('./bin/chromedriver.exe', options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Make its calls wait for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()


# This working like a charm before config added

# @pytest.fixture
# def browser():

#   # Initialize the ChromeDriver instance
#   b = selenium.webdriver.Chrome('./bin/chromedriver.exe')
  

#   # Make its calls wait up to 10 seconds for elements to appear
#   b.implicitly_wait(10)

#   # Return the WebDriver instance for the setup
#   yield b

#   # Quit the WebDriver instance for the cleanup
#   b.quit()