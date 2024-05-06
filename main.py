# Kullanıcıları saklamak için bir liste
users = {
	"Manager": [],
	"Administrative Assistant": [],
	"Technical Personnel": [],
	"Cleaner": [],
	"Project Manager": [],
	"Project Executor": [],
}
# Pozisyonlar için en fazla eklenecek kişi sayısı
max_users_person_position = {
	"Manager": 1,
	"Administrative Assistant": 10,
	"Technical Personnel": 40,
	"Cleaner": 10,
	"Project Manager": 15,
	"Project Executor": 24,
}

# Her pozisyon için dolar cinsinden maaş  değerleri
salary_mapping = {
	"manager": 3661,
	"administrative assistant": 3647,
	"technical personnel": 3273,
	"cleaner": 3000,
	"project manager": 8556,
	"project executor": 13992
}
# Yapmak istediğin seçimi seç
def Positions():
    while True:
        print("-------------------------")
        print("1. Boss Login")
        print("-------------------------")
        print("2. View Manager Information")
        print("-------------------------")
        print("3. View Administrative Assistant Information")
        print("-------------------------")
        print("4. View Technical Personnel Information")
        print("-------------------------")
        print("5. View Cleaner Information")
        print("-------------------------")
        print("6. View Project Manager Information")
        print("-------------------------")
        print("7. View Project Executor Information")
        print("-------------------------")
        print("8. Show Users")
        print("-------------------------")
        print("9. Exit")

        selection = input("Please select an option: ")

        if selection == "1":
            position = Manager()
            if position:
                print("---------------")
                print(f"Merhaba Sayın Patron")
                while True:
                    print("Please select the action you want to perform: ")
                    print("1. Add User ")
                    print("2. Delete User ")
                    print("3. Change Salary ")
                    print("4. Back to Main Menu")
                    user_selection = int(input("Your selection: "))
                    if user_selection == 1:
                        add_user()
                    elif user_selection == 2:
                        delete_user()
                    elif user_selection == 3:
                        change_salary()
                        break
                    elif user_selection == 4:
                        break
                    else:
                        print("Invalid selection")
        elif selection == "2":
            view_position_information("manager")
        elif selection == "3":
            view_position_information("administrative assistant")
        elif selection == "4":
            view_position_information("technical personnel")
        elif selection == "5":
            view_position_information("cleaner")
        elif selection == "6":
            view_position_information("project manager")
        elif selection == "7":
            view_position_information("project executor")
        elif selection == "8":
            show_users()
        elif selection == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection")



# Patron girişi
def Manager():
    managerEmail = "yasar@gmail.com"
    managerPassword = "123456789"
    ManagerMail1 = str(input("Lütfen E-postanızı Girin: ")).lower()
    ManagerPassword1 = str(input("Lütfen Şifrenizi Girin: "))

    if ManagerMail1 == managerEmail and ManagerPassword1 == managerPassword:
        print("Giriş Başarılı")
        return "Manager"  # Pozisyonu doğru harfle döndür
    else:
        print("Giriş Başarısız")
        return

# Pozisyonlar hakkında bilgi
def view_position_information(position):
    position_key = position[0].upper() + position[1:  ]  # ilk harfi büyük harfe çevir
    print(f"Viewing {position_key} Information:")

    if position_key in users and users[position_key]:
        for i in range(len(users[position_key])):
            user = users[position_key][i]
            user_name_key = 'ad' if 'ad' in user else 'name'
            print(
                f"{position_key} {i + 1}: User Name: {user[user_name_key]}, Email: {user['email']}, Cinsiyet: {user['cinsiyet']}")
    else:
        print(f"No users found for {position_key} position.")
        return


