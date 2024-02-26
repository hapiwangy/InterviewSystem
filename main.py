# run this to do everthings you have to do
import os
import codes.helper as chp
System_Word = '''
Welcome to use this System, chose your options from below:
1. setup the environment
2. running the phase1
3. running the phase2
4. extract merge cell in excel
5. quit
'''
options = {
    '1': 'setup.py',
    '2': 'phase1.py',
    '3': 'phase2.py',
    '4': 'extractmergecell.py',
}
while True:    
    print(System_Word)
    select = input()
    if select in list(options.keys()):
        try:
            if select == '4':
                print("input your excel name (not need to type.xlsx): ")
                lang = input()
                chp.dealingwithmergecell(lang)
            else:
                os.system(f"python codes\\{options[select]}")
            print('results are: ')
            print('------------------------------------')
        except:
            print(f'Something went wrong when running{options[select]}')
    else:
        print('Thanks for using the system!')
        break
