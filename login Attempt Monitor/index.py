data={}
total_login=0
total_failed=0
report=""
conclusion=""

with open("login.log","r") as f : #reading the file
    while True :
        line=f.readline().strip()
        if not line :
            break
        part=line.split()  #spliting the line to get date,user & result
        date=part[0]
        user=part[1]
        result=part[2]
        print(f'User : {user} | Result : {result} ') #printing user and result
        total_login += 1
        
        if result.lower()=="failed" : #counting for failed attempts
            total_failed += 1
            if user not in data :
                data[user]=1
            else :
                data[user] +=1

    print(data)
    f=0
    #detecting suspicious activity if login attempts failed more than 2 times
    print("Suspicious Users :- ")
    for user in data :
         if(data[user] >=3) :
            print(f'{user} :- {data[user]} Failed attempts\n')
            report += f'{user} :- {data[user]} Failed attempts\n'
            f=1
    if f==0 :
        print("No Suspicious User")
        report +="No Suspicious User"
        conclusion +="Everthing allright\n "
    else :
        conclusion += "Potential brute-force login attempt detected\n"

# writing in the report file for final summary of login attempts
with open("Final_report.txt","w") as q :
    q.write("----------------------------------\n LOGIN ATTEMPT SECURITY REPORT \n --------------------------------\n")
    q.write(f'\nTotal Login Attempts :- {total_login} \nTotal Failed Attempts :- {total_failed}\n')
    q.write(f'\nSuspicious Users :-\n{report}')
    q.write(f'\nConclusion :-\n{conclusion}\n')

