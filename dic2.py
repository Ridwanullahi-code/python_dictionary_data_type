user_profile = {
	"user1":{
	"name1":{ "surname":"Ajayi", "middleName":"Ridwanullahi", "lastName": "Olalekan"},

	"address1":{"state":"osun state", "Town":"ileogbo", "compound": "omoforilu"}
	},


	"user2" :{
	"name2":{ "surname":"Akintade", "middleName":"Halimat", "lastName": "ishola"},

	"address2":{"state":"ondo state", "Town":"akure", "compound": "futa"}
	},

	"user3" : {
	"name3":{ "surname":"Alabi", "middleName":"Tunde", "lastName": "Bisi"},

	"address3":{"state":"kogi state", "Town":"eleni", "compound": "iro"}
	},


}

total_user_name ={}

for name in (user_profile["user1"]["name1"].items(),
	user_profile["user2"]["name2"].items(),user_profile["user3"]["name3"].items()):
	
	total_user_name.update(name)
	print(total_user_name)

total_user_address = {}
for adres in (user_profile["user1"]["address1"].items(),
	user_profile["user2"]["address2"].items(),user_profile["user3"]["address3"].items()):

	total_user_address.update(adres)
	print(total_user_address)



