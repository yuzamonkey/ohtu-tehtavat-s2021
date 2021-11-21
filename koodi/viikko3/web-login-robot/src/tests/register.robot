*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kati
    Set Password  kati1234
    Set Password Confirmation  kati1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kati1234
    Set Password Confirmation  kati1234
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long, and contain letters a-z

Register With Valid Username And Too Short Password
    Set Username  otto
    Set Password  ot12
    Set Password Confirmation  ot12
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long, and contain special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  otto
    Set Password  otto1234
    Set Password Confirmation  otto5678
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Login Page
    Set Username  kati
    Set Password  kati1234
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username  otto
    Set Password  otto1234
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}