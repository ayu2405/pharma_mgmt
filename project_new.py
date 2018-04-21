from Tkinter import *
from tkMessageBox import *
import sqlite3
root=Tk()
root.attributes('-fullscreen',True)




def see(root):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fr1=Frame(root,height=50,bg='light green').pack()

    def showrbm(root):
        showinfo('RBM','REGIONAL BUSINESS MANAGER\nRoles of RBM\n1) Middle management role, handling ABMs & MRs.\n2) Responsible for setting goals for his region/dept.\n3) Disseminate company strategies & information from top management to ABM & MRs and vice-versa.\n4) More concentration in Planning, Organizing & Controlling but less in Leading, compared to ABM.\n5) Less customer focused than ABM.')
        root.destroy()
        instr()
    def showabm(root):
        showinfo('ABM','AREA BUSINESS MANAGER\nRoles of ABM\n1) Lower management role, handling only MRs.\n2) Do not set goals for organization/dept but carrying out the goals set by mid/top management.\n3) Disseminate information from RBM to MRs and provide feedback to RBM.\n4) More concentration on leading but less on all 3, compared to RBM.\n5) More customer focused than RBM.')
        root.destroy()
        instr()
    def showmr(root):
        showinfo('MR','MEDICAL REPRESENTATIVE\nExcellent sales skills are a key requirement for medical representatives.\nRoles:\n1)Organising appointments and meetings with community and hospital-based healthcare staff.\n2)Demonstrating or presenting products to doctors, nurses and pharmacists.\n3)Promoting the products and maintaining records of doctors,pharmacists if they are using the companys product')
        root.destroy()
        instr()
        

    def instr():
        root1=Tk()
        Button(root1,text='What is RBM?',font='Jokerman 15',command=lambda:showrbm(root1)).pack()
        Button(root1,text='What is ABM?',font='Jokerman 15',command=lambda:showabm(root1)).pack()
        Button(root1,text='What is MR?',font='Jokerman 15',command=lambda:showmr(root1)).pack()
        mainloop()

    
    l=Label(fr1,text='WELCOME TO PHARMACEUTICALS',bg='light green',fg='dark green',height=4,font='CalibriLight 16 bold')
    l.pack(side=TOP,fill=X,expand=YES)
    fr2=Frame(root,height=30,bg='light blue').pack()
    l2=Label(fr1,text='PLEASE LOGIN',bg='light blue',fg='dark blue',height=2,font='CalibriLight 12 bold')
    l2.pack(side=TOP,fill=X,expand=YES)
    Button(fr1,text='ABOUT',font='Jokerman',command=instr).pack(padx=20, pady=20,side="left")
    i=Label(fr1,text='Enter admin to enter administration mode\nTo enter marketing department:\n   Enter mrbm1/mrbm2/mrbm3 to enter as Regional Business Manager\n       Enter mabm1/mabm2/mabm3/mabm4...mabm9 to enter as Area Business Manager\n   Enter mmr1/mmr2/mmr3...mmr27 to enter as Medical Representative.',font='CalibriLight 12 bold')
    i.pack(fill=X,expand=YES)
    l.pack(side=TOP,fill=X,expand=YES)
    eid=Entry(fr1,width=16,font="Arial 15",bd=7)
    eid.pack()
    Button(fr1,text='Sign In',font='Arial 15',command=lambda:check(root,eid)).pack()


fr1=Frame(root,height=50,bg='light green').pack()
l2=Label(fr1,text='WELCOME TO MY PROJECT',bg='red',fg='yellow',height=4,font='CalibriLight 16 bold').pack(fill=X,expand=YES)
l=Label(fr1,text='AYUSHI MATHUR',bg='light green',fg='dark blue',height=4,font='CalibriLight 10 bold').pack(fill=X,expand=YES)
l1=Label(fr1,text='ENROLLMENT 151267',bg='light blue',fg='dark blue',height=4,font='CalibriLight 10 bold').pack(fill=X,expand=YES)
l6=Label(fr1,text='Batch B2',bg='misty rose',fg='dark blue',height=4,font='CalibriLight 10 bold').pack(fill=X,expand=YES)
l3=Label(fr1,text='2nd year',bg='DarkOrchid1',fg='gray1',height=4,font='CalibriLight 10 bold').pack(fill=X,expand=YES)
l4=Label(fr1,text='EMAIL ID - ashi.211822@gmail.com',bg='SeaGreen1',fg='dark blue',height=4,font='CalibriLight 10 bold').pack(fill=X,expand=YES)
l5=Label(fr1,text='Contact No. 7240915616',bg='misty rose',fg='dark blue',height=4,font='CalibriLight 10 bold').pack(fill=X,expand=YES)


Button(fr1,text='SEE PROJECT',font='Jokerman',command=lambda:see(root)).pack()






#**************************************     DATABASE     **************************************************************

con=sqlite3.Connection('pharma')
cur=con.cursor()
cur.execute("create table if not exists doc(doc_id varchar2(10) primary key,name varchar2(20),mr_id varchar2(10) references MR(mr_id))")



cur.execute("create table if not exists doc_visit(doc_id varchar2(10),visiting_status char(1) default 'N')")


cur.execute("create table if not exists team(team_no number primary key,type_of_med varchar2(15))")

cur.execute("create table if not exists ABM(abm_id varchar2(10) primary key,name varchar2(15),area varchar2(15),team_no number references team(team_no),reporting varchar2(15),salary number(10),sal_p_inc number(10))") 


cur.execute("create table if not exists MR(mr_id varchar2(10) primary key,name varchar2(15),region varchar2(15),team_no number references team(team_no),reporting varchar2(15),salary number(10),sal_p_inc number(10))") 


cur.execute("create table if not exists RBM(rbm_id varchar2(10) primary key,name varchar2(15),Region varchar2(10),team_no number references team(team_no),salary number(10),sal_p_inc number(10))")


cur.execute("create table if not exists target_abm(abm_id varchar2(10) references ABM(abm_id),target_given number,target_completed number,incentive number)")

cur.execute("create table if not exists target_mr(mr_id varchar2(10) references MR(mr_id),target_given number,target_completed number,incentive number)")

cur.execute("delete from RBM")
cur.execute("delete from ABM")
cur.execute("delete from MR")
cur.execute("delete from target_mr")
cur.execute("delete from doc_visit")
cur.execute("delete from doc")
cur.execute("delete from team")

cur.execute("delete from target_abm")



#*************************************INPUTS***************************************************************************************
cur.execute("insert into team values('1','analgesics')")
cur.execute("insert into team values('2','antibiotics')")
cur.execute("insert into team values('3','antiseptics')")


