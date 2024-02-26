# InterviewSystem
an system inorder to record the interviewers' state 
usually used once a week

# usage
before started: we have to import worksheet2 data
usage : run the code main.py
if you need : use option 4 to manage tour cell 

# using flow
running main.py 
first time: running setup.py to set up directory
everytime adding datas from new resource : using option 4 to to revising
after adding data to the new candidate
running phase1.py and phase2.py to meet your need

# design thought
# split into two phase

## phase1 
### 1. copy new data from worksheet2 to worksheet1
### 2. check state and decide the updated woksheet(fail ,tech_2, non_tech_2) and record the member(produce three lists to send email)

## phase2
### 1. do the update from tech_2, non_tech_2 to fail, tech_3, non_tech_3

# pre-request
## run the setup.py to prepare the directory that is needed
phase1_pass、phase1_thanks、phase2_pass、phase2_thanks

# 修正
1. 第二階段和感謝信增加已經寄信(時間戳記) V
2. 每個階段的欄位做調整，更改如下 V
    是否已經寄信|通過|剩下資料
3. 有資料有空行的時候，會出錯
    測試是否可以並行或是max_row的計算方式
4. 移動到總表和感謝的時候移除通過欄位 V

bouns:
1. pre-request prepare V
2. 考慮增加次作業的數量，可以用來確保沒有少做或是多做


# 實際測試
## 流程
1. 先透過option 4 來做分割
    備註部分的分割可能會有小問題。
2. 透過option 2 來做phase1 驗證(通過與否自己弄得)
3. 透過option 3 來做phase2 驗證(通過與否自己決定)
4. 確認有空格的情下也可以正常行為
