from tkinter import*
import math,random,os
import tempfile
from tkinter import messagebox
class bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry('500x500')
        self.root.minsize(500,400)
        self.root.title("Billing Software")
        bg_color="black"
        title=Label(self.root,text="Billing Software",border=13,relief=GROOVE,bg=bg_color,fg="red",

                    font=("times new roman",30,"bold"),pady=2,).pack(fill=X)
        # variable
        #cosmetic
        self.shop=IntVar()
        self.face=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        # Glocery
        self.rice = IntVar()
        self.oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # cool drink
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        # Total Product Price & Tax
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()
        # Customer
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.c_bill_no.set(str(x))
        self.c_search_bill=StringVar()
        #customer Details...
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),
                      fg="gold",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(f1,text="Customer Name:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(f1,width=10,textvariable=self.c_name,font="arial 15",bd=7,relief=GROOVE).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl = Label(f1, text="Customer Email ID:", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(f1, width=10,textvariable=self.c_phone, font="arial 15", bd=7, relief=GROOVE).grid(row=0, column=3, padx=10, pady=5)


        c_bill_lbl = Label(f1, text="Bill Number:", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(f1, width=10,textvariable=self.c_search_bill,font="arial 15", bd=7, relief=GROOVE).grid(row=0, column=5, padx=10, pady=5)
        bill_btn=Button(f1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        # cosmetics

        f2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f2.place(x=5,y=170,width=300,height=400)
        bath_lbl=Label(f2,text="Bath Shop",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(f2,width=10,textvariable=self.shop,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_cream=Label(f2,text="Face Cream",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(f2,width=10,textvariable=self.face,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(f2,text="Face Wash",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl=Label(f2,text="Hair Spray",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(f2,width=10,textvariable=self.spray,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(f2,text="Hair Gell",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(f2,width=10,textvariable=self.gell,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(f2,text="Body Loshan",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(f2,width=10,textvariable=self.loshan,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        # Grocery

        f3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        f3.place(x=340, y=170, width=300, height=400)
        rice_lbl = Label(f3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(
            row=0, column=0, padx=10, pady=10, sticky="w")
        rice_txt = Entry(f3, width=10,textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                       padx=10, pady=10)

        food_lbl = Label(f3, text="Food Oil ", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        food_txt = Entry(f3, width=10,textvariable=self.oil, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=10)

        daal_lbl = Label(f3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        daal_txt = Entry(f3, width=10,textvariable=self.daal, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        wheat_lbl = Label(f3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        wheat_txt = Entry(f3, width=10,textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        sugar_lbl = Label(f3, text="Sugar", font=("times new roman", 16, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sugar_txt = Entry(f3, width=10,textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=10)

        tea_lbl = Label(f3, text="Tea", font=("times new roman", 16, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        tea_txt = Entry(f3, width=10,textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)

        # cold Dirink

        f4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f4.place(x=670,y=180,width=300,height=400)
        maza_lbl=Label(f4,text="Maza",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(f4,width=10,textvariable=self.maza,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cock_lbl=Label(f4,text="Coco Cola",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cock_txt=Entry(f4,width=10,textvariable=self.cock,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frooti_lbl=Label(f4,text="Frooti",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(f4,width=10,textvariable=self.frooti,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        tump_lbl=Label(f4,text="Thumbs Up",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tump_txt=Entry(f4,width=10,textvariable=self.thumbup,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        limca_lbl=Label(f4,text="Limca",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(f4,width=10,textvariable=self.limca,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite_lbl=Label(f4,text="Sprite",font=("times new roman", 16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(f4,width=10,textvariable=self.sprite,font=("times new roman" ,16, "bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         # BillArea
        f5 =LabelFrame(self.root, bd=10, relief=GROOVE)
        f5.place(x=1000, y=180, width=340, height=400)
        bill_title=Label(f5,text="=========Bill Area==========",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill='x')
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scrol_y)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Button
        f6 = LabelFrame(self.root, bd=10, relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="red",bg=bg_color)
        f6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(f6,text="Total Cosmetic Price:",bg=bg_color,fg="orange",font=("times new roman",14,"bold")).grid(row=0,column=0,sticky="w")
        m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=GROOVE).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(f6, text="Total Grocery Price:", bg=bg_color, fg="orange",
                       font=("times new roman", 14, "bold")).grid(row=1, column=0, sticky="w")
        m2_txt = Entry(f6, width=18,textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=1, column=1, padx=10, pady=1)

        m3_lbl = Label(f6, text="Total Cool Drink Price:", bg=bg_color, fg="orange",
                       font=("times new roman", 14, "bold")).grid(row=2, column=0, sticky="w")
        m3_txt = Entry(f6, width=18,textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=GROOVE).grid(row=2, column=1, padx=10, pady=1)

        c1_lbl = Label(f6, text="Cosmetic GST:", bg=bg_color, fg="orange",
                       font=("times new roman", 14, "bold")).grid(row=0, column=2, sticky="w")
        c1_txt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.cosmetic_tax, bd=7, relief=GROOVE).grid(row=0, column=3, padx=10, pady=1)

        c2_lbl = Label(f6, text="Grocery GST:", bg=bg_color, fg="orange",
                       font=("times new roman", 14, "bold")).grid(row=1, column=2, sticky="w")
        c2_txt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.grocery_tax,bd=7, relief=GROOVE).grid(row=1, column=3, padx=10, pady=1)

        c3_lbl = Label(f6, text="Cool Drink GST:", bg=bg_color, fg="orange",
                       font=("times new roman", 14, "bold")).grid(row=2, column=2, sticky="w")
        c3_txt = Entry(f6, width=18, font="arial 10 bold",textvariable=self.cold_drink_tax, bd=7, relief=GROOVE).grid(row=2, column=3, padx=10, pady=1)
        btn_f=Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=740,width=580,height=100)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="green",fg="white",bd=5,pady=10,width=7,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,text="Genrate Bill",command=self.bill_area,bg="green",fg="white",bd=5,pady=10,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_s,bg="green",fg="white",bd=5,pady=10,width=5,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_f,text="Exit",command=self.Exit_s,bg="green",fg="white",bd=5,pady=10,width=5,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        prit_btn=Button(btn_f,text="Print Now",command=self.print_now,bg="green",fg="white",bd=5,pady=10,width=7,font="arial 15 bold").grid(row=0,column=4,padx=5,pady=5)
        self.welcome_bill()
     # Cosmetic Product
    def total(self):
        self.cos_shop_price=self.shop.get()*10
        self.cos_face_price=self.face.get()*60
        self.cos_wash_price=self.face_wash.get()*50
        self.cos_spray_price=self.spray.get()*150
        self.cos_gell_price=self.gell.get()*50
        self.cos_loshan_price=self.loshan.get()*80
        self.total_cosmetic_price=float(
                                self.cos_shop_price+
                                self.cos_face_price+
                                self.cos_wash_price+
                                self.cos_spray_price+
                                self.cos_gell_price+
                                self.cos_loshan_price

                                  )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.cosm_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.cosm_tax))
       # Grocery Product
        self.gro_rice_price = self.rice.get() * 50
        self.gro_oil_price = self.oil.get() * 100
        self.gro_daal_price = self.daal.get() * 80
        self.gro_wheat_price = self.wheat.get() *20
        self.gro_sugar_price = self.sugar.get() * 35
        self.gro_tea_price = self.tea.get() * 100
        self.total_grocery_price = float(
                                    self.gro_rice_price +
                                    self.gro_oil_price +
                                    self.gro_daal_price +
                                    self.gro_wheat_price +
                                    self.gro_sugar_price +
                                    self.gro_tea_price
                                   )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.grs_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs." + str(self.grs_tax))

        # cold_Drink
        self.cold_maza_price = self.maza.get() *20
        self.cold_cock_price = self.cock.get() * 20
        self.cold_frooti_price = self.frooti.get() *20
        self.cold_thumb_price = self.thumbup.get() * 20
        self.cold_limca_price = self.limca.get() *20
        self.cold_sprite_price = self.sprite.get() *20
        self.total_cold_price = float(
                                self.cold_maza_price +
                                self.cold_cock_price +
                                self.cold_frooti_price +
                                self.cold_thumb_price +
                                self.cold_limca_price +
                                self.cold_sprite_price
                                  )
        self.cold_drink_price.set("Rs."+str(self.total_cold_price))
        self.cold_tax = round((self.total_cold_price * 0.05), 2)
        self.cold_drink_tax.set("Rs." + str(self.cold_tax))



        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_price+
                              self.cosm_tax+
                              self.grs_tax+
                              self.cold_tax
                              )
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"This is E-Generated Bill :\n")
        self.textarea.insert(END,f"\nBill Number:{self.c_bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\nE-Mail ID:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n=====================================")
        self.textarea.insert(END,f"\nProduct\t\t Quantity\t\tPrice")
        self.textarea.insert(END,f"\n=====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer Details Are Must")
        elif self.cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.cold_drink_price.get()=="Rs.0.0":
            messagebox.showerror("Error", "No Product Selected")
        else:
            self.welcome_bill()
            #cosmetic
            if self.shop.get()!=0:
               self.textarea.insert(END,f"\nBath Shop:\t\t{self.shop.get()}\t\t{self.cos_shop_price}")
            if self.face.get()!=0:
               self.textarea.insert(END,f"\nFace Cream:\t\t{self.face.get()}\t\t{self.cos_face_price}")
            if self.face_wash.get() != 0:
               self.textarea.insert(END, f"\nFace Wash:\t\t{self.face_wash.get()}\t\t{self.cos_wash_price}")
            if self.spray.get() != 0:
               self.textarea.insert(END, f"\nHair Spray:\t\t{self.spray.get()}\t\t{self.cos_spray_price}")
            if self.gell.get() != 0:
               self.textarea.insert(END, f"\nHair Gell:\t\t{self.gell.get()}\t\t{self.cos_gell_price}")
            if self.loshan.get() != 0:
               self.textarea.insert(END, f"\nBody Loshan:\t\t{self.loshan.get()}\t\t{self.cos_loshan_price}")
    #       #grocery
            if self.rice.get() != 0:
                    self.textarea.insert(END,f"\nRice:\t\t{self.rice.get()}\t\t{self.gro_rice_price}")
            if self.oil.get() != 0:
                    self.textarea.insert(END, f"\nFood Oli:\t\t{self.oil.get()}\t\t{self.gro_oil_price}")
            if self.daal.get() != 0:
                    self.textarea.insert(END, f"\nDaal:\t\t{self.daal.get()}\t\t{self.gro_daal_price}")
            if self.wheat.get() != 0:
                    self.textarea.insert(END, f"\nWheat:\t\t{self.wheat.get()}\t\t{self.gro_wheat_price}")
            if self.sugar.get() != 0:
                    self.textarea.insert(END, f"\nSugar:\t\t{self.sugar.get()}\t\t{self.gro_sugar_price}")
            if self.tea.get() != 0:
                    self.textarea.insert(END, f"\nTea:\t\t{self.tea.get()}\t\t{self.gro_tea_price}")

            # Cold Drinks
            if self.maza.get() != 0:
                self.textarea.insert(END, f"\nMaza:\t\t{self.maza.get()}\t\t{self.cold_maza_price}")
            if self.cock.get() != 0:
                self.textarea.insert(END, f"\nCoco Cola:\t\t{self.cock.get()}\t\t{self.cold_cock_price}")
            if self.frooti.get() != 0:
                self.textarea.insert(END, f"\nFrooti:\t\t{self.frooti.get()}\t\t{self.cold_frooti_price}")
            if self.thumbup.get() != 0:
                self.textarea.insert(END, f"\nThumbsup:\t\t{self.thumbup.get()}\t\t{self.cold_thumb_price}")
            if self.limca.get() != 0:
                self.textarea.insert(END, f"\nLimca:\t\t{self.limca.get()}\t\t{self.cold_limca_price}")
            if self.sprite.get() != 0:

                self.textarea.insert(END, f"\nSprite:\t\t{self.sprite.get()}\t\t{self.cold_sprite_price}")

            self.textarea.insert(END, f"\n=====================================")
            if self.cosmetic_tax.get()!="Rs.0.0":
               self.textarea.insert(END, f"\nGST Tax:\t\t\t{self.cosmetic_tax.get()}")
            self.textarea.insert(END, f"\n-------------------------------------")
            if self.grocery_tax.get()!="Rs.0.0":
               self.textarea.insert(END, f"\nGST Tax:\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Rs.0.0":
               self.textarea.insert(END, f"\nGST Tax:\t\t\t{self.cold_drink_tax.get()}")
               self.textarea.insert(END, f"\n-------------------------------------")
            self.textarea.insert(END, f"\nTotal Bill:\t\t\tRs.{self.Total_bill}")

            self.textarea.insert(END, f"\n-------------------------------------")
            self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do Want Save Bill")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("C:\MyBill/"+str(self.c_bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            
            messagebox.showinfo("Saved",f"Bill Number:{self.c_bill_no.get()} Your Bill Saved Sucessfuly...")
            import smtplib, ssl

            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "harsh8750994013@gmail.com" # GMail
            receiver_email = self.c_phone.get()
            password = "shubh@123#"                    #password
            message = str(self.bill_data)
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

        else:
            return
    def find_bill(self):
        present="No"
        for i in os.listdir("C:\MyBill"):
            if i.split('.')[0]==self.c_search_bill.get():
                f1=open(f"C:\MyBill/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                self.textarea.insert(END,d)
                f1.close()
                present="Yes"
        if present=="No":
                messagebox.showerror("Error","Invalid Bill Number")
    def clear_s(self):
        #cosmetic
        self.shop.set(0)
        self.face.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        # Glocery
        self.rice.set(0)
        self.oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        # cool drink
        self.maza .set(0)
        self.cock .set(0)
        self.frooti .set(0)
        self.thumbup .set(0)
        self.limca .set(0)
        self.sprite .set(0)
        # Total Product Price & Tax
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drink_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")
        # Customer
        self.c_name.set("")
        self.c_phone.set("")
        self.c_bill_no.set("")
        x = random.randint(1000, 9999)
        self.c_bill_no.set(str(x))
        self.c_search_bill.set("")
        self.welcome_bill()
    def Exit_s(self):
        op=messagebox.askyesno("Exit","Do You Really Want to Exit ")
        if op>0:
            self.root.destroy()
    def print_now(self):
        q=self.textarea.get('1.0',END)
        file=tempfile.mktemp(".txt")
        open(file,"w").write(q)
        os.startfile(file)
root=Tk()
b=bill_app(root)
root.mainloop()

#completed the code
