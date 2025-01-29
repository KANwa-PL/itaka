# ITAKA
# Automated Testing Solution
## Introduction
This is an automated testing solution using a production ITAKA travel agency website. It's been created as a proof-of-concept solution for a job application. The solution is written in Python using Selenium and Behave. The tests are written in BDD format using Cucumber.
## Technologies used
Python, Selenium, Behave, Cucumber
## Folder Structure
1. Features folder contains all the BDD feature files written in **Cucumber**. They correspond to individual test cases.
2. There a steps subfolder containing individual testing functions written in **Python**.
3. Environment.py file is a configuration file with all the _before_ and _after_ steps.
## How to run?
1. Clone the repository.
2. Install the dependencies.
3. Create a .env file with the following variables:
```USERNAME=your_ITAKA_username```
```PASSWORD=your_ITAKA_password```
dotenv library is used to read the .env file. It should pick up your .env file automatically.
3. Run the command `behave` in the terminal.