cur.execute("insert into RBM values('mrbm1','Ayushi Mathur','U.P.','0','100000','0')")
cur.execute("insert into RBM values('mrbm2','Jyoti Sharma','M.P.','0','100000','0')")
cur.execute("insert into RBM values('mrbm3','Priya Joshi','Rajasthan','0','100000','0')")

cur.execute("insert into ABM values('mabm1','Aniket Singh','Lucknow','0','Ayushi Mathur','50000','0')")
cur.execute("insert into ABM values('mabm2','Ankit Saxena','Kanpur','0','Ayushi Mathur','50000','0')")
cur.execute("insert into ABM values('mabm3','Arpit Nigam','Lucknow','0','Ayushi Mathur','50000','0')")
cur.execute("insert into ABM values('mabm4','Mohit Sharma','Bhopal','0','Jyoti Sharma','50000','0')")
cur.execute("insert into ABM values('mabm5','Ranu Singh','Indore','0','Jyoti Sharma','50000','0')")
cur.execute("insert into ABM values('mabm6','Tanya Nigam','Gwalior','0','Jyoti Sharma','50000','0')")
cur.execute("insert into ABM values('mabm7','Rita Kumar','Jaipur','0','Priya Joshi','50000','0')")
cur.execute("insert into ABM values('mabm8','Nikhil Raj','Jaipur','0','Priya Joshi','50000','0')")
cur.execute("insert into ABM values('mabm9','Amrita Saxena','Jaipur','0','Priya Joshi','50000','0')")


cur.execute("insert into target_abm values('mabm1','0','0','0')")
cur.execute("insert into target_abm values('mabm2','0','0','0')")
cur.execute("insert into target_abm values('mabm3','0','0','0')")
cur.execute("insert into target_abm values('mabm4','0','0','0')")
cur.execute("insert into target_abm values('mabm5','0','0','0')")
cur.execute("insert into target_abm values('mabm6','0','0','0')")
cur.execute("insert into target_abm values('mabm7','0','0','0')")
cur.execute("insert into target_abm values('mabm8','0','0','0')")
cur.execute("insert into target_abm values('mabm9','0','0','0')")





cur.execute("insert into MR values('mmr1','Pawan Mathur','Ashiana','1','Aniket Singh','45000','0')")
cur.execute("insert into MR values('mmr2','Ayush Mishra','Aliganj','2','Aniket Singh','45000','0')")
cur.execute("insert into MR values('mmr3','Akash Saxena','Hazratganj','3','Aniket Singh','45000','0')")
cur.execute("insert into MR values('mmr4','Priya Saxena','Ashok Nagar','1','Ankit Saxena','45000','0')")
cur.execute("insert into MR values('mmr5','Tanveer Singh','G.T. Road','2','Ankit Saxena','45000','0')")
cur.execute("insert into MR values('mmr6','Mika Singh','Indira Nagar','1','Ankit Saxena','45000','0')")
cur.execute("insert into MR values('mmr7','Arijit Singh','Kamala Nagar','1','Arpit Nigam','45000','0')")
cur.execute("insert into MR values('mmr8','Mika Singh','Nehru Nagar','2','Arpit Nigam','45000','0')")
cur.execute("insert into MR values('mmr9','Raman Khatri','Khandari','3','Arpit Nigam','45000','0')")
cur.execute("insert into MR values('mmr10','Lalu Prasad','Govind Pura','1','Mohit Sharma','45000','0')")
cur.execute("insert into MR values('mmr11','Honey Singh','Indrapuri','3','Mohit Sharma','45000','0')")
cur.execute("insert into MR values('mmr12','Amir Khan','M.P Nagar','2','Mohit Sharma','45000','0')")
cur.execute("insert into MR values('mmr13','Nitin Kumar','Anoop Nagar','1','Ranu Singh','45000','0')")
cur.execute("insert into MR values('mmr14','Anubhav Sharma','Ashish Nagar','2','Ranu Singh','45000','0')")
cur.execute("insert into MR values('mmr15','Akash Katarey','Morya Hills','3','Ranu Singh','45000','0')")
cur.execute("insert into MR values('mmr16','John Abraham','Alkapuri','1','Tanya Nigam','45000','0')")
cur.execute("insert into MR values('mmr17','Fawad Khan','DogarPur','2','Tanya Nigam','45000','0')")
cur.execute("insert into MR values('mmr18','Shahid Kapoor','Govindpuri','3','Tanya Nigam','45000','0')")
cur.execute("insert into MR values('mmr19','Kareena Kapoor','Ajmer road','2','Rita Kumar','45000','0')")
cur.execute("insert into MR values('mmr20','Ranbir Kapoor','Jagatpura','1','Rita Kumar','45000','0')")
cur.execute("insert into MR values('mmr21','Ranveer Singh','Mansarover','3','Rita Kumar','45000','0')")
cur.execute("insert into MR values('mmr22','Karishma','Madhuvan','1','Nikhil Raj','45000','0')")
cur.execute("insert into MR values('mmr23','Akshat Mathur','Shakti Nagar','2','Nikhil Raj','45000','0')")
cur.execute("insert into MR values('mmr24','Deepika Nigam','Subhash Nagar','3','Nikhil Raj','45000','0')")
cur.execute("insert into MR values('mmr25','Surabhi Lal','Panchsheel','2','Amrita Saxena','45000','0')")
cur.execute("insert into MR values('mmr26','Shubhangi Rai','Rang ganj','1','Amrita Saxena','45000','0')")
cur.execute("insert into MR values('mmr27','Divya Tripathi','Pushkar road','3','Amrita Saxena','45000','0')")






cur.execute("insert into target_mr values('mmr1','0','0','0')")
cur.execute("insert into target_mr values('mmr2','0','0','0')")
cur.execute("insert into target_mr values('mmr3','0','0','0')")
cur.execute("insert into target_mr values('mmr4','0','0','0')")
cur.execute("insert into target_mr values('mmr5','0','0','0')")
cur.execute("insert into target_mr values('mmr6','0','0','0')")
cur.execute("insert into target_mr values('mmr7','0','0','0')")
cur.execute("insert into target_mr values('mmr8','0','0','0')")
cur.execute("insert into target_mr values('mmr9','0','0','0')")
cur.execute("insert into target_mr values('mmr10','0','0','0')")
cur.execute("insert into target_mr values('mmr11','0','0','0')")
cur.execute("insert into target_mr values('mmr12','0','0','0')")
cur.execute("insert into target_mr values('mmr13','0','0','0')")
cur.execute("insert into target_mr values('mmr14','0','0','0')")
cur.execute("insert into target_mr values('mmr15','0','0','0')")
cur.execute("insert into target_mr values('mmr16','0','0','0')")
cur.execute("insert into target_mr values('mmr17','0','0','0')")
cur.execute("insert into target_mr values('mmr18','0','0','0')")
cur.execute("insert into target_mr values('mmr19','0','0','0')")
cur.execute("insert into target_mr values('mmr20','0','0','0')")
cur.execute("insert into target_mr values('mmr21','0','0','0')")
cur.execute("insert into target_mr values('mmr22','0','0','0')")
cur.execute("insert into target_mr values('mmr23','0','0','0')")
cur.execute("insert into target_mr values('mmr24','0','0','0')")
cur.execute("insert into target_mr values('mmr25','0','0','0')")
cur.execute("insert into target_mr values('mmr26','0','0','0')")
cur.execute("insert into target_mr values('mmr27','0','0','0')")













