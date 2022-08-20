from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyodbc

global fg_color_text, bg_color_text, bg_color_buttons

fg_color_text = 'white'
bg_color_text = 'gray30'
bg_color_buttons = 'aquamarine4'
fg_color_checkbox = 'green3'

class Main_menu():
	"""docstring for main main_w"""
	def __init__(self, root, geom, titl, icon):
		self.main_w = root
		self.main_w.geometry(geom)
		self.main_w.title(titl)
		self.main_w.iconbitmap(icon)
		self.main_w['bg'] = bg_color_text

	def create_wigets_for_main_w(self):
		self.main_w.title('Fitness')
		self.main_w.geometry('450x200')
		self.welcome_text = Label(self.main_w,
				text = "Добро пожаловать!",
				font = (20),
				bg = bg_color_text,
				fg = fg_color_text)
		self.text2 = Label(self.main_w,
				text = "Что желаете сделать?", 
				bg = bg_color_text,
				fg = fg_color_text) 
		self.btn_find_in_db = Button(self.main_w,
				text = "Найти объект в базе",
				bg = bg_color_buttons ,
				fg = fg_color_text, command = lambda: self.create_wigets_for_option_w('F'))
		self.btn2 = Button(self.main_w,
				text = 'Записать данные в базу',
				bg = bg_color_buttons ,
				fg = fg_color_text, command = lambda: self.create_wigets_for_option_w('W'))
		self.btn3 = Button(self.main_w,
				text = 'Посмотреть отчеты',
				bg = bg_color_buttons,
				fg = fg_color_text, command = lambda: self.create_wigets_for_option_w('R'))
		self.exit_btn = Button(self.main_w,
					text = 'Выход',
					command = self.main_w.destroy)
		self.exit_btn.grid(column = 2, row = 3, padx = 5, pady = 10, sticky = 'n')
		self.welcome_text.grid(column = 1, row = 0, padx = 5, pady = 10, sticky = "n")
		self.text2.grid(column = 1, row = 1,padx = 5, pady = 10, sticky = "n")
		self.btn_find_in_db.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = "n")
		self.btn2.grid(column = 1, row = 2, padx = 5, pady = 10, sticky = "n")
		self.btn3.grid(column = 2, row = 2, padx = 5, pady = 10, sticky = "n")

	def create_wigets_for_option_w(self, type_of_button):
		self.destroyer('main')
		self.main_w.geometry('330x200')
		if type_of_button == 'F':
			self.main_w.geometry('680x360')
			self.main_w.title('Найти человека в базе')
			self.text = Label(self.main_w,
					text = "Выберите таблицу для поиска:", 
					bg = bg_color_text,
					fg = fg_color_text)
			self.entry_button = Button(self.main_w,
						text = 'Найти',
						bg = bg_color_buttons,
						fg = fg_color_text, command = lambda: self.find_in_database(self.combbox.get()))
			self.lbox = Text(self.main_w,
						width = 80, 
						height = 10)
			self.lbox.grid(column = 1,
						row = 11,
						padx = 5,
						pady = 10,
						sticky = 'n',
						columnspan = 3)
		elif type_of_button == 'W':

			self.main_w.title('Записать данные в базу')
			self.text = Label(self.main_w,
				text = "Выберите таблицу для записи:", 
				bg = bg_color_text,
				fg = fg_color_text)
			self.entry_button = Button(self.main_w,
						text = 'Записать',
						bg = bg_color_buttons,
						fg = fg_color_text, command = lambda: self.insert_into_database(self.combbox.get()))

		elif type_of_button == 'R':
			self.main_w.geometry('680x360')
			self.main_w.title('Посмотреть отчеты')
			self.text = Label(self.main_w,
					text = "Выберите отчет:", 
					bg = bg_color_text,
					fg = fg_color_text)
			self.lbox = Text(self.main_w,
						width = 80, 
						height = 10)
			self.lbox.grid(column = 1,
						row = 11,
						padx = 5,
						pady = 10,
						sticky = 'n',
						columnspan = 3)
			self.entry_button = Button(self.main_w,
						text = 'Выполнить',
						bg = bg_color_buttons,
						fg = fg_color_text, command = self.query_in_database)

		if type_of_button == 'W' or type_of_button == 'F':
			lst_of_values = [
				"Клиенты",
				"Тренеры",
				"Каталог"]
		elif type_of_button == 'R':
			lst_of_values = ["Список категорий тренеров",
							"Расписание",
							"Оплаты",
							"Продажи тренеров",
							"Отчеты"]
		self.combbox = ttk.Combobox(self.main_w,
				values = lst_of_values, width=27, state="readonly")
		self.combbox.current(0)
		self.combbox.bind("<<ComboboxSelected>>", lambda event: self.form_creator(event, type_of_button))

		self.back_button = Button(self.main_w,
					text = 'Назад',
					bg = bg_color_buttons,
					fg = fg_color_text, command = self.back_button_command)
		self.text.grid(column = 1, row = 1, padx = 5 , pady = 10, sticky = 'SW', columnspan = 2)
		self.combbox.grid(column = 1, row = 2, padx = 5, pady = 10, sticky = 'w')
		self.entry_button.grid(column = 2, row = 10, padx = 5, pady = 10, sticky = 'W') 
		self.back_button.grid(column = 3, row = 12, padx = 5, pady = 10, sticky = "E")

	def form_creator(self, event, type_of_w):
		evt = self.combbox.get()
		if evt == 'Клиенты':
			self.destroyer(type_of_w)
			if type_of_w == 'F':
				self.lbox.delete(1.0, END)
				self.main_w.geometry('680x580')
			elif type_of_w == 'W':
				self.main_w.geometry('400x420')
			self.name_client = Label(self.main_w,
						text = 'Имя:',
						bg = bg_color_text,
						fg = fg_color_text)
			self.surname_client = Label(self.main_w,
						text = 'Фамилия:',
						bg = bg_color_text,
						fg = fg_color_text)
			self.passport_client = Label(self.main_w,
						text = 'Паспорт:',
						bg = bg_color_text,
						fg = fg_color_text)
			self.adress_client = Label(self.main_w,
						text = 'Адрес:',
						bg = bg_color_text,
						fg = fg_color_text)
			self.Birthday_client = Label(self.main_w,
						text = 'День рождения:',
						bg = bg_color_text,
						fg = fg_color_text)
			
			self.sex_client = Label(self.main_w,
						text = 'Пол (М\\Ж):',
						bg = bg_color_text,
						fg = fg_color_text)
			
			self.PhoneNumber_client = Label(self.main_w,
						text = 'Номер телефона:',
						bg = bg_color_text,
						fg = fg_color_text)
		
			self.entry_client_birthday = Entry(self.main_w)
			self.entry_client_sex = Entry(self.main_w)
			self.entry_client_phonenumber = Entry(self.main_w)

			self.entry_client_adress = Entry(self.main_w)
			self.entry_client_name = Entry(self.main_w)
			self.entry_client_surname = Entry(self.main_w)
			self.entry_client_passport = Entry(self.main_w)

			self.entry_client_adress.grid(column = 2, row = 6, padx = 5, pady = 5, sticky = 'wN')
			self.entry_client_name.grid(column = 1, row = 4, padx = 5, pady = 5, sticky = 'wN')
			self.entry_client_surname.grid(column = 2, row = 4, padx = 5, pady = 5, sticky = 'wN')
			self.entry_client_passport.grid(column = 1, row = 6, padx = 5, pady = 5, sticky = 'wN')
			self.entry_client_birthday.grid(column = 1, row = 8, padx = 5, pady = 5, sticky = 'wN')
			self.entry_client_phonenumber.grid(column = 1, row = 10, padx = 5, pady = 5, sticky = 'wN')
			self.entry_client_sex.grid(column = 2, row = 8, padx = 5, pady = 5, sticky = 'wN')

			self.Birthday_client.grid(column = 1, row = 7, padx = 5, pady = 5, sticky = 'WS')
			self.sex_client.grid(column = 2, row = 7, padx = 5, pady = 5, sticky = 'WS')
			self.PhoneNumber_client.grid(column = 1, row = 9, padx = 5, pady = 5, sticky = 'WS')
			self.name_client.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'WS')
			self.surname_client.grid(column = 2, row = 3, padx = 5, pady = 5, sticky = 'WS')
			self.passport_client.grid(column = 1, row = 5, padx = 5, pady = 5, sticky = 'WS')
			self.adress_client.grid(column = 2, row = 5, padx = 5, pady = 5, sticky = 'WS')

		elif evt == 'Тренеры':
			self.destroyer(type_of_w)
			if type_of_w == 'F':
				self.lbox.delete(1.0, END)
				self.main_w.geometry('680x500')
			elif type_of_w == 'W':
				self.main_w.geometry('380x300')
			self.coach_name = Label(self.main_w,
					text = 'Имя:',
					bg = bg_color_text,
					fg = fg_color_text)
			self.coach_surname = Label(self.main_w,
					text = 'Фамилия:',
					bg = bg_color_text,
					fg = fg_color_text)
			self.id_coach_text = Label(self.main_w,
					text = 'ID категории:',
					bg = bg_color_text,
					fg = fg_color_text)

			self.entry_id_coach = Entry(self.main_w)
			self.entry_coach_name = Entry(self.main_w)
			self.entry_coach_surname = Entry(self.main_w)
			self.entry_id_coach.config(width = 1)
			self.coach_name.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'WS')
			self.entry_coach_name.grid(column = 1, row = 4, padx = 5, pady = 10, sticky = 'wN')
			self.coach_surname.grid(column = 2, row = 3, padx = 5, pady = 5, sticky = 'WS')
			self.id_coach_text.grid(column = 1, row = 5, padx = 5, pady = 5, sticky = 'WS')
			self.entry_coach_surname.grid(column = 2, row = 4, padx = 5, pady = 10, sticky = 'wN')
			self.entry_id_coach.grid(column = 1, row = 6, padx = 5, pady = 0, sticky = 'WN')
		elif evt == 'Каталог':
			self.destroyer(type_of_w)
			if type_of_w == 'F':
				self.lbox.delete(1.0, END)
				self.main_w.geometry('700x600')
			elif type_of_w == 'W':
				self.main_w.geometry('390x380')
			self.name_of_product = Label(self.main_w,
					text = 'Название товара:',
					bg = bg_color_text,
					fg = fg_color_text)

			self.price = Label(self.main_w,
					text = 'Цена:',
					bg = bg_color_text,
					fg = fg_color_text)

			self.description = Label(self.main_w,
					text = 'Описание:',
					bg = bg_color_text,
					fg = fg_color_text)
			self.entry_name_of_product = Entry(self.main_w)
			self.entry_price = Entry(self.main_w)

			self.entry_description = Text(self.main_w, width = 40, height = 5)
			self.price.grid(column = 2, row = 3, padx = 5, pady = 5, sticky = 'WS')
			self.name_of_product.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'WS')
			self.description.grid(column = 1, row = 5, padx = 5, pady = 5, sticky = 'WS')

			self.entry_name_of_product.grid(column = 1, row = 4, padx = 5, pady = 10, sticky = 'wN')
			self.entry_price.grid(column = 2, row = 4, padx = 5, pady = 10, sticky = 'wN')
			self.entry_description.grid(column = 1, row = 6, padx = 5, pady = 10, sticky = 'w', columnspan = 2)
		elif evt == 'Продажи тренеров':
			self.destroyer('R')
			self.lbox.delete(1.0, END)
			self.main_w.geometry('680x450')
			self.start_date = Label(self.main_w,
					text = 'Дата от:',
					bg = bg_color_text,
					fg = fg_color_text)
			self.finish_date = Label(self.main_w,
					text = 'Дата до:',
					bg = bg_color_text,
					fg = fg_color_text)
			self.entry_start_date = Entry(self.main_w)
			self.entry_finish_date = Entry(self.main_w)
			self.start_date.grid(column = 1, row = 3, padx = 5, pady = 5, sticky = 'W')
			self.finish_date.grid(column = 2, row = 3, padx = 5, pady = 5, sticky = 'W')
			self.entry_start_date.grid(column = 1, row = 4, padx = 5, pady =5 , sticky = 'WN')
			self.entry_finish_date.grid(column = 2, row = 4, padx =5, pady = 5, sticky = 'WN')
		elif evt == 'Список категорий тренеров':
			self.destroyer('R')
			self.lbox.delete(1.0, END)
		elif evt == 'Расписание':
			self.destroyer('R')
			self.lbox.delete(1.0, END)
		elif evt == 'Оплаты':
			self.destroyer('R')
			self.lbox.delete(1.0, END)
		elif evt == 'Отчеты':
			self.destroyer('R')
			self.main_w.geometry('700x500')
			self.lbox.delete(1.0, END)
			self.C_Fname = BooleanVar()
			self.C_Lname = BooleanVar()
			self.C_Adress = BooleanVar()
			self.C_Passport = BooleanVar()
			self.C_Birthday = BooleanVar()
			self.C_Sex = BooleanVar()
			self.C_PhoneNumber = BooleanVar()
			self.check_FName = Checkbutton(self.main_w,
						text = 'Имя',
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_Fname,
						onvalue=1, offvalue=0)
			self.check_Lname = Checkbutton(self.main_w,
						text = 'Фамилия',
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_Lname,
						onvalue=1, offvalue=0)
			self.check_Adress = Checkbutton(self.main_w,
						text = 'Адрес',
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_Adress,
						onvalue=1, offvalue=0)
			self.check_PassportID = Checkbutton(self.main_w,
						text = "Паспорт",
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_Passport,
						onvalue=1, offvalue=0)
			self.check_Birthday = Checkbutton(self.main_w,
						text = 'ДР',
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_Birthday,
						onvalue=1, offvalue=0)
			self.check_Sex = Checkbutton(self.main_w,
						text = 'Пол',
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_Sex,
						onvalue=1, offvalue=0)
			self.check_PhoneNumber = Checkbutton(self.main_w,
						text = 'Номер телефона',
						bg = bg_color_text,
						fg = fg_color_checkbox,
						activebackground = bg_color_text,
						activeforeground = fg_color_checkbox,
						variable = self.C_PhoneNumber,
						onvalue=1, offvalue=0)
			self.check_FName.grid(column = 1, row = 3, sticky = "WN")
			self.check_Lname.grid(column = 2, row = 3, sticky = "WN")
			self.check_Adress.grid(column = 1, row = 4, sticky = "WN")
			self.check_PassportID.grid(column = 2, row = 4, sticky = "WN")
			self.check_Birthday.grid(column = 1, row = 5, sticky = "WN")
			self.check_Sex.grid(column = 2, row = 5, sticky = "WN")
			self.check_PhoneNumber.grid(column = 1, row = 6, sticky = "WN")


	def destroyer(self, type_of_w):
		if type_of_w == 'main':	
			self.lst = self.main_w.grid_slaves()
			self.size = len(self.lst)
			for i in range(self.size):
				self.lst[i].destroy()
		elif type_of_w == 'W':
			self.lst = self.main_w.grid_slaves()
			self.size = len(self.lst)
			for i in range(self.size - 4):
				self.lst[i].destroy()
		elif type_of_w == 'F' or type_of_w == 'R':
			self.lst = self.main_w.grid_slaves()
			self.size = len(self.lst)
			for i in range(self.size - 5):
				self.lst[i].destroy()

	def back_button_command(self):
		self.destroyer('main')
		self.create_wigets_for_main_w()

	def connect_to_database(self):
		conn = pyodbc.connect(
		'Driver={ODBC Driver 17 for SQL Server};'
		'Server=ILYA-PC\\SQLEXPRESS;'
		'Database=FitnessClub;'
		'Trusted_Connection=yes;')
		return conn

	def insert_into_database(self, name_of_table):
		if name_of_table == 'Клиенты':
			query = f'''INSERT INTO [dbo].Clients(FName, Lname, Adress, PassportID, Birthday, Sex, PhoneNumber) VALUES
					('{self.entry_client_name.get()}',
					 '{self.entry_client_surname.get()}',
					 '{self.entry_client_adress.get()}',
					 '{self.entry_client_passport.get()}',
					 '{self.entry_client_birthday.get()}',
					 '{self.entry_client_sex.get()}',
					 '{self.entry_client_phonenumber.get()}')'''

		elif name_of_table == 'Тренеры':
			coach_name = self.entry_coach_name.get()
			coach_surname = self.entry_coach_surname.get()
			id_coach = self.entry_id_coach.get()
			query = f'''INSERT INTO [dbo].Coaches(FName, LName, ID_CATEGORY) VALUES
					('{coach_name}', '{coach_surname}', '{id_coach}')'''

		elif name_of_table == 'Каталог':
			name_of_product = self.entry_name_of_product.get()
			price = self.entry_price.get()
			description = self.entry_description.get('1.0', END)
			query = f'''
			INSERT INTO [dbo].Catalog(Name, Price, Description) VALUES
					('{name_of_product}','{price}','{description}')'''
		try:
			conn = self.connect_to_database()
			cursor = conn.cursor()
			cursor.execute(query)
			conn.commit()
			conn.close()
			messagebox.showinfo("Fitness", "Данные успешно внесены!")
		except:
			messagebox.showinfo("Fitness", "Ошибка внесения данных!")

	def find_query_generator(self, name_of_table):
		try:
			if name_of_table == 'Клиенты':
				dict_params = {'Fname': self.entry_client_name,
								'Lname': self.entry_client_surname,
								'Adress': self.entry_client_adress,
								'PassportID': self.entry_client_passport,
								'Birthday': self.entry_client_birthday,
								'Sex': self.entry_client_sex,
								'PhoneNumber': self.entry_client_phonenumber}
				query = f'''SELECT * FROM Clients WHERE'''
			elif name_of_table == 'Тренеры':
				dict_params = {'Fname': self.entry_coach_name,
								'Lname': self.entry_coach_surname,
								'ID_CATEGORY': self.entry_id_coach
								}
				query = f'''SELECT * FROM Coaches WHERE'''
			elif name_of_table == 'Каталог':
				dict_params = {'Name': self.entry_name_of_product,
								'Price': self.entry_price
								}
				query = f'''SELECT * FROM Catalog WHERE'''

			for param in dict_params:
				if dict_params[param].get() == '':
					continue
				else:
					key = list(dict_params.keys())[list(dict_params.values()).index(dict_params[param])]
					query = query + f'({key} = \'{dict_params[key].get()}\')' + ' AND'
			query = query[:-4]
			return query	
		except:
			messagebox.showinfo("Fitness", "Выберите таблицу!")	


	def find_in_database(self, option):
		query = self.find_query_generator(option)	
		cursor = self.connect_to_database().cursor()
		cursor.execute(query)
		self.lbox.delete(1.0, END)

		for row in cursor:
			[self.lbox.insert(END, x) for x in self.find_parser(row)]
			self.lbox.insert(END, '\n\n')

	def query_in_database(self):
		evt = self.combbox.get()
		if evt == 'Список категорий тренеров':
			query = '''
					SELECT ID_COACH, FName, LName, Zone, LevelOfCategory
					FROM dbo.Coaches
					JOIN category_of_coaches on Coaches.ID_CATEGORY = category_of_coaches.ID_CATEGORY 
					ORDER BY Zone'''
		elif evt == 'Расписание':
			query = '''
					SELECT Name, duration, LName, FName
					FROM dbo.schedule
					JOIN Coaches on Coaches.ID_COACH = schedule.ID_COACH
					'''
		elif evt == 'Оплаты':
			query = '''
					SELECT FName, LName, Amount, Name, [Payment type], PaymentDate
					FROM dbo.Clients
					JOIN Payments on Payments.ID_CLIENT = Clients.ID_CLIENT
					JOIN dbo.Catalog on Catalog.ID_PRODUCT = Payments.ID_PRODUCT
					'''
		elif evt == 'Продажи тренеров':
			query = f'''
					SELECT FName, LName, SUM(Amount) as 'Сумма продаж'
					FROM dbo.Payments
					JOIN Coaches on Coaches.ID_COACH = Payments.ID_COACH 
					WHERE PaymentDate > '{self.entry_start_date.get()}' AND PaymentDate < '{self.entry_finish_date.get()}'
					Group by FName, LName
					ORDER BY Sum(Amount) DESC
					'''
		elif evt == 'Отчеты':
			dict_params = {'Fname': self.C_Fname,
				'Lname': self.C_Lname,
				'Adress': self.C_Adress,
				'PassportID': self.C_Passport,
				'Birthday': self.C_Birthday,
				'Sex': self.C_Sex,
				'PhoneNumber': self.C_PhoneNumber}
			query = '''SELECT'''
			for param in dict_params:
				if dict_params[param].get() == False:
					continue
				else:
					key = list(dict_params.keys())[list(dict_params.values()).index(dict_params[param])]
					query = query + f' {key},'
			query = query[:-1]
			query = query + ' FROM Clients'
			print(query)
		cursor = self.connect_to_database().cursor()
		cursor.execute("set nocount on;" + query)
		self.lbox.delete(1.0, END)
		for row in cursor:
			[self.lbox.insert(END, x) for x in self.find_parser(row)]
			self.lbox.insert(END, '\n\n')
	


	def find_parser(self, tple):
		lst = list(tple)
		lst = [str(x).strip() + '\t' for x in lst]
		# lst = [str(x) + '\t' for x in lst]
		return lst
root = Tk()
w1 = Main_menu(root, '450x200', 'Fitness', 'fitness.ico')
w1.create_wigets_for_main_w()
root.mainloop()