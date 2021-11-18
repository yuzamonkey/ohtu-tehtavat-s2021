*** Settings ***
Resource  resource.robot
Test Setup  Register User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jaakko  jaakko123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  jaakko  jaakko456
    Input New Command
    Input Credentials  jaakko  jaakko456
    Output Should Contain  Username 'jaakko' is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ja  jaakko123
    Output Should Contain  Username must be at least 3 characters long, and contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  jaakko  jaa
    Output Should Contain  Password must be at least 8 characters long, and contain special characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jaakko  jaakkojaakko
    Output Should Contain  Password must be at least 8 characters long, and contain special characters

*** Keywords ***
Register User
   Input New Command