cur.execute("insert into doc values('doc1','Dr. Hari Prasad','mmr1')")
cur.execute("insert into doc values('doc18','Dr. Manish Gupta','mmr2')")
cur.execute("insert into doc values('doc2','Dr. Umakar Das','mmr3')")
cur.execute("insert into doc values('doc3','Dr. Hridesh Singh','mmr4')")
cur.execute("insert into doc values('doc4','Dr. Akash Sengal','mmr5')")
cur.execute("insert into doc values('doc5','Dr. Shruti Gupta','mmr6')")
cur.execute("insert into doc values('doc6','Dr. Rakhi Mathur','mmr7')")
cur.execute("insert into doc values('doc7','Dr. Ayush Mathur','mmr8')")
cur.execute("insert into doc values('doc8','Dr. Amrit Puri','mmr9')")
cur.execute("insert into doc values('doc9','Dr. Venkash Vankha','mmr10')")
cur.execute("insert into doc values('doc10','Dr. Harbhajan Singh','mmr11')")
cur.execute("insert into doc values('doc11','Dr. M.S. Dhoni','mmr12')")
cur.execute("insert into doc values('doc12','Dr. Virat Kohli','mmr13')")
cur.execute("insert into doc values('doc13','Dr. Amitabh Bachchan','mmr14')")
cur.execute("insert into doc values('doc14','Dr. Aishwarya Rai','mmr15')")
cur.execute("insert into doc values('doc15','Dr. Anushka Sharma','mmr16')")
cur.execute("insert into doc values('doc16','Dr. Aditi Rao','mmr17')")
cur.execute("insert into doc values('doc17','Dr. Akshay Kumar','mmr18')")
a=[('doc1',),('doc2',),('doc3',),('doc4',),('doc5',),('doc6',),('doc7',),('doc8',),('doc9',),('doc10',),('doc11',),('doc12',),('doc13',),('doc14',),('doc15',),('doc16',),('doc17',),('doc18',)]
cur.executemany("insert into doc_visit(doc_id) values(?)",a)

def insert_abm(abmid,name,area,team,reporting,salary,root):
    a=[abmid,name,area,team,reporting,salary,0]
    cur.execute("insert into ABM values(?,?,?,?,?,?,?)",a)
    b=[abmid,0,0,0]
    cur.execute("insert into target_abm values(?,?,?,?)",b)
    showinfo('Congrats','DONE')
    con.commit()

def insert_rbm(rbmid,name,region,team,salary,root):
    a=[rbmid,name,region,team,salary,0]
    cur.execute("insert into RBM values(?,?,?,?,?,?)",a)
    showinfo('Congrats','DONE')
    con.commit()
       
def insert_mr(mrid,name,region,team,report,sal,root):
    a=[mrid,name,region,team,report,sal,0]
    cur.execute("insert into MR values(?,?,?,?,?,?,?)",a)
    b=[mrid,0,0,0]
    cur.execute("insert into target_mr values(?,?,?,?)",b)
    showinfo('Congrats','DONE')
    con.commit()
    
def insert_doc(docid,name,mrid):
    a=[docid,name,mrid]
    cur.execute("insert into doc values(?,?,?)",a)
    showinfo('Congrats','DONE')
    con.commit()
    

def insert_doc_visited_by_mr(root,docid,mrid):
    a=[]
    a.append(docid)
    cur.execute("update doc_visit set visiting_status='Y' where doc_id=?",a)
    showinfo('Congrats','DONE')
    con.commit()


def delete_rbm(rbmid,root,e):
    a=(rbmid,)
    cur.execute("update ABM set reporting=NULL where reporting=(select name from RBM where rbm_id=?)",a)
    cur.execute("delete from RBM where rbm_id=?",a)
    showinfo('Congrats','DONE')
    con.commit()
def delete_abm(abmid,root,e):
    a=(abmid,)
    cur.execute("update MR set reporting=NULL where reporting=(select name from ABM where abm_id=?)",a)
    cur.execute("delete from ABM where abm_id=?",a)
    cur.execute("delete from target_abm where abm_id=?",a)
    showinfo('Congrats','DONE')
    con.commit()
def delete_mr(mrid,root,e):
    a=(mrid,)
    cur.execute("update doc set mr_id=NULL where mr_id=?",a)
    cur.execute("delete from MR where mr_id=?",a)
    cur.execute("delete from target_mr where mr_id=?",a)
    showinfo('Congrats','DONE')
    con.commit()
    

def show_rbm(rbmid,root):
    k=(rbmid,)
    cur.execute("select * from RBM where rbm_id=?",k)
    #cur.fetchall()
    a=()
    if cur.fetchone() is not None:
        cur.execute("select * from RBM where rbm_id=?",k)
        for r in cur.fetchone():
            a=a+(r,)
    else:
        showerror('Sorry','NO RBM Registered')
    if a is not ():
        Label(root,text="RBM_ID :"+str(a[0]),font='Arial 10 bold').pack()
        Label(root,text="NAME :"+str(a[1]),font='Arial 10 bold').pack()
        Label(root,text="REGION :"+str(str(a[2])),font='Arial 10 bold').pack()
        Label(root,text="TEAM NO :"+str(str(a[3])),font='Arial 10 bold').pack()
        Label(root,text="Salary :"+str(str(a[4])),font='Arial 10 bold').pack()
def show_abm(abmid,root):
    k=(abmid,)
    cur.execute("select * from ABM where abm_id=?",k)
    a=()
    if cur.fetchone() is not None:
        cur.execute("select * from ABM where abm_id=?",k)
        for r in cur.fetchone():
            a=a+(r,)
    else:
        showerror('Sorry','NO ABM Registered')
    if a is not ():
        Label(root,text="ABM_ID :"+str(a[0]),font='Arial 10 bold').pack()
        Label(root,text="NAME :"+str(a[1]),font='Arial 10 bold').pack()
        Label(root,text="REGION :"+str(str(a[2])),font='Arial 10 bold').pack()
        Label(root,text="TEAM NO :"+str(str(a[3])),font='Arial 10 bold').pack()
        Label(root,text="REPORTING TO :"+str(str(a[4])),font='Arial 10 bold').pack()
        Label(root,text="SALARY :"+str(str(a[5])),font='Arial 10 bold').pack()
