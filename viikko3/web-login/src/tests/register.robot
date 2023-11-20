
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle  
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

# ...
Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Register Should Fail With Message  Password may not only contain lower case chraracters
# ...
Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set password_confirmation  kalle12
    Submit Credentials
    Register Should Fail With Message  Wrong password confirmation
# ...
Login After Successful Registration
# ...

Login After Failed Registration
# ...



*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Go To Welcome to Ohtu Application! Page