# Çalışan ekleme
def add_user():
    position = input("Enter the user's position (Manager, Technical Personnel, Administrative Assistant, Cleaner, Project Manager, Project Executor): ")
    position = position[0].upper() + position[1:]  # ilk harfi büyük harfe çevir

    # hatalı pozisyon girildiğini kontrol et
    if position in max_users_person_position:
        user_list = users[position]
    else:
        print(f"Invalid position: {position}")
        return

    # Pozisyonda maksimum sınıra ulaştı mı kontrol et
    max_limit = max_users_person_position[position]
    if len(user_list) >= max_limit:
        print(f"The position {position} is already occupied. You cannot add another user to this position. Maximum limit: {max_limit}")  # pozisyon doluysa mesaj ver
        return

    # Ad al
    while True:
        user_name = str(input("Enter the user's name: "))
        if user_name:
            break
        else:
            print("Invalid name. Please enter a valid name.")

    # Soyad al
    while True:
        user_surname = str(input("Enter the user's Surname: "))
        if user_surname:
            break
        else:
            print("Invalid Surname. Please enter a valid Surname.")

    # Email al
    while True:
        user_email = input("Enter the user's email: ")
        if user_email:
            break
        else:
            print("Invalid email. Please enter a valid email.")

    # Yaş al
    while True:
        user_age_input = input("Enter the user's age (between 18 and 65): ")
        if user_age_input and 18 <= int(user_age_input) <= 65:
            user_age = int(user_age_input)
            break
        else:
            print("Invalid age. Please enter a valid age between 18 and 65.")
				
				# GSM al
    while True:
        user_gsm_input = input("Enter the user's GSM: ")
        if user_gsm_input and int(user_gsm_input) > 0:
            user_gsm = int(user_gsm_input)
            break
        else:
            print("Invalid GSM. Please enter a valid GSM.")

    while True:
        user_tc_input = input("Enter the user's TC:")
        if user_tc_input and int(user_tc_input) > 0:
            user_tc = int(user_tc_input)
            break
        else:
            print("Invalid Tc. Please enter a valid Tc.")

    # Cinsiyet al
    user_gender = str(input("Enter the user's gender: "))

    # Kullanıcıyı listeye ekle
    users[position] += [{"ad": user_name, "surname": user_surname, "email": user_email, "yas": user_age, "cinsiyet": user_gender,
                         "gsm": user_gsm, "tc": user_tc}]

    print(f"{user_name} user successfully added!!")


# İşten çıkan veya çıkan kişileri kolayca silmek için
def delete_user():
	position = input(
		"Enter the user's position (Manager, Technical Personnel, Cleaner, Administrative Assistant, Project Manager, Project Executive): ")
	position_key = position[0].upper() + position[1:]  # ilk harfi büyük harfe çevir
	
	if position_key not in users or not users[
		position_key]:
		print(f"No users found for {position_key} position.")
		return
	else:
		while True:
			user_info = input("Enter the name or email of the user to delete: ")
			
			# Kullanıcının girdiği değeri hem isimde hem de emailde ara
			matching_users = [user for user in users[position_key] if
												user_info.lower() in [user['ad'].lower() if 'ad' in user else '',
																							user['email'].lower() if 'email' in user else '']]
			
			if matching_users:
				user_to_delete = matching_users[0]
				confirm = input(f"Do you really want to delete user {user_to_delete['ad']}? (yes/no): ").lower()
				if confirm == "yes":
					users[position_key] = [user for user in users[position_key] if user != user_to_delete]
					print(f"User {user_to_delete['ad']} deleted successfully!")
				else:
					print("Deletion cancelled.")
				break
			else:
				print("No matching user found. Please enter a valid name or email.")


# Çalışanları Göster
def show_users():
	print("------List of Users-----")
	for position in users:
		user_list = users[position]
		print(f"{position} Users:")
		for user in user_list:
			print(
				f"Name: {user.get('ad', '')}, Email: {user.get('email', '')}, Age: {user.get('yas', '')}, "
				f"Gender: {user.get('cinsiyet', '')}, Gsm: {user.get('gsm', '')}, Tc: {user.get ('tc', '')}")


# Maaşları hesapla
def calculate_salary(position):
	position_lower = position.lower()
	if position_lower in salary_mapping:
		return salary_mapping[position_lower]
	else:
		return 0


# Maaş değiştirme
def change_salary():
	if Manager():
		position = input("Enter the position to change salary: ").lower()  # pozisyonu öğren
		new_salary = input("Enter the new salary: ")  # yeni maaşı al
		salary_mapping[position] = int(new_salary)  # tanımla
		print(f"Salary for {position} has been changed to {new_salary}")  # değiştiği mesajını ver
	else:
		print("You do not have the permission to change salaries.")  # pozisyon olmadığı bilgisi


# Çağrı
Positions()