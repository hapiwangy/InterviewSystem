def ReturnCurrentDate()-> str:
    '''
        get current date and turn into string
    '''
    import datetime
    currentdate = datetime.datetime.now()
    currentdate = str(currentdate)[:10]
    currentdate = "".join(currentdate.split('-'))
    return currentdate
def NameListTomail(NameList: list, name: str)-> None:
    '''
        this function will turn namelist and name into a record list
        Namelist: record the name lists 
        name: the record's list name
    '''
    # produce a current date function
    currentdate = ReturnCurrentDate()
    with open(f"{name}{currentdate}.txt", "w+") as fp:
        for n in NameList:
            fp.write(f"{n}\n")
    return None
