*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Input New Command 
    Create User  kalle  kalle123

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  matti1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  mo  matti1234
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  Kalle  matti1234
    Output Should Contain  Username must contain only lower case chraracters

Register With Valid Username And Too Short Password
    Input Credentials  matti  matti1
    Output Should Contain  Password must be at least 8 chraracters long 

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattimoi
    Output Should Contain  Password may not only contain lower case chraracters