def show_mr(mrid,root):
    k=(mrid,)
    cur.execute("select * from MR where mr_id=?",k)
    a=()
    if cur.fetchone() is not None:
        cur.execute("select * from MR where mr_id=?",k)
        for r in cur.fetchone():
            a=a+(r,)
    else:
        showerror('Sorry','NO MR Registered')
    if a is not ():
        Label(root,text="MR_ID :"+str(a[0]),font='Arial 10 bold').pack()
        Label(root,text="NAME :"+str(a[1]),font='Arial 10 bold').pack()
        Label(root,text="REGION :"+str(str(a[2])),font='Arial 10 bold').pack()
        Label(root,text="TEAM NO :"+str(str(a[3])),font='Arial 10 bold').pack()
        Label(root,text="REPORTING TO :"+str(str(a[4])),font='Arial 10 bold').pack()
        Label(root,text="SALARY :"+str(str(a[5])),font='Arial 10 bold').pack()

def show_all_abm_under_rbm(root,rbmid):
    a=(rbmid,)
    b=()
    cur.execute("select distinct o2.name from RBM o1,ABM o2 where o2.reporting in(select name from RBM where rbm_id=?)",a)
    for r in cur.fetchall():
        b=b+(r,)
    print b
    for x in b:
        showinfo('ABM',str(x))
def show_all_mr_under_abm(root,abmid):
    a=(abmid,)
    b=()
    cur.execute("select o2.name from ABM o1,MR o2 where o2.reporting in(select name from ABM where abm_id=?)",a)
    for r in cur.fetchall():
        b=b+(r,)
    for x in b:
        showinfo('MR',str(x))
def show_doc_under_mr(root,mrid):
    a=(mrid,)
    b=()
    cur.execute("select name from doc where mr_id=?",a)
    showinfo('Doctor',cur.fetchall())


def show_details_doc(root,mrid,docid):
    k=(docid,)
    cur.execute("select * from doc where doc_id=?",k)
    a=()
    for r in cur.fetchone():
        a=a+(r,)
        print a
    if a is not ():
        Label(root,text="Doc Id:  "+str(a[0]),font='Arial 10 bold').pack()
        Label(root,text="Doctor Name:  "+str(a[1]),font='Arial 10 bold').pack()
        Label(root,text="Attended by MR:  "+str(a[2]),font='Arial 10 bold').pack()
        

