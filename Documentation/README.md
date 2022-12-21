# Project README for News_Bytes
 
## Project News_Bytes

### This application runs on the command line.  

[News_Bytes Application](/news_scraper/menu.py)

---

## Web Application

[Requirements and Vision Statement](/Documentation/requirements.md)

Welcome to our streamlined news-gathering experience! Here a user can more efficiently stay informed on diverse topics 
with a more balanced picture as we utilize data from multiple news sources.  Our console application cuts down on time 
for users to access and read top headlines, then can further provide sorted headlines by categories of news. The output 
received is the headline and link of an article. The user has the option to see the summary of that article then decide 
weather they would like to click the link to read the full piece, return to the prior headline options or quit the 
application. We hope you enjoy our approach to news-gathering.

---

## Tools Used

- PyCharm
- Trello
- Figma
- Python
- Pytest
- ChatGPT3 (OpenAI)
- Selenium
- Rich Library
- PyFiglet

---

## Recent Updates

#### V 1.0
* Initiated project team agreement and brainstormed ideas for team project. - December 8, 2022

#### V 1.1
* Initiated News_Bytes project with Trello Cards, README.md, created initial file structure. - December 10, 2022

#### V 1.2
* Initial webscrape started with BBC news selenium for ChatGPT3. - December 12, 2022

#### V 1.3
* Successful scrape made with selenium, completed base logic for ChatGPT3, initialized Rich library for menu. - 
December 13, 2022

#### V 1.4
* Initialized webscrape for additional news website sources and styling added to menu. - December 14, 2022

#### V 1.5
* Changed one news source to scrape, continued scraping and initial refactor of classes and class methods. - December 
15, 2022

#### V 1.6
* Refactoring all files to classes and class methods, troubleshooting method errors and nesting file changes, initial 
testing created. - December 17, 2022

#### V 1.7
* Scraping more data, adding data for option of local news category request, furthering menu logic, refactoring to meet 
same naming conventions of files in individual news source scrapes, created additional testing. - December 18, 2022

#### V 1.8
* Refactoring, finalizing scraping and bug fixes. - December 19, 2022

#### V 1.9
* All scraping complete, final webscrape integrated, final refactoring completed, additional testing created and 
README.md finalized, updated Trello Board. - December 20, 2022

---

## Getting Started

Clone this repository to your local machine.
Install dependencies if not already installed, refer to dependencies in requirements.txt.
In the command line run python3 bytes_app.py.

```
$ git clone https://github.com/Sleuthsz/News_Bytes.git
```

Once downloaded, activate your virtual environment and run by running your .venv file.
```
python3 -m venv .venv
source .venv/bin/activate
```

Navigate into your cloned down repository.
```
cd YourRepo/YourProject
```

Unit testing is included in the tests folder in your project using the pytest test framework.

To run console application, initialize with the following code in your terminal.
```
python3 news_scraper/menu.py
```

Follow user input prompts. The initial scrape provided will be the top headlines and the option to access those, choose 
a different category or quit application. Navigation options are selected as follows:

Return to prior headline screen:

```
'r' or 'return'
```

Quit the application:
```
'q' or 'quit'
```

For category selections, enter the numeric representation next to the category intended.

---

## Trello Board

[Trello Board](https://trello.com/b/mzyzdVX4/newsbytes)

---
## Data Flow

![Wireframe and Domain Model](img/wireframe&domain_model.png)

---

## Change Log

1.0 Initial creation of News_Bytes Project to include Trello setup and documentation/development planning. - 10 Dec 2022

1.1 Initial creation of function get_headlines() to scrape the top ten headlines of BBC. Initialization of ChatGPT for 
scraping - 12 Dec 2022

1.2 Initial implementation of Rich library with headlines_table() and categories_panel() in menu.py. Successfully receive 
article summary from OpenAI for a BBC article. Updated README.md - 13 Dec 2022

1.3 Created reuters.py, nbc.py, guardian.py for webscrape of websites. Stylized menu.py, created logic for top headlines, 
link and article text for msnbc, updated README.md - December 14, 2022

1.4 Finalized headline and link scrape and started categories scrape in nbc. Refactored menu.py with classes and class 
methods. Updated guardian.py to add category headlines. Pivot scrape from MSNBC to CBS, scraped multiple categories and 
work in progress for scraping sports category. Added news category in reuters.py scraping. Updated README.md. - December
15, 2022

1.5 Finalized scrape of sports category in cbs.py. - December 16, 2022

1.6 Converted nbc.py, guardian.py and reuters.py to classes and refactored to class methods. In cbs.py, refactored classes
and methods to match team method naming conventions, refactored news classes to inherit from base class. Added bbc.py 
article text handles for sports category. Troubleshoot nbc.py methods, scraped world news category and refactored 
business category. Updated menu.py and nested bbc.py in News class. Updated README.md. - December 17, 2022 

1.7 Added axios.py with local news. Troubleshoot and refactor methods in nbc.py to match team naming conventions. Updated 
README.md. - December 18, 2022

1.8 Finalized nbc.py methods. Add spinners while getting article headlines, updated tests for cbs.py. Refactoring and fix 
bugs in menu.py, cbs.py. Achieved MVP, Updated README.md. - December 19, 2022

1.9 Completed nbc.py scrape and finalized menu.py. Integrated nbc.py scrape and added more tests. - December 20, 2022

---

## Authors

Monika Davies
Alejandro Rivera
Daniel Brott
Andy Nguyen
Natalija Germek
