def ReturnCurrentDate()-> str:
    '''
        get current date and turn into string
    '''
    import datetime
    currentdate = datetime.datetime.now()
    currentdate = str(currentdate)[:10]
    currentdate = "".join(currentdate.split('-'))
    return currentdate
def NameListTomail(NameList: list, name: str, phase:str, port:str)-> None:
    '''
        this function will turn namelist and name into a record list
        Namelist: record the name lists 
        name: the record's list name
    '''
    # produce a current date function
    currentdate = ReturnCurrentDate()
    with open(f"{phase}_{port}\\{name}{currentdate}.csv", "w+") as fp:
        fp.write("name,mail,passornot\n")
        for n in NameList:
            fp.write(",".join(n))
            fp.write(f"\n")
    return None