def show_doc(root,mrid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(root,text="\n\n").pack()
    Button(root,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter doc1/doc2/doc3...')).pack()
    Label(root,text='\n').pack()
    Label(root,text='Doc_id',bg='red',font='Arial 15 bold').pack()
    Label(root,text="\n\n").pack()
    eid=Entry(root,width=20,font="Arial 15",bd=4)
    eid.pack()
    Button(root,text='OK',font='Arial 15 bold',command=lambda:show_details_doc(root,mrid,eid.get())).pack()
    Button(root,text='BACK',font='Arial 15 bold',command=lambda:mrr(root,mrid)).pack(side=BOTTOM)

    
   
    

#------------------------------------------------------------------------------------------------------------------
def add_abm_target(root,rbmid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(root,text="\n\n").pack()
    Button(root,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mabm1/mabm2/mabm3...')).pack()
    Label(root,text='\n').pack()
    Label(root,text='ABM_id',bg='red',font='Arial 15 bold').pack()
    Label(root,text="\n\n").pack()
    eid=Entry(root,width=20,font="Arial 15",bd=4)
    eid.pack()
    Label(root,text="\n\n").pack()
    Label(root,text='Target',bg='red',font='Arial 15 bold').pack()
    Label(root,text="\n\n").pack()
    t=Entry(root,width=20,font="Arial 15",bd=4)
    t.pack()
    Label(root,text="\n\n").pack()
    Button(root,text='OK',font='Arial 15 bold',command=lambda:add_abm_t(root,rbmid,eid.get(),int(t.get()))).pack()
    Button(root,text='BACK',font='Arial 15 bold',command=lambda:rbmm(root,rbmid)).pack(side=BOTTOM)

def add_abm_t(root,rbm,abm,t):
    b=(rbm,)
    a=()
    cur.execute("select o2.abm_id from RBM o1,ABM o2 where o2.reporting in(select name from RBM where rbm_id=?)",b)
    for r in cur.fetchone():
        print r
        a=a+(r,)
        
    
    z=[t,abm]
        
    cur.execute("update target_abm set target_given=? where abm_id=?",z)
    con.commit()
    showinfo('Congrats','DONE')
    con.commit()


def add_mr_target(root,abmid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(root,text="\n\n").pack()
    Button(root,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mmr1/mmr2/mmr3...')).pack()
    Label(root,text='\n').pack()
    Label(root,text='MR_id',bg='red',font='Arial 15 bold').pack()
    Label(root,text="\n\n").pack()
    eid=Entry(root,width=15,font="Arial 15",bd=4)
    eid.pack()
    Label(root,text="\n\n").pack()
    Label(root,text='Target',bg='red',font='Arial 15 bold').pack()
    Label(root,text="\n\n").pack()
    t=Entry(root,width=20,font="Arial 15",bd=4)
    t.pack()
    Label(root,text="\n\n").pack()
    Button(root,text='OK',font='Arial 15 bold',command=lambda:add_mr_t(root,abmid,eid.get(),int(t.get()))).pack()
    Button(root,text='BACK',font='Arial 15 bold',command=lambda:abmm(root,abmid)).pack(side=BOTTOM)
def add_mr_t(root,abm,mr,t):
    b=(abm,)
    a=()
    cur.execute("select o2.mr_id from ABM o1,MR o2 where o2.reporting in(select name from ABM where abm_id=?)",b)
    for r in cur.fetchone():
        a=a+(r,)
    
    z=[t,mr]
        
    cur.execute("update target_mr set target_given=? where mr_id=?",z)
    con.commit()
    showinfo('Congrats','DONE')
    con.commit()


#------------------------------------------ADD TARGET STATUS----------------------------------------------------

def add_target_status_abm(root,abmid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    x=(abmid,)
    cur.execute("select * from target_abm where abm_id=?",x)
    Label(root,text='\n\n\n').pack()
    c=()
    for r in cur.fetchone():
        c=c+(r,)
    Label(root,text="ABM_ID :"+str(c[0]),font='Arial 15 bold').pack()
    Label(root,text="Target given :"+str(c[1]),font='Arial 15 bold').pack()

    Label(root,text='Enter Target Completed\n\n',bg='red',font='Arial 15 bold').pack()
    eid=Entry(root,width=12,font="Arial 15",bd=4)
    eid.pack()
    
    Button(root,text='BACK',font='Arial 15 bold',command=lambda:abmm(root,abmid)).pack(side=BOTTOM)
    Button(root,text='OK',font='Arial 15 bold',command=lambda:add_abm_s(root,int(eid.get()),abmid)).pack(side=BOTTOM)
    
def add_abm_s(root,t,idd):
    m=[t,idd]
    i=(idd,)
    cur.execute("update target_abm set target_completed=? where abm_id=?",m)
    cur.execute("update target_abm set incentive=incentive+(1.5* ? ) where abm_id=?",m)
    con.commit()
    showinfo('CONGRATS','Status updated')
    
    cur.execute("select incentive from target_abm where abm_id=?",i)
    showinfo('INCENTIVE','Incentive='+str((cur.fetchone())[0]))



    
def add_target_status_mr(root,mrid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    x=[mrid,]
    cur.execute("select * from target_mr where mr_id=?",x)
    Label(root,text='\n\n\n').pack()
    c=()
    for r in cur.fetchone():
        c=c+(r,)
    Label(root,text="MR_ID :"+str(c[0]),font='Arial 15 bold').pack()
    Label(root,text="Target given :"+str(c[1]),font='Arial 15 bold').pack()

    Label(root,text='Enter Target Completed\n\n',bg='red',font='Arial 15 bold').pack()
    eid=Entry(root,width=12,font="Arial 15",bd=4)
    eid.pack()
    
    Button(root,text='BACK',font='Arial 15 bold',command=lambda:mrr(root,mrid)).pack(side=BOTTOM)
    Button(root,text='OK',font='Arial 15 bold',command=lambda:add_mr_s(root,int(eid.get()),mrid)).pack(side=BOTTOM)
    
def add_mr_s(root,t,idd):
    m=[t,idd]
    i=(idd,)
    cur.execute("update target_mr set target_completed=? where mr_id=?",m)
    cur.execute("update target_mr set incentive=incentive+(1.5* ? ) where mr_id=?",m)
    con.commit()
    showinfo('CONGRATS','Status updated')
    
    cur.execute("select incentive from target_mr where mr_id=?",i)
    showinfo('INCENTIVE ADDED','Incentive='+str((cur.fetchone())[0]))


#---------------------------------------------------------------------------------------------------------------------------------------

#************************SHOW TARGET*****************************************************


    
def show_target_abm(root,rbmid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Button(root,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mabm1/mabm2/mabm3...')).pack()
    Label(root,text='\n').pack()
    Label(root,text='ABM_id\n\n',bg='red',font='Arial 15 bold').pack()
    eid=Entry(root,width=12,font="Arial 15",bd=4)
    eid.pack()
    Button(root,text='OK',font='Arial 15 bold',command=lambda:show_abm_t(root,rbmid,eid.get())).pack()
def show_abm_t(root,rbm,abm):
    b=[]
    b.append(rbm)
    x=(abm,)
    a=()
    #cur.execute("select o2.abm_id from RBM o1,ABM o2 where o2.reporting in(select name from RBM where rbm_id=?)",b)
    #print cur.fetchall()
    cur.execute("select o2.abm_id from RBM o1,ABM o2 where o2.reporting in(select name from RBM where rbm_id=?)",b)
    for r in cur.fetchall():
        a=a+(r,)
    print a
    c=()
   
    cur.execute("select * from target_abm where abm_id=?",x)
    Label(root,text='\n\n\n').pack()
    for r in cur.fetchone():
        c=c+(r,)
    Label(root,text="ABM_ID :"+str(c[0]),font='Arial 15 bold').pack()
    Label(root,text="Target given :"+str(c[1]),font='Arial 15 bold').pack()
    Label(root,text="Target completed :"+str(str(c[2])),font='Arial 15 bold').pack()

    Button(root,text='BACK',font='Arial 15 bold',command=lambda:rbmm(root,rbm)).pack(side=BOTTOM)




def show_target_mr(root,abmid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    l=Label(root,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(root,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Button(root,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mmr1/mmr2/mmr3...')).pack()
    Label(root,text='\n').pack()
    Label(root,text='MR_id',bg='red',font='Arial 10 bold').pack()
    eid=Entry(root,width=12,font="Arial 15",bd=4)
    eid.pack()
    Button(root,text='OK',font='Arial 15 bold',command=lambda:show_mr_t(root,abmid,eid.get())).pack()
def show_mr_t(root,abm,mr):
    b=(abm,)
    x=(mr,)
    a=()
    cur.execute("select o2.mr_id from ABM o1,MR o2 where o2.reporting in(select name from ABM where abm_id=?)",b)
    for r in cur.fetchone():
        a=a+(r,)
    c=()

    cur.execute("select * from target_mr where mr_id=?",x)
    Label(root,text='\n\n\n').pack()
    for r in cur.fetchone():
         c=c+(r,)
    Label(root,text="MR_ID :"+str(c[0]),font='Arial 15 bold').pack()
    Label(root,text="Target given :"+str(c[1]),font='Arial 15 bold').pack()
    Label(root,text="Target completed :"+str(str(c[2])),font='Arial 15 bold').pack()
    Button(root,text='BACK',font='Arial 15 bold',command=lambda:abmm(root,abm)).pack(side=BOTTOM)



#*******************************************************PAY********************************************************************

def pay_mr(mrid):
    a=(mrid,)
    cur.execute("select salary from MR where mr_id=?",a)
    if cur.fetchone() is not None:
        cur.execute("select salary from MR where mr_id=?",a)
        showinfo('Medical Representative',"Salary="+str((cur.fetchone())[0]))
    else:
        showerror('Oops','Id not Registered')
    cur.execute("select sal_p_inc from MR where mr_id=?",a)
    showinfo('Medical Representative','Incentive='+str((cur.fetchone())[0]))
def pay_rbm(rbmid):
    a=(rbmid,)
    cur.execute("select salary from RBM where rbm_id=?",a)
    if cur.fetchone() is not None:
        cur.execute("select salary from RBM where rbm_id=?",a)
        showinfo('Regional Business Manager',"Salary="+str((cur.fetchone())[0]))
    else:
        showerror('Oops','Id not Registered')
    cur.execute("select sal_p_inc from RBM where rbm_id=?",a)
    showinfo('Regional Business Manager','Incentive='+str((cur.fetchone())[0]))
def pay_abm(abmid):
    a=(abmid,)
    cur.execute("select salary from ABM where abm_id=?",a)
    if cur.fetchone() is not None:
        cur.execute("select salary from ABM where abm_id=?",a)
        showinfo('Area Business Manager','Salary='+str((cur.fetchone())[0]))
    else:
        showerror('Oops','Id not Registered')
    cur.execute("select sal_p_inc from ABM where abm_id=?",a)
    showinfo('Area Representative',"Incentive="+str((cur.fetchone())[0]))

#*************************************************     Insert    *************************************************************


def showteams(root):
    cur.execute("select * from team")
    a=()
    for r in cur.fetchall():
        a=a+(r,)
    if a is not ():
        Label(root,text="Team no.:  "+str(a[0][0]),font='Arial 10 bold').pack()
        Label(root,text="Medicine category:  "+str(a[0][1]),font='Arial 10 bold').pack()
        Label(root,text="Team no.:  "+str(a[1][0]),font='Arial 10 bold').pack()
        Label(root,text="Medicine category:  "+str(a[1][1]),font='Arial 10 bold').pack()
        Label(root,text="Team no.:  "+str(a[2][0]),font='Arial 10 bold').pack()
        Label(root,text="Medicine category:  "+str(a[2][1]),font='Arial 10 bold').pack()
        
    


def insertemp(root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='ADD EMPLOYEE',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n\n\n").pack()
    Label(fra,text='Insert which employee?\n',font='Arial 20 bold').pack(side=TOP,fill=X,expand=NO)
    v=IntVar()
    Radiobutton(fra,text='Regional Business Manager',font='Arial 15 bold',variable=v,value=1).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Area Business Manager',font='Arial 15 bold',variable=v,value=2).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Medical Representative',font='Arial 15 bold',variable=v,value=3).pack(side=TOP,fill=X,expand=NO)
    Button(fra,text='OK',font='Arial 15 bold',command=lambda:insert(v.get(),root,e)).pack()
    Button(fra,text='BACK',font='Arial 15 bold',command=lambda:admin(root,e)).pack(side=BOTTOM)
def insert(v,root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='WELCOME',bg='yellow',fg='black',height=2,font='Arial 20 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light green',fg='dark green',height=2,font='CalibriLight 15 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    def helpp(i):
        if i==1:
            root1=Tk()
            root.title("INSTRUCTONS")
            Label(root1,text='INSERTING NEW RBM\n',font='Arial 15 bold').pack()
            Label(root1,text='1. Enter ID in the form mrbm1/mrbm2/mrbm3...etc.\n').pack()
            Label(root1,text='2. Enter Name of the employee\n').pack()
            Label(root1,text='3. Enter Region\n').pack()
            Label(root1,text='4. Enter Team\n').pack()
            Button(root1,text='Example of Teams',command=lambda:showteams(root1)).pack()
            Label(root1,text='4.Enter Salary').pack()
            mainloop()
            
        if i==2:
            root1=Tk()
            Label(root1,text='INSERTING NEW ABM\n',font='Arial 15 bold').pack()
            Label(root1,text='1. Enter ID in the form mabm1/mabm2/mabm3...etc.\n').pack()
            Label(root1,text='2. Enter Name of the employee\n').pack()
            Label(root1,text='3. Enter Area\n').pack()
            Label(root1,text='4. Enter Team\n').pack()
            Button(root1,text='Example of Teams',command=lambda:showteams(root1)).pack()
            Label(root1,text='4.Reporting should be to RBM already registered.\n').pack()
            Label(root1,text='5.Enter Salary').pack()
            mainloop()
        if i==3:
            root1=Tk()
            Label(root1,text='INSERTING NEW MR\n',font='Arial 15 bold').pack()
            Label(root1,text='1. Enter ID in the form mmr1/mmr2/mmr3...etc.\n').pack()
            Label(root1,text='2. Enter Name of the employee\n').pack()
            Label(root1,text='3. Enter Area\n').pack()
            Label(root1,text='4. Enter Team\n').pack()
            Button(root1,text='Example of Teams',command=lambda:showteams(root1)).pack()
            Label(root1,text='4.Reporting should be to ABM already registered.\n').pack()
            Label(root1,text='5.Enter Salary').pack()
            mainloop() 
    if v==1:
        Button(fra,text='HELP',font='Jokerman',command=lambda:helpp(1)).pack()
        Label(fra,text='RBM_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Label(fra,text='Name of RBM',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        ename=Entry(fra,width=14,font="Arial 15",bd=7)
        ename.pack()
        Label(fra,text='Region',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        ereg=Entry(fra,width=14,font="Arial 15",bd=7)
        ereg.pack()
        Label(fra,text='Team no.',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        eteam=Entry(fra,width=14,font="Arial 15",bd=7)
        eteam.pack()
        Label(fra,text='Salary',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        esal=Entry(fra,width=14,font="Arial 15",bd=7)
        esal.pack()
        Button(fra,text='INSERT',font='Arial 12 bold',command=lambda:insert_rbm(eid.get(),ename.get(),ereg.get(),int(eteam.get()),int(esal.get()),fra)).pack()
    elif v==2:
        Button(fra,text='HELP',font='Jokerman',command=lambda:helpp(2)).pack()
        #abmid,name,area,team,reporting,salary)
        Label(fra,text='ABM_id',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        eid=Entry(fra,width=10,font="Arial 15",bd=7)
        eid.pack()
        Label(fra,text='Name of ABM',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        ename=Entry(fra,width=10,font="Arial 15",bd=7)
        ename.pack()
        Label(fra,text='Area',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        ereg=Entry(fra,width=10,font="Arial 15",bd=7)
        ereg.pack()
        Label(fra,text='Team no.',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        eteam=Entry(fra,width=10,font="Arial 15",bd=7)
        eteam.pack()
        Label(fra,text='Reporting to',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        erep=Entry(fra,width=10,font="Arial 15",bd=7)
        erep.pack()
        Label(fra,text='Salary',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        esal=Entry(fra,width=10,font="Arial 15",bd=7)
        esal.pack()
        Button(fra,text='INSERT',font='Arial 10 bold',command=lambda:insert_abm(eid.get(),ename.get(),ereg.get(),int(eteam.get()),erep.get(),int(esal.get()),fra)).pack()
    elif v==3:
        Button(fra,text='HELP',font='Jokerman',command=lambda:helpp(3)).pack()
        Label(fra,text='MR_id',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        eid=Entry(fra,width=12,font="Arial 15",bd=7)
        eid.pack()
        Label(fra,text='Name of MR',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        ename=Entry(fra,width=10,font="Arial 15",bd=7)
        ename.pack()
        Label(fra,text='Region',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        ereg=Entry(fra,width=10,font="Arial 15",bd=7)
        ereg.pack()
        Label(fra,text='Team no.',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        eteam=Entry(fra,width=10,font="Arial 15",bd=7)
        eteam.pack()
        Label(fra,text='Reporting to',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        erep=Entry(fra,width=10,font="Arial 15",bd=7)
        erep.pack()
        Label(fra,text='Salary',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        esal=Entry(fra,width=10,font="Arial 15",bd=7)
        esal.pack()
        Button(fra,text='INSERT',font='Arial 12 bold',command=lambda:insert_mr(eid.get(),ename.get(),ereg.get(),int(eteam.get()),erep.get(),int(esal.get()),fra)).pack()
    else:
        insertemp(root)
    Button(fra,text='INSERT MORE',font='Arial 10 bold',command=lambda:insertemp(root)).pack(side=BOTTOM)
    Button(fra,text='BACK',font='Arial 10 bold',command=lambda:admin(root,e)).pack(side=BOTTOM)
def add_status_doc(root,mrid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='grey').pack()
    l=Label(fra,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text='Enter Doc id',font='Arial 15 bold',bg='light grey').pack()
    e=Entry(fra,width=15,bd=7)
    e.pack()
    Button(fra,text='Update Yes',font='Arial 12 bold',command=lambda:insert_doc_visited_by_mr(root,e.get(),mrid)).pack()
    Button(fra,text='BACK',font='Arial 12 bold',command=lambda:mrr(root,mrid)).pack(side=BOTTOM)
        
        
    

        
        
#***************************************************    Check id    *********************************************************
def check(root,eid):
    e=str(eid.get())
    if e.startswith('a'):
        admin(root,e)
    elif e.startswith('m'):
        marketing(root,e)
    else:
        Label(fr1,text='Wrong ID. Enter Again').pack()
#****************************************************       Delete     **********************************************************
def deleteemp(root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='REMOVE EMPLOYEE',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n\n\n").pack()
    Label(fra,text='Delete which employee?\n',font='Arial 20 bold').pack(side=TOP,fill=X,expand=NO)
    v=IntVar()
    Radiobutton(fra,text='Regional Business Manager',font='Arial 15 bold',variable=v,value=1).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Area Business Manager',font='Arial 15 bold',variable=v,value=2).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Medical Representative',font='Arial 15 bold',variable=v,value=3).pack(side=TOP,fill=X,expand=NO)
    Button(fra,text='OK',font='Arial 15 bold',command=lambda:delete(v.get(),root,e)).pack()
    Button(fra,text='BACK',font='Jokerman',command=lambda:admin(root,e)).pack(side=BOTTOM)
def delete(v,root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='REMOVE EMPLOYEE',bg='grey',fg='black',height=4,font='Arial 30 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=4,font='CalibriLight 16 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    if v==1:
        Label(fra,text='RBM_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mrbm1/mrbm2/mrbm3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='DELETE',font='Arial 15 bold',command=lambda:delete_rbm(eid.get(),fra,e)).pack()
    elif v==2:
        Label(fra,text='ABM_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mabm1/mabm2/mabm3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='DELETE',font='Arial 15 bold',command=lambda:delete_abm(eid.get(),fra,e)).pack()
    elif v==3:
        Label(fra,text='MR_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mmr1/mmr2/mmr3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='DELETE',font='Arial 15 bold',command=lambda:delete_mr(eid.get(),fra,e)).pack()
    else:
        deleteemp(root,e)
    Button(fra,text='BACK',font='Jokerman',command=lambda:deleteemp(root,e)).pack(side=BOTTOM)
#***************************************************       Display     ******************************************************
def showemp(root,eid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='SHOW EMPLOYEE',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n\n\n").pack()
    Label(fra,text='SHOW which employee?\n',font='Arial 20 bold').pack(side=TOP,fill=X,expand=NO)
    v=IntVar()
    Radiobutton(fra,text='Regional Business Manager',font='Arial 15 bold',variable=v,value=1).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Area Business Manager',font='Arial 15 bold',variable=v,value=2).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Medical Representative',font='Arial 15 bold',variable=v,value=3).pack(side=TOP,fill=X,expand=NO)
    Button(fra,text='OK',font='Arial 15 bold',command=lambda:show(v.get(),root,1,eid)).pack()
    Button(fra,text='BACK',font='Arial 15 bold',command=lambda:admin(root,eid)).pack(side=BOTTOM)
def show(v,root,k,idd):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='SHOW EMPLOYEE',bg='grey',fg='black',height=4,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=4,font='CalibriLight 16 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    if v==1:
        Label(fra,text='RBM_id',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mrbm1/mrbm2/mrbm3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='SHOW',font='Arial 10 bold',command=lambda:show_rbm(eid.get(),root)).pack()
        
    elif v==2:
        Label(fra,text='ABM_id',font='Arial 10 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mabm1/mabm2/mabm3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='SHOW',font='Arial 10 bold',command=lambda:show_abm(eid.get(),root)).pack()
        
    elif v==3:
        Label(fra,text='MR_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mmr1/mmr2/mmr3...')).pack()
        Label(fra,text='\n').pack()
        
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='SHOW',font='Arial 10 bold',command=lambda:show_mr(eid.get(),root)).pack()
    if k==0:
        Button(fra,text='BACK',font='Jokerman',command=lambda:abmm(root,idd)).pack(side=BOTTOM)
    if k==1:
        Button(fra,text='BACK',font='Jokerman',command=lambda:admin(root,idd)).pack(side=BOTTOM)

        
   
#************************************************   Pay Salary   ********************************************************
    
def payemp(root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='PAY SALARY',bg='grey',fg='black',height=2,font='Arial 25 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n\n\n").pack()
    Label(fra,text='pay which employee?\n',font='Arial 20 bold').pack(side=TOP,fill=X,expand=NO)
    v=IntVar()
    Radiobutton(fra,text='Regional Business Manager',font='Arial 15 bold',variable=v,value=1).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Area Business Manager',font='Arial 15 bold',variable=v,value=2).pack(side=TOP,fill=X,expand=NO)
    Radiobutton(fra,text='Medical Representative',font='Arial 15 bold',variable=v,value=3).pack(side=TOP,fill=X,expand=NO)
    Button(fra,text='OK',font='Arial 15 bold',command=lambda:pay(v.get(),root,e)).pack()
    Button(fra,text='BACK',font='Jokerman',command=lambda:admin(root,e)).pack(side=BOTTOM)
def pay(v,root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='PAY EMPLOYEE',bg='grey',fg='black',height=4,font='Arial 30 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=4,font='CalibriLight 16 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    if v==1:
        Label(fra,text='RBM_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mrbm1/mrbm2/mrbm3....')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='PAY',font='Arial 15 bold',command=lambda:pay_rbm(eid.get())).pack()
    elif v==2:
        
        Label(fra,text='ABM_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mabm1/mabm2/mabm3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='PAY',font='Arial 15 bold',command=lambda:pay_abm(eid.get())).pack()
    elif v==3:
        
        Label(fra,text='MR_id',font='Arial 15 bold',bg='light grey').pack(side=TOP,fill=X,expand=Y)
        Button(fra,text='HELP',font='Jokerman',command=lambda:showinfo('Entry?','Enter mmr1/mmr2/mmr3...')).pack()
        Label(fra,text='\n').pack()
        eid=Entry(fra,width=14,font="Arial 15",bd=7)
        eid.pack()
        Button(fra,text='PAY',font='Arial 15 bold',command=lambda:pay_mr(eid.get())).pack()
    else:
        payemp(root,e)
    Button(fra,text='BACK',font='Jokerman',command=lambda:payemp(root,e)).pack(side=BOTTOM)
#*************************************************************************************************************
def rbmm(root,myid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='grey').pack()
   # l=Label(fra,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    #l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 20 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Choose an activity',bg='red',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n").pack()
    Button(fra,text='Details Abm Under Supervision',command=lambda:show_all_abm_under_rbm(root,myid),bg='white smoke',bd=4,font='Arial 15 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='Add Target for abm',command=lambda:add_abm_target(root,myid),bg='white smoke',bd=4,font='Arial 15 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='View Target Status of abm',command=lambda:show_target_abm(root,myid),bg='white smoke',bd=4,font='Arial 15 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='View Details of ABM',command=lambda:show(2,root,0,myid),bg='white smoke',bd=4,font='Arial 15 bold').pack()
    Button(fra,text='BACK',font='Jokerman',command=lambda:marketing(root,myid)).pack(side=BOTTOM)

def abmm(root,myid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='grey').pack()
    #l=Label(fra,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    #l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 20 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Choose an activity',bg='red',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n").pack()
    Button(fra,text='Details MR Under Supervision',command=lambda:show_all_mr_under_abm(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='Add Target for MR',command=lambda:add_mr_target(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='View Target Status of mr',command=lambda:show_target_mr(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='Update My Target Status',command=lambda:add_target_status_abm(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='View Details of mr',command=lambda:show(3,root,0,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()

    Button(fra,text='BACK',font='Jokerman',command=lambda:marketing(root,myid)).pack(side=BOTTOM)

def mrr(root,myid):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='grey').pack()
    #l=Label(fra,text='WELCOME',bg='grey',fg='black',height=2,font='Arial 25 bold')
    #l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Marketing Department',bg='light steel blue',fg='black',height=2,font='CalibriLight 20 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Choose an activity',bg='red',fg='black',height=2,font='CalibriLight 14 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n").pack()
    Button(fra,text='Details doc Under Me',command=lambda:show_doc_under_mr(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='Add Status for doc',command=lambda:add_status_doc(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='Update My Target Status',command=lambda:add_target_status_mr(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n\n").pack()
    Button(fra,text='View Details of doc',command=lambda:show_doc(root,myid),bg='white smoke',bd=4,font='Arial 12 bold').pack()
    Label(fra,text="\n").pack()

    Button(fra,text='BACK',font='Jokerman',command=lambda:marketing(root,myid)).pack(side=BOTTOM)

#******************************************************************************************************
'''def backk(root):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    fr1=Frame(root,height=50,bg='light green').pack()
    l=Label(fr1,text='WELCOME TO PHARMACEUTICALS',bg='light green',fg='dark green',height=4,font='CalibriLight 16 bold')
    l.pack(side=TOP,fill=X,expand=YES)
    fr2=Frame(root,height=30,bg='light blue').pack()    
    l=Label(fr1,text='PLEASE LOGIN',bg='light blue',fg='dark blue',height=2,font='CalibriLight 12 bold')
    l.pack(side=TOP,fill=X,expand=YES)
    eid=Entry(fr1,width=16,font="Arial 15",bd=7)
    eid.pack()
    Button(fr1,text='Sign In',font='Arial 15 bold',command=lambda:check(root,eid)).pack()'''
    
    
    
    
        
    
    

#************************************************   Admin and MArketing   ********************************************************

def admin(root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=20,side="top")
    fra=Frame(root,height=50,bg='light green').pack()
    l=Label(fra,text='WELCOME',bg='yellow',fg='black',height=4,font='Arial 30 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Administration Department',bg='light steel blue',fg='black',height=4,font='CalibriLight 16 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n\n\n").pack()
    Button(fra,text='ADD NEW EMPLOYEE',bg='white smoke',bd=4,command=lambda:insertemp(root,e),font='Arial 10').pack()
    Label(fra,text="\n").pack()
    Button(fra,text='REMOVE EMPLOYEE',bg='white smoke',bd=4,command=lambda:deleteemp(root,e),font='Arial 10').pack()
    Label(fra,text="\n").pack()
    Button(fra,text='PAY SALARY',bg='white smoke',bd=4,command=lambda:payemp(root,e),font='Arial 10').pack()
    Label(fra,text="\n").pack()
    Button(fra,text='SEE EMPLOYEE DETAILS',bg='white smoke',bd=4,command=lambda:showemp(root,e),font='Arial 10').pack()
    Button(fra,text='Login again',font='Jokerman',command=lambda:see(root)).pack(padx=5, pady=10, side=LEFT)


    
def marketing(root,e):
    root.destroy()
    root=Tk()
    root.attributes('-fullscreen',True)
    Button(root,text='Exit',font='Arial 15 bold',command=lambda:root.destroy()).pack(padx=20, pady=10,side="top")
    fra=Frame(root,height=40,bg='light green').pack()
    l=Label(fra,text='WELCOME',bg='yellow',fg='black',height=4,font='Arial 30 bold')
    l.pack(side=TOP,fill=X,expand=NO)
    l1=Label(fra,text='Marketing Department',bg='light steel blue',fg='black',height=4,font='CalibriLight 16 bold')
    l1.pack(side=TOP,fill=X,expand=NO)
    l2=Label(fra,text='What are you?',bg='red',fg='black',height=2,font='CalibriLight 14 bold')
    l2.pack(side=TOP,fill=X,expand=NO)
    Label(fra,text="\n").pack()
    
    Button(fra,text='Regional Business Manager',command=lambda:rbmm(root,e),bg='white smoke',bd=4,font='Arial 10 bold').pack()
    Label(fra,text="\n").pack()
    Button(fra,text='Area Business Manager',command=lambda:abmm(root,e),bg='white smoke',bd=4,font='Arial 10 bold').pack()
    Label(fra,text="\n").pack()
    Button(fra,text='Medical Representative',command=lambda:mrr(root,e),bg='white smoke',bd=4,font='Arial 10 bold').pack()
    Label(fra,text="\n").pack()
    Button(fra,text='Login again',font='Jokerman',command=lambda:see(root)).pack(padx=5,pady=10,side=LEFT)

#*******************************************       MARKETING         **************************************************
root.mainloop()
