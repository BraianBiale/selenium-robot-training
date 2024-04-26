*** Settings ***
Library  SeleniumLibrary
Suite Setup  Navigate To Home Page
Suite Teardown  Close Browser


*** Test Cases ***
Using Variables
    ${comment_data}=  Set Variable  This test should use variables for the url and the browser.
  Log To Console    ${comment_data}

*** Keywords ***
Navigate To Home Page
    Open Browser    ${main_page_url}	${browser}


*** Variables ***
${main_page_url}  http://inv.beaufortfairmont.com
${browser}  Chrome