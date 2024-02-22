# InterviewSystem

# an system inorder to record the interviewers' state 
# usually used once a week
# before started: we have to import worksheet2 data

# split into two phase

## phase1 
### 1. copy new data from worksheet2 to worksheet1
### 2. check state and decide the updated woksheet(fail ,tech_2, non_tech_2) and record the member(produce three lists to send email)

## phase2
### 1. do the update from tech_2, non_tech_2 to fail, tech_3, non_tech_3

# pre-request
# have directory to put your csv files
    # phase1_pass
    # phase1_thanks
    # phase2_pass
    # phase2_thanks

# 修正
1. 第二階段和感謝信增加已經寄信(時間戳記)
2. 每個階段的欄位做調整，更改如下
是否已經寄信|通過|剩下資料
3. 有資料有空行的時候，會出錯
    測試是否可以並行或是max_row的計算方式
4. 移動到總表和感謝的時候移除通過欄位
bouns:
1. pre-request prepare

