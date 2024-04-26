*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Test Cases ***
Succesfull Login
    ${baseUrl}=  Get Environment Variable  BASE_URL
    Log To Console    ${baseUrl}
    Open Browser  ${baseUrl}  chrome
    Set Selenium Implicit Wait    10 sec
    #Wait Until Element Is Visible    //div/div/div/div/h1
    Element Text Should Be  //div/div/div/div/h1  Enter your email or @username
