init:
    pass



label tests_1:
    return True

label tests_1b:
    return False
    
label tests_2b:
    "???" "test_2b"
    return

label tests_2:
    $ myAnsweringMachineVal = True
    if myAnsweringMachineVal: 
        "???" "answer machine test"
    return
    
label tests_3:
    nvl clear
    n "test_3"
    nvl clear
    "???" "test"
    return
    
label tests_4:
    "???" "tests_4"
    return
    
label tests_5a:
    "???" "tests_5a"
    return

label tests_2c:
    "????" "2c"
    return
    
label tests_6:
    "???" "tests_6"
    return