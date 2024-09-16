import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from RepositoryAdd.repositoryAdd import blCar
from be import Personel
from RepositoryDataBase.RepositoryDataBase import Repository
from API import request
import persian

Personel.UP()
print(request.lasts_day(7)[1])

print(request.days())

print(request.dates())

print(request.months())

print(request.get_season())

print(request.Full_Date())

print(request.baze_date(1403,4,24,1403,4,20))

class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.master = screen
        self.CreateWidget()
        self.textClass = ""
        self.day_Zang = ""
    def CreateWidget(self):
        # Frame

        self.frm1 = Frame(self.master, bg="blue")

        self.frm1_2 = Frame(self.master, bg="white")

        self.frm1_3 = Frame(self.master, bg="#6edece")

        self.frm2 = Frame(self.master)

        self.frm3 = Frame(self.master)

        self.frm6 = Frame(self.master)


        self.frmCom = Frame(self.master)

        self.frm_Zang = Frame(self.master)

        self.frm_Hozor_Add = Frame(self.master)

        self.frm_Add_Student = Frame(self.master)

        self.frm_Hozor_List = Frame(self.master)


        self.frmTar1 = Frame(self.master)

        self.frmTarClass10 = Frame(self.master)

        self.frmTarClass11 = Frame(self.master)

        self.frmTarClass12 = Frame(self.master)

        self.frm_List = Frame(self.master)

        self.frm_hosh = Frame(self.master)

        # end Frame

        # ttk theme

        style = ttk.Style()
        style.theme_use("vista")

        # end ttk theme

        # body layer 1

        self.image = PhotoImage(file="file/8.png")

        self.lbl = Label(self.frm1, image=self.image, bg="blue")
        self.lbl.place(x=23, y=0)

        self.txt = Label(self.frm1, text="نرم افزار اداره ی مدرسه", fg="white", bg="blue", font=("Calibri", 14, "bold")).place(x=125, y=370)

        self.imgV = PhotoImage(file="file/54.png")

        self.btngo = Label(self.frm1, text="وارد شدن", image=self.imgV, compound="center", bg="blue")
        self.btngo.place(x=100, y=400)
        self.btngo.bind("<Button-1>", self.shownewfrm)

        self.txt = Label(self.frm1, text="در صورتی که قبلا ثبت نام کردید وارد شوید", fg="white", bg="blue", font=("Calibri", 14, "bold")).place(x=65, y=500)

        # end body layer 1

        # body layer 1_2

        self.img = PhotoImage(file="file/56.png")

        self.lblbtn = Label(self.frm1_2, image=self.img, width=40, height=40)
        self.lblbtn.place(x=350, y=4)
        self.lblbtn.bind("<Button-1>", self.Close)

        self.lblsabt = Label(self.frm1_2, text="ثبت نام", bg="white", fg="#fe7188",font=("Calibri", 25, "bold")).place(x=165,y=30)

        self.lblname = Label(self.frm1_2, text="نام کاربری", bg="white", fg="#fe7188",font=("Calibri", 12, "bold")).place(x=175,y=130)

        self.txtname = StringVar()

        self.txtU = StringVar()

        self.ent1 = ttk.Entry(self.frm1_2, textvariable=self.txtU, justify="center")
        self.ent1.place(x=145, y=180)

        self.lblf = Label(self.frm1_2, text="رمز عبور", bg="white", fg="#fe7188",font=("Calibri", 12, "bold")).place(x=175, y=230)

        self.txtpass = StringVar()

        self.ent2 = ttk.Entry(self.frm1_2, textvariable=self.txtpass, justify="center", show="*")
        self.ent2.place(x=145, y=275)

        self.lblf2 = Label(self.frm1_2, text="تکرار رمز عبور", bg="white", fg="#fe7188",font=("Calibri", 12, "bold")).place(x=160, y=330)

        self.txtpass2 = StringVar()

        self.ent3 = ttk.Entry(self.frm1_2, textvariable=self.txtpass2, justify="center", show="*")
        self.ent3.place(x=145, y=380)

        self.imgS = PhotoImage(file="file/54.png")

        self.lblbtnn = Label(self.frm1_2, text="ثبت نام", compound="center", image=self.imgS, bg="white")
        self.lblbtnn.place(x=110, y=450)
        self.lblbtnn.bind("<Button-1>", self.Sabt)
        # end body layer 1_2

        # body layer 1_3

        self.img2 = PhotoImage(file="file/787.png")

        self.lblbtn2 = Label(self.frm1_3, image=self.img2, bg="#6edece", width=40, height=40)
        self.lblbtn2.place(x=350, y=4)
        self.lblbtn2.bind("<Button-1>", self.Close)

        self.imgret = PhotoImage(file="file/100.png")

        self.lblreturn = Label(self.frm1_3, image=self.imgret, bg="#6edece")
        self.lblreturn.place(x=0, y=0)
        self.lblreturn.bind("<Button-1>", self.backlayer1_3)

        self.lblW = Label(self.frm1_3, text="ورود", font=("Calibri", 30, "bold"), bg="#6edece", fg="#fe7188").place(x=165, y=86)

        self.lblname = Label(self.frm1_3, text="نام کاربری", bg="#6edece", fg="#fe7188",font=("Calibri", 14, "bold")).place(x=170,y=180)

        self.txtUser = StringVar()

        self.User = ttk.Entry(self.frm1_3, textvariable=self.txtUser, justify="center")
        self.User.place(x=145, y=230)

        self.lblf = Label(self.frm1_3, text="رمز عبور", bg="#6edece", fg="#fe7188",font=("Calibri", 14, "bold")).place(x=170, y=270)

        self.txtPass = StringVar()

        self.Pass = ttk.Entry(self.frm1_3, textvariable=self.txtPass, justify="center", show="*")
        self.Pass.place(x=145, y=310)

        self.imgsd = PhotoImage(file="file/878.png")

        self.lblclick = Label(self.frm1_3, text="ورود", image=self.imgsd, compound="center", bg="#6edece")
        self.lblclick.place(x=110, y=400)
        self.lblclick.bind("<Button-1>", self.Welcome2)

        # end body layer 1_3

        # body layer 2

        self.bgS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frm2, image=self.bgS)
        self.lblbgS.place(x=0, y=0)

        self.imgd = PhotoImage(file="file/787.png")

        self.lbln = Label(self.frm2, image=self.imgd, bg="#023912", width=40, height=40)
        self.lbln.place(x=725, y=35)
        self.lbln.bind("<Button-1>", self.Close)

        self.List = PhotoImage(file="file/List.png")

        self.Lists = Label(self.frm2, font=("Calibri", 16, "bold"), image=self.List)
        self.Lists.place(x=34, y=47, width=100, height=74)
        self.Lists.bind("<Button-1>", self.onclickList)

        self.List_ss = PhotoImage(file="file/hosh.png")

        self.Lists_hosh = Label(self.frm2, font=("Calibri", 16, "bold"), image=self.List_ss)
        self.Lists_hosh.place(x=134, y=47, width=100, height=74)
        self.Lists_hosh.bind("<Button-1>", self.onclickhosh)

        self.Tchs = PhotoImage(file="file/Add_Tch.png")

        self.Tch_s = Label(self.frm2, font=("Calibri", 16, "bold"), image=self.Tchs)
        self.Tch_s.place(x=34, y=197, width=100, height=74)
        self.Tch_s.bind("<Button-1>", self.onclickTeacher)

        self.Std_icon = PhotoImage(file="file/add_std.png")

        self.Students = Label(self.frm2, font=("Calibri", 16, "bold"), image=self.Std_icon)
        self.Students.place(x=134, y=197, width=100, height=74)
        self.Students.bind("<Button-1>", self.showLayer_Add_Std)

        self.Hgh = PhotoImage(file="file/12.png")

        self.Hozur = Label(self.frm2, font=("Calibri", 16, "bold"), image=self.Hgh)
        self.Hozur.place(x=34, y=347, width=100, height=74)
        self.Hozur.bind("<Button-1>", self.onclickHozur)

        self.Backimg = PhotoImage(file="file/bg.png")

        self.Back = Label(self.frm2, font=("Calibri", 16, "bold"), image=self.Backimg)
        self.Back.place(x=34, y=497, width=100, height=74)
        self.Back.bind("<Button-1>", self.onclickBack)

        #end body layer 2

        #body layer 3
        self.btnback1 = Button(self.frm3, pady=7, padx=15, text="برگشتن", fg="red", command=self.back)
        self.btnback1.place(x=10, y=10)

        self.img144 = PhotoImage(file="file/787.png")

        self.lblbtn13 = Label(self.frm3, image=self.img144, width=40, height=40, bg="#f0f0f0")
        self.lblbtn13.place(x=750, y=10)
        self.lblbtn13.bind("<Button-1>", self.Close)

        self.getSearch2 = StringVar()
        self.Search2 = ttk.Entry(self.frm3, textvariable=self.getSearch2, font=("Calibri", 12, "bold"))
        self.Search2.place(x=538, y=250)

        self.btnSearch2 = Button(self.frm3, padx=5, text="جستوجو", font=("Calibri", 11, "bold"), command=self.oneclickSearch2)
        self.btnSearch2.place(x=460, y=246)

        self.refresh2 = Button(self.frm3, padx=5, pady=2, text="Refresh", font=("Calibri", 11, "bold"), command=self.Refresh2)
        self.refresh2.place(x=350, y=246)

        self.col_Tch_Add = ("c1", "c2", "c3", "c4", "c5", "c6", "c7")
        self.tbl_Tch_Add = ttk.Treeview(self.frm3, columns=self.col_Tch_Add, show="headings", height=12)

        self.tbl_Tch_Add.column("# 7", anchor=N, width=0, minwidth=0, stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 7", text="")

        self.tbl_Tch_Add.column("# 6", anchor=N, width=90,minwidth=90,stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 6", anchor=N, text="نام معلم")

        self.tbl_Tch_Add.column("# 5", anchor=N, width=120,minwidth=120,stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 5", anchor=N, text="نام خانوادگی")

        self.tbl_Tch_Add.column("# 4", anchor=N, width=120,minwidth=120,stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 4", anchor=N, text="درس تحصیلی")

        self.tbl_Tch_Add.column("# 3", anchor=N, width=120,minwidth=120,stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 3", anchor=N, text="مدرک تحصیلی")

        self.tbl_Tch_Add.column("# 2", anchor=N, width=120,minwidth=120,stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 2", anchor=N, text="کد پرسنلی")

        self.tbl_Tch_Add.column("# 1", anchor=N, width=120,minwidth=120,stretch=tkinter.YES)
        self.tbl_Tch_Add.heading("# 1", anchor=N, text="کد ملی")
        self.tbl_Tch_Add.bind("<Button-1>", self.getsc)

        self.tbl_Tch_Add.place(x=56, y=300)

        self.Ida = StringVar()
        self.txtIda = ttk.Entry(self.frm3, textvariable=self.Ida, justify="right")
        self.txtIda.place_forget()

        self.nameTget = StringVar()
        self.nameT = ttk.Entry(self.frm3, justify="center", textvariable=self.nameTget, font=("Calibri", 12, "bold"))
        self.nameT.place(x=475, y=25)

        self.familyTget = StringVar()
        self.familyT = ttk.Entry(self.frm3, justify="center", textvariable=self.familyTget, font=("Calibri", 12, "bold"))
        self.familyT.place(x=150, y=25)

        self.DarsT_Addget = StringVar()
        self.DarsT_Add = ttk.Entry(self.frm3, justify="center", textvariable=self.DarsT_Addget,
                                   font=("Calibri", 12, "bold"))
        self.DarsT_Add.place(x=475, y=100)

        self.madrak_get = StringVar()
        self.madrak_Tch = ttk.Entry(self.frm3, justify="center", textvariable=self.madrak_get,
                                    font=("Calibri", 12, "bold"))
        self.madrak_Tch.place(x=150, y=100)

        self.personel_codeget = StringVar()
        self.personel_code = ttk.Entry(self.frm3, justify="center", textvariable=self.personel_codeget, font=("Calibri", 12, "bold"))
        self.personel_code.place(x=475, y=175)

        self.National_CodeTget = StringVar()
        self.National_CodeT = ttk.Entry(self.frm3, justify="center", textvariable=self.National_CodeTget,
                                        font=("Calibri", 12, "bold"))
        self.National_CodeT.place(x=150, y=175)

        self.btnSave_Tch = Button(self.frm3, padx=7, text="ثبت اطلاعات", font=("Calibri", 12, "bold"), command=self.Register2)
        self.btnSave_Tch.place(x=230, y=246.5)

        self.lblTname = Label(self.frm3, text="نام معلم", font=("Calibri", 12, "bold")).place(x=650, y=25)

        self.lblTF = Label(self.frm3, text="نام خانوادگی معلم", font=("Calibri", 12, "bold")).place(x=325, y=25)

        self.lblTD = Label(self.frm3, text="درس تحصیلی", font=("Calibri", 12, "bold")).place(x=650, y=100)

        self.lblTage = Label(self.frm3, text="مدرک تحصیلی", font=("Calibri", 12, "bold")).place(x=325, y=100)

        self.lblTD = Label(self.frm3, text="کد ملی", font=("Calibri", 12, "bold")).place(x=325, y=175)

        self.lblTD = Label(self.frm3, text="کد پرسنلی", font=("Calibri", 12, "bold")).place(x=650, y=175)


        self.btnD = Button(self.frm3, text="حذف", bg="red", font=("Calibri", 12, "bold"), padx=5, command=self.OnclickDelet)
        self.btnD.place_forget()

        self.btnE = Button(self.frm3, text="ویرایش", bg="green", font=("Calibri", 12, "bold"), padx=15, command=self.OnclickEdit)
        self.btnE.place_forget()

        #end body layer 3

        # body layer 6

        self.bgSS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frm6, image=self.bgSS, bg="#023912")
        self.lblbgS.place(x=0, y=0)

        self.img3 = PhotoImage(file="file/787.png")

        self.lblbtn3 = Label(self.frm6, image=self.img3, width=40, height=40, bg="#023912")
        self.lblbtn3.place(x=725, y=35)
        self.lblbtn3.bind("<Button-1>", self.Close)

        self.btnback4 = Button(self.frm6, pady=7, padx=15, text="برگشتن", fg="red", command=self.back)
        self.btnback4.place(x=10, y=10)

        self.Select1 = Button(self.frm6, padx=5, text="رشته تربیت بدنی", font=("Calibri", 11, "bold"), command=self.SelectTar)
        self.Select1.place(x=260, y=246)

        self.Select2 = Button(self.frm6, padx=5, text="رشته شبکه و نرم افزار", font=("Calibri", 11, "bold"), command=self.SelectCom)
        self.Select2.place(x=460, y=246)

        # end body layer 6

        # body layer Com

        self.bgSSS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frmCom, image=self.bgSSS)
        self.lblbgS.place(x=0, y=0)

        self.img4 = PhotoImage(file="file/787.png")

        self.lblbtn4 = Label(self.frmCom, image=self.img4, width=40, height=40, bg="#023912")
        self.lblbtn4.place(x=725, y=35)
        self.lblbtn4.bind("<Button-1>", self.Close)

        self.btnbackCom = Button(self.frmCom, pady=7, padx=15, text="برگشتن", fg="red", command=self.showLayer_6)
        self.btnbackCom.place(x=10, y=10)

        self.SelectCom1 = Button(self.frmCom, padx=5, text="۱۰شبکه", font=("Calibri", 11, "bold"),
                                 command=lambda: self.showLayer_Add_Hozor("۱۰شبکه"))
        self.SelectCom1.place(x=210, y=246)

        self.SelectCom2 = Button(self.frmCom, padx=5, text="۱۱شبکه", font=("Calibri", 11, "bold"),
                                 command=lambda: self.showLayer_Add_Hozor("۱۱شبکه"))
        self.SelectCom2.place(x=360, y=246)

        self.SelectCom3 = Button(self.frmCom, padx=5, text="۱۲شبکه", font=("Calibri", 11, "bold"),
                                 command=lambda: self.showLayer_Add_Hozor("۱۲شبکه"))
        self.SelectCom3.place(x=510, y=246)

        #end body layer Com

        # body layer Tar1

        self.bgSSSS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frmTar1, image=self.bgSSSS)
        self.lblbgS.place(x=0, y=0)

        self.img5 = PhotoImage(file="file/787.png")

        self.lblbtn5 = Label(self.frmTar1, image=self.img5, width=40, height=40, bg="#023912")
        self.lblbtn5.place(x=725, y=35)
        self.lblbtn5.bind("<Button-1>", self.Close)

        self.btnbackTar1 = Button(self.frmTar1, pady=7, padx=15, text="برگشتن", fg="red", command=self.showLayer_6)
        self.btnbackTar1.place(x=10, y=10)

        self.SelectTar1 = Button(self.frmTar1, padx=5, text="۱۰تربیت بدنی", font=("Calibri", 11, "bold"),
                                 command=self.showLayer_TarClass10)
        self.SelectTar1.place(x=210, y=246)

        self.SelectTar2 = Button(self.frmTar1, padx=5, text="۱۱تربیت بدنی", font=("Calibri", 11, "bold"),
                                 command=self.showLayer_TarClass11)
        self.SelectTar2.place(x=360, y=246)

        self.SelectTar3 = Button(self.frmTar1, padx=5, text="۱۲تربیت بدنی", font=("Calibri", 11, "bold"),
                                 command=self.showLayer_TarClass12)
        self.SelectTar3.place(x=510, y=246)

        # end body layer Com

        # body layer TarClass10

        self.bgSSSSS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frmTarClass10, image=self.bgSSSSS)
        self.lblbgS.place(x=0, y=0)

        self.img7 = PhotoImage(file="file/787.png")

        self.lblbtn7 = Label(self.frmTarClass10, image=self.img7, width=40, height=40, bg="#023912")
        self.lblbtn7.place(x=725, y=35)
        self.lblbtn7.bind("<Button-1>", self.Close)

        self.btnbackTarClass10 = Button(self.frmTarClass10, pady=7, padx=15, text="برگشتن", fg="red", command=self.showLayer_Tar1)
        self.btnbackTarClass10.place(x=10, y=10)

        self.lblbgS = Label(self.frmTarClass10, text="رشته تربیت بدنی", font=("Calibri", 11, "bold"), bg="green", fg="white")
        self.lblbgS.place(x=360, y=150)

        self.SelectClass10_1 = Button(self.frmTarClass10, padx=5, text="۱۰/۱تربیت بدنی", font=("Calibri", 11, "bold"),
                                      command=lambda: self.showLayer_Add_Hozor("۱۰/۱تربیت بدنی"))
        self.SelectClass10_1.place(x=251, y=246)

        self.SelectClass_10_2 = Button(self.frmTarClass10, padx=5, text="۱۰/۲تربیت بدنی", font=("Calibri", 11, "bold"),
                                       command=lambda: self.showLayer_Add_Hozor("۱۰/۲تربیت بدنی"))
        self.SelectClass_10_2.place(x=460, y=246)

        # end body layer TarClass10

        # body layer TarClass11

        self.bgSSSSSS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frmTarClass11, image=self.bgSSSSSS)
        self.lblbgS.place(x=0, y=0)

        self.img8 = PhotoImage(file="file/787.png")

        self.lblbtn8 = Label(self.frmTarClass11, image=self.img8, width=40, height=40, bg="#023912")
        self.lblbtn8.place(x=725, y=35)
        self.lblbtn8.bind("<Button-1>", self.Close)

        self.btnbackTarClass11 = Button(self.frmTarClass11, pady=7, padx=15, text="برگشتن", fg="red", command=self.showLayer_Tar1)
        self.btnbackTarClass11.place(x=10, y=10)

        self.lblbgS = Label(self.frmTarClass11, text="رشته تربیت بدنی", font=("Calibri", 11, "bold"), bg="green", fg="white")
        self.lblbgS.place(x=360, y=150)

        self.SelectClass11_1 = Button(self.frmTarClass11, padx=5, text="۱۱/۱تربیت بدنی", font=("Calibri", 11, "bold"),
                                      command=lambda: self.showLayer_Add_Hozor("۱۱/۱تربیت بدنی"))
        self.SelectClass11_1.place(x=251, y=246)

        self.SelectClass_11_2 = Button(self.frmTarClass11, padx=5, text="۱۱/۲تربیت بدنی", font=("Calibri", 11, "bold"),
                                       command=lambda: self.showLayer_Add_Hozor("۱۱/۲تربیت بدنی"))
        self.SelectClass_11_2.place(x=460, y=246)

        # end body layer TarClass11

        # body layer TarClass12

        self.bgSSSSSSS = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frmTarClass12, image=self.bgSSSSSSS)
        self.lblbgS.place(x=0, y=0)

        self.img9 = PhotoImage(file="file/787.png")

        self.lblbtn9 = Label(self.frmTarClass12, image=self.img9, width=40, height=40, bg="#023912")
        self.lblbtn9.place(x=725, y=35)
        self.lblbtn9.bind("<Button-1>", self.Close)

        self.btnbackTarClass12 = Button(self.frmTarClass12, pady=7, padx=15, text="برگشتن", fg="red",
                                        command=self.showLayer_Tar1)
        self.btnbackTarClass12.place(x=10, y=10)

        self.lblbgS = Label(self.frmTarClass12, text="رشته تربیت بدنی", font=("Calibri", 11, "bold"), bg="green", fg="white")
        self.lblbgS.place(x=360, y=150)

        self.SelectClass12_1 = Button(self.frmTarClass12, padx=5, text="۱۲/۱تربیت بدنی", font=("Calibri", 11, "bold"),
                                      command=lambda: self.showLayer_Add_Hozor("۱۲/۱تربیت بدنی"))
        self.SelectClass12_1.place(x=251, y=246)

        self.SelectClass_12_2 = Button(self.frmTarClass12, padx=5, text="۱۲/۲تربیت بدنی", font=("Calibri", 11, "bold"),
                                       command=lambda: self.showLayer_Add_Hozor("۱۲/۲تربیت بدنی"))
        self.SelectClass_12_2.place(x=460, y=246)

        # end body layer TarClass12

        #body layer Add_Hozor

        self.btn_backzang = Button(self.frm_Hozor_Add, pady=7, padx=15, text="برگشتن", fg="red",
                                   command=self.back_zang)
        self.btn_backzang.place(x=10, y=10)

        self.img10 = PhotoImage(file="file/787.png")

        self.lblbtn10 = Label(self.frm_Hozor_Add, image=self.img10, width=40, height=40, bg="#f0f0f0")
        self.lblbtn10.place(x=750, y=10)
        self.lblbtn10.bind("<Button-1>", self.Close)

        self.btn_List_Student = Button(self.frm_Hozor_Add, padx=5, text="دیدن نتایج",
                                       font=("Calibri", 12, "bold"), fg="cyan", bg="green",
                                       command=self.showLayer_Hozor_List)
        self.btn_List_Student.place(x=600, y=146.4)

        self.lbl_Add_Hozor_STd = Label(self.frm_Hozor_Add, text=": نام هنرجو", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_STd.place(x=600, y=80)

        self.lbl_Add_Hozor_STd = Label(self.frm_Hozor_Add, text=": نام خانوادگی هنرجو", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_STd.place(x=600, y=110)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_Add, text=": نام هنرآموز", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=500, y=160)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_Add, text=": نام خانوادگی هنرآموز", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=500, y=190)

        self.btn_Add_Student_Hozor_Yes = Button(self.frm_Hozor_Add, padx=5, text="حاضر",
                                                font=("Calibri", 11, "bold"),fg="green",bg="lightblue",
                                                command=lambda: self.Hozor_Ghiyab("Std","حاضر"))
        self.btn_Add_Student_Hozor_Yes.place(x=370, y=96.4)

        self.btn_Add_Student_Hozor_No = Button(self.frm_Hozor_Add, padx=5, text="غایب",
                                               font=("Calibri", 11, "bold"),fg="red",bg="lightblue",
                                               command=lambda: self.Hozor_Ghiyab("Std","غایب"))
        self.btn_Add_Student_Hozor_No.place(x=315, y=96.4)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_Add, text=": تاخیر", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=270, y=100)

        self.check_Std_Long_var = BooleanVar()
        self.CK_btn_Std_long = Checkbutton(self.frm_Hozor_Add,variable=self.check_Std_Long_var,
                                           font=("Calibri", 11, "bold"), fg="orange")
        self.CK_btn_Std_long.place(x=245, y=100)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_Add, text=": اخراج", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=190, y=100)

        self.check_Std_Exit_C_var = BooleanVar()
        self.CK_btn_Exit_Class = Checkbutton(self.frm_Hozor_Add,variable=self.check_Std_Exit_C_var,
                                             font=("Calibri", 11, "bold"), fg="red")
        self.CK_btn_Exit_Class.place(x=165, y=100)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_Add, text=": فرار", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=120, y=100)

        self.check_Std_Exit_S_var = BooleanVar()
        self.CK_btn_Exit_School = Checkbutton(self.frm_Hozor_Add,variable=self.check_Std_Exit_S_var,
                                              font=("Calibri", 11, "bold"), fg="red")
        self.CK_btn_Exit_School.place(x=95, y=100)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_Add, text=": تاخیر", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=155, y=171.4)

        self.check_Tch_Long_var = BooleanVar()
        self.CK_btn_Tch_long = Checkbutton(self.frm_Hozor_Add,variable=self.check_Tch_Long_var,
                                           font=("Calibri", 11, "bold"), fg="orange")
        self.CK_btn_Tch_long.place(x=130, y=171.4)

        self.btn_Add_Tch_Hozor_Yes = Button(self.frm_Hozor_Add, padx=5, text="حاضر",
                                            font=("Calibri", 11, "bold"), fg="green", bg="lightblue",
                                            command=lambda: self.Hozor_Ghiyab("Tch","حاضر"))
        self.btn_Add_Tch_Hozor_Yes.place(x=270, y=171.4)

        self.btn_Add_Tch_Hozor_No = Button(self.frm_Hozor_Add, padx=5, text="غایب",
                                           font=("Calibri", 11, "bold"), fg="red", bg="lightblue",
                                           command=lambda: self.Hozor_Ghiyab("Tch","غایب"))
        self.btn_Add_Tch_Hozor_No.place(x=215, y=171.4)

        self.Honar_Jo_get = StringVar()
        self.Honar_Jo = ttk.Entry(self.frm_Hozor_Add, justify="center",textvariable=self.Honar_Jo_get, font=("Calibri", 12, "bold"))
        self.Honar_Jo.place(x=425, y=80)

        self.Honar_Jo_get_Family = StringVar()
        self.Honar_Jo_Family = ttk.Entry(self.frm_Hozor_Add, justify="center", textvariable=self.Honar_Jo_get_Family,
                                         font=("Calibri", 12, "bold"))
        self.Honar_Jo_Family.place(x=425, y=110)

        self.Honar_Amoz_get = StringVar()
        self.Honar_Amoz = ttk.Entry(self.frm_Hozor_Add, justify="center", textvariable=self.Honar_Amoz_get,
                                    font=("Calibri", 12, "bold"))
        self.Honar_Amoz.place(x=325, y=160)

        self.Honar_Amoz_get_Family = StringVar()
        self.Honar_Amoz_Family = ttk.Entry(self.frm_Hozor_Add, justify="center", textvariable=self.Honar_Amoz_get_Family,
                                           font=("Calibri", 12, "bold"))
        self.Honar_Amoz_Family.place(x=325, y=190)

        self.cols_day_Tch = ("c1", "c2", "c3")
        self.tbl_day_Tch = ttk.Treeview(self.frm_Hozor_Add, columns=self.cols_day_Tch, show="headings", height=16)

        self.tbl_day_Tch.column("# 3", anchor=N, width=0, minwidth=0)
        self.tbl_day_Tch.heading("# 3", text="سطر")

        self.tbl_day_Tch.column("# 2", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_day_Tch.heading("# 2", anchor=N, text="نام هنرآموز")

        self.tbl_day_Tch.column("# 1", anchor=N, width=150, minwidth=150, stretch=tkinter.YES)
        self.tbl_day_Tch.heading("# 1", anchor=N, text="نام خانوادگی هنرآموز")

        self.tbl_day_Tch.bind("<Button-1>", self.getsc_Tch_List)

        self.tbl_day_Tch.place(x=405, y=250)

        self.Idde = StringVar()
        self.txtIdde = ttk.Entry(self.frm_Hozor_Add, textvariable=self.Idde, justify="right")
        self.txtIdde.place_forget()

        self.Iddt = StringVar()
        self.txtIddt = ttk.Entry(self.frm_Hozor_Add, textvariable=self.Iddt, justify="right")
        self.txtIddt.place_forget()

        self.cols_day_Std = ("c1", "c2", "c3")
        self.tbl_day_Std = ttk.Treeview(self.frm_Hozor_Add, columns=self.cols_day_Std, show="headings", height=16)

        self.tbl_day_Std.column("# 3", anchor=N, width=0, minwidth=0)
        self.tbl_day_Std.heading("# 3", text="سطر")

        self.tbl_day_Std.column("# 2", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_day_Std.heading("# 2", anchor=N, text="نام هنرجو")

        self.tbl_day_Std.column("# 1", anchor=N, width=150, minwidth=150, stretch=tkinter.YES)
        self.tbl_day_Std.heading("# 1", anchor=N, text="نام خانوادگی هنرجو")

        self.tbl_day_Std.bind("<Button-1>", self.getsc_Std_List)

        self.tbl_day_Std.place(x=125, y=250)

        # end body layer Add_Hozor

        # body layer Zang

        self.bg_Zang = PhotoImage(file="file/blackboard.png")

        self.lblbgS = Label(self.frm_Zang, image=self.bg_Zang)
        self.lblbgS.place(x=0, y=0)

        self.img11 = PhotoImage(file="file/787.png")

        self.lblbtn11 = Label(self.frm_Zang, image=self.img11, width=40, height=40, bg="#023912")
        self.lblbtn11.place(x=725, y=35)
        self.lblbtn11.bind("<Button-1>", self.Close)

        self.btnbackdays = Button(self.frm_Zang, pady=7, padx=15, text="برگشتن", fg="red",
                                  command=self.showLayer_Select_Class)
        self.btnbackdays.place(x=10, y=10)

        self.lblzang = Label(self.frm_Zang, text="زنگ را وارد کنید")
        self.lblzang.place(x=350, y=50)

        # end body layer Zang

        # body layer Hozor_List

        self.btn_backHozor = Button(self.frm_Hozor_List, pady=7, padx=15, text="برگشتن", fg="red",
                                    command=self.showLayer_Hozor_Add)
        self.btn_backHozor.place(x=10, y=10)

        self.img12 = PhotoImage(file="file/787.png")

        self.lblbtn12 = Label(self.frm_Hozor_List, image=self.img12, width=40, height=40, bg="#f0f0f0")
        self.lblbtn12.place(x=750, y=10)
        self.lblbtn12.bind("<Button-1>", self.Close)


        self.lbl_Add_Hozor_STd = Label(self.frm_Hozor_List, text=": نام هنرجو", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_STd.place(x=620, y=80)

        self.lbl_Add_Hozor_STd = Label(self.frm_Hozor_List, text=": نام خانوادگی هنرجو", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_STd.place(x=620, y=110)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_List, text=": نام هنرآموز", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=520, y=160)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_List, text=": نام خانوادگی هنرآموز", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=520, y=190)

        self.Std_Radio_yes = IntVar()
        self.btn_Add_Student_Hozor_Yes_List = Radiobutton(self.frm_Hozor_List, padx=5, text="حاضر",value=1,
                                                          font=("Calibri", 11, "bold"),fg="green",variable=self.Std_Radio_yes,
                                                          command=lambda: self.Radio_Check("Std", "yes"))
        self.btn_Add_Student_Hozor_Yes_List.place(x=370, y=96.4)

        self.Std_Radio_no = IntVar()
        self.btn_Add_Student_Hozor_No_List = Radiobutton(self.frm_Hozor_List, padx=5, text="غایب",value=2,
                                                         font=("Calibri", 11, "bold"),fg="red",variable=self.Std_Radio_no,
                                                         command=lambda: self.Radio_Check("Std", "no"))
        self.btn_Add_Student_Hozor_No_List.place(x=315, y=96.4)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_List, text=": تاخیر", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=270, y=100)

        self.check_Std_Long_var_List = BooleanVar()
        self.CK_btn_Std_long_List = Checkbutton(self.frm_Hozor_List,variable=self.check_Std_Long_var_List,
                                                font=("Calibri", 11, "bold"), fg="orange")
        self.CK_btn_Std_long_List.place(x=245, y=100)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_List, text=": اخراج", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=190, y=100)

        self.check_Std_Exit_C_var_List = BooleanVar()
        self.CK_btn_Exit_Class_List = Checkbutton(self.frm_Hozor_List,variable=self.check_Std_Exit_C_var_List,
                                                  font=("Calibri", 11, "bold"), fg="red")
        self.CK_btn_Exit_Class_List.place(x=165, y=100)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_List, text=": فرار", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=120, y=100)

        self.check_Std_Exit_S_var_List = BooleanVar()
        self.CK_btn_Exit_School_List = Checkbutton(self.frm_Hozor_List,variable=self.check_Std_Exit_S_var_List,
                                                   font=("Calibri", 11, "bold"), fg="red")
        self.CK_btn_Exit_School_List.place(x=95, y=100)

        self.lbl_Add_Hozor_Tch = Label(self.frm_Hozor_List, text=": تاخیر", font=("Calibri", 12, "bold"))
        self.lbl_Add_Hozor_Tch.place(x=155, y=175)

        self.check_Tch_Long_var_List = BooleanVar()
        self.CK_btn_Tch_long_List = Checkbutton(self.frm_Hozor_List,variable=self.check_Tch_Long_var_List,
                                                font=("Calibri", 11, "bold"), fg="orange")
        self.CK_btn_Tch_long_List.place(x=130, y=175)

        self.Tch_Radio_yes = IntVar()
        self.btn_Add_Tch_Hozor_Yes_List = Radiobutton(self.frm_Hozor_List, padx=5, text="حاضر",
                                                      font=("Calibri", 11, "bold"), fg="green",variable=self.Tch_Radio_yes,value=1,
                                                      command=lambda: self.Radio_Check("Tch", "yes"))
        self.btn_Add_Tch_Hozor_Yes_List.place(x=270, y=171.4)

        self.Tch_Radio_no = IntVar()
        self.btn_Add_Tch_Hozor_No_List = Radiobutton(self.frm_Hozor_List, padx=5, text="غایب",value=2,
                                                     font=("Calibri", 11, "bold"), fg="red",variable=self.Tch_Radio_no,
                                                     command=lambda: self.Radio_Check("Tch", "no"))
        self.btn_Add_Tch_Hozor_No_List.place(x=215, y=171.4)

        self.Honar_Jo_get_List = StringVar()
        self.Honar_Jo_List = ttk.Entry(self.frm_Hozor_List, justify="center",textvariable=self.Honar_Jo_get_List, font=("Calibri", 12, "bold"))
        self.Honar_Jo_List.place(x=445, y=80)

        self.Honar_Jo_get_List_Family = StringVar()
        self.Honar_Jo_List_Family = ttk.Entry(self.frm_Hozor_List, justify="center", textvariable=self.Honar_Jo_get_List_Family,
                                              font=("Calibri", 12, "bold"))
        self.Honar_Jo_List_Family.place(x=445, y=110)

        self.Honar_Amoz_get_List = StringVar()
        self.Honar_Amoz_List = ttk.Entry(self.frm_Hozor_List, justify="center", textvariable=self.Honar_Amoz_get_List,
                                         font=("Calibri", 12, "bold"))
        self.Honar_Amoz_List.place(x=345, y=160)

        self.Honar_Amoz_get_List_Family = StringVar()
        self.Honar_Amoz_List_Family = ttk.Entry(self.frm_Hozor_List, justify="center", textvariable=self.Honar_Amoz_get_List_Family,
                                                font=("Calibri", 12, "bold"))
        self.Honar_Amoz_List_Family.place(x=345, y=190)

        self.col_Student_Hozor = ("c1", "c2", "c3", "c4", "c5", "c6", "c7")
        self.tbl_Hozor_Student = ttk.Treeview(self.frm_Hozor_List,
                                              columns=self.col_Student_Hozor, show="headings", height=14)

        self.tbl_Hozor_Student.column("# 7", anchor=N, width=0, minwidth=0, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 7", text="سطر")

        self.tbl_Hozor_Student.column("# 6", anchor=N, width=80,minwidth=80, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 6", anchor=N, text="نام هنرجو")

        self.tbl_Hozor_Student.column("# 5", anchor=N, width=105, minwidth=105, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 5", anchor=N, text="نام خانوادگی هنرجو")

        self.tbl_Hozor_Student.column("# 4", anchor=N, width=70,minwidth=70, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 4", anchor=N, text="حاضر غایب")

        self.tbl_Hozor_Student.column("# 3", anchor=N, width=70,minwidth=70, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 3", anchor=N, text="تاخیر")

        self.tbl_Hozor_Student.column("# 2", anchor=N, width=70,minwidth=70, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 2", anchor=N, text="اخراج")

        self.tbl_Hozor_Student.column("# 1", anchor=N, width=60,minwidth=60, stretch=tkinter.YES)
        self.tbl_Hozor_Student.heading("# 1", anchor=N, text="فرار")

        self.tbl_Hozor_Student.bind("<Button-1>", self.getsc_Hozor_Std_List)

        self.tbl_Hozor_Student.place(x=340, y=290)

        self.col_Tch_Hozor = ("c1", "c2", "c3", "c4", "c5")
        self.tbl_Hozor_Tch = ttk.Treeview(self.frm_Hozor_List,
                                          columns=self.col_Tch_Hozor, show="headings", height=5)

        self.tbl_Hozor_Tch.column("# 5", anchor=N, width=0, minwidth=0, stretch=tkinter.YES)
        self.tbl_Hozor_Tch.heading("# 5", text="سطر")

        self.tbl_Hozor_Tch.column("# 4", anchor=N, width=80, minwidth=80, stretch=tkinter.YES)
        self.tbl_Hozor_Tch.heading("# 4", anchor=N, text="نام هنرآموز")

        self.tbl_Hozor_Tch.column("# 3", anchor=N, width=110, minwidth=110, stretch=tkinter.YES)
        self.tbl_Hozor_Tch.heading("# 3", anchor=N, text="نام خانوادگی هنرآموز")

        self.tbl_Hozor_Tch.column("# 2", anchor=N, width=70, minwidth=70, stretch=tkinter.YES)
        self.tbl_Hozor_Tch.heading("# 2", anchor=N, text="حاضر غایب")

        self.tbl_Hozor_Tch.column("# 1", anchor=N, width=70, minwidth=70, stretch=tkinter.YES)
        self.tbl_Hozor_Tch.heading("# 1", anchor=N, text="تاخیر")

        self.tbl_Hozor_Tch.bind("<Button-1>", self.getsc_Hozor_Tch_List)

        self.tbl_Hozor_Tch.place(x=3, y=290)

        self.Srch_Std_List_val = StringVar()
        self.Srch_Std_List = ttk.Entry(self.frm_Hozor_List, justify="center", textvariable=self.Srch_Std_List_val,
                                       font=("Calibri", 12, "bold"))
        self.Srch_Std_List.place(x=550, y=250)

        self.btn_Srch_List_Std = Button(self.frm_Hozor_List, text="جتسوجو", font=("Calibri", 12, "bold"),
                                        command=self.oneclickSearch_Std)
        self.btn_Srch_List_Std.place(x=475, y=246)

        self.btn_Refresh_List_Std = Button(self.frm_Hozor_List, text="Refresh", font=("Calibri", 12, "bold"),
                                           command=self.Std_Refresh)
        self.btn_Refresh_List_Std.place(x=400, y=246)

        self.btnE_Hozor_List = Button(self.frm_Hozor_List, text="ویرایش", bg="green", font=("Calibri", 12, "bold"), padx=15,
                                      command=self.Check_Std_Tch_Edit)
        self.btnE_Hozor_List.place_forget()

        self.btnD_Hozor_List = Button(self.frm_Hozor_List, text="حذف", bg="red", font=("Calibri", 12, "bold"), padx=5,
                                      command=self.Check_Std_Tch)
        self.btnD_Hozor_List.place_forget()

        self.Id_Tch = StringVar()
        self.txtId_Tch = ttk.Entry(self.frm_Hozor_List, textvariable=self.Id_Tch, justify="right")
        self.txtId_Tch.place_forget()

        self.Id_Std = StringVar()
        self.txtId_Std = ttk.Entry(self.frm_Hozor_List, textvariable=self.Id_Std, justify="right")
        self.txtId_Std.place_forget()

        # end body layer Hozor_List

        #body layer Add_Student

        self.btn_backadd = Button(self.frm_Add_Student, pady=7, padx=15, text="برگشتن", fg="red",
                                  command=self.showLayer_2)
        self.btn_backadd.place(x=10, y=10)

        self.img13 = PhotoImage(file="file/787.png")

        self.lblbtn13 = Label(self.frm_Add_Student, image=self.img13, width=40, height=40, bg="#f0f0f0")
        self.lblbtn13.place(x=750, y=10)
        self.lblbtn13.bind("<Button-1>", self.Close)

        self.getSearch3 = StringVar()
        self.Search3 = ttk.Entry(self.frm_Add_Student, textvariable=self.getSearch3, font=("Calibri", 12, "bold"))
        self.Search3.place(x=538, y=285)

        self.btnSearch3 = Button(self.frm_Add_Student, padx=5, text="جستوجو", font=("Calibri", 11, "bold"),
                                 command=self.oneclickSearch3)
        self.btnSearch3.place(x=460, y=281)

        self.refresh3 = Button(self.frm_Add_Student, padx=5, pady=2, text="Refresh", font=("Calibri", 11, "bold"),
                               command=self.Refresh3)
        self.refresh3.place(x=360, y=281)

        self.col_add_student = ("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10")
        self.tbl_add_student = ttk.Treeview(self.frm_Add_Student, columns=self.col_add_student, show="headings", height=13)

        self.tbl_add_student.column("# 10", anchor=N, width=0, minwidth=0)
        self.tbl_add_student.heading("# 10", text="")

        self.tbl_add_student.column("# 9", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 9", anchor=N, text="نام")

        self.tbl_add_student.column("# 8", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 8", anchor=N, text="نام خانوادگی")

        self.tbl_add_student.column("# 7", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 7", anchor=N, text="نام پدر")

        self.tbl_add_student.column("# 6", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 6", anchor=N, text="کد ملی")

        self.tbl_add_student.column("# 5", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 5", anchor=N, text="متولد")

        self.tbl_add_student.column("# 4", anchor=N, width=83,minwidth=83,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 4", anchor=N, text="کد دانش آموزی")

        self.tbl_add_student.column("# 3", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 3", anchor=N, text="کلاس")

        self.tbl_add_student.column("# 2", anchor=N, width=80,minwidth=80,stretch=tkinter.YES)
        self.tbl_add_student.heading("# 2", anchor=N, text="شماره پدر")

        self.tbl_add_student.column("# 1", anchor=N, width=80, minwidth=80, stretch=tkinter.YES)
        self.tbl_add_student.heading("# 1", anchor=N, text="شماره مادر")

        self.tbl_add_student.bind("<Button-1>", self.getsc2)

        self.tbl_add_student.place(x=40, y=330)

        self.lblnameS = Label(self.frm_Add_Student, text="نام هنرجو", font=("Calibri", 12, "bold")).place(x=650, y=25)

        self.lblfamilyS = Label(self.frm_Add_Student, text="نام خانوادگی", font=("Calibri", 12, "bold")).place(x=325, y=25)

        self.lblDadS = Label(self.frm_Add_Student, text="نام پدر", font=("Calibri", 12, "bold")).place(x=650, y=75)

        self.lblDarsT = Label(self.frm_Add_Student, text="کد ملی", font=("Calibri", 12, "bold")).place(x=325, y=75)

        self.lblDarsT = Label(self.frm_Add_Student, text="تاریخ تولد", font=("Calibri", 12, "bold")).place(x=650, y=125)

        self.lblDarsT = Label(self.frm_Add_Student, text="کد دانش آموزی", font=("Calibri", 12, "bold")).place(x=325, y=125)

        self.lblclassT = Label(self.frm_Add_Student, text="شماره تماس پدر", font=("Calibri", 12, "bold")).place(x=650, y=175)

        self.lblclassT = Label(self.frm_Add_Student, text="شماره تماس مادر", font=("Calibri", 12, "bold")).place(x=325, y=175)

        self.lblclassT = Label(self.frm_Add_Student, text="کلاس", font=("Calibri", 12, "bold")).place(x=650, y=225)

        self.Idb = StringVar()
        self.txtIdb = ttk.Entry(self.frm_Add_Student, textvariable=self.Idb, justify="right")
        self.txtIdb.place_forget()

        self.nameSget = StringVar()
        self.nameS = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.nameSget, font=("Calibri", 12, "bold"))


        self.nameS.place(x=450, y=25)

        self.familySget = StringVar()
        self.familyS = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.familySget,
                                 font=("Calibri", 12, "bold"))
        self.familyS.place(x=125, y=25)

        self.dad_Sget = StringVar()
        self.dad_S = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.dad_Sget, font=("Calibri", 12, "bold"))
        self.dad_S.place(x=450, y=75)

        self.Code_Sget = StringVar()
        self.Code_S = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.Code_Sget, font=("Calibri", 12, "bold"))
        self.Code_S.place(x=125, y=75)

        self.Day_Sget = StringVar()
        self.Day_S = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.Day_Sget, font=("Calibri", 12, "bold"))
        self.Day_S.place(x=585, y=125, width=50)

        self.Month_Sget = StringVar()
        self.Month_S = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.Month_Sget,
                                 font=("Calibri", 12, "bold"))
        self.Month_S.place(x=517, y=125, width=50)

        self.Date_Sget = StringVar()
        self.Date_S = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.Date_Sget, font=("Calibri", 12, "bold"))
        self.Date_S.place(x=450, y=125, width=50)

        self.N_Code_Stdget = StringVar()
        self.National_Code_Student = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.N_Code_Stdget, font=("Calibri", 12, "bold"))
        self.National_Code_Student.place(x=125, y=125)

        self.mobile_dad_sget = StringVar()
        self.mobile_dad_s = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.mobile_dad_sget, font=("Calibri", 12, "bold"))
        self.mobile_dad_s.place(x=450, y=175)

        self.mother_number = StringVar()
        self.M_Num = ttk.Entry(self.frm_Add_Student, justify="center", textvariable=self.mother_number,
                               font=("Calibri", 12, "bold"))
        self.M_Num.place(x=125, y=175)

        self.class_sget = StringVar()
        self.class_S = ttk.Combobox(self.frm_Add_Student, justify="center", textvariable=self.class_sget,
                                    font=("Calibri", 12, "bold"),state="readonly")
        self.class_S['values'] = ('10 شبکه','11 شبکه','12 شبکه','10/1 تربیت','10/2 تربیت','11/1 تربیت','11/2 تربیت',
                                  '12/1 تربیت','12/2 تربیت')
        self.class_S.current(0)
        self.class_S.place(x=450, y=225)

        self.btnSave2 = Button(self.frm_Add_Student, padx=7, text="ثبت اطلاعات", font=("Calibri", 12, "bold"),
                               command=self.Register3)
        self.btnSave2.place(x=230, y=282)

        self.btnD2 = Button(self.frm_Add_Student, text="حذف", bg="red", font=("Calibri", 12, "bold"), padx=5,
                            command=self.OnclickDelet2)
        self.btnD2.place_forget()

        self.btnE2 = Button(self.frm_Add_Student, text="ویرایش", bg="green", font=("Calibri", 12, "bold"), padx=15,
                            command=self.OnclickEdit2)
        self.btnE2.place_forget()

        # end body layer Add_Student

        #body layer List

        self.btn_back_22 = Button(self.frm_List, pady=7, padx=15, text="برگشتن", fg="red",
                                  command=self.showLayer_2_back)
        self.btn_back_22.place(x=10, y=10)

        self.img1311 = PhotoImage(file="file/787.png")

        self.lblbtn1311 = Label(self.frm_List, image=self.img1311, width=40, height=40, bg="#f0f0f0")
        self.lblbtn1311.place(x=750, y=10)
        self.lblbtn1311.bind("<Button-1>", self.Close)

        self.lbl_Add_Header2 = Label(self.frm_List,
                                     text="گزارش گیری اسامی دلخواه",
                                     font=("Calibri", 12, "bold"))
        self.lbl_Add_Header2.place(x=325, y=10)

        self.lbl_Add_Header2 = Label(self.frm_List,
                                     text="گزارش مورد نظر",
                                     font=("Calibri", 12, "bold"))
        self.lbl_Add_Header2.place(x=675, y=150)

        self.Info_Type = StringVar()
        self.Info_Types = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Info_Type,
                                       font=("Calibri", 12, "bold"), state="readonly")
        self.Info_Types['values'] = (
            '','حاضرین', 'غایبین', 'تاخیری', 'اخراج شده', 'فرار کرده','فردی')
        self.Info_Types.current(0)
        self.Info_Types.place(x=575, y=150, width=100)
        self.Info_Types.bind("<<ComboboxSelected>>", self.Select_Type)

        # end body layer List

        # body layer hosh

        self.btn_back_2 = Button(self.frm_hosh, pady=7, padx=15, text="برگشتن", fg="red",
                                 command=self.showLayer_2_back)
        self.btn_back_2.place(x=10, y=10)

        self.img131 = PhotoImage(file="file/787.png")

        self.lblbtn131 = Label(self.frm_hosh, image=self.img131, width=40, height=40, bg="#f0f0f0")
        self.lblbtn131.place(x=750, y=10)
        self.lblbtn131.bind("<Button-1>", self.Close)

        Date = request.lasts_day(7)

        self.lbl_Add_Header2 = Label(self.frm_hosh, text=f"اسامی هنرجوهایی که از تاریخ {Date[0]} تا {Date[7]} حضور نداشتند", font=("Calibri", 12, "bold"))
        self.lbl_Add_Header2.place(x=150, y=10)

        self.col_hosh = ("c1", "c2", "c3", "c4", "c5", "c6")
        self.tbl_hosh = ttk.Treeview(self.frm_hosh, columns=self.col_hosh, show="headings", height=22)

        self.tbl_hosh.column("# 6", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_hosh.heading("# 6", anchor=N, text="نام هنرجو")

        self.tbl_hosh.column("# 5", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_hosh.heading("# 5", anchor=N, text="نام خانوادگی هنرجو")

        self.tbl_hosh.column("# 4", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_hosh.heading("# 4", anchor=N, text="کد دانش آموزی")

        self.tbl_hosh.column("# 3", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_hosh.heading("# 3", anchor=N, text="کلاس")

        self.tbl_hosh.column("# 2", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_hosh.heading("# 2", anchor=N, text="شماره پدر")

        self.tbl_hosh.column("# 1", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_hosh.heading("# 1", anchor=N, text="شماره مادر")

        self.tbl_hosh.place(x=90, y=100)

        self.SMS = Button(self.frm_hosh, padx=5, text="ارسال اس ام اس", font=("Calibri", 11, "bold"),
                          command=self.SURE)
        self.SMS.place(x=350, y=50)

        # end body layer hosh

        #end

        self.HideLayer_All()
        self.showLayer_1()
        self.showLayer_1_2()
        """
        self.showLayer_3()
        self.frm_Add_Student.place(x=0, y=0, width=800, height=600)
        self.showLayer_timetable_Add_default()
        self.showLayer_Hozor_Add()

        self.showLayer_2()"""

    def SelectTar(self):
        self.frmTar1.place(x=0, y=0, width=800, height=600)

    def SelectCom(self):
        self.frmCom.place(x=0,y=0, width=800, height=600)


    def Register2(self):
        repository = Repository()
        MyList = []
        if self.nameT.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام معلم را پر کنید")
            self.nameT.focus_set()

        elif self.familyT.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام خانوادگی معلم را پر کنید")
            self.familyT.focus_set()

        elif self.DarsT_Addget.get() == "":
            messagebox.showerror("پر کردن", "لطفا درس تحصیلی را پر کنید")
            self.DarsT_Add.focus_set()

        elif self.madrak_get.get() == "":
            messagebox.showerror("پر کردن", "لطفا مدرک تحصیلی را پر کنید")
            self.madrak_Tch.focus_set()

        elif self.personel_codeget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد پرسنلی را پر کنید")
            self.personel_code.focus_set()

        elif not self.personel_codeget.get().isnumeric():
            messagebox.showerror("پر کردن", "خطا از داده کد پرسنلی")
            self.personel_code.focus_set()

        elif self.National_CodeTget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد ملی معلم را پر کنید")
            self.National_CodeT.focus_set()

        elif not self.National_CodeTget.get().isnumeric():
            messagebox.showerror("پر کردن", "خطا از داده کد ملی معلم")
            self.National_CodeT.focus_set()

        elif len(self.National_CodeTget.get()) != 10:
            messagebox.showerror("پر کردن", "کد ملی معلم را صحیح وارد کنید")
            self.National_CodeT.focus_set()

        else:
            where = f" Name= '{self.nameTget.get()}' and Family= '{self.familyTget.get()}' and National_Code= '{self.National_CodeTget.get()}'"
            Where = persian.convert_fa_numbers(where)
            result = repository.Search("Teacher_" + Variable, "[Name],[Family],[National_Code]", Where, "Family")
            for item in result:
                MyList.append(item)

            if len(MyList) >= 1:
                messagebox.showerror("تکراری", "این هنرآموز قبلا ثبت شده است")
            else:
                messagebox.showinfo("ثبت اطلاعات", "ثبت اطلاعات با موفقیت انجام شد")
                obj = (self.nameTget.get(), self.familyTget.get(), self.DarsT_Addget.get(), self.madrak_get.get(), self.personel_codeget.get(), self.National_CodeTget.get())
                objcar = blCar()
                Tablename = "Teacher_" + Variable
                Cols = " (Name,Family,Dars,madrak,personel_code,National_Code) "
                objcar.Insert(str(obj), Tablename, Cols)
                self.set2()
                self.cleantable5()
                self.loads()

    def SetAll(self):
        self.nameTget.set("")
        self.familyTget.set("")
        self.DarsT_Addget.set("")
        self.madrak_get.set("")
        self.personel_codeget.set("")
        self.National_CodeTget.set("")
        self.getSearch2.set("")
        self.Ida.set("")
        self.getSearch3.set("")
        self.Idb.set("")
        self.nameSget.set("")
        self.familySget.set("")
        self.dad_Sget.set("")
        self.Code_Sget.set("")
        self.Day_Sget.set("")
        self.Month_Sget.set("")
        self.Date_Sget.set("")
        self.N_Code_Stdget.set("")
        self.mobile_dad_sget.set("")
        self.class_sget.set("")
        self.txtUser.set("")
        self.txtPass.set("")
        self.txtU.set("")
        self.txtpass.set("")
        self.txtpass2.set("")
        self.txtname.set("")
        self.getSearch2.set("")
        self.getSearch3.set("")
        self.nameSget.set("")
        self.familySget.set("")
        self.Code_Sget.set("")
        self.Day_Sget.set("")
        self.Month_Sget.set("")
        self.Date_Sget.set("")
        self.dad_Sget.set("")


    def set2(self):
        self.nameTget.set("")
        self.familyTget.set("")
        self.madrak_get.set("")
        self.DarsT_Addget.set("")
        self.personel_codeget.set("")
        self.National_CodeTget.set("")
        self.getSearch2.set("")


    def Register3(self):
        repository = Repository()
        len_mother = len(self.mother_number.get())
        len_dad = len(self.mobile_dad_sget.get())
        MyList = []
        if self.nameSget.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام را پر کنید")
            self.nameS.focus_set()

        elif self.familySget.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام خانوادگی را پر کنید")
            self.familyS.focus_set()

        elif self.dad_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام پدر را پر کنید")
            self.dad_S.focus_set()

        elif self.Code_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد ملی را پر کنید")
            self.Code_S.focus_set()

        elif not self.Code_Sget.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده کدملی")
            self.Code_S.focus_set()

        elif len(self.Code_Sget.get()) != 10:
            messagebox.showerror("پر کردن", "لطفا کد ملی را صحیح وارد کنید")
            self.Code_S.focus_set()

        elif self.Day_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا روز تولد را پر کنید")
            self.Day_S.focus_set()

        elif not self.Day_S.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده روز تولد")
            self.Day_S.focus_set()

        elif self.Month_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا ماه تولد را پر کنید")
            self.Month_S.focus_set()

        elif not self.Month_S.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده ماه تولد")
            self.Month_S.focus_set()

        elif self.Date_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا سال تولد را پر کنید")
            self.Date_S.focus_set()

        elif not self.Date_S.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده سال تولد")
            self.Date_S.focus_set()

        elif self.N_Code_Stdget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد دانش آموزی را پر کنید")
            self.National_Code_Student.focus_set()

        elif not self.N_Code_Stdget.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده کد دانش آموزی")
            self.National_Code_Student.focus_set()

        elif self.N_Code_Stdget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد دانش آموزی را پر کنید")
            self.National_Code_Student.focus_set()

        elif self.mobile_dad_sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا شماره تماس پدر را پر کنید")
            self.mobile_dad_s.focus_set()

        elif not self.mobile_dad_sget.get().isnumeric() and self.mobile_dad_sget.get() != "-":
            messagebox.showerror("داده", "خطا از داده شماره تماس پدر")
            self.mobile_dad_s.focus_set()

        elif len_dad != 11 and self.mobile_dad_sget.get() != "-":
            messagebox.showerror("پر کردن", "لطفا شماره تماس پدر را صحیح وارد کنید")
            self.mobile_dad_s.focus_set()

        elif self.mother_number.get() == "":
            messagebox.showerror("پر کردن", "لطفا شماره تماس مادر را پر کنید")
            self.M_Num.focus_set()

        elif not self.mother_number.get().isnumeric() and self.mother_number.get() != "-":
            messagebox.showerror("داده", "خطا از داده شماره تماس مادر")
            self.M_Num.focus_set()

        elif len_mother != 11 and self.mother_number.get() != "-":
            messagebox.showerror("پر کردن", "لطفا شماره تماس مادر را صحیح وارد کنید")
            self.M_Num.focus_set()

        elif self.class_sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کلاس را پر کنید")
            self.class_S.focus_set()
        else:
            where = f" Name= '{self.nameSget.get()}' and Family= '{self.familySget.get()}' and National_Code= '{self.Code_Sget.get()}'"
            Where = persian.convert_fa_numbers(where)
            result = repository.Search("Student_" + Variable, "[Name],[Family],[National_Code]", Where, "Family")
            for item in result:
                MyList.append(item)

            if len(MyList) >= 1:
                messagebox.showerror("تکراری", "این هنرجو قبلا ثبت شده است")

            else:
                messagebox.showinfo("اطلاعات", "ثبت اطلاعات با موفقیت انجام شد")
                Date = self.Date_Sget.get() + "/" + self.Month_Sget.get() + "/" + self.Day_Sget.get()

                obj = (self.nameSget.get(), self.familySget.get(), self.dad_Sget.get(),
                       self.Code_Sget.get(),Date, self.N_Code_Stdget.get(), self.class_sget.get(),
                       self.mobile_dad_sget.get(),self.mother_number.get())

                objcar = blCar()
                Tablename = "Student_" + Variable
                Cols = " (Name,Family,dadName,National_Code,Date,Code_S,Reshte,mobile_dad,mobile_mother) "
                objcar.Insert(str(obj), Tablename, Cols)
                self.set3()
                self.cleantable6()
                self.load_Std()

    def CleanTables(self):
        self.cleantable5()
        self.cleantable6()
        self.cleantable_Std_List()
        self.cleantable_Tch_List()


    def loads(self):
        self.load6()
        self.load_Std()


    def set3(self):
        self.nameSget.set("")
        self.familySget.set("")
        self.dad_Sget.set("")
        self.N_Code_Stdget.set("")
        self.Day_Sget.set("")
        self.Month_Sget.set("")
        self.Date_Sget.set("")
        self.Code_Sget.set("")
        self.class_sget.set("")
        self.mobile_dad_sget.set("")
        self.mother_number.set("")
        self.getSearch3.set("")


    def oneclickSearch_Std(self):
        self.query = self.Srch_Std_List_val.get()
        self.search_Std(self.query)

    def search_Std(self, value):
        repository = Repository()
        where = f" (Date = '{request.Full_Date()}') AND" + " (Name like '" + value + "' or Family like '" + value\
                + "' or res like '" + value + "' or Long like '" + value\
                + "' or Exit_Class like '" + value + "' or Exit_School like '" +\
                value + "')"
        Where = persian.convert_fa_numbers(where)
        result = repository.Search("Presentation_" + Variable, "*", Where, "Family")
        self.cleantable_Hozor_List_Std()
        for item in result:
            if item[3] == "Std":
                if item[9] == "yes":
                    Long = "تاخیر داشته"
                else:
                    Long = "تاخیر نداشته"

                if item[10] == "yes":
                    Exit_Class = "اخراج شده"
                else:
                    Exit_Class = "اخراج نشده"

                if item[11] == "yes":
                    Exit_School = "فرار کرده"
                else:
                    Exit_School = "فرار نکرده"

                self.tbl_Hozor_Student.insert('', "end", values=[Exit_School, Exit_Class, Long, item[6],item[2], item[1], item[0]])


    def oneclickSearch2(self):
        self.query = self.Search2.get()
        self.search2(self.query)

    def search2(self, value):
        repository = Repository()
        where = " Name like '" + value + "' or Family like '" + value + "' or Dars like '" + value + "' or madrak like '" + value + "' or personel_code like '" + value + "' or National_Code like '" + value + "'"
        result = repository.Search("Teacher_" + Variable, "*", where, "Family")
        self.cleantable5()
        for item in result:
            self.tbl_Tch_Add.insert('', "end", values=[item[6],item[5], item[3],item[4], item[2], item[1], item[0]])

    def oneclickSearch3(self):
        self.query = self.Search3.get()
        self.search3(self.query)

    def search3(self, value):
        repository = Repository()
        res = True
        self.getSearch3.set("")
        self.getSearch3.set(value)
        Class = [('۱۰/۱تربیت بدنی', '۱۰/۱ تربیت بدنی', '۱۰/۱ تربیت', '۱۰/۱تربیت', '10/1تربیت بدنی', '10/1 تربیت بدنی', '10/1تربیت', '10/1 تربیت'),
                 ('۱۰/۲تربیت بدنی', '۱۰/۲ تربیت بدنی', '۱۰/۲ تربیت', '۱۰/۲تربیت', '10/2تربیت بدنی', '10/2 تربیت بدنی', '10/2تربیت', '10/2 تربیت'),
                 ('۱۱/۱تربیت بدنی', '۱۱/۱ تربیت بدنی', '۱۱/۱ تربیت', '۱۱/۱تربیت', '11/1تربیت بدنی', '11/1 تربیت بدنی', '11/1تربیت', '11/1 تربیت'),
                 ('۱۱/۲تربیت بدنی', '۱۱/۲ تربیت بدنی', '۱۱/۲ تربیت', '۱۱/۲تربیت', '11/2تربیت بدنی', '11/2 تربیت بدنی', '11/2تربیت', '11/2تربیت'),
                 ('۱۲/۱تربیت بدنی', '۱۲/۱ تربیت بدنی', '۱۲/۱ تربیت', '۱۲/۱تربیت', '12/1تربیت بدنی', '12/1 تربیت بدنی', '12/1تربیت', '12/1 تربیت'),
                 ('۱۲/۲تربیت بدنی', '۱۲/۲ تربیت بدنی', '۱۲/۲ تربیت', '۱۲/۲تربیت', '12/2تربیت بدنی', '12/2 تربیت بدنی', '12/2تربیت', '12/2 تربیت'),
                 ('۱۰شبکه', '۱۰ شبکه', '10شبکه', '10 شبکه'),
                 ('۱۱شبکه', '۱۱ شبکه', '11شبکه', '11 شبکه'),
                 ('۱۲شبکه', '۱۲ شبکه', '12شبکه', '12 شبکه')]

        self.cleantable6()
        for items in Class:
            if self.getSearch3.get() in items:
                ClassList = items
                for itm in ClassList:
                    where = " Reshte like '" + itm + "'"
                    result = repository.Search("Student_" + Variable, "*", where, "Family")
                    if result != []:
                        for item in result:
                            self.tbl_add_student.insert('', "end",values=[item[9], item[8], item[7], item[6], item[5], item[4], item[3],item[2], item[1], item[0]])
                res = False
                break
        if res:

            where = " Name like '" + value + "' or Family like '" + value + "' or dadName like '"\
                    + value + "' or National_Code like '" + value + "' or Date like '"\
                    + value + "' or Code_S like '" + value + "' or Reshte like '"\
                    + value + "' or mobile_dad like '" + value + "' or mobile_mother like '" + value + "'"

            result = repository.Search("Student_" + Variable, "*", where, "Family")
            for item in result:
                self.tbl_add_student.insert('', "end", values=[item[9],item[8],item[7], item[6], item[5], item[4], item[3], item[2], item[1], item[0]])


    def Std_Refresh(self):
        self.cleantable_Hozor_List_Std()
        self.load_Hozor_List_Std()
        self.Srch_Std_List_val.set("")
        self.btnE_Hozor_List.place_forget()
        self.btnD_Hozor_List.place_forget()


    def Refresh2(self):
        self.cleantable5()
        self.load6()
        self.getSearch2.set("")

    def Refresh3(self):
        self.cleantable6()
        self.load_Std()
        self.getSearch3.set("")
        self.btnD2.place_forget()
        self.btnE2.place_forget()


    def load6(self):
            objcar = blCar()
            result = objcar.Read_Sort("Teacher_" + Variable, "*", "Family")
            for item in result:
                self.tbl_Tch_Add.insert('', "end", values=[item[6], item[5], item[3], item[4], item[2], item[1], item[0]])


    def load_Std(self):
            objcar = blCar()

            result = objcar.Read_Sort("Student_" + Variable, "*", "Family")
            for item in result:
                self.tbl_add_student.insert('', "end", values=[item[9],item[8],item[7],item[6],item[5], item[4], item[3], item[2], item[1], item[0]])


    def load_Tch_list(self):
            objcar = blCar()

            result = objcar.Read_Sort("Teacher_" + Variable, "[Teachers_id], [Name], [Family]", "Family")
            for item in result:
                self.tbl_day_Tch.insert('', "end", values=[item[2],item[1], item[0]])


    def load_Std_list(self):
            objcar = blCar()
            repository = Repository()
            text = self.textClass
            Reshte = ""
            if text == "۱۰/۱تربیت بدنی":
                Reshte = "10/1 تربیت"

            elif text == "۱۰/۲تربیت بدنی":
                Reshte = "10/2 تربیت"

            elif text == "۱۱/۱تربیت بدنی":
                Reshte = "11/1 تربیت"

            elif text == "۱۱/۲تربیت بدنی":
                Reshte = "11/2 تربیت"

            elif text == "۱۲/۱تربیت بدنی":
                Reshte = "12/1 تربیت"

            elif text == "۱۲/۲تربیت بدنی":
                Reshte = "12/2 تربیت"

            elif text == "۱۰شبکه":
                Reshte = "10 شبکه"

            elif text == "۱۱شبکه":
                Reshte = "11 شبکه"

            elif text == "۱۲شبکه":
                Reshte = "12 شبکه"

            where = " Reshte like '" + Reshte + "'"
            result = repository.Search("Student_" + Variable, "[std_id], [Name], [Family]", where, "Family")
            if result != ():
                for item in result:
                    self.tbl_day_Std.insert('', "end", values=[item[2], item[1], item[0]])


    def cleantable5(self):
        for item in self.tbl_Tch_Add.get_children():
            self.sel = (str(item))
            self.tbl_Tch_Add.delete(self.sel)

    def cleantable6(self):
        for item in self.tbl_add_student.get_children():
            self.sel = (str(item))
            self.tbl_add_student.delete(self.sel)


    def cleantable_Std_List(self):
        for item in self.tbl_day_Std.get_children():
            self.sel = (str(item))
            self.tbl_day_Std.delete(self.sel)


    def cleantable_Tch_List(self):
        for item in self.tbl_day_Tch.get_children():
            self.sel = (str(item))
            self.tbl_day_Tch.delete(self.sel)

    def cleantable_hosh(self):
        for item in self.tbl_hosh.get_children():
            self.sel = (str(item))
            self.tbl_hosh.delete(self.sel)

    def back(self):
        self.btnD.place_forget()
        self.btnE.place_forget()
        self.set2()
        self.cleantable5()
        self.load6()
        self.HideLayer_All()
        self.showLayer_2()

    def backlayer1_3(self, e):
        self.showLayer_1_2()

    def onclickHozur(self, e):
        self.HideLayer_All()
        self.showLayer_6()

    def onclickTeacher(self, e):
        self.HideLayer_All()
        self.showLayer_3()


    def Close(self, e):
        self.master.destroy()

    def HideLayer_All(self):
        self.frm1.place_forget()
        self.frm2.place_forget()
        self.frm3.place_forget()
        self.frm6.place_forget()
        self.frmCom.place_forget()
        self.frmTar1.place_forget()
        self.frm_Zang.place_forget()
        self.frm_Hozor_Add.place_forget()
        self.frm_Hozor_List.place_forget()
        self.frmTarClass10.place_forget()
        self.frmTarClass11.place_forget()
        self.frmTarClass12.place_forget()
        self.frm_Add_Student.place_forget()
        self.frm_List.place_forget()
        self.frm_hosh.place_forget()

    def showLayer_1(self):
        self.txtU.set("")
        self.txtUser.set("")
        self.txtPass.set("")
        self.txtpass.set("")
        self.txtpass2.set("")
        self.HideLayer_All()
        self.frm1.place(x=0, y=0, width=800, height=600)

    def showLayer_1_2(self):
        self.txtU.set("")
        self.txtUser.set("")
        self.txtPass.set("")
        self.txtpass.set("")
        self.txtpass2.set("")
        self.frm1_3.place_forget()
        self.frm1_2.place(x=400, y=0, width=400, height=600)

    def showLayer_1_3(self):
        self.txtU.set("")
        self.txtUser.set("")
        self.txtPass.set("")
        self.txtpass.set("")
        self.txtpass2.set("")
        self.frm1_3.place(x=400, y=0, width=400, height=600)

    def showLayer_2(self):
        self.txtU.set("")
        self.txtUser.set("")
        self.txtPass.set("")
        self.txtpass.set("")
        self.txtpass2.set("")
        self.set3()
        self.cleantable6()
        self.load_Std()
        self.btnD2.place_forget()
        self.btnE2.place_forget()
        self.cleantable5()
        self.load6()
        self.HideLayer_All()
        self.frm2.place(x=0, y=0, width=800, height=600)

    def showLayer_2_back(self):
        self.HideLayer_All()
        self.frm2.place(x=0, y=0, width=800, height=600)

    def showLayer_3(self):
        self.HideLayer_All()
        self.frm3.place(x=0, y=0, width=800, height=600)


    def showLayer_6(self):
        self.HideLayer_All()
        self.frm6.place(x=0, y=0, width=800, height=600)


    def showLayer_Tar1(self):
        self.HideLayer_All()
        self.frmTar1.place(x=0, y=0, width=800, height=600)

    def showLayer_TarClass10(self):
        self.HideLayer_All()
        self.frmTarClass10.place(x=0, y=0, width=800, height=600)

    def showLayer_TarClass11(self):
        self.HideLayer_All()
        self.frmTarClass11.place(x=0, y=0, width=800, height=600)

    def showLayer_TarClass12(self):
        self.HideLayer_All()
        self.frmTarClass12.place(x=0, y=0, width=800, height=600)



    def onclickList(self, e):
        self.HideLayer_All()
        self.showLayer_List()


    def onclickhosh(self, e):
        self.HideLayer_All()
        self.showLayer_hosh()

    def showLayer_List(self):
        self.HideLayer_All()
        self.frm_List.place(x=0, y=0, width=800, height=600)


    def showLayer_hosh(self):
        self.HideLayer_All()
        self.frm_hosh.place(x=0, y=0, width=800, height=600)
        self.cleantable_hosh()
        self.load_hosh()


    def showLayer_Add_Hozor(self,text):
        self.textClass = text
        self.HideLayer_All()
        if hasattr(self, 'Zang1'):
            self.Zang1.destroy()
        if hasattr(self, 'Zang2'):
            self.Zang2.destroy()
        if hasattr(self, 'Zang3'):
            self.Zang3.destroy()
        if hasattr(self, 'Zang4'):
            self.Zang4.destroy()

        self.frm_Zang.place(x=0, y=0, width=800, height=600)
        day = request.days()
        if day == "پنجشنبه":
            self.Zang1 = Button(self.frm_Zang, padx=5, text="زنگ اول", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ اول"))
            self.Zang1.place(x=475, y=246)

            self.Zang2 = Button(self.frm_Zang, padx=5, text="زنگ دوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ دوم"))
            self.Zang2.place(x=375, y=246)

            self.Zang3 = Button(self.frm_Zang, padx=5, text="زنگ سوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ سوم"))
            self.Zang3.place(x=275, y=246)

        else:
            self.Zang1 = Button(self.frm_Zang, padx=5, text="زنگ اول", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ اول"))
            self.Zang1.place(x=500, y=246)

            self.Zang2 = Button(self.frm_Zang, padx=5, text="زنگ دوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ دوم"))

            self.Zang2.place(x=400, y=246)

            self.Zang3 = Button(self.frm_Zang, padx=5, text="زنگ سوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ سوم"))
            self.Zang3.place(x=300, y=246)

            self.Zang4 = Button(self.frm_Zang, padx=5, text="زنگ چهارم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ چهارم"))
            self.Zang4.place(x=200, y=246)

    def back_zang(self):
        self.HideLayer_All()
        if hasattr(self, 'Zang1'):
            self.Zang1.destroy()
        if hasattr(self, 'Zang2'):
            self.Zang2.destroy()
        if hasattr(self, 'Zang3'):
            self.Zang3.destroy()
        if hasattr(self, 'Zang4'):
            self.Zang4.destroy()

        self.frm_Zang.place(x=0, y=0, width=800, height=600)
        day = request.days()
        if day == "پنجشنبه":
            self.Zang1 = Button(self.frm_Zang, padx=5, text="زنگ اول", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ اول"))
            self.Zang1.place(x=475, y=246)

            self.Zang2 = Button(self.frm_Zang, padx=5, text="زنگ دوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ دوم"))
            self.Zang2.place(x=375, y=246)

            self.Zang3 = Button(self.frm_Zang, padx=5, text="زنگ سوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ سوم"))
            self.Zang3.place(x=275, y=246)

        else:
            self.Zang1 = Button(self.frm_Zang, padx=5, text="زنگ اول", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ اول"))
            self.Zang1.place(x=500, y=246)

            self.Zang2 = Button(self.frm_Zang, padx=5, text="زنگ دوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ دوم"))

            self.Zang2.place(x=400, y=246)

            self.Zang3 = Button(self.frm_Zang, padx=5, text="زنگ سوم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ سوم"))
            self.Zang3.place(x=300, y=246)

            self.Zang4 = Button(self.frm_Zang, padx=5, text="زنگ چهارم", font=("Calibri", 11, "bold"),
                                command=lambda: self.get_Zang("زنگ چهارم"))
            self.Zang4.place(x=200, y=246)

    def showLayer_Hozor_Add(self):
        self.HideLayer_All()
        self.frm_Hozor_Add.place(x=0, y=0, width=800, height=600)
        self.Set_Val_Hozor_Add()
        self.load_Tch_list()
        self.load_Std_list()
        if hasattr(self, 'lbl_Add_Header2'):
            self.lbl_Add_Header2.destroy()

        if hasattr(self, 'lbl_Add_Header124'):
            self.lbl_Add_Header124.destroy()

        if hasattr(self, 'lbl_Add_Header22'):
            self.lbl_Add_Header22.destroy()

        if hasattr(self, 'lbl_Add_Header223'):
            self.lbl_Add_Header223.destroy()

        text = self.textClass
        if text == "۱۰شبکه" or text == "۱۱شبکه" or text == "۱۲شبکه":

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lbl_Add_Header2.place(x=530, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text=" و ", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header2.place(x=520, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lbl_Add_Header2.place(x=490, y=10)

            self.lbl_Add_Header124 = Label(self.frm_Hozor_Add, text=text, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header124.place(x=435, y=10)

            self.lbl_Add_Header22 = Label(self.frm_Hozor_Add, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header22.place(x=300, y=10)

            self.lbl_Add_Header223 = Label(self.frm_Hozor_Add, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header223.place(x=235, y=10)

        elif text == "۱۰/۱تربیت بدنی" or text == "۱۰/۲تربیت بدنی":

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lbl_Add_Header2.place(x=560, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text=" و ", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header2.place(x=550, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lbl_Add_Header2.place(x=520, y=10)

            self.lbl_Add_Header124 = Label(self.frm_Hozor_Add, text=text, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header124.place(x=420, y=10)

            self.lbl_Add_Header22 = Label(self.frm_Hozor_Add, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header22.place(x=280, y=10)

            self.lbl_Add_Header223 = Label(self.frm_Hozor_Add, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header223.place(x=215, y=10)

        elif text == "۱۱/۱تربیت بدنی" or text == "۱۱/۲تربیت بدنی":
            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lbl_Add_Header2.place(x=560, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text=" و ", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header2.place(x=550, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lbl_Add_Header2.place(x=520, y=10)

            self.lbl_Add_Header124 = Label(self.frm_Hozor_Add, text=text, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header124.place(x=420, y=10)

            self.lbl_Add_Header22 = Label(self.frm_Hozor_Add, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header22.place(x=280, y=10)

            self.lbl_Add_Header223 = Label(self.frm_Hozor_Add, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header223.place(x=215, y=10)

        elif text == "۱۲/۱تربیت بدنی" or text == "۱۲/۲تربیت بدنی":
            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lbl_Add_Header2.place(x=560, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text=" و ", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header2.place(x=550, y=10)

            self.lbl_Add_Header2 = Label(self.frm_Hozor_Add, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lbl_Add_Header2.place(x=520, y=10)

            self.lbl_Add_Header124 = Label(self.frm_Hozor_Add, text=text, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header124.place(x=420, y=10)

            self.lbl_Add_Header22 = Label(self.frm_Hozor_Add, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lbl_Add_Header22.place(x=280, y=10)

            self.lbl_Add_Header223 = Label(self.frm_Hozor_Add, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lbl_Add_Header223.place(x=215, y=10)


    def showLayer_Add_Std(self,e):
        self.HideLayer_All()
        self.frm_Add_Student.place(x=0, y=0, width=800, height=600)


    def showLayer_Hozor_List(self):
        self.HideLayer_All()
        self.frm_Hozor_List.place(x=0, y=0, width=800, height=600)

        if hasattr(self, 'lba1'):
            self.lba1.destroy()

        if hasattr(self, 'lba2'):
            self.lba2.destroy()

        if hasattr(self, 'lba3'):
            self.lba3.destroy()

        if hasattr(self, 'lba4'):
            self.lba4.destroy()

        text = self.textClass
        if text == "۱۰شبکه" or text == "۱۱شبکه" or text == "۱۲شبکه":

            self.lba1 = Label(self.frm_Hozor_List, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lba1.place(x=530, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text=" و ", font=("Calibri", 12, "bold"))
            self.lba1.place(x=520, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lba1.place(x=490, y=10)

            self.lba2 = Label(self.frm_Hozor_List, text=text, font=("Calibri", 12, "bold"))
            self.lba2.place(x=435, y=10)

            self.lba3 = Label(self.frm_Hozor_List, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lba3.place(x=300, y=10)

            self.lba4 = Label(self.frm_Hozor_List, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lba4.place(x=235, y=10)

        elif text == "۱۰/۱تربیت بدنی" or text == "۱۰/۲تربیت بدنی":

            self.lba1 = Label(self.frm_Hozor_List, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lba1.place(x=560, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text=" و ", font=("Calibri", 12, "bold"))
            self.lba1.place(x=550, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lba1.place(x=520, y=10)

            self.lba2 = Label(self.frm_Hozor_List, text=text, font=("Calibri", 12, "bold"))
            self.lba2.place(x=420, y=10)

            self.lba3 = Label(self.frm_Hozor_List, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lba3.place(x=280, y=10)

            self.lba4 = Label(self.frm_Hozor_List, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lba4.place(x=215, y=10)

        elif text == "۱۱/۱تربیت بدنی" or text == "۱۱/۲تربیت بدنی":
            self.lba1 = Label(self.frm_Hozor_List, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lba1.place(x=560, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text=" و ", font=("Calibri", 12, "bold"))
            self.lba1.place(x=550, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lba1.place(x=520, y=10)

            self.lba2 = Label(self.frm_Hozor_List, text=text, font=("Calibri", 12, "bold"))
            self.lba2.place(x=420, y=10)

            self.lba3 = Label(self.frm_Hozor_List, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lba3.place(x=280, y=10)

            self.lba4 = Label(self.frm_Hozor_List, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lba4.place(x=215, y=10)

        elif text == "۱۲/۱تربیت بدنی" or text == "۱۲/۲تربیت بدنی":
            self.lba1 = Label(self.frm_Hozor_List, text="حضور", font=("Calibri", 12, "bold"), fg="green")
            self.lba1.place(x=560, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text=" و ", font=("Calibri", 12, "bold"))
            self.lba1.place(x=550, y=10)

            self.lba1 = Label(self.frm_Hozor_List, text="غیاب", font=("Calibri", 12, "bold"), fg="red")
            self.lba1.place(x=520, y=10)

            self.lba2 = Label(self.frm_Hozor_List, text=text, font=("Calibri", 12, "bold"))
            self.lba2.place(x=420, y=10)

            self.lba3 = Label(self.frm_Hozor_List, text=request.Full_Date() + " |", font=("Calibri", 12, "bold"))
            self.lba3.place(x=280, y=10)

            self.lba4 = Label(self.frm_Hozor_List, text=self.day_Zang, font=("Calibri", 12, "bold"))
            self.lba4.place(x=215, y=10)

        self.Set_Val_Hozor_List()
        self.load_Hozor_List_Std()
        self.load_Hozor_List_Tch()


    def showLayer_Select_Class(self):
        self.HideLayer_All()
        text = self.textClass
        if text == "۱۰شبکه" or text == "۱۱شبکه" or text == "۱۲شبکه":
            self.frmCom.place(x=0,y=0, width=800, height=600)

        elif text == "۱۰/۱تربیت بدنی" or text == "۱۰/۲تربیت بدنی":
            self.frmTarClass10.place(x=0, y=0, width=800, height=600)

        elif text == "۱۱/۱تربیت بدنی" or text == "۱۱/۲تربیت بدنی":
            self.frmTarClass11.place(x=0, y=0, width=800, height=600)

        elif text == "۱۲/۱تربیت بدنی" or text == "۱۲/۲تربیت بدنی":
            self.frmTarClass12.place(x=0, y=0, width=800, height=600)


    def get_Zang(self,zang):
        self.day_Zang = zang
        self.GoAdd_Hozor()


    def GoAdd_Hozor(self):

        self.showLayer_Hozor_Add()

    def Sabt(self, e):
        if self.ent1.get() == "":
            messagebox.showerror("نام کاربری", "نام کاربری خود را وارد کنید")
            self.ent1.focus_set()

        elif self.ent2.get() == "":
            messagebox.showerror("رمز عبور", "رمز عبور خود را وارد وارد کنید")
            self.ent2.focus_set()

        elif self.ent3.get() == "":
            messagebox.showerror("تکرار رمز عبور", "تکرار رمز عبور را وارد کنید")
            self.ent3.focus_set()

        elif self.ent2.get() != self.ent3.get():
            messagebox.showerror(" تکرار رمز عبور", "تکرار رمز عبور با رمز عبور مطابقت ندارد")
            self.ent2.focus_set()

        else:
            messagebox.showinfo("ثبت اطلاعات", "ثبت اطلاعات با موفقیت انجام شد")
            obj = self.txtU.get(), self.txtpass.get()
            objcar = blCar()
            result = objcar.Add(obj[0],obj[1])
            repos = Repository
            objcar = blCar()
            result = objcar.Create(self.ent1.get())
            self.txtU.set(""), self.txtpass.set(""), self.txtpass2.set("")

    def Welcome(self, User, Pass):
        if User == "":
            self.User.focus_set()
            messagebox.showerror("خطا", "نام کاربری را وارد کنید")

        elif Pass == "":
            self.Pass.focus_set()
            messagebox.showerror("خطا", "رمز عبور را وارد کنید")

        else:
            where = " User_name = '" + User + "' and Pass_name = '" + Pass + "'"
            repository = Repository()
            result = repository.default_Search("User_Pass", "*", where)
            if result == ():
                print("error")
            else:
                print("ok")
                objcar = blCar()
                results = objcar.Read("User_Pass", "*")
                Number_results = False
                for item in results:
                    if User == item[1] and Pass == item[2]:
                        Number_results = True
                        break

                if Number_results:
                    messagebox.showinfo("ورود", "خوش آمدید")
                    Val = self.txtUser.get()
                    global Variable
                    Variable = Val
                    self.HideLayer_All()
                    self.showLayer_2()
                    self.CleanTables()
                    self.loads()
                else:
                    messagebox.showerror("خطا", "نام کاربری وجود ندارد")
    def Welcome2(self, e):
        self.Welcome(self.txtUser.get(), self.txtPass.get())

    def shownewfrm(self, e):
        self.frm1_2.place_forget()
        self.showLayer_1_3()

    def OnclickDelet(self):
        result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

        if result == "yes":
            self.Delete()

    def Delete(self):
        repository = Repository()
        select_row = self.tbl_Tch_Add.selection()

        if select_row != ():
            SelectItem = self.tbl_Tch_Add.item(select_row)["values"]
            where = " Teachers_id='" + str(SelectItem[6]) + "' "
            result = repository.delete("Teacher_" + Variable, where)
            if result:
                messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")
                self.set2()
                self.cleantable5()
                self.load6()
                self.btnE.place_forget()
                self.btnD.place_forget()
        else:
            messagebox.showerror("خطا", "حذف انجام نشد")
            self.btnD.place_forget()

    def OnclickEdit(self):
        if self.nameT.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام معلم را پر کنید")
            self.nameT.focus_set()

        elif self.familyT.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام خانوادگی معلم را پر کنید")
            self.familyT.focus_set()

        elif self.DarsT_Addget.get() == "":
            messagebox.showerror("پر کردن", "لطفا درس تحصیلی را پر کنید")
            self.DarsT_Add.focus_set()

        elif self.madrak_get.get() == "":
            messagebox.showerror("پر کردن", "لطفا مدرک تحصیلی را پر کنید")
            self.madrak_Tch.focus_set()

        elif self.personel_codeget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد پرسنلی را پر کنید")
            self.personel_code.focus_set()

        elif not self.personel_codeget.get().isnumeric():
            messagebox.showerror("پر کردن", "خطا از داده کد پرسنلی")
            self.personel_code.focus_set()

        elif self.National_CodeTget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد ملی معلم را پر کنید")
            self.National_CodeT.focus_set()

        elif not self.National_CodeTget.get().isnumeric():
            messagebox.showerror("پر کردن", "خطا از داده کد ملی معلم")
            self.National_CodeT.focus_set()

        elif len(self.National_CodeTget.get()) != 10:
            messagebox.showerror("پر کردن", "کد ملی معلم را صحیح وارد کنید")
            self.National_CodeT.focus_set()

        else:
            repository = Repository()
            select_row = self.tbl_Tch_Add.selection()

            SelectItem = self.tbl_Tch_Add.item(select_row)["values"]

            where = " Teachers_id= '" + self.txtIda.get() + "' "

            col = "  Name='" + self.nameTget.get() + "',Family='" +\
                  self.familyTget.get() + "',Dars='" + self.DarsT_Addget.get() +\
                  "',madrak='" + self.madrak_get.get() +\
                  "',personel_code='" + self.personel_codeget.get() +\
                  "',National_Code='" + self.National_CodeTget.get() + "' "

            result = repository.update("Teacher_" + Variable, col, where)
            if result:
                self.cleantable5()
                self.load6()
                self.set2()
                self.btnE.place_forget()
                self.btnD.place_forget()
                self.clear(self.txtIda)

                messagebox.showinfo("انجام شد", "ویرایش انجام شد")
            else:
                messagebox.showerror("   خطا", "  انجام نشد")

    def clear(self, listval):
        try:
            for item in listval:
                item.set("")
        except:
            pass

    def getsc(self, e):
        select = self.tbl_Tch_Add.selection()
        if select != ():
            self.btnD.place(x=50, y=246)
            self.btnE.place(x=130, y=246)
            repository = Repository()
            where = " Teachers_id='" + str(self.tbl_Tch_Add.item(select)["values"][6]) + "' "
            data = repository.Search("Teacher_" + Variable, "[personel_code],[National_Code]", where, "Family")
            Mylist = []
            for item in data:
                Mylist.append(item)

            self.personel_codeget.set(Mylist[0][0])
            self.National_CodeTget.set(Mylist[0][1])
            self.DarsT_Addget.set(self.tbl_Tch_Add.item(select)["values"][2])

            self.madrak_get.set(self.tbl_Tch_Add.item(select)["values"][3])
            self.familyTget.set(self.tbl_Tch_Add.item(select)["values"][4])
            self.nameTget.set(self.tbl_Tch_Add.item(select)["values"][5])
            self.Ida.set(self.tbl_Tch_Add.item(select)["values"][6])

    def OnclickDelet2(self):
        result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

        if result == "yes":
            self.Delete2()

    def Delete2(self):
        repository = Repository()
        select_row = self.tbl_add_student.selection()

        if select_row != ():
            SelectItem = self.tbl_add_student.item(select_row)["values"]
            where = " std_id='" + str(SelectItem[10]) + "' "
            result = repository.delete("Student_" + Variable, where)
            if result:
                messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")
                self.set3()
                self.cleantable6()
                self.load_Std()
                self.btnE2.place_forget()
                self.btnD2.place_forget()
        else:
            messagebox.showerror("خطا", "حذف انجام نشد")
            self.btnD2.place_forget()

    def OnclickEdit2(self):
        len_mother = len(self.mother_number.get())
        len_dad = len(self.mobile_dad_sget.get())
        if self.nameSget.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام را پر کنید")
            self.nameS.focus_set()

        elif self.familySget.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام خانوادگی را پر کنید")
            self.familyS.focus_set()

        elif self.dad_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا نام پدر را پر کنید")
            self.dad_S.focus_set()

        elif self.Code_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد ملی را پر کنید")
            self.Code_S.focus_set()

        elif not self.Code_Sget.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده کدملی")
            self.Code_S.focus_set()

        elif len(self.Code_Sget.get()) != 10:
            messagebox.showerror("پر کردن", "لطفا کد ملی را صحیح وارد کنید")
            self.Code_S.focus_set()

        elif self.Day_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا روز تولد را پر کنید")
            self.Day_S.focus_set()

        elif not self.Day_S.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده روز تولد")
            self.Day_S.focus_set()

        elif self.Month_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا ماه تولد را پر کنید")
            self.Month_S.focus_set()

        elif not self.Month_S.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده ماه تولد")
            self.Month_S.focus_set()

        elif self.Date_Sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا سال تولد را پر کنید")
            self.Date_S.focus_set()

        elif not self.Date_S.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده سال تولد")
            self.Date_S.focus_set()

        elif self.N_Code_Stdget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد دانش آموزی را پر کنید")
            self.National_Code_Student.focus_set()

        elif not self.N_Code_Stdget.get().isnumeric():
            messagebox.showerror("داده", "خطا از داده کد دانش آموزی")
            self.National_Code_Student.focus_set()

        elif self.N_Code_Stdget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کد دانش آموزی را پر کنید")
            self.National_Code_Student.focus_set()

        elif self.mobile_dad_sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا شماره تماس پدر را پر کنید")
            self.mobile_dad_s.focus_set()

        elif not self.mobile_dad_sget.get().isnumeric() and self.mobile_dad_sget.get() != "-":
            messagebox.showerror("داده", "خطا از داده شماره تماس پدر")
            self.mobile_dad_s.focus_set()

        elif len_dad != 11 and self.mobile_dad_sget.get() != "-":
            messagebox.showerror("پر کردن", "لطفا شماره تماس پدر را صحیح وارد کنید")
            self.mobile_dad_s.focus_set()

        elif self.mother_number.get() == "":
            messagebox.showerror("پر کردن", "لطفا شماره تماس مادر را پر کنید")
            self.M_Num.focus_set()

        elif not self.mother_number.get().isnumeric() and self.mother_number.get() != "-":
            messagebox.showerror("داده", "خطا از داده شماره تماس مادر")
            self.M_Num.focus_set()

        elif len_mother != 11 and self.mother_number.get() != "-":
            messagebox.showerror("پر کردن", "لطفا شماره تماس مادر را صحیح وارد کنید")
            self.M_Num.focus_set()

        elif self.class_sget.get() == "":
            messagebox.showerror("پر کردن", "لطفا کلاس را پر کنید")
            self.class_S.focus_set()
        else:
            where = " std_id= '" + self.txtIdb.get() + "' "
            Date = self.Date_Sget.get() + "/" + self.Month_Sget.get() + "/" + self.Day_Sget.get()
            col = "  Name='" + self.nameSget.get() + "',Family='" + self.familySget.get() + "' , dadName='" + \
                  self.dad_Sget.get() + "',National_Code='" + self.Code_Sget.get() + "',Date='" + Date + "',Code_S='" + \
                  self.N_Code_Stdget.get() + "',Reshte='" + self.class_sget.get() + "',mobile_dad='" + \
                  self.mobile_dad_sget.get() + "',mobile_mother='" + self.mother_number.get() + "' "
            repository = Repository()
            result = repository.update("Student_" + Variable, col, where)
            if result:
                self.set3()
                self.cleantable6()
                self.load_Std()
                self.btnE2.place_forget()
                self.btnD2.place_forget()
                messagebox.showinfo("انجام شد", "ویرایش انجام شد")
            else:
                messagebox.showerror("   خطا", "  انجام نشد")

    def getsc2(self, e):
        select = self.tbl_add_student.selection()
        if select != ():
            self.btnD2.place(x=50, y=282)
            self.btnE2.place(x=130, y=282)

            repository = Repository()
            where = " std_id='" + str(self.tbl_add_student.item(select)["values"][9]) + "' "
            data = repository.Search("Student_" + Variable, "[National_Code],[Code_S],[mobile_dad],[mobile_mother]", where, "Family")
            Mylist = []
            for item in data:
                Mylist.append(item)

            Date = self.tbl_add_student.item(select)["values"][4]

            numbers = [int(x) for x in Date.split("/") if x.isdigit()]

            self.mobile_dad_sget.set(Mylist[0][2])
            self.mother_number.set(Mylist[0][3])

            self.class_sget.set(str(self.tbl_add_student.item(select)["values"][2]))
            self.N_Code_Stdget.set(Mylist[0][1])

            self.Day_Sget.set(str(numbers[2]))
            self.Month_Sget.set(str(numbers[1]))
            self.Date_Sget.set(str(numbers[0]))

            self.Code_Sget.set(Mylist[0][0])
            self.dad_Sget.set(str(self.tbl_add_student.item(select)["values"][6]))
            self.familySget.set(str(self.tbl_add_student.item(select)["values"][7]))
            self.nameSget.set(str(self.tbl_add_student.item(select)["values"][8]))
            self.Idb.set(str(self.tbl_add_student.item(select)["values"][9]))


    def getsc_Std_List(self, e):
        select = self.tbl_day_Std.selection()
        if select != ():

            self.Honar_Jo_get_Family.set(self.tbl_day_Std.item(select)["values"][0])
            self.Honar_Jo_get.set(self.tbl_day_Std.item(select)["values"][1])
            self.Idde.set(self.tbl_day_Std.item(select)["values"][2])


    def getsc_Tch_List(self, e):
        select = self.tbl_day_Tch.selection()
        if select != ():

            self.Honar_Amoz_get_Family.set(self.tbl_day_Tch.item(select)["values"][0])
            self.Honar_Amoz_get.set(self.tbl_day_Tch.item(select)["values"][1])
            self.Iddt.set(self.tbl_day_Tch.item(select)["values"][2])

    def onclickBack(self, e):
        self.HideLayer_All()
        self.showLayer_1_2()
        self.showLayer_1()
        self.SetAll()


    def Hozor_Ghiyab(self,State,h_g):
        name = ""
        field = ""
        field2 = ""
        Std_Long = "no"
        Std_Exit_Class = "no"
        Std_Exit_School = "no"

        Tch_Long = "no"
        Tch_Exit_Class = "None"
        Tch_Exit_School = "None"

        S = False
        if State == "Std":
            field = self.Honar_Jo_get.get()
            field2 = self.Honar_Jo_get_Family.get()
            name = "هنرجو"
            if self.Honar_Jo_get.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام هنرجو را وارد کنید")
                self.Honar_Jo.focus_set()

            elif self.Honar_Jo_get_Family.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام خانوادگی هنرجو را وارد کنید")
                self.Honar_Jo_Family.focus_set()
            else:
                S = True
        if State == "Tch":
            field = self.Honar_Amoz_get.get()
            field2 = self.Honar_Amoz_get_Family.get()
            name = "هنرآموز"
            if self.Honar_Amoz_get.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام هنرآموز را وارد کنید")
                self.Honar_Amoz.focus_set()

            elif self.Honar_Amoz_get_Family.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام خانوادگی هنرآموز را وارد کنید")
                self.Honar_Amoz_Family.focus_set()
            else:
                S = True

        if self.check_Std_Long_var.get():
            Std_Long = "yes"

        if self.check_Std_Exit_C_var.get():
            Std_Exit_Class = "yes"

        if self.check_Std_Exit_S_var.get():
            Std_Exit_School = "yes"

        if self.check_Tch_Long_var.get():
            Tch_Long = "yes"
        if S:
            days = request.days()
            repository = Repository()
            Std_Found = []
            where = "Name = '" + field + "' and Family = '" + field2 \
                    + "' and Zang = '" + self.day_Zang + "' and Type = '" + State +\
                    "' and Date = '" + request.Full_Date() + "' and Class = '" + self.textClass + "'"
            Where = persian.convert_fa_numbers(where)

            result = repository.Search("Presentation_" + Variable, "*", Where, "Family")
            for item in result:
                Std_Found.append(item)

            if len(Std_Found) != 0:
                if State == "Std":
                    messagebox.showerror("تکراری", "این هنرجو قبلا ثبت شده است")
                if State == "Tch":
                    messagebox.showerror("تکراری", "این هنرآموز قبلا ثبت شده است")

            else:
                messagebox.showinfo("ثبت اطلاعات", "ثبت اطلاعات با موفقیت انجام شد")
                MyList = []
                if days == "پنجشنبه":
                    Zang_List = ["زنگ اول", "زنگ دوم", "زنگ سوم"]
                else:
                    Zang_List = ["زنگ اول", "زنگ دوم", "زنگ سوم", "زنگ چهارم"]

                for items in Zang_List:
                    if State == "Std":
                        where = "Name = '" + self.Honar_Jo_get.get() + "' and Family = '" + self.Honar_Jo_get_Family.get()\
                            + "' and day = '" + days + "' and Date = '" + request.Full_Date() +\
                                "' and Zang = '" + items + "' and Class = '" + self.textClass + "'"
                    else:
                        where = "Name = '" + self.Honar_Amoz_get.get() + "' and Family = '" + self.Honar_Amoz_get_Family.get() \
                                + "' and day = '" + days + "' and Date = '" + request.Full_Date() + \
                                "' and Zang = '" + items + "' and Class = '" + self.textClass + "'"
                    Where = persian.convert_fa_numbers(where)

                    result = repository.Search("Presentation_" + Variable, "[res]", Where, "Family")
                    for item in result:
                        MyList.append(item)
                print(MyList)
                obj = ""
                Today_hozor = ""
                len_List = []
                List = [item[0] for item in MyList]
                List.append(h_g)
                if len(MyList) == 0:
                    Today_hozor = "NULL"
                if days == "پنجشنبه" and len(MyList) == 2:
                    print(List)
                    for item in List:
                        print(item)
                        if item == "غايب" or item == "غایب":
                            len_List.append("غایب")
                    print(len_List)
                    if len(len_List) == 3:
                        Today_hozor = "NO"
                    else:
                        Today_hozor = "YES"

                else:
                    if days != "پنجشنبه" and len(MyList) == 3:
                        for item in List:
                            print(item)
                            if item == "غايب" or item == "غایب":
                                len_List.append("غايب")
                        if len(len_List) == 4:
                            Today_hozor = "NO"
                        else:
                            Today_hozor = "YES"
                    else:
                        Today_hozor = "NULL"
                print(Today_hozor)
                if name == "هنرجو":
                    data = self.Honar_Jo_get.get(), self.Honar_Jo_get_Family.get(), State,\
                        request.Full_Date(), days, h_g, self.textClass, self.day_Zang, Std_Long,\
                        Std_Exit_Class, Std_Exit_School, Today_hozor

                    obj = persian.convert_fa_numbers(data)
                else:
                    data = self.Honar_Amoz_get.get(), self.Honar_Amoz_get_Family.get(), State,\
                        request.Full_Date(), days, h_g, self.textClass, self.day_Zang, Tch_Long,\
                        Tch_Exit_Class, Tch_Exit_School, Today_hozor

                    obj = persian.convert_fa_numbers(data)

                objcar = blCar()
                Cols = " (Name,Family,Type,Date,day,res,Class,Zang,Long,Exit_Class,Exit_School,today_hozor) "
                objcar.Insert(str(obj), "Presentation_" + Variable, Cols)

                self.Set_Val_Hozor()
                self.load_Hozor_List_Std()
                self.load_Hozor_List_Tch()


    def cleantable_Hozor_List_Std(self):
        for item in self.tbl_Hozor_Student.get_children():
            self.sel = (str(item))
            self.tbl_Hozor_Student.delete(self.sel)

    def cleantable_Hozor_List_Tch(self):
        for item in self.tbl_Hozor_Tch.get_children():
            self.sel = (str(item))
            self.tbl_Hozor_Tch.delete(self.sel)

    def load_Hozor_List_Std(self):
            repository = Repository()
            where = f"Class = '" + self.textClass + "' and Zang = '" +\
                    self.day_Zang + "' and Type = '" + 'Std' + "' and Date = '" + request.Full_Date() + "'"
            Where = persian.convert_fa_numbers(where)

            result = repository.Search("Presentation_" + Variable, "*", Where, "Family")

            for item in result:
                if item[9] == "yes":
                    Long = "تاخیر داشته"
                else:
                    Long = "تاخیر نداشته"

                if item[10] == "yes":
                    Exit_Class = "اخراج شده"
                else:
                    Exit_Class = "اخراج نشده"

                if item[11] == "yes":
                    Exit_School = "فرار کرده"
                else:
                    Exit_School = "فرار نکرده"

                self.tbl_Hozor_Student.insert('', "end", values=[Exit_School,Exit_Class,Long,item[6],item[2], item[1],item[0]])


    def load_Hozor_List_Tch(self):
            repository = Repository()
            where = f"Class = '{persian.convert_fa_numbers(self.textClass)}' and Zang = '{self.day_Zang}' and Type = 'Tch' and Date = '{request.Full_Date()}'"
            Where = persian.convert_fa_numbers(where)
            result = repository.Search("Presentation_" + Variable, "*", Where, "Family")
            for item in result:
                if item[9] == "yes":
                    Long = "تاخیر داشته"
                else:
                    Long = "تاخیر نداشته"

                self.tbl_Hozor_Tch.insert('', "end", values=[Long,item[6],item[2],item[1],item[0]])


    def load_hosh(self):
        repository = Repository()
        Date = request.lasts_day(7)
        MyList = []
        result = ""
        Ghayeb_List = []
        Lisst = []
        i = 0
        for items in Date:
            where = f" Date = '{items}' and today_hozor = 'NO' and Type = 'Std'"
            Where = persian.convert_fa_numbers(where)
            result = repository.Search("Presentation_" + Variable, "[Name],[Family],[Class]", Where, "Family")
            if result != []:
                for item in result:
                    Ghayeb_List.append((item[0], item[1], item[2]))

        Ghayeb_List = list(set(Ghayeb_List))
        for item in Ghayeb_List:
            for itms in Date:
                where = f" Name = '{item[0]}' and Family = '{item[1]}'" + \
                        f" and Date = '{itms}' and today_hozor = 'NO'"
                Where = persian.convert_fa_numbers(where)
                res = repository.Search("Presentation_" + Variable, "[today_hozor]", Where, "Family")

                for itm in res:
                    MyList.append(itm)
            if len(MyList) == 3:
                where = f" Name = '{Ghayeb_List[i][0]}' and Family = '{Ghayeb_List[i][1]}'"
                Where = persian.convert_fa_numbers(where)
                results = repository.Search("Student_" + Variable, "[Code_S],[mobile_dad],[mobile_mother]",
                                            Where, "Family")
                if i < 1:
                    i += 1
                if results:
                    for itm in results:
                        self.tbl_hosh.insert('', "end",
                                             values=[itm[2], itm[1], item[2], itm[0], item[1], item[0]])
                MyList.clear()


    def Set_Val_Hozor_Add(self):
        self.cleantable_Tch_List()
        self.cleantable_Std_List()
        self.Honar_Amoz_get.set("")
        self.Honar_Amoz_get_Family.set("")
        self.Honar_Jo_get.set("")
        self.Honar_Jo_get_Family.set("")
        self.check_Std_Long_var.set(False)
        self.check_Tch_Long_var.set(False)
        self.check_Std_Exit_C_var.set(False)
        self.check_Std_Exit_S_var.set(False)

    def Set_Val_Hozor_List(self):
        self.Std_Radio_yes.set(False)
        self.Std_Radio_no.set(False)
        self.Tch_Radio_yes.set(False)
        self.Tch_Radio_no.set(False)
        self.cleantable_Hozor_List_Std()
        self.cleantable_Hozor_List_Tch()
        self.Honar_Amoz_get_List.set("")
        self.Honar_Amoz_get_List_Family.set("")
        self.Honar_Jo_get_List.set("")
        self.Honar_Jo_get_List_Family.set("")
        self.check_Std_Long_var_List.set(False)
        self.check_Tch_Long_var_List.set(False)
        self.check_Std_Exit_C_var_List.set(False)
        self.check_Std_Exit_S_var_List.set(False)
        self.btnE_Hozor_List.place_forget()
        self.btnD_Hozor_List.place_forget()


    def Set_Val_Hozor(self):
        self.cleantable_Hozor_List_Std()
        self.cleantable_Hozor_List_Tch()
        self.Honar_Amoz_get.set("")
        self.Honar_Amoz_get_Family.set("")
        self.Honar_Jo_get.set("")
        self.Honar_Jo_get_Family.set("")
        self.check_Std_Long_var.set(False)
        self.check_Tch_Long_var.set(False)
        self.check_Std_Exit_C_var.set(False)
        self.check_Std_Exit_S_var.set(False)

    def getsc_Hozor_Std_List(self, e):
        self.cleantable_Hozor_List_Tch()
        self.load_Hozor_List_Tch()
        self.check_Std_Long_var_List.set(False)
        self.check_Tch_Long_var_List.set(False)
        self.check_Std_Exit_C_var_List.set(False)
        self.check_Std_Exit_S_var_List.set(False)
        select = self.tbl_Hozor_Student.selection()
        if select != ():
            if self.tbl_Hozor_Student.item(select)["values"][2] == "تاخیر داشته":
                self.check_Std_Long_var_List.set(True)

            if self.tbl_Hozor_Student.item(select)["values"][1] == "اخراج شده":
                self.check_Std_Exit_C_var_List.set(True)

            if self.tbl_Hozor_Student.item(select)["values"][0] == "فرار کرده":
                self.check_Std_Exit_S_var_List.set(True)

            self.Std_Radio_yes.set(0)
            self.Std_Radio_no.set(0)

            if self.tbl_Hozor_Student.item(select)["values"][3] == "حاضر":
                self.Std_Radio_yes.set(1)
            else:
                self.Std_Radio_no.set(2)

            self.Honar_Jo_get_List_Family.set(self.tbl_Hozor_Student.item(select)["values"][4])
            self.Honar_Jo_get_List.set(self.tbl_Hozor_Student.item(select)["values"][5])
            self.Id_Std.set(self.tbl_Hozor_Student.item(select)["values"][6])
            self.Honar_Amoz_get_List.set("")
            self.Honar_Amoz_get_List_Family.set("")
            self.btnE_Hozor_List.place(x=310, y=246)
            self.btnD_Hozor_List.place(x=250, y=246)

    def getsc_Hozor_Tch_List(self, e):
        self.cleantable_Hozor_List_Std()
        self.load_Hozor_List_Std()
        self.check_Std_Long_var_List.set(False)
        self.check_Tch_Long_var_List.set(False)
        self.check_Std_Exit_C_var_List.set(False)
        self.check_Std_Exit_S_var_List.set(False)
        select = self.tbl_Hozor_Tch.selection()
        if select != ():
            if self.tbl_Hozor_Tch.item(select)["values"][0] == "تاخیر داشته":
                self.check_Tch_Long_var_List.set(True)

            self.Tch_Radio_yes.set(0)
            self.Tch_Radio_no.set(0)

            if self.tbl_Hozor_Tch.item(select)["values"][1] == "حاضر":
                self.Tch_Radio_yes.set(1)
            else:
                self.Tch_Radio_no.set(2)

            self.Honar_Amoz_get_List.set(self.tbl_Hozor_Tch.item(select)["values"][2])
            self.Honar_Amoz_get_List_Family.set(self.tbl_Hozor_Tch.item(select)["values"][3])
            self.Id_Tch.set(self.tbl_Hozor_Tch.item(select)["values"][4])
            self.Honar_Jo_get_List.set("")
            self.Honar_Jo_get_List_Family.set("")
            self.btnE_Hozor_List.place(x=310, y=246)
            self.btnD_Hozor_List.place(x=250, y=246)

    def Check_Std_Tch_Edit(self):
        select = self.tbl_Hozor_Student.selection()
        select2 = self.tbl_Hozor_Tch.selection()

        if select != ():
            self.OnclickEdit_Std_Tch_List("Std", self.Id_Std.get(), self.Honar_Jo_get_List.get(),self.Honar_Jo_get_List_Family.get())

        if select2 != ():
            self.OnclickEdit_Std_Tch_List("Tch", self.Id_Tch.get(),self.Honar_Amoz_get_List.get(),self.Honar_Amoz_get_List_Family.get())


    def OnclickEdit_Std_Tch_List(self, State, field, Name, Family):

        name = ""
        Std_Long = "no"
        Std_Exit_Class = "no"
        Std_Exit_School = "no"

        Std_r_no = "False"
        Std_r_yes = "False"
        Tch_r_no = "False"
        Tch_r_yes = "False"

        Tch_Long = "no"
        Tch_Exit_Class = "None"
        Tch_Exit_School = "None"

        select_row_Std = self.tbl_Hozor_Student.selection()

        select_row_Tch = self.tbl_Hozor_Tch.selection()

        S = False
        if State == "Std":
            name = "هنرجو"
            if self.Honar_Jo_get_List.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام هنرجو را وارد کنید")
                self.Honar_Jo_List.focus_set()

            elif self.Honar_Jo_List_Family.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام خانوادگی هنرجو را وارد کنید")
                self.Honar_Jo_List_Family.focus_set()
            else:
                S = True
        if State == "Tch":
            name = "هنرآموز"
            if self.Honar_Amoz_get_List.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام هنرآموز را وارد کنید")
                self.Honar_Amoz_List.focus_set()

            elif self.Honar_Amoz_get_List_Family.get() == "":
                messagebox.showerror("پر کردن", "لطفا نام خانوادگی هنرآموز را وارد کنید")
                self.Honar_Amoz_List_Family.focus_set()
            else:
                S = True

        if State == "Std":
            if self.check_Std_Long_var_List.get():
                Std_Long = "yes"

            if self.check_Std_Exit_C_var_List.get():
                Std_Exit_Class = "yes"

            if self.check_Std_Exit_S_var_List.get():
                Std_Exit_School = "yes"

            if self.Std_Radio_yes.get() != 0:
                Std_r_yes = "True"

            if self.Std_Radio_no.get() != 0:
                Std_r_no = "True"

        if State == "Tch":

            if self.check_Tch_Long_var_List.get():
                Tch_Long = "yes"

            if self.Tch_Radio_yes.get() != 0:
                Tch_r_yes = "True"

            if self.Tch_Radio_no.get() != 0:
                Tch_r_no = "True"

        if S:
            days = request.days()
            repository = Repository()
            messagebox.showinfo("ثبت اطلاعات", "ثبت اطلاعات با موفقیت انجام شد")

            if State == "Std":
                if Std_r_yes == "True":
                    present = "حاضر"
                else:
                    present = "غایب"
            else:
                if Tch_r_yes == "True":
                    present = "حاضر"
                else:
                    present = "غایب"

            if name == "هنرآموز":

                Cols = "  Name='" + Name + "',Family='" + Family + "',Type='" + \
                       State + "',res='" + present + "',Long='" + Tch_Long + \
                       "',Exit_Class='" + Tch_Exit_Class + "',Exit_School='" + Tch_Exit_School + "' "

            else:

                Cols = "  Name='" + Name + "',Family='" + Family + "',Type='" + \
                       State + "',res='" + present + "',Long='" + Std_Long + \
                       "',Exit_Class='" + Std_Exit_Class + "',Exit_School='" + Std_Exit_School + "' "


            repository = Repository()
            Tablename = "Presentation_" + Variable
            where = " Std_Tch_id= '" + field + "' "
            repository.update(Tablename, Cols, where)


            MyList = []
            if days == "پنجشنبه":
                Zang_List = ["زنگ اول", "زنگ دوم", "زنگ سوم"]
            else:
                Zang_List = ["زنگ اول", "زنگ دوم", "زنگ سوم", "زنگ چهارم"]

            for items in Zang_List:
                if State == "Std":
                    where = "Name = '" + self.Honar_Jo_get_List.get() + "' and Family = '" + self.Honar_Jo_get_List_Family.get() \
                            + "' and day = '" + days + "' and Date = '" + request.Full_Date() + \
                            "' and Zang = '" + items + "' and Class = '" + self.textClass + "'"
                    Where = persian.convert_fa_numbers(where)
                else:
                    where = "Name = '" + self.Honar_Amoz_get_List.get() + "' and Family = '" + self.Honar_Amoz_get_List_Family.get() \
                            + "' and day = '" + days + "' and Date = '" + request.Full_Date() + \
                            "' and Zang = '" + items + "' and Class = '" + self.textClass + "'"
                    Where = persian.convert_fa_numbers(where)

                result = repository.Search("Presentation_" + Variable, "[res]", Where, "Family")
                for item in result:
                    MyList.append(item)

            obj = ""
            Today_hozor = ""
            len_List = []
            List = [item[0] for item in MyList]
            print(List)

            if days == "پنجشنبه" and len(List) == 3:
                for item in List:
                    print(item)
                    if item == "غايب" or item == "غایب":
                        len_List.append("غایب")
                print(len(len_List))
                if len(len_List) == 3:
                    Today_hozor = "NO"
                else:
                    Today_hozor = "YES"

            else:
                if days != "پنجشنبه" and len(List) == 4:
                    for item in List:
                        if item == "غايب" or item == "غایب":
                            len_List.append("غايب")
                    if len(len_List) == 4:
                        Today_hozor = "NO"
                    else:
                        Today_hozor = "YES"
                else:
                    Today_hozor = "NULL"

            Where = ""
            if Today_hozor == "YES" or Today_hozor == "NO":

                for items in Zang_List:
                    if State == "Std":
                        Cols = "  today_hozor='" + "NULL" + "' "
                        where = "Name = '" + self.Honar_Jo_get_List.get() + "' and Family = '" + self.Honar_Jo_get_List_Family.get() \
                                + "' and day = '" + days + "' and Date = '" + request.Full_Date() + \
                                "' and Zang = '" + items + "' and Class = '" + self.textClass + "'"
                        Where = persian.convert_fa_numbers(where)

                    else:
                        Cols = "  today_hozor='" + "NULL" + "' "
                        where = "Name = '" + self.Honar_Amoz_get_List.get() + "' and Family = '" + self.Honar_Amoz_get_List_Family.get() \
                                + "' and day = '" + days + "' and Date = '" + request.Full_Date() + \
                                "' and Zang = '" + items + "' and Class = '" + self.textClass + "'"
                        Where = persian.convert_fa_numbers(where)

                    Tablename = "Presentation_" + Variable
                    repository.update(Tablename, Cols, Where)

                    Col = f"  today_hozor='{Today_hozor}' "
                    where = " Std_Tch_id= '" + field + "' "
                    repository.update(Tablename, Col, where)

            self.Set_Val_Hozor_List()
            self.load_Hozor_List_Std()
            self.load_Hozor_List_Tch()


    def Check_Std_Tch(self):
        select = self.tbl_Hozor_Student.selection()
        select2 = self.tbl_Hozor_Tch.selection()

        if select != ():
            self.OnclickDelet_Std_List()

        if select2 != ():
            self.OnclickDelet_Tch_List()

    def OnclickDelet_Std_List(self):
        result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

        if result == "yes":
            self.Delete_Std_List()

    def Delete_Std_List(self):
        repository = Repository()
        select_row = self.tbl_Hozor_Student.selection()

        if select_row != ():
            SelectItem = self.tbl_Hozor_Student.item(select_row)["values"]
            where = " Std_Tch_id='" + str(SelectItem[6]) + "' "
            result = repository.delete("Presentation_" + Variable, where)
            if result:
                days = request.days()
                messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")

                where = "Name = '" + self.Honar_Jo_get_List.get() + "' and Family = '" +\
                        self.Honar_Jo_get_List_Family.get() + "' and day = '" + days +\
                        "' and Date = '" + request.Full_Date() + "' and Class = '" + self.textClass + "'"

                Where = persian.convert_fa_numbers(where)

                result = repository.Search("Presentation_" + Variable, "[Std_Tch_id]", Where, "Family")
                MyList = []
                for item in result:
                    MyList.append(item)

                for item in MyList:
                    where = f" Std_Tch_id= '{item[0]}' "

                    col = "  today_hozor='" + "NULL" + "' "

                    result = repository.update("Presentation_" + Variable, col, where)

                self.Set_Val_Hozor_List()
                self.load_Hozor_List_Tch()
                self.load_Hozor_List_Std()
                self.btnE_Hozor_List.place_forget()
                self.btnD_Hozor_List.place_forget()
        else:
            messagebox.showerror("خطا", "حذف انجام نشد")
            self.btnE_Hozor_List.place_forget()
            self.btnD_Hozor_List.place_forget()


    def OnclickDelet_Tch_List(self):
        result = messagebox.askquestion("هشدار", "آیا مطمعن هستید میخواهید این داده را حذف کنید")

        if result == "yes":
            self.Delete_Tch_List()


    def Delete_Tch_List(self):
        repository = Repository()
        select_row = self.tbl_Hozor_Tch.selection()
        days = request.days()

        if select_row != ():
            SelectItem = self.tbl_Hozor_Tch.item(select_row)["values"]
            where = " Std_Tch_id='" + str(SelectItem[4]) + "' "
            result = repository.delete("Presentation_" + Variable, where)
            if result:
                messagebox.showinfo("انجام شد ", "حذف اطلاعات با موفقیت انجام شد")
                where = "Name = '" + self.Honar_Amoz_get_List.get() + "' and Family = '" +\
                        self.Honar_Amoz_get_List_Family.get() + "' and day = '" + days +\
                        "' and Date = '" + request.Full_Date() + "' and Class = '" + self.textClass + "'"

                Where = persian.convert_fa_numbers(where)

                result = repository.Search("Presentation_" + Variable, "[Std_Tch_id]", Where, "Family")
                MyList = []
                for item in result:
                    MyList.append(item)

                for item in MyList:
                    where = f" Std_Tch_id= '{item[0]}' "

                    col = "  today_hozor='" + "NULL" + "' "

                    result = repository.update("Presentation_" + Variable, col, where)
                self.Set_Val_Hozor_List()
                self.load_Hozor_List_Tch()
                self.load_Hozor_List_Std()
                self.btnE_Hozor_List.place_forget()
                self.btnD_Hozor_List.place_forget()
        else:
            messagebox.showerror("خطا", "حذف انجام نشد")
            self.btnE_Hozor_List.place_forget()
            self.btnD_Hozor_List.place_forget()


    def Radio_Check(self, State, yes_no):
        if State == "Std":
            if yes_no == "yes":
                self.Std_Radio_no.set(0)

            if yes_no == "no":
                self.Std_Radio_yes.set(0)

        if State == "Tch":
            if yes_no == "yes":
                self.Tch_Radio_no.set(0)

            if yes_no == "no":
                self.Tch_Radio_yes.set(0)


    def Select_Type(self, event):
        Value = self.Info_Type.get()
        Val = ""

        if Value != "":
            if Value == "حاضرین" or Value == "غایبین" or Value == "تاخیری":

                if hasattr(self, 'tbl_Lists_hazer_ghiyab'):
                    self.tbl_Lists_hazer_ghiyab.destroy()

                if hasattr(self, 'tbl_Lists_Long'):
                    self.tbl_Lists_Long.destroy()

                if hasattr(self, 'tbl_Lists_personel_h_gh_t'):
                    self.tbl_Lists_personel_h_gh_t.destroy()

                if hasattr(self, 'lbl_Lists_LastName'):
                    self.lbl_Lists_LastName.destroy()

                if hasattr(self, 'lbl_Lists_Name'):
                    self.lbl_Lists_Name.destroy()

                if hasattr(self, 'Select_person'):
                    self.Select_person.destroy()

                if hasattr(self, 'lbl_Type_person'):
                    self.lbl_Type_person.destroy()

                if hasattr(self, 'btn_hazer_info'):
                    self.btn_hazer_info.destroy()

                if hasattr(self, 'Times3'):
                    self.Times3.destroy()

                if hasattr(self, 'Lists_LastName'):
                    self.Lists_LastName.destroy()

                if hasattr(self, 'Lists_Name'):
                    self.Lists_Name.destroy()

                if hasattr(self, 'btn_Exit_School_info'):
                    self.btn_Exit_School_info.destroy()

                if hasattr(self, 'btn_Exit_Class_info'):
                    self.btn_Exit_Class_info.destroy()

                if hasattr(self, 'btn_Long_info'):
                    self.btn_Long_info.destroy()

                if hasattr(self, 'btn_ghayeb_info'):
                    self.btn_ghayeb_info.destroy()

                if hasattr(self, 'btn_Find_List'):
                    self.btn_Find_List.destroy()

                if hasattr(self, 'lbl_Select_Class_S'):
                    self.lbl_Select_Class_S.destroy()

                if hasattr(self, 'Classes_S'):
                    self.Classes_S.destroy()

                if hasattr(self, 'hazer_list'):
                    Val = self.Hazer_List.get()
                    self.hazer_list.destroy()

                if hasattr(self, 'Times_2'):
                    self.Time_2.set("")
                    self.Times_2.destroy()

                if hasattr(self, 'lbl_Time_DayS'):
                    self.lbl_Time_DayS.destroy()

                if hasattr(self, 'lbl_Time_DayS1'):
                    self.lbl_Time_DayS1.destroy()

                if hasattr(self, 'lbl_Time_DayS2'):
                    self.lbl_Time_DayS2.destroy()

                if hasattr(self, 'lbl_Time_MonthS'):
                    self.lbl_Time_MonthS.destroy()

                if hasattr(self, 'lbl_Time_MonthS1'):
                    self.lbl_Time_MonthS1.destroy()

                if hasattr(self, 'lbl_Time_MonthS2'):
                    self.lbl_Time_MonthS2.destroy()

                if hasattr(self, 'lbl_Time_YearS'):
                    self.lbl_Time_YearS.destroy()

                if hasattr(self, 'lbl_Time_YearS1'):
                    self.lbl_Time_YearS1.destroy()

                if hasattr(self, 'lbl_Time_YearS2'):
                    self.lbl_Time_YearS2.destroy()

                if hasattr(self, 'time_daysS'):
                    self.time_daysS.destroy()

                if hasattr(self, 'time_daysS1'):
                    self.time_daysS1.destroy()

                if hasattr(self, 'time_daysS2'):
                    self.time_daysS2.destroy()

                if hasattr(self, 'time_monthsS'):
                    self.time_monthsS.destroy()

                if hasattr(self, 'time_monthsS1'):
                    self.time_monthsS1.destroy()

                if hasattr(self, 'time_monthsS2'):
                    self.time_monthsS2.destroy()

                if hasattr(self, 'time_yearsS'):
                    self.time_yearsS.destroy()

                if hasattr(self, 'time_yearsS1'):
                    self.time_yearsS1.destroy()

                if hasattr(self, 'time_yearsS2'):
                    self.time_yearsS2.destroy()

                if hasattr(self, 'lbl_azS'):
                    self.lbl_azS.destroy()

                if hasattr(self, 'lbl_taS'):
                    self.lbl_taS.destroy()

                if hasattr(self, 'lbl_Lists'):
                    self.lbl_Lists.destroy()

                self.lbl_Lists = Label(self.frm_List,
                                       text="اسامی",
                                       font=("Calibri", 12, "bold"))
                self.lbl_Lists.place(x=525, y=150)

                self.Hazer_List = StringVar()
                self.hazer_list = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Hazer_List,
                                               font=("Calibri", 12, "bold"), state="readonly")
                self.hazer_list['values'] = (
                    '', 'هنرآموزان', 'هنرجویان')
                self.hazer_list.current(0)
                self.hazer_list.place(x=425, y=150, width=100)
                self.hazer_list.bind("<<ComboboxSelected>>", self.Select_hazer_list)
                self.Hazer_List.set(Val)

                self.btn_Find_List = Button(self.frm_List, text="جستجو", font=("Calibri", 12, "bold"),
                                            command=self.Find_List)
                self.btn_Find_List.place(x=175, y=195)

                if self.Hazer_List.get() == "":
                    if hasattr(self, 'lbl_Time_Day'):
                        self.lbl_Time_Day.destroy()

                    if hasattr(self, 'lbl_Time_Day_'):
                        self.lbl_Time_Day_.destroy()

                    if hasattr(self, 'lbl_Time_DayS'):
                        self.lbl_Time_DayS.destroy()

                    if hasattr(self, 'lbl_Time_DayS1'):
                        self.lbl_Time_DayS1.destroy()

                    if hasattr(self, 'lbl_Time_DayS2'):
                        self.lbl_Time_DayS2.destroy()

                    if hasattr(self, 'lbl_Time_Day_2'):
                        self.lbl_Time_Day_2.destroy()

                    if hasattr(self, 'lbl_Time_Month'):
                        self.lbl_Time_Month.destroy()

                    if hasattr(self, 'lbl_Time_Month_'):
                        self.lbl_Time_Month_.destroy()

                    if hasattr(self, 'lbl_Time_MonthS'):
                        self.lbl_Time_MonthS.destroy()

                    if hasattr(self, 'lbl_Time_MonthS1'):
                        self.lbl_Time_MonthS1.destroy()

                    if hasattr(self, 'lbl_Time_MonthS2'):
                        self.lbl_Time_MonthS2.destroy()

                    if hasattr(self, 'lbl_Time_Month_2'):
                        self.lbl_Time_Month_2.destroy()

                    if hasattr(self, 'lbl_Time_Year'):
                        self.lbl_Time_Year.destroy()

                    if hasattr(self, 'lbl_Time_Year_'):
                        self.lbl_Time_Year_.destroy()

                    if hasattr(self, 'lbl_Time_YearS'):
                        self.lbl_Time_YearS.destroy()

                    if hasattr(self, 'lbl_Time_YearS1'):
                        self.lbl_Time_YearS1.destroy()

                    if hasattr(self, 'lbl_Time_YearS2'):
                        self.lbl_Time_YearS2.destroy()

                    if hasattr(self, 'lbl_Time_Year_2'):
                        self.lbl_Time_Year_2.destroy()

                    if hasattr(self, 'time_days'):
                        self.time_days.destroy()

                    if hasattr(self, 'time_months'):
                        self.time_months.destroy()

                    if hasattr(self, 'time_years'):
                        self.time_years.destroy()

                    if hasattr(self, 'time_daysS'):
                        self.time_daysS.destroy()

                    if hasattr(self, 'time_daysS1'):
                        self.time_daysS1.destroy()

                    if hasattr(self, 'time_daysS2'):
                        self.time_daysS2.destroy()

                    if hasattr(self, 'time_monthsS'):
                        self.time_monthsS.destroy()

                    if hasattr(self, 'time_monthsS1'):
                        self.time_monthsS1.destroy()

                    if hasattr(self, 'time_monthsS2'):
                        self.time_monthsS2.destroy()

                    if hasattr(self, 'time_yearsS'):
                        self.time_yearsS.destroy()

                    if hasattr(self, 'time_yearsS1'):
                        self.time_yearsS1.destroy()

                    if hasattr(self, 'time_yearsS2'):
                        self.time_yearsS2.destroy()

                    if hasattr(self, 'lbl_az'):
                        self.lbl_az.destroy()

                    if hasattr(self, 'lbl_ta'):
                        self.lbl_ta.destroy()

                    if hasattr(self, 'lbl_azS'):
                        self.lbl_azS.destroy()

                    if hasattr(self, 'lbl_taS'):
                        self.lbl_taS.destroy()

                    if hasattr(self, 'time_years'):
                        self.time_years.destroy()

                    if hasattr(self, 'time_days_'):
                        self.time_days_.destroy()

                    if hasattr(self, 'time_days_2'):
                        self.time_days_2.destroy()

                    if hasattr(self, 'time_months_'):
                        self.time_months_.destroy()

                    if hasattr(self, 'time_months_2'):
                        self.time_months_2.destroy()

                    if hasattr(self, 'time_years_'):
                        self.time_years_.destroy()

                    if hasattr(self, 'time_years_2'):
                        self.time_years_2.destroy()

                    if hasattr(self, 'time_years'):
                        self.time_years.destroy()

                    if hasattr(self, 'lbl_Lists_LastName'):
                        self.lbl_Lists_LastName.destroy()

                    if hasattr(self, 'lbl_Lists_Name'):
                        self.lbl_Lists_Name.destroy()

                    if hasattr(self, 'Select_person'):
                        self.Select_person.destroy()

                    if hasattr(self, 'lbl_Type_person'):
                        self.lbl_Type_person.destroy()

                    if hasattr(self, 'btn_hazer_info'):
                        self.btn_hazer_info.destroy()

                    if hasattr(self, 'Times3'):
                        self.Times3.destroy()

                    if hasattr(self, 'Lists_LastName'):
                        self.Lists_LastName.destroy()

                    if hasattr(self, 'Lists_Name'):
                        self.Lists_Name.destroy()

                    if hasattr(self, 'btn_Exit_School_info'):
                        self.btn_Exit_School_info.destroy()

                    if hasattr(self, 'btn_Exit_Class_info'):
                        self.btn_Exit_Class_info.destroy()

                    if hasattr(self, 'btn_Long_info'):
                        self.btn_Long_info.destroy()

                    if hasattr(self, 'btn_ghayeb_info'):
                        self.btn_ghayeb_info.destroy()

                    if hasattr(self, 'lbl_Time'):
                        self.lbl_Time.destroy()

            elif Value == "فردی":
                self.hasattr()

                if hasattr(self, 'btn_Exit_Class_info'):
                    self.btn_Exit_Class_info.destroy()

                if hasattr(self, 'btn_Exit_School_info'):
                    self.btn_Exit_School_info.destroy()

                if hasattr(self, 'btn_Find_List'):
                    self.btn_Find_List.destroy()

                self.lbl_Type_person = Label(self.frm_List,text="نوع",font=("Calibri", 12, "bold"))
                self.lbl_Type_person.place(x=540, y=150)

                self.Select_Type_person = StringVar()
                self.Select_person = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Select_Type_person,
                                                  font=("Calibri", 12, "bold"), state="readonly")
                self.Select_person['values'] = (
                    'هنرجو', 'هنرآموز')
                self.Select_person.current(0)
                self.Select_person.place(x=460, y=150, width=75)
                self.Select_person.bind("<<ComboboxSelected>>", self.Select_persons)

                self.lbl_Lists_Name = Label(self.frm_List,text="نام",font=("Calibri", 12, "bold"))
                self.lbl_Lists_Name.place(x=435, y=150)

                self.Get_Lists_Name = StringVar()
                self.Lists_Name = ttk.Entry(self.frm_List, justify="center", textvariable=self.Get_Lists_Name,
                                            font=("Calibri", 12, "bold"))
                self.Lists_Name.place(x=290, y=150, width=130)

                self.lbl_Lists_LastName = Label(self.frm_List,text="نام خانوادگی",font=("Calibri", 12, "bold"))
                self.lbl_Lists_LastName.place(x=215, y=150)

                self.Get_Lists_LastName = StringVar()
                self.Lists_LastName = ttk.Entry(self.frm_List, justify="center", textvariable=self.Get_Lists_LastName,
                                                font=("Calibri", 12, "bold"))
                self.Lists_LastName.place(x=75, y=150, width=130)

                self.lbl_Time = Label(self.frm_List,
                                      text="تاریخ",
                                      font=("Calibri", 12, "bold"))
                self.lbl_Time.place(x=700, y=200)

                self.Time3 = StringVar()
                self.Times3 = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Time3,
                                           font=("Calibri", 12, "bold"), state="readonly")
                self.Times3['values'] = (
                    '', 'تکی', 'بازه ای')
                self.Times3.current(0)
                self.Times3.place(x=600, y=200, width=75)
                self.Times3.bind("<<ComboboxSelected>>", self.Select_Date_person)

                self.btn_hazer_info = Button(self.frm_List, padx=5, text="حاضر", fg="green", font=("Calibri", 11, "bold"),
                                             command=lambda: self.person_Lists("حاضر"))
                self.btn_hazer_info.place(x=625, y=250)

                self.btn_ghayeb_info = Button(self.frm_List, padx=5, text="غایب", fg="red", font=("Calibri", 11, "bold"),
                                              command=lambda: self.person_Lists("غایب"))
                self.btn_ghayeb_info.place(x=550, y=250)

                self.btn_Long_info = Button(self.frm_List, padx=5, text="تاخیر", fg="orange", font=("Calibri", 11, "bold"),
                                            command=lambda: self.person_Lists("تاخیر"))
                self.btn_Long_info.place(x=475, y=250)

                self.btn_Exit_Class_info = Button(self.frm_List, padx=5, text="اخراج", font=("Calibri", 11, "bold"),
                                                  command=lambda: self.person_Lists("اخراج"))
                self.btn_Exit_Class_info.place(x=400, y=250)

                self.btn_Exit_School_info = Button(self.frm_List, padx=5, text="فرار", font=("Calibri", 11, "bold"),
                                                   command=lambda: self.person_Lists("فرار"))
                self.btn_Exit_School_info.place(x=325, y=250)


            else:

                if hasattr(self, 'lbl_Lists_LastName'):
                    self.lbl_Lists_LastName.destroy()

                if hasattr(self, 'lbl_Lists_Name'):
                    self.lbl_Lists_Name.destroy()

                if hasattr(self, 'Select_person'):
                    self.Select_person.destroy()

                if hasattr(self, 'lbl_Type_person'):
                    self.lbl_Type_person.destroy()

                if hasattr(self, 'btn_hazer_info'):
                    self.btn_hazer_info.destroy()

                if hasattr(self, 'Times3'):
                    self.Times3.destroy()

                if hasattr(self, 'Lists_LastName'):
                    self.Lists_LastName.destroy()

                if hasattr(self, 'Lists_Name'):
                    self.Lists_Name.destroy()

                if hasattr(self, 'btn_Exit_School_info'):
                    self.btn_Exit_School_info.destroy()

                if hasattr(self, 'btn_Exit_Class_info'):
                    self.btn_Exit_Class_info.destroy()

                if hasattr(self, 'btn_Long_info'):
                    self.btn_Long_info.destroy()

                if hasattr(self, 'btn_ghayeb_info'):
                    self.btn_ghayeb_info.destroy()

                if hasattr(self, 'btn_Find_List'):
                    self.btn_Find_List.destroy()

                if hasattr(self, 'Times_2'):
                    self.Time_2.set("")
                    self.Times_2.destroy()

                if hasattr(self, 'lbl_Time_DayS'):
                    self.lbl_Time_DayS.destroy()

                if hasattr(self, 'lbl_Time_DayS1'):
                    self.lbl_Time_DayS1.destroy()

                if hasattr(self, 'lbl_Time_DayS2'):
                    self.lbl_Time_DayS2.destroy()

                if hasattr(self, 'lbl_Time_MonthS'):
                    self.lbl_Time_MonthS.destroy()

                if hasattr(self, 'lbl_Time_MonthS1'):
                    self.lbl_Time_MonthS1.destroy()

                if hasattr(self, 'lbl_Time_MonthS2'):
                    self.lbl_Time_MonthS2.destroy()

                if hasattr(self, 'lbl_Time_YearS'):
                    self.lbl_Time_YearS.destroy()

                if hasattr(self, 'lbl_Time_YearS1'):
                    self.lbl_Time_YearS1.destroy()

                if hasattr(self, 'lbl_Time_YearS2'):
                    self.lbl_Time_YearS2.destroy()

                if hasattr(self, 'time_daysS'):
                    self.time_daysS.destroy()

                if hasattr(self, 'time_daysS1'):
                    self.time_daysS1.destroy()

                if hasattr(self, 'time_daysS2'):
                    self.time_daysS2.destroy()

                if hasattr(self, 'time_monthsS'):
                    self.time_monthsS.destroy()

                if hasattr(self, 'time_monthsS1'):
                    self.time_monthsS1.destroy()

                if hasattr(self, 'time_monthsS2'):
                    self.time_monthsS2.destroy()

                if hasattr(self, 'time_yearsS'):
                    self.time_yearsS.destroy()

                if hasattr(self, 'time_yearsS1'):
                    self.time_yearsS1.destroy()

                if hasattr(self, 'time_yearsS2'):
                    self.time_yearsS2.destroy()

                if hasattr(self, 'lbl_azS'):
                    self.lbl_azS.destroy()

                if hasattr(self, 'lbl_taS'):
                    self.lbl_taS.destroy()

                if hasattr(self, 'hazer_list'):
                    self.Hazer_List.set("")
                    self.hazer_list.destroy()

                if hasattr(self, 'lbl_Lists'):
                    self.lbl_Lists.destroy()

                if hasattr(self, 'Times_2'):
                    Val = self.Time_2.get()
                    self.Times_2.destroy()

                if hasattr(self, 'lbl_Time'):
                    self.lbl_Time.destroy()

                if hasattr(self, 'Times'):
                    self.Time.set("")
                    self.Times.destroy()

                if hasattr(self, 'lbl_Time_Day'):
                    self.lbl_Time_Day.destroy()

                if hasattr(self, 'lbl_Time_Month'):
                    self.lbl_Time_Month.destroy()

                if hasattr(self, 'lbl_Time_Year'):
                    self.lbl_Time_Year.destroy()

                if hasattr(self, 'lbl_Time_Day_'):
                    self.lbl_Time_Day_.destroy()

                if hasattr(self, 'lbl_Time_Month_'):
                    self.lbl_Time_Month_.destroy()

                if hasattr(self, 'lbl_Time_Year_'):
                    self.lbl_Time_Year_.destroy()

                if hasattr(self, 'lbl_Time_Day_2'):
                    self.lbl_Time_Day_2.destroy()

                if hasattr(self, 'lbl_Time_Month_2'):
                    self.lbl_Time_Month_2.destroy()

                if hasattr(self, 'lbl_Time_Year_2'):
                    self.lbl_Time_Year_2.destroy()

                if hasattr(self, 'time_days'):
                    self.time_days.destroy()

                if hasattr(self, 'time_months'):
                    self.time_months.destroy()

                if hasattr(self, 'time_years'):
                    self.time_years.destroy()

                if hasattr(self, 'time_days_'):
                    self.time_days_.destroy()

                if hasattr(self, 'time_months_'):
                    self.time_months_.destroy()

                if hasattr(self, 'time_years_'):
                    self.time_years_.destroy()

                if hasattr(self, 'time_days_2'):
                    self.time_days_2.destroy()

                if hasattr(self, 'time_months_2'):
                    self.time_months_2.destroy()

                if hasattr(self, 'time_years_2'):
                    self.time_years_2.destroy()

                if hasattr(self, 'lbl_az'):
                    self.lbl_az.destroy()

                if hasattr(self, 'lbl_ta'):
                    self.lbl_ta.destroy()

                if hasattr(self, 'lbl_Time_2'):
                    self.lbl_Time_2.destroy()

                if hasattr(self, 'lbl_Select_Class'):
                    self.lbl_Select_Class.destroy()

                if hasattr(self, 'Classes'):
                    self.Classes.destroy()

                if hasattr(self, 'Classes_T'):
                    self.Classes_T.destroy()

                if hasattr(self, 'lbl_Select_Class_T'):
                    self.lbl_Select_Class_T.destroy()

                if hasattr(self, 'Classes_S'):
                    self.Classes_S.destroy()

                if hasattr(self, 'lbl_Select_Class_S'):
                    self.lbl_Select_Class_S.destroy()

                self.lbl_Time_2 = Label(self.frm_List,
                                        text="تاریخ",
                                        font=("Calibri", 12, "bold"))
                self.lbl_Time_2.place(x=525, y=150)

                self.Time_2 = StringVar()
                self.Times_2 = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Time_2,
                                            font=("Calibri", 12, "bold"), state="readonly")
                self.Times_2['values'] = (
                    '', 'تکی', 'بازه ای')
                self.Times_2.current(0)
                self.Times_2.place(x=450, y=150, width=75)
                self.Times_2.bind("<<ComboboxSelected>>", self.Select_Date)
                self.Time_2.set(Val)

                self.lbl_Select_Class_S = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                self.lbl_Select_Class_S.place(x=675, y=200)

                self.Class_S = StringVar()
                self.Classes_S = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class_S,
                                              font=("Calibri", 12, "bold"), state="readonly")
                self.Classes_S['values'] = (
                    'همه', '10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                    '12/1تربیت', '12/2تربیت')
                self.Classes_S.current(0)
                self.Classes_S.place(x=575, y=200, width=100)

                self.btn_Find_List = Button(self.frm_List, text="جستجو", font=("Calibri", 12, "bold"),
                                            command=self.Find_List)
                self.btn_Find_List.place(x=175, y=195)
        else:
            self.hasattr()

    def Select_hazer_list(self, event):
        Value = self.Hazer_List.get()
        Val = ""

        if Value != "":

            if True:
                if Value == "هنرجویان":
                    if hasattr(self, 'Times'):
                        self.Times.destroy()
                        if self.Time.get() != "":
                            if self.Time.get() == "بازه ای":
                                if hasattr(self, 'lbl_Select_Class'):
                                    self.lbl_Select_Class.destroy()

                                if hasattr(self, 'Classes'):
                                    self.Classes.destroy()

                                if hasattr(self, 'lbl_Select_Class_S'):
                                    self.lbl_Select_Class_S.destroy()

                                if hasattr(self, 'Classes_S'):
                                    self.Classes_S.destroy()
                                self.lbl_Select_Class = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                                self.lbl_Select_Class.place(x=250, y=150)

                                self.Class = StringVar()
                                self.Classes = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class,
                                                            font=("Calibri", 12, "bold"), state="readonly")
                                self.Classes['values'] = (
                                    'همه','10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                                    '12/1تربیت', '12/2تربیت')

                                self.Classes.current(0)
                                self.Classes.place(x=150, y=150, width=100)
                            else:
                                if hasattr(self, 'lbl_Select_Class'):
                                    self.lbl_Select_Class.destroy()

                                if hasattr(self, 'Classes'):
                                    self.Classes.destroy()

                                if hasattr(self, 'lbl_Select_Class_S'):
                                    self.lbl_Select_Class_S.destroy()

                                if hasattr(self, 'Classes_S'):
                                    self.Classes_S.destroy()
                                self.lbl_Select_Class_T = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                                self.lbl_Select_Class_T.place(x=675, y=200)

                                self.Class_T = StringVar()
                                self.Classes_T = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class_T,
                                                              font=("Calibri", 12, "bold"), state="readonly")
                                self.Classes_T['values'] = (
                                    'همه','10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                                    '12/1تربیت', '12/2تربیت')
                                self.Classes_T.current(0)
                                self.Classes_T.place(x=575, y=200, width=100)
                else:

                    if hasattr(self, 'lbl_Select_Class'):
                        self.lbl_Select_Class.destroy()

                    if hasattr(self, 'Classes'):
                        self.Classes.destroy()

                    if hasattr(self, 'Classes_T'):
                        self.Classes_T.destroy()

                    if hasattr(self, 'lbl_Select_Class_T'):
                        self.lbl_Select_Class_T.destroy()

                if hasattr(self, 'Times'):
                    Val = self.Time.get()
                    self.Times.destroy()

            if hasattr(self, 'lbl_Time'):
                self.lbl_Time.destroy()

            if hasattr(self, 'Times'):
                self.Times.destroy()

            self.lbl_Time = Label(self.frm_List,
                                  text="تاریخ",
                                  font=("Calibri", 12, "bold"))
            self.lbl_Time.place(x=375, y=150)

            self.Time = StringVar()
            self.Times = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Time,
                                      font=("Calibri", 12, "bold"), state="readonly")
            self.Times['values'] = (
                '', 'تکی', 'بازه ای')
            self.Times.current(0)
            self.Times.place(x=300, y=150, width=75)
            self.Times.bind("<<ComboboxSelected>>", self.Select_Date)
            self.Time.set(Val)

        else:
            if hasattr(self, 'lbl_Time'):
                self.lbl_Time.destroy()

            if hasattr(self, 'Times'):
                Val = self.Time.get()
                self.Time.set("")
                self.Times.destroy()

            if hasattr(self, 'lbl_Time_Day'):
                self.lbl_Time_Day.destroy()

            if hasattr(self, 'lbl_Time_Month'):
                self.lbl_Time_Month.destroy()

            if hasattr(self, 'lbl_Time_Year'):
                self.lbl_Time_Year.destroy()

            if hasattr(self, 'lbl_Time_Day_'):
                self.lbl_Time_Day_.destroy()

            if hasattr(self, 'lbl_Time_Month_'):
                self.lbl_Time_Month_.destroy()

            if hasattr(self, 'lbl_Time_Year_'):
                self.lbl_Time_Year_.destroy()

            if hasattr(self, 'lbl_Time_Day_2'):
                self.lbl_Time_Day_2.destroy()

            if hasattr(self, 'lbl_Time_Month_2'):
                self.lbl_Time_Month_2.destroy()

            if hasattr(self, 'lbl_Time_Year_2'):
                self.lbl_Time_Year_2.destroy()

            if hasattr(self, 'time_days'):
                self.time_days.destroy()

            if hasattr(self, 'time_months'):
                self.time_months.destroy()

            if hasattr(self, 'time_years'):
                self.time_years.destroy()

            if hasattr(self, 'time_days_'):
                self.time_days_.destroy()

            if hasattr(self, 'time_months_'):
                self.time_months_.destroy()

            if hasattr(self, 'time_years_'):
                self.time_years_.destroy()

            if hasattr(self, 'time_days_2'):
                self.time_days_2.destroy()

            if hasattr(self, 'time_months_2'):
                self.time_months_2.destroy()

            if hasattr(self, 'time_years_2'):
                self.time_years_2.destroy()

            if hasattr(self, 'lbl_az'):
                self.lbl_az.destroy()

            if hasattr(self, 'lbl_ta'):
                self.lbl_ta.destroy()

            if hasattr(self, 'Classes'):
                self.Classes.destroy()

            if hasattr(self, 'lbl_Select_Class'):
                self.lbl_Select_Class.destroy()

            if hasattr(self, 'Classes_T'):
                self.Class_T.set("")
                self.Classes_T.destroy()

            if hasattr(self, 'lbl_Select_Class_T'):
                self.lbl_Select_Class_T.destroy()

    def Select_Date(self, event):
        Value = ""
        Valuee = ""
        Vall = self.Info_Type.get()
        if hasattr(self, 'Times_2'):
            Valuee = self.Time_2.get()

        if hasattr(self, 'Times'):
            Value = self.Time.get()

        if hasattr(self, 'lbl_Time_Day'):
            self.lbl_Time_Day.destroy()

        if hasattr(self, 'lbl_Time_Day_'):
            self.lbl_Time_Day_.destroy()

        if hasattr(self, 'lbl_Time_DayS'):
            self.lbl_Time_DayS.destroy()

        if hasattr(self, 'lbl_Time_DayS1'):
            self.lbl_Time_DayS1.destroy()

        if hasattr(self, 'lbl_Time_DayS2'):
            self.lbl_Time_DayS2.destroy()

        if hasattr(self, 'lbl_Time_Day_2'):
            self.lbl_Time_Day_2.destroy()

        if hasattr(self, 'lbl_Time_Month'):
            self.lbl_Time_Month.destroy()

        if hasattr(self, 'lbl_Time_Month_'):
            self.lbl_Time_Month_.destroy()

        if hasattr(self, 'lbl_Time_MonthS'):
            self.lbl_Time_MonthS.destroy()

        if hasattr(self, 'lbl_Time_MonthS1'):
            self.lbl_Time_MonthS1.destroy()

        if hasattr(self, 'lbl_Time_MonthS2'):
            self.lbl_Time_MonthS2.destroy()

        if hasattr(self, 'lbl_Time_Month_2'):
            self.lbl_Time_Month_2.destroy()

        if hasattr(self, 'lbl_Time_Year'):
            self.lbl_Time_Year.destroy()

        if hasattr(self, 'lbl_Time_Year_'):
            self.lbl_Time_Year_.destroy()

        if hasattr(self, 'lbl_Time_YearS'):
            self.lbl_Time_YearS.destroy()

        if hasattr(self, 'lbl_Time_YearS1'):
            self.lbl_Time_YearS1.destroy()

        if hasattr(self, 'lbl_Time_YearS2'):
            self.lbl_Time_YearS2.destroy()

        if hasattr(self, 'lbl_Time_Year_2'):
            self.lbl_Time_Year_2.destroy()

        if hasattr(self, 'time_days'):
            self.time_days.destroy()

        if hasattr(self, 'time_months'):
            self.time_months.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'time_daysS'):
            self.time_daysS.destroy()

        if hasattr(self, 'time_daysS1'):
            self.time_daysS1.destroy()

        if hasattr(self, 'time_daysS2'):
            self.time_daysS2.destroy()

        if hasattr(self, 'time_monthsS'):
            self.time_monthsS.destroy()

        if hasattr(self, 'time_monthsS1'):
            self.time_monthsS1.destroy()

        if hasattr(self, 'time_monthsS2'):
            self.time_monthsS2.destroy()

        if hasattr(self, 'time_yearsS'):
            self.time_yearsS.destroy()

        if hasattr(self, 'time_yearsS1'):
            self.time_yearsS1.destroy()

        if hasattr(self, 'time_yearsS2'):
            self.time_yearsS2.destroy()

        if hasattr(self, 'lbl_az'):
            self.lbl_az.destroy()

        if hasattr(self, 'lbl_ta'):
            self.lbl_ta.destroy()

        if hasattr(self, 'lbl_azS'):
            self.lbl_azS.destroy()

        if hasattr(self, 'lbl_taS'):
            self.lbl_taS.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'time_days_'):
            self.time_days_.destroy()

        if hasattr(self, 'time_days_2'):
            self.time_days_2.destroy()

        if hasattr(self, 'time_months_'):
            self.time_months_.destroy()

        if hasattr(self, 'time_months_2'):
            self.time_months_2.destroy()

        if hasattr(self, 'time_years_'):
            self.time_years_.destroy()

        if hasattr(self, 'time_years_2'):
            self.time_years_2.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'lbl_Select_Class_T'):
            self.lbl_Select_Class_T.destroy()

        if hasattr(self, 'Classes_T'):
            self.Classes_T.destroy()

        if hasattr(self, 'lbl_Select_Class'):
            self.lbl_Select_Class.destroy()

        if hasattr(self, 'Classes'):
            self.Classes.destroy()


        if Value != "":
            if Value == "تکی":

                self.lbl_Time_Day = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                self.lbl_Time_Day.place(x=250, y=150)

                self.lbl_Time_Month = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                self.lbl_Time_Month.place(x=180, y=150)

                self.lbl_Time_Year = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                self.lbl_Time_Year.place(x=110, y=150)

                self.time_day = StringVar()
                self.time_days = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_day,
                                           font=("Calibri", 12, "bold"))
                self.time_days.place(x=220, y=150, width=30)

                self.time_month = StringVar()
                self.time_months = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_month,
                                             font=("Calibri", 12, "bold"))
                self.time_months.place(x=150, y=150, width=30)

                self.time_year = StringVar()
                self.time_years = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_year,
                                            font=("Calibri", 12, "bold"))
                self.time_years.place(x=70, y=150, width=40)
                if self.Hazer_List.get() == "هنرجویان":

                    self.lbl_Select_Class_T = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                    self.lbl_Select_Class_T.place(x=675, y=200)

                    self.Class_T = StringVar()
                    self.Classes_T = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class_T,
                                                  font=("Calibri", 12, "bold"), state="readonly")
                    self.Classes_T['values'] = (
                                    'همه','10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                                    '12/1تربیت', '12/2تربیت')
                    self.Classes_T.current(0)
                    self.Classes_T.place(x=575, y=200, width=100)

            else:
                if self.Hazer_List.get() == "هنرجویان":

                    self.lbl_Select_Class = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                    self.lbl_Select_Class.place(x=250, y=150)

                    self.Class = StringVar()
                    self.Classes = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class,
                                                font=("Calibri", 12, "bold"), state="readonly")
                    self.Classes['values'] = (
                                    'همه','10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                                    '12/1تربیت', '12/2تربیت')
                    self.Classes.current(0)
                    self.Classes.place(x=150, y=150, width=100)

                self.lbl_az = Label(self.frm_List, text="از", font=("Calibri", 12, "bold"))
                self.lbl_az.place(x=760, y=200)

                self.lbl_Time_Day_ = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                self.lbl_Time_Day_.place(x=710, y=200)

                self.lbl_Time_Month_ = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                self.lbl_Time_Month_.place(x=640, y=200)

                self.lbl_Time_Year_ = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                self.lbl_Time_Year_.place(x=570, y=200)

                self.time_day_ = StringVar()
                self.time_days_ = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_day_,
                                            font=("Calibri", 12, "bold"))
                self.time_days_.place(x=680, y=200, width=30)

                self.time_month_ = StringVar()
                self.time_months_ = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_month_,
                                              font=("Calibri", 12, "bold"))
                self.time_months_.place(x=610, y=200, width=30)

                self.time_year_ = StringVar()
                self.time_years_ = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_year_,
                                             font=("Calibri", 12, "bold"))
                self.time_years_.place(x=530, y=200, width=40)

                self.lbl_ta = Label(self.frm_List, text="تا", font=("Calibri", 12, "bold"))
                self.lbl_ta.place(x=490, y=200)

                self.lbl_Time_Day_2 = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                self.lbl_Time_Day_2.place(x=440, y=200)

                self.lbl_Time_Month_2 = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                self.lbl_Time_Month_2.place(x=370, y=200)

                self.lbl_Time_Year_2 = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                self.lbl_Time_Year_2.place(x=300, y=200)

                self.time_day_2 = StringVar()
                self.time_days_2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_day_2,
                                             font=("Calibri", 12, "bold"))
                self.time_days_2.place(x=410, y=200, width=30)

                self.time_month_2 = StringVar()
                self.time_months_2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_month_2,
                                               font=("Calibri", 12, "bold"))
                self.time_months_2.place(x=340, y=200, width=30)

                self.time_year_2 = StringVar()
                self.time_years_2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_year_2,
                                              font=("Calibri", 12, "bold"))
                self.time_years_2.place(x=260, y=200, width=40)


        if Vall != "":
            if Valuee != "":
                if Vall == "اخراج شده" or Vall == "فرار کرده":

                    if Valuee == "تکی":
                        self.lbl_Time_DayS = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                        self.lbl_Time_DayS.place(x=400, y=150)

                        self.lbl_Time_MonthS = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                        self.lbl_Time_MonthS.place(x=330, y=150)

                        self.lbl_Time_YearS = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                        self.lbl_Time_YearS.place(x=260, y=150)

                        self.time_dayS = StringVar()
                        self.time_daysS = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_dayS,
                                                    font=("Calibri", 12, "bold"))
                        self.time_daysS.place(x=370, y=150, width=30)

                        self.time_monthS = StringVar()
                        self.time_monthsS = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_monthS,
                                                      font=("Calibri", 12, "bold"))
                        self.time_monthsS.place(x=300, y=150, width=30)

                        self.time_yearS = StringVar()
                        self.time_yearsS = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_yearS,
                                                     font=("Calibri", 12, "bold"))
                        self.time_yearsS.place(x=220, y=150, width=40)

                        if hasattr(self, 'lbl_Select_Class_S'):
                            self.lbl_Select_Class_S.destroy()

                        if hasattr(self, 'Classes_S'):
                            self.Classes_S.destroy()

                        self.lbl_Select_Class_S = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                        self.lbl_Select_Class_S.place(x=675, y=200)

                        self.Class_S = StringVar()
                        self.Classes_S = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class_S,
                                                      font=("Calibri", 12, "bold"), state="readonly")
                        self.Classes_S['values'] = (
                            'همه', '10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                            '12/1تربیت', '12/2تربیت')
                        self.Classes_S.current(0)
                        self.Classes_S.place(x=575, y=200, width=100)

                    else:
                        self.lbl_azS = Label(self.frm_List, text="از", font=("Calibri", 12, "bold"))
                        self.lbl_azS.place(x=430, y=150)

                        self.lbl_Time_DayS1 = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                        self.lbl_Time_DayS1.place(x=400, y=150)

                        self.lbl_Time_MonthS1 = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                        self.lbl_Time_MonthS1.place(x=330, y=150)

                        self.lbl_Time_YearS1 = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                        self.lbl_Time_YearS1.place(x=260, y=150)

                        self.time_dayS1 = StringVar()
                        self.time_daysS1 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_dayS1,
                                                     font=("Calibri", 12, "bold"))
                        self.time_daysS1.place(x=370, y=150, width=30)

                        self.time_monthS1 = StringVar()
                        self.time_monthsS1 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_monthS1,
                                                       font=("Calibri", 12, "bold"))
                        self.time_monthsS1.place(x=300, y=150, width=30)

                        self.time_yearS1 = StringVar()
                        self.time_yearsS1 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_yearS1,
                                                      font=("Calibri", 12, "bold"))
                        self.time_yearsS1.place(x=220, y=150, width=40)

                        self.lbl_taS = Label(self.frm_List, text="تا", font=("Calibri", 12, "bold"))
                        self.lbl_taS.place(x=200, y=150)

                        self.lbl_Time_DayS2 = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                        self.lbl_Time_DayS2.place(x=170, y=150)

                        self.lbl_Time_MonthS2 = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                        self.lbl_Time_MonthS2.place(x=110, y=150)

                        self.lbl_Time_YearS2 = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                        self.lbl_Time_YearS2.place(x=50, y=150)

                        self.time_dayS2 = StringVar()
                        self.time_daysS2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_dayS2,
                                                     font=("Calibri", 12, "bold"))
                        self.time_daysS2.place(x=140, y=150, width=30)

                        self.time_monthS2 = StringVar()
                        self.time_monthsS2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_monthS2,
                                                       font=("Calibri", 12, "bold"))
                        self.time_monthsS2.place(x=80, y=150, width=30)

                        self.time_yearS2 = StringVar()
                        self.time_yearsS2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_yearS2,
                                                      font=("Calibri", 12, "bold"))
                        self.time_yearsS2.place(x=0, y=150, width=40)

                        if hasattr(self, 'lbl_Select_Class_S'):
                            self.lbl_Select_Class_S.destroy()

                        if hasattr(self, 'Classes_S'):
                            self.Classes_S.destroy()

                        self.lbl_Select_Class_S = Label(self.frm_List, text="کلاس", font=("Calibri", 12, "bold"))
                        self.lbl_Select_Class_S.place(x=675, y=200)

                        self.Class_S = StringVar()
                        self.Classes_S = ttk.Combobox(self.frm_List, justify="center", textvariable=self.Class_S,
                                                      font=("Calibri", 12, "bold"), state="readonly")
                        self.Classes_S['values'] = (
                            'همه', '10شبکه', '11شبکه', '12شبکه', '10/1تربیت', '10/2تربیت', '11/1تربیت', '11/2تربیت',
                            '12/1تربیت', '12/2تربیت')
                        self.Classes_S.current(0)
                        self.Classes_S.place(x=575, y=200, width=100)


    def Select_Date_person(self, event):

        if hasattr(self, 'lbl_Time_Day'):
            self.lbl_Time_Day.destroy()

        if hasattr(self, 'lbl_Time_Day_'):
            self.lbl_Time_Day_.destroy()

        if hasattr(self, 'lbl_Time_DayS'):
            self.lbl_Time_DayS.destroy()

        if hasattr(self, 'lbl_Time_DayS1'):
            self.lbl_Time_DayS1.destroy()

        if hasattr(self, 'lbl_Time_DayS2'):
            self.lbl_Time_DayS2.destroy()

        if hasattr(self, 'lbl_Time_Day_2'):
            self.lbl_Time_Day_2.destroy()

        if hasattr(self, 'lbl_Time_Month'):
            self.lbl_Time_Month.destroy()

        if hasattr(self, 'lbl_Time_Month_'):
            self.lbl_Time_Month_.destroy()

        if hasattr(self, 'lbl_Time_MonthS'):
            self.lbl_Time_MonthS.destroy()

        if hasattr(self, 'lbl_Time_MonthS1'):
            self.lbl_Time_MonthS1.destroy()

        if hasattr(self, 'lbl_Time_MonthS2'):
            self.lbl_Time_MonthS2.destroy()

        if hasattr(self, 'lbl_Time_Month_2'):
            self.lbl_Time_Month_2.destroy()

        if hasattr(self, 'lbl_Time_Year'):
            self.lbl_Time_Year.destroy()

        if hasattr(self, 'lbl_Time_Year_'):
            self.lbl_Time_Year_.destroy()

        if hasattr(self, 'lbl_Time_YearS'):
            self.lbl_Time_YearS.destroy()

        if hasattr(self, 'lbl_Time_YearS1'):
            self.lbl_Time_YearS1.destroy()

        if hasattr(self, 'lbl_Time_YearS2'):
            self.lbl_Time_YearS2.destroy()

        if hasattr(self, 'lbl_Time_Year_2'):
            self.lbl_Time_Year_2.destroy()

        if hasattr(self, 'time_days'):
            self.time_days.destroy()

        if hasattr(self, 'time_months'):
            self.time_months.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'time_daysS'):
            self.time_daysS.destroy()

        if hasattr(self, 'time_daysS1'):
            self.time_daysS1.destroy()

        if hasattr(self, 'time_daysS2'):
            self.time_daysS2.destroy()

        if hasattr(self, 'time_monthsS'):
            self.time_monthsS.destroy()

        if hasattr(self, 'time_monthsS1'):
            self.time_monthsS1.destroy()

        if hasattr(self, 'time_monthsS2'):
            self.time_monthsS2.destroy()

        if hasattr(self, 'time_yearsS'):
            self.time_yearsS.destroy()

        if hasattr(self, 'time_yearsS1'):
            self.time_yearsS1.destroy()

        if hasattr(self, 'time_yearsS2'):
            self.time_yearsS2.destroy()

        if hasattr(self, 'lbl_az'):
            self.lbl_az.destroy()

        if hasattr(self, 'lbl_ta'):
            self.lbl_ta.destroy()

        if hasattr(self, 'lbl_azS'):
            self.lbl_azS.destroy()

        if hasattr(self, 'lbl_taS'):
            self.lbl_taS.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'time_days_'):
            self.time_days_.destroy()

        if hasattr(self, 'time_days_2'):
            self.time_days_2.destroy()

        if hasattr(self, 'time_months_'):
            self.time_months_.destroy()

        if hasattr(self, 'time_months_2'):
            self.time_months_2.destroy()

        if hasattr(self, 'time_years_'):
            self.time_years_.destroy()

        if hasattr(self, 'time_years_2'):
            self.time_years_2.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        Value = self.Time3.get()

        if Value != "":
            if Value == "تکی":

                self.lbl_Time_Day = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                self.lbl_Time_Day.place(x=560, y=200)

                self.lbl_Time_Month = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                self.lbl_Time_Month.place(x=490, y=200)

                self.lbl_Time_Year = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                self.lbl_Time_Year.place(x=420, y=200)

                self.time_day = StringVar()
                self.time_days = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_day,
                                           font=("Calibri", 12, "bold"))
                self.time_days.place(x=530, y=200, width=30)

                self.time_month = StringVar()
                self.time_months = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_month,
                                             font=("Calibri", 12, "bold"))
                self.time_months.place(x=460, y=200, width=30)

                self.time_year = StringVar()
                self.time_years = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_year,
                                            font=("Calibri", 12, "bold"))
                self.time_years.place(x=380, y=200, width=40)

            else:
                self.lbl_az = Label(self.frm_List, text="از", font=("Calibri", 12, "bold"))
                self.lbl_az.place(x=560, y=200)

                self.lbl_Time_Day_ = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                self.lbl_Time_Day_.place(x=510, y=200)

                self.lbl_Time_Month_ = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                self.lbl_Time_Month_.place(x=440, y=200)

                self.lbl_Time_Year_ = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                self.lbl_Time_Year_.place(x=370, y=200)

                self.time_day_ = StringVar()
                self.time_days_ = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_day_,
                                            font=("Calibri", 12, "bold"))
                self.time_days_.place(x=480, y=200, width=30)

                self.time_month_ = StringVar()
                self.time_months_ = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_month_,
                                              font=("Calibri", 12, "bold"))
                self.time_months_.place(x=410, y=200, width=30)

                self.time_year_ = StringVar()
                self.time_years_ = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_year_,
                                             font=("Calibri", 12, "bold"))
                self.time_years_.place(x=330, y=200, width=40)

                self.lbl_ta = Label(self.frm_List, text="تا", font=("Calibri", 12, "bold"))
                self.lbl_ta.place(x=290, y=200)

                self.lbl_Time_Day_2 = Label(self.frm_List, text="روز", font=("Calibri", 12, "bold"))
                self.lbl_Time_Day_2.place(x=240, y=200)

                self.lbl_Time_Month_2 = Label(self.frm_List, text="ماه", font=("Calibri", 12, "bold"))
                self.lbl_Time_Month_2.place(x=170, y=200)

                self.lbl_Time_Year_2 = Label(self.frm_List, text="سال", font=("Calibri", 12, "bold"))
                self.lbl_Time_Year_2.place(x=100, y=200)

                self.time_day_2 = StringVar()
                self.time_days_2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_day_2,
                                             font=("Calibri", 12, "bold"))
                self.time_days_2.place(x=210, y=200, width=30)

                self.time_month_2 = StringVar()
                self.time_months_2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_month_2,
                                               font=("Calibri", 12, "bold"))
                self.time_months_2.place(x=140, y=200, width=30)

                self.time_year_2 = StringVar()
                self.time_years_2 = ttk.Entry(self.frm_List, justify="center", textvariable=self.time_year_2,
                                              font=("Calibri", 12, "bold"))
                self.time_years_2.place(x=60, y=200, width=40)


    def Select_persons(self, event):
        Value = self.Select_Type_person.get()
        if Value == "هنرآموز":

            if hasattr(self, 'btn_Exit_Class_info'):
                self.btn_Exit_Class_info.destroy()

            if hasattr(self, 'btn_Exit_School_info'):
                self.btn_Exit_School_info.destroy()

        else:
            self.btn_Exit_Class_info = Button(self.frm_List, padx=5, text="اخراج", font=("Calibri", 11, "bold"),
                                              command=lambda: self.person_Lists("اخراج"))
            self.btn_Exit_Class_info.place(x=400, y=250)

            self.btn_Exit_School_info = Button(self.frm_List, padx=5, text="فرار", font=("Calibri", 11, "bold"),
                                               command=lambda: self.person_Lists("فرار"))
            self.btn_Exit_School_info.place(x=325, y=250)


    def person_Lists(self, event):
        repository = Repository()
        Name = self.Get_Lists_Name.get()
        LastName = self.Get_Lists_LastName.get()
        Value = self.Select_Type_person.get()
        Time = self.Time3.get()
        res = True
        result = False
        R = False

        if Name == "":
            messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")

        elif LastName == "":
            messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")

        elif Time == "":
            messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")

        else:
            result = True

        if result:
            if event == "حاضر":
                if Value != "":
                    if Value == "هنرجو":
                        if Time == "تکی":
                            try:
                                Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                         int(self.time_day.get()))
                                R = True
                            except:
                                messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                            if R:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and res= 'حاضر'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")

                                self.Create_Table_personel_h_gh_t()
                                self.cleantable_Table_personel_h_gh_ts()

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])

                        if Time == "بازه ای":
                            r = True
                            result = request.baze_date(int(self.time_year_.get()),
                                                       int(self.time_month_.get()), int(self.time_day_.get()),
                                                       int(self.time_year_2.get()),
                                                       int(self.time_month_2.get()), int(self.time_day_2.get()))
                            for Date in result:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and res= 'حاضر'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                if r:
                                    self.Create_Table_personel_h_gh_t()
                                    self.cleantable_Table_personel_h_gh_ts()
                                    r = False

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                                res = False
                    else:
                        if Time == "تکی":
                            Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                     int(self.time_day.get()))
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Tch' and Date= '{Date}' and res= 'حاضر'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            self.Create_Table_personel_h_gh_t()
                            self.cleantable_Table_personel_h_gh_ts()

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                        else:
                            r = True
                            result = request.baze_date(int(self.time_year_.get()),
                                                       int(self.time_month_.get()), int(self.time_day_.get()),
                                                       int(self.time_year_2.get()),
                                                       int(self.time_month_2.get()), int(self.time_day_2.get()))
                            for Date in result:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Tch' and Date= '{Date}' and res= 'حاضر'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")

                                if r:
                                    self.Create_Table_personel_h_gh_t()
                                    self.cleantable_Table_personel_h_gh_ts()
                                    r = False

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                                res = False

            if event == "غایب":
                if Value != "":
                    if Value == "هنرجو":
                        if Time == "تکی":
                            try:
                                Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                         int(self.time_day.get()))
                                R = True
                            except:
                                messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                            if R:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and res= 'غایب'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                self.Create_Table_personel_h_gh_t()
                                self.cleantable_Table_personel_h_gh_ts()

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                        else:
                            r = True
                            result = request.baze_date(int(self.time_year_.get()),
                                                       int(self.time_month_.get()), int(self.time_day_.get()),
                                                       int(self.time_year_2.get()),
                                                       int(self.time_month_2.get()), int(self.time_day_2.get()))
                            for Date in result:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and res= 'غایب'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                if r:
                                    self.Create_Table_personel_h_gh_t()
                                    self.cleantable_Table_personel_h_gh_ts()
                                    r = False

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                                res = False
                    else:
                        if Time == "تکی":
                            try:
                                Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                         int(self.time_day.get()))
                            except:
                                messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Tch' and Date= '{Date}' and res= 'غایب'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            self.Create_Table_personel_h_gh_t()
                            self.cleantable_Table_personel_h_gh_ts()

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                        else:
                            r = True
                            result = request.baze_date(int(self.time_year_.get()),
                                                       int(self.time_month_.get()), int(self.time_day_.get()),
                                                       int(self.time_year_2.get()),
                                                       int(self.time_month_2.get()), int(self.time_day_2.get()))
                            for Date in result:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Tch' and Date= '{Date}' and res= 'غایب'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                if r:
                                    self.Create_Table_personel_h_gh_t()
                                    self.cleantable_Table_personel_h_gh_ts()
                                    r = False

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                                res = False

            if event == "تاخیر":
                if Value != "":
                    if Value == "هنرجو":
                        if Time == "تکی":
                            try:
                                Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                         int(self.time_day.get()))
                                R = True
                            except:
                                messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                            if R:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and Long= 'yes'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                self.Create_Table_personel_h_gh_t()
                                self.cleantable_Table_personel_h_gh_ts()
                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                        else:
                            r = True
                            result = request.baze_date(int(self.time_year_.get()),
                                                       int(self.time_month_.get()), int(self.time_day_.get()),
                                                       int(self.time_year_2.get()),
                                                       int(self.time_month_2.get()), int(self.time_day_2.get()))
                            for Date in result:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and Long= 'yes'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                if r:
                                    self.Create_Table_personel_h_gh_t()
                                    self.cleantable_Table_personel_h_gh_ts()
                                    r = False
                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                                res = False
                    else:
                        if Time == "تکی":
                            Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                     int(self.time_day.get()))
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Tch' and Date= '{Date}' and Long= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            self.Create_Table_personel_h_gh_t()
                            self.cleantable_Table_personel_h_gh_ts()

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                        else:
                            r = True
                            result = request.baze_date(int(self.time_year_.get()),
                                                       int(self.time_month_.get()), int(self.time_day_.get()),
                                                       int(self.time_year_2.get()),
                                                       int(self.time_month_2.get()), int(self.time_day_2.get()))
                            for Date in result:
                                where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Tch' and Date= '{Date}' and Long= 'yes'"
                                results = repository.Search("Presentation_" + Variable,
                                                            "[Name],[Family],[Date],[Zang]", where, "Family")
                                if r:
                                    self.Create_Table_personel_h_gh_t()
                                    self.cleantable_Table_personel_h_gh_ts()
                                    r = False

                                for item in results:
                                    self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                          values=[item[3], item[2],
                                                                                  item[1], item[0]])
                                res = False

            if event == "اخراج":
                if Value != "":
                    if Time == "تکی":
                        try:
                            Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                     int(self.time_day.get()))
                            R = True
                        except:
                            messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                        if R:
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and Exit_Class= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            self.Create_Table_personel_h_gh_t()
                            self.cleantable_Table_personel_h_gh_ts()

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                    else:
                        r = True
                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()), int(self.time_day_.get()),
                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()), int(self.time_day_2.get()))
                        for Date in result:
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and Exit_Class= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            if r:
                                self.Create_Table_personel_h_gh_t()
                                self.cleantable_Table_personel_h_gh_ts()
                                r = False

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                            res = False

            if event == "فرار":
                if Value != "":
                    if Time == "تکی":
                        try:
                            Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                     int(self.time_day.get()))
                            R = True
                        except:
                            messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                        if R:
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and Exit_School= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            self.Create_Table_personel_h_gh_t()
                            self.cleantable_Table_personel_h_gh_ts()

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                    else:
                        r = True
                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()), int(self.time_day_.get()),
                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()), int(self.time_day_2.get()))
                        for Date in result:
                            where = f" Name= '{Name}' and Family= '{LastName}' and Type= 'Std' and Date= '{Date}' and Exit_School= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang]", where, "Family")
                            if r:
                                self.Create_Table_personel_h_gh_t()
                                self.cleantable_Table_personel_h_gh_ts()
                                r = False

                            for item in results:
                                self.tbl_Lists_personel_h_gh_t.insert('', "end",
                                                                      values=[item[3], item[2],
                                                                              item[1], item[0]])
                            res = False


    def hasattr(self):
        if hasattr(self, 'btn_Find_List'):
            self.btn_Find_List.destroy()

        if hasattr(self, 'tbl_Lists_personel_h_gh_t'):
            self.tbl_Lists_personel_h_gh_t.destroy()

        if hasattr(self, 'lbl_Lists_LastName'):
            self.lbl_Lists_LastName.destroy()

        if hasattr(self, 'lbl_Lists_Name'):
            self.lbl_Lists_Name.destroy()

        if hasattr(self, 'Select_person'):
            self.Select_person.destroy()

        if hasattr(self, 'lbl_Type_person'):
            self.lbl_Type_person.destroy()

        if hasattr(self, 'btn_hazer_info'):
            self.btn_hazer_info.destroy()

        if hasattr(self, 'Times3'):
            self.Times3.destroy()

        if hasattr(self, 'Lists_LastName'):
            self.Lists_LastName.destroy()

        if hasattr(self, 'Lists_Name'):
            self.Lists_Name.destroy()

        if hasattr(self, 'btn_Exit_School_info'):
            self.btn_Exit_School_info.destroy()

        if hasattr(self, 'btn_Exit_Class_info'):
            self.btn_Exit_Class_info.destroy()

        if hasattr(self, 'btn_Long_info'):
            self.btn_Long_info.destroy()

        if hasattr(self, 'btn_ghayeb_info'):
            self.btn_ghayeb_info.destroy()

        if hasattr(self, 'lbl_Select_Class_S'):
            self.lbl_Select_Class_S.destroy()

        if hasattr(self, 'Classes_S'):
            self.Classes_S.destroy()

        if hasattr(self, 'lbl_Select_Class'):
            self.lbl_Select_Class.destroy()

        if hasattr(self, 'Classes_S'):
            self.Classes_S.destroy()

        if hasattr(self, 'tbl_Lists_hazer_ghiyab'):
            self.cleantable_Table_hazer_ghiyab()
            self.tbl_Lists_hazer_ghiyab.destroy()

        if hasattr(self, 'tbl_Lists_Long'):
            self.cleantable_Table_Long_Exit_Class()
            self.tbl_Lists_Long.destroy()

        if hasattr(self, 'Times_2'):
            self.Times_2.destroy()
            self.Time_2.set("")

        if hasattr(self, 'Times'):
            self.Time.set("")
            self.Times.destroy()

        if hasattr(self, 'lbl_Lists'):
            self.lbl_Lists.destroy()

        if hasattr(self, 'lbl_Time_2'):
            self.lbl_Time_2.destroy()

        if hasattr(self, 'lbl_Lists'):
            self.lbl_Lists.destroy()

        if hasattr(self, 'hazer_list'):
            self.Hazer_List.set("")
            self.hazer_list.destroy()

        if hasattr(self, 'lbl_Time'):
            self.lbl_Time.destroy()

        if hasattr(self, 'lbl_Time_2'):
            self.lbl_Time_2.destroy()

        if hasattr(self, 'lbl_Time_Day'):
            self.lbl_Time_Day.destroy()

        if hasattr(self, 'lbl_Time_Day_'):
            self.lbl_Time_Day_.destroy()

        if hasattr(self, 'lbl_Time_DayS'):
            self.lbl_Time_DayS.destroy()

        if hasattr(self, 'lbl_Time_DayS1'):
            self.lbl_Time_DayS1.destroy()

        if hasattr(self, 'lbl_Time_DayS2'):
            self.lbl_Time_DayS2.destroy()

        if hasattr(self, 'lbl_Time_Day_2'):
            self.lbl_Time_Day_2.destroy()

        if hasattr(self, 'lbl_Time_Month'):
            self.lbl_Time_Month.destroy()

        if hasattr(self, 'lbl_Time_Month_'):
            self.lbl_Time_Month_.destroy()

        if hasattr(self, 'lbl_Time_MonthS'):
            self.lbl_Time_MonthS.destroy()

        if hasattr(self, 'lbl_Time_MonthS1'):
            self.lbl_Time_MonthS1.destroy()

        if hasattr(self, 'lbl_Time_MonthS2'):
            self.lbl_Time_MonthS2.destroy()

        if hasattr(self, 'lbl_Time_Month_2'):
            self.lbl_Time_Month_2.destroy()

        if hasattr(self, 'lbl_Time_Year'):
            self.lbl_Time_Year.destroy()

        if hasattr(self, 'lbl_Time_Year_'):
            self.lbl_Time_Year_.destroy()

        if hasattr(self, 'lbl_Time_YearS'):
            self.lbl_Time_YearS.destroy()

        if hasattr(self, 'lbl_Time_YearS1'):
            self.lbl_Time_YearS1.destroy()

        if hasattr(self, 'lbl_Time_YearS2'):
            self.lbl_Time_YearS2.destroy()

        if hasattr(self, 'lbl_Time_Year_2'):
            self.lbl_Time_Year_2.destroy()

        if hasattr(self, 'time_days'):
            self.time_days.destroy()

        if hasattr(self, 'time_months'):
            self.time_months.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'time_daysS'):
            self.time_daysS.destroy()

        if hasattr(self, 'time_daysS1'):
            self.time_daysS1.destroy()

        if hasattr(self, 'time_daysS2'):
            self.time_daysS2.destroy()

        if hasattr(self, 'time_monthsS'):
            self.time_monthsS.destroy()

        if hasattr(self, 'time_monthsS1'):
            self.time_monthsS1.destroy()

        if hasattr(self, 'time_monthsS2'):
            self.time_monthsS2.destroy()

        if hasattr(self, 'time_yearsS'):
            self.time_yearsS.destroy()

        if hasattr(self, 'time_yearsS1'):
            self.time_yearsS1.destroy()

        if hasattr(self, 'time_yearsS2'):
            self.time_yearsS2.destroy()

        if hasattr(self, 'lbl_az'):
            self.lbl_az.destroy()

        if hasattr(self, 'lbl_ta'):
            self.lbl_ta.destroy()

        if hasattr(self, 'lbl_azS'):
            self.lbl_azS.destroy()

        if hasattr(self, 'lbl_taS'):
            self.lbl_taS.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'time_days_'):
            self.time_days_.destroy()

        if hasattr(self, 'time_days_2'):
            self.time_days_2.destroy()

        if hasattr(self, 'time_months_'):
            self.time_months_.destroy()

        if hasattr(self, 'time_months_2'):
            self.time_months_2.destroy()

        if hasattr(self, 'time_years_'):
            self.time_years_.destroy()

        if hasattr(self, 'time_years_2'):
            self.time_years_2.destroy()

        if hasattr(self, 'time_years'):
            self.time_years.destroy()

        if hasattr(self, 'Classes'):
            self.Class.set("")
            self.Classes.destroy()

        if hasattr(self, 'lbl_Select_Class'):
            self.lbl_Select_Class.destroy()

        if hasattr(self, 'Classes_T'):
            self.Class_T.set("")
            self.Classes_T.destroy()

        if hasattr(self, 'lbl_Select_Class_T'):
            self.lbl_Select_Class_T.destroy()

    def Find_List(self):
        info = self.Info_Type.get()
        result = False
        if info == "":
            messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
        else:
            if info == "حاضرین" or info == "غایبین" or info == "تاخیری":
                if self.Hazer_List.get() == "":
                    messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")

                elif self.Time.get() == "":
                    messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")

                elif self.Time.get() == "تکی":
                    if self.time_day.get() == "" or self.time_month.get() == "" or self.time_year.get() == "":
                        messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                    else:
                        result = True
                else:
                    if self.time_day_.get() == "" or self.time_month_.get() == "" or\
                        self.time_year_.get() == "" or self.time_day_2.get() == "" or\
                            self.time_month_2.get() == "" or self.time_year_2.get() == "":
                        messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                    else:
                        result = True
            else:
                if self.Time_2.get() == "":
                    messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")

                elif self.Time_2.get() == "تکی":
                    if self.time_dayS.get() == "" or self.time_monthS.get() == "" or self.time_yearS.get() == "":
                        messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                    else:
                        result = True
                else:
                    if self.time_dayS1.get() == "" or self.time_monthS1.get() == "" or \
                            self.time_yearS1.get() == "" or self.time_dayS2.get() == "" or \
                            self.time_monthS2.get() == "" or self.time_yearS2.get() == "":
                        messagebox.showerror("پر کردن", "لطفا اطلاعات را صحیح وارد کنید")
                    else:
                        result = True
        if result:
            repository = Repository()
            if info == "حاضرین":
                if self.Hazer_List.get() == "هنرآموزان":
                    if self.Time.get() == "تکی":
                        Date = request.find_date(int(self.time_year.get()),int(self.time_month.get()),
                                                 int(self.time_day.get()))

                        where = f" Type= 'Tch' and Date= '{Date}' and res= 'حاضر'"
                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[res],[Class]", where, "Family")
                        if results:
                            self.Create_Table_hazer_ghiyab()
                            self.cleantable_Table_hazer_ghiyab()
                        for item in results:
                            self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                               values=[item[5], item[4],
                                                                       item[3], item[2],
                                                                       item[1], item[0]])

                    elif self.Time.get() == "بازه ای":
                        res = True
                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()),int(self.time_day_.get()),

                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()),int(self.time_day_2.get()))
                        for Date in result:
                            where = f" Type= 'Tch' and Date= '{Date}' and res= 'حاضر'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[res],[Class]", where, "Family")
                            if res:
                                self.Create_Table_hazer_ghiyab()
                                self.cleantable_Table_hazer_ghiyab()
                            for item in results:
                                self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                                   values=[item[5],item[4],
                                                                           item[3], item[2],
                                                                           item[1], item[0]])
                            res = False
                elif self.Hazer_List.get() == "هنرجویان":
                    if self.Time.get() == "تکی":
                        Class = self.Class_T.get()
                        Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                 int(self.time_day.get()))
                        if Class == "همه":
                            where = f" Type= 'Std' and Date= '{Date}' and res= 'حاضر'"
                        else:
                            where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and res= 'حاضر'"


                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[res],[Class]",where, "Family")
                        if results:
                            self.Create_Table_hazer_ghiyab()
                            self.cleantable_Table_hazer_ghiyab()
                        for item in results:
                            self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                               values=[item[5], item[4],
                                                                       item[3], item[2],
                                                                       item[1], item[0]])

                    elif self.Time.get() == "بازه ای":
                        res = True
                        vaz = False
                        Class = self.Class.get()
                        if Class == "همه":
                            vaz = True

                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()),int(self.time_day_.get()),

                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()),int(self.time_day_2.get()))
                        for Date in result:
                            if vaz:
                                where = f" Type= 'Std' and Date= '{Date}' and res= 'حاضر'"
                            else:

                                where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and res= 'حاضر'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[res],[Class]", where, "Family")
                            if res:
                                self.Create_Table_hazer_ghiyab()
                                self.cleantable_Table_hazer_ghiyab()
                            for item in results:
                                self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                                   values=[item[5], item[4],
                                                                           item[3], item[2],
                                                                           item[1], item[0]])
                            res = False

            if info == "غایبین":
                if self.Hazer_List.get() == "هنرآموزان":
                    if self.Time.get() == "تکی":
                        Date = request.find_date(int(self.time_year.get()),int(self.time_month.get()),
                                                 int(self.time_day.get()))

                        where = f" Type= 'Tch' and Date= '{Date}' and res= 'غایب'"
                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[res],[Class]", where, "Family")
                        if results:
                            self.Create_Table_hazer_ghiyab()
                            self.cleantable_Table_hazer_ghiyab()
                        for item in results:
                            self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                               values=[item[5], item[4],
                                                                       item[3], item[2],
                                                                       item[1], item[0]])

                    elif self.Time.get() == "بازه ای":
                        res = True
                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()),int(self.time_day_.get()),

                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()),int(self.time_day_2.get()))
                        for Date in result:
                            where = f" Type= 'Tch' and Date= '{Date}' and res= 'غایب'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[res],[Class]", where, "Family")
                            if res:
                                self.Create_Table_hazer_ghiyab()
                                self.cleantable_Table_hazer_ghiyab()
                            for item in results:
                                self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                                   values=[item[5],item[4],
                                                                           item[3], item[2],
                                                                           item[1], item[0]])
                            res = False

                elif self.Hazer_List.get() == "هنرجویان":
                    if self.Time.get() == "تکی":
                        Class = self.Class_T.get()
                        Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                 int(self.time_day.get()))
                        if Class == "همه":
                            where = f" Type= 'Std' and Date= '{Date}' and res= 'غایب'"
                        else:
                            where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and res= 'غایب'"


                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[res],[Class]",where, "Family")
                        if results:
                            self.Create_Table_hazer_ghiyab()
                            self.cleantable_Table_hazer_ghiyab()
                        for item in results:
                            self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                               values=[item[5], item[4],
                                                                       item[3], item[2],
                                                                       item[1], item[0]])

                    elif self.Time.get() == "بازه ای":
                        res = True
                        vaz = False
                        Class = self.Class.get()
                        if Class == "همه":
                            vaz = True

                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()),int(self.time_day_.get()),

                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()),int(self.time_day_2.get()))
                        for Date in result:
                            if vaz:
                                where = f" Type= 'Std' and Date= '{Date}' and res= 'غایب'"
                            else:

                                where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and res= 'غایب'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[res],[Class]", where, "Family")
                            if res:
                                self.Create_Table_hazer_ghiyab()
                                self.cleantable_Table_hazer_ghiyab()
                            for item in results:
                                self.tbl_Lists_hazer_ghiyab.insert('', "end",
                                                                   values=[item[5], item[4],
                                                                           item[3], item[2],
                                                                           item[1], item[0]])
                            res = False

            if info == "تاخیری":
                if self.Hazer_List.get() == "هنرآموزان":
                    if self.Time.get() == "تکی":
                        Date = request.find_date(int(self.time_year.get()),int(self.time_month.get()),
                                                 int(self.time_day.get()))

                        where = f" Type= 'Tch' and Date= '{Date}' and Long= 'yes'"
                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[Class]", where, "Family")
                        if results:
                            self.Create_Table_Long_Exit_Class()
                            self.cleantable_Table_Long_Exit_Class()
                        for item in results:
                            self.tbl_Lists_Long.insert('', "end",
                                                       values=[item[4],
                                                               item[3], item[2],
                                                               item[1], item[0]])

                    elif self.Time.get() == "بازه ای":
                        res = True
                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()),int(self.time_day_.get()),

                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()),int(self.time_day_2.get()))
                        for Date in result:
                            where = f" Type= 'Tch' and Date= '{Date}' and Long= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[Class]", where, "Family")
                            if res:
                                self.Create_Table_Long_Exit_Class()
                                self.cleantable_Table_Long_Exit_Class()
                            for item in results:
                                self.tbl_Lists_Long.insert('', "end",
                                                           values=[item[4],
                                                                   item[3], item[2],
                                                                   item[1], item[0]])
                            res = False
                elif self.Hazer_List.get() == "هنرجویان":
                    if self.Time.get() == "تکی":
                        Class = self.Class_T.get()
                        Date = request.find_date(int(self.time_year.get()), int(self.time_month.get()),
                                                 int(self.time_day.get()))
                        if Class == "همه":
                            where = f" Type= 'Std' and Date= '{Date}' and Long= 'yes'"
                        else:
                            where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and Long= 'yes'"


                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[Class]",where, "Family")
                        if results:
                            self.Create_Table_Long_Exit_Class()
                            self.cleantable_Table_Long_Exit_Class()
                        for item in results:
                            self.tbl_Lists_Long.insert('', "end",
                                                       values=[item[4],
                                                               item[3], item[2],
                                                               item[1], item[0]])

                    elif self.Time.get() == "بازه ای":
                        res = True
                        vaz = False
                        Class = self.Class.get()
                        if Class == "همه":
                            vaz = True

                        result = request.baze_date(int(self.time_year_.get()),
                                                   int(self.time_month_.get()),int(self.time_day_.get()),

                                                   int(self.time_year_2.get()),
                                                   int(self.time_month_2.get()),int(self.time_day_2.get()))
                        for Date in result:
                            if vaz:
                                where = f" Type= 'Std' and Date= '{Date}' and Long= 'yes'"
                            else:

                                where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and Long= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[Class]", where, "Family")
                            if res:
                                self.Create_Table_Long_Exit_Class()
                                self.cleantable_Table_Long_Exit_Class()
                            for item in results:
                                self.tbl_Lists_Long.insert('', "end",
                                                           values=[item[4],
                                                                   item[3], item[2],
                                                                   item[1], item[0]])
                            res = False

            if info == "اخراج شده":
                    if self.Time_2.get() == "تکی":
                        Class = self.Class_S.get()
                        Date = request.find_date(int(self.time_yearS.get()), int(self.time_monthS.get()),
                                                 int(self.time_dayS.get()))
                        if Class == "همه":
                            where = f" Type= 'Std' and Date= '{Date}' and Exit_Class= 'yes'"
                        else:
                            where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and Exit_Class= 'yes'"


                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[Class]",where, "Family")
                        if results:
                            self.Create_Table_Long_Exit_Class()
                            self.cleantable_Table_Long_Exit_Class()
                        for item in results:
                            self.tbl_Lists_Long.insert('', "end",
                                                       values=[item[4],
                                                               item[3], item[2],
                                                               item[1], item[0]])

                    elif self.Time_2.get() == "بازه ای":
                        res = True
                        vaz = False
                        Class = self.Class_S.get()
                        if Class == "همه":
                            vaz = True

                        result = request.baze_date(int(self.time_yearS1.get()),
                                                   int(self.time_monthS1.get()),int(self.time_dayS1.get()),

                                                   int(self.time_yearS2.get()),
                                                   int(self.time_monthS2.get()),int(self.time_dayS2.get()))
                        for Date in result:
                            if vaz:
                                where = f" Type= 'Std' and Date= '{Date}' and Exit_Class= 'yes'"
                            else:

                                where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and Exit_Class= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[Class]", where, "Family")
                            if res:
                                self.Create_Table_Long_Exit_Class()
                                self.cleantable_Table_Long_Exit_Class()
                            for item in results:
                                self.tbl_Lists_Long.insert('', "end",
                                                           values=[item[4],
                                                                   item[3], item[2],
                                                                   item[1], item[0]])
                            res = False

            if info == "فرار کرده":
                    if self.Time_2.get() == "تکی":
                        Class = self.Class_S.get()
                        Date = request.find_date(int(self.time_yearS.get()), int(self.time_monthS.get()),
                                                 int(self.time_dayS.get()))
                        if Class == "همه":
                            where = f" Type= 'Std' and Date= '{Date}' and Exit_School= 'yes'"
                        else:
                            where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and Exit_School= 'yes'"


                        results = repository.Search("Presentation_" + Variable, "[Name],[Family],[Date],[Zang],[Class]",where, "Family")
                        if results:
                            self.Create_Table_Long_Exit_Class()
                            self.cleantable_Table_Long_Exit_Class()
                        for item in results:
                            self.tbl_Lists_Long.insert('', "end",
                                                       values=[item[4],
                                                               item[3], item[2],
                                                               item[1], item[0]])

                    elif self.Time_2.get() == "بازه ای":
                        res = True
                        vaz = False
                        Class = self.Class_S.get()
                        if Class == "همه":
                            vaz = True

                        result = request.baze_date(int(self.time_yearS1.get()),
                                                   int(self.time_monthS1.get()),int(self.time_dayS1.get()),

                                                   int(self.time_yearS2.get()),
                                                   int(self.time_monthS2.get()),int(self.time_dayS2.get()))
                        for Date in result:
                            if vaz:
                                where = f" Type= 'Std' and Date= '{Date}' and Exit_School= 'yes'"
                            else:

                                where = f" Class= '{Class}' and Type= 'Std' and Date= '{Date}' and Exit_School= 'yes'"
                            results = repository.Search("Presentation_" + Variable,
                                                        "[Name],[Family],[Date],[Zang],[Class]", where, "Family")
                            if res:
                                self.Create_Table_Long_Exit_Class()
                                self.cleantable_Table_Long_Exit_Class()
                            for item in results:
                                self.tbl_Lists_Long.insert('', "end",
                                                           values=[item[4],
                                                                   item[3], item[2],
                                                                   item[1], item[0]])
                            res = False


    def SURE(self):
        repository = Repository()
        List = []
        result = messagebox.askyesno("اطمینان","آیا از فرستادن sms اطمینان دارید")
        if result:
            for child in self.tbl_hosh.get_children():
                where = f" Name='{self.tbl_hosh.item(child)['values'][5]}'" \
                        f"and Family= '{self.tbl_hosh.item(child)['values'][4]}'"
                result = repository.Search("Student_" + Variable, "[mobile_dad],[mobile_mother]", where, "Family")
                for item in result:
                    List.append(item)
            Phone_List = [item for tuple in List for item in tuple]
            for item in Phone_List:
                if item != "-":
                    print(item)

    def Create_Table_hazer_ghiyab(self):
        if hasattr(self, 'tbl_Lists_hazer_ghiyab'):
            self.tbl_Lists_hazer_ghiyab.destroy()

        self.col_Lists_hazer_ghiyab = ("c1", "c2", "c3", "c4", "c5", "c6")
        self.tbl_Lists_hazer_ghiyab = ttk.Treeview(self.frm_List, columns=self.col_Lists_hazer_ghiyab, show="headings", height=16)

        self.tbl_Lists_hazer_ghiyab.column("# 6", anchor=N, width=90, minwidth=90, stretch=tkinter.YES)
        self.tbl_Lists_hazer_ghiyab.heading("# 6", anchor=N, text="نام")

        self.tbl_Lists_hazer_ghiyab.column("# 5", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_Lists_hazer_ghiyab.heading("# 5", anchor=N, text="نام خانوادگی")

        self.tbl_Lists_hazer_ghiyab.column("# 4", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_Lists_hazer_ghiyab.heading("# 4", anchor=N, text="تاریخ")

        self.tbl_Lists_hazer_ghiyab.column("# 3", anchor=N, width=80, minwidth=80, stretch=tkinter.YES)
        self.tbl_Lists_hazer_ghiyab.heading("# 3", anchor=N, text="زنگ")

        self.tbl_Lists_hazer_ghiyab.column("# 2", anchor=N, width=60, minwidth=60, stretch=tkinter.YES)
        self.tbl_Lists_hazer_ghiyab.heading("# 2", anchor=N, text="وضعیت")

        self.tbl_Lists_hazer_ghiyab.column("# 1", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_Lists_hazer_ghiyab.heading("# 1", anchor=N, text="کلاس")

        self.tbl_Lists_hazer_ghiyab.place(x=115, y=240)

    def cleantable_Table_hazer_ghiyab(self):
        try:
            for item in self.tbl_Lists_hazer_ghiyab.get_children():
                self.sel = (str(item))
                self.tbl_Lists_hazer_ghiyab.delete(self.sel)
        except:
            pass



    def Create_Table_Long_Exit_Class(self):
        if hasattr(self, 'tbl_Lists_Long'):
            self.tbl_Lists_Long.destroy()

        self.col_Lists_Long = ("c1", "c2", "c3", "c4", "c5")
        self.tbl_Lists_Long = ttk.Treeview(self.frm_List, columns=self.col_Lists_Long, show="headings", height=16)

        self.tbl_Lists_Long.column("# 5", anchor=N, width=90, minwidth=90, stretch=tkinter.YES)
        self.tbl_Lists_Long.heading("# 5", anchor=N, text="نام")

        self.tbl_Lists_Long.column("# 4", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_Lists_Long.heading("# 4", anchor=N, text="نام خانوادگی")

        self.tbl_Lists_Long.column("# 3", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_Lists_Long.heading("# 3", anchor=N, text="تاریخ")

        self.tbl_Lists_Long.column("# 2", anchor=N, width=80, minwidth=80, stretch=tkinter.YES)
        self.tbl_Lists_Long.heading("# 2", anchor=N, text="زنگ")

        self.tbl_Lists_Long.column("# 1", anchor=N, width=100, minwidth=100, stretch=tkinter.YES)
        self.tbl_Lists_Long.heading("# 1", anchor=N, text="کلاس")

        self.tbl_Lists_Long.place(x=150, y=240)

    def cleantable_Table_Long_Exit_Class(self):
        try:
            for item in self.tbl_Lists_Long.get_children():
                self.sel = (str(item))
                self.tbl_Lists_Long.delete(self.sel)
        except:
            pass


    def Create_Table_personel_h_gh_t(self):
        if hasattr(self, 'tbl_Lists_personel_h_gh_t'):
            self.tbl_Lists_personel_h_gh_t.destroy()

        self.col_Lists_personel_h_gh_t = ("c1", "c2", "c3", "c4")
        self.tbl_Lists_personel_h_gh_t = ttk.Treeview(self.frm_List, columns=self.col_Lists_personel_h_gh_t, show="headings", height=12)

        self.tbl_Lists_personel_h_gh_t.column("# 4", anchor=N, width=90, minwidth=90, stretch=tkinter.YES)
        self.tbl_Lists_personel_h_gh_t.heading("# 4", anchor=N, text="نام")

        self.tbl_Lists_personel_h_gh_t.column("# 3", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_Lists_personel_h_gh_t.heading("# 3", anchor=N, text="نام خانوادگی")

        self.tbl_Lists_personel_h_gh_t.column("# 2", anchor=N, width=120, minwidth=120, stretch=tkinter.YES)
        self.tbl_Lists_personel_h_gh_t.heading("# 2", anchor=N, text="تاریخ")

        self.tbl_Lists_personel_h_gh_t.column("# 1", anchor=N, width=80, minwidth=80, stretch=tkinter.YES)
        self.tbl_Lists_personel_h_gh_t.heading("# 1", anchor=N, text="زنگ")

        self.tbl_Lists_personel_h_gh_t.place(x=200, y=325)

    def cleantable_Table_personel_h_gh_ts(self):
        try:
            for item in self.tbl_Lists_personel_h_gh_t.get_children():
                self.sel = (str(item))
                self.tbl_Lists_personel_h_gh_t.delete(self.sel)
        except:
            pass