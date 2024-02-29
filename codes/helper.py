def ReturnCurrentDate()-> str:
    '''
        get current date and turn into string
    '''
    import datetime
    currentdate = datetime.datetime.now()
    currentdate = str(currentdate)[:10]
    currentdate = "".join(currentdate.split('-'))
    return currentdate
def NameListTomail(NameList: list, name: str, phase:str, port:str, header_to_index)-> None:
    '''
        this function will turn namelist and name into a record list
        Namelist: record the name lists 
        name: the record's list name
    '''
    # produce a current date function
    currentdate = ReturnCurrentDate()
    with open(f"{phase}_{port}\\{name}{currentdate}.csv", "w+", encoding="utf-8-sig") as fp:
        fp.write("name,mail,phone\n")
        for n in NameList:
            fp.write(f"{n[header_to_index['姓名']].value},{n[header_to_index['Email']].value},{n[header_to_index['手機號碼']].value}")
            fp.write(f"\n")
    return None
def establishdirectory(NameLists:list)-> None:
    '''
        establish directory according to the namelist 
    '''
    import os
    for name in NameLists:  
        try:
            os.mkdir(name)
        except:
            print(f"{name} already exist!")
def dealingwithmergecell(excelname:str):
    '''
        dealing with the excel that contain merge cell
    '''
    import pandas as pd
    # 读取 Excel 文件
    df = pd.read_excel(f'{excelname}.xlsx')

    # 将合并单元格的值填充到所有合并单元格的单元格
    df = df.fillna(method='ffill')

    # 保存处理后的 DataFrame 到 Excel 文件
    df.to_excel(f'{excelname}_revise.xlsx', index=False)
