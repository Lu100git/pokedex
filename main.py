from os import system
import pkdatabase
green = "\033[0;32m"
def main():
	print(green)
	executing = True
	
	#main titlle
	system("clear")
	system("cat title")

	#main loop
	while executing:
		print("\n")
		print("\t .:Welcome!, please make a choice:. ")

		print("1. Display all available pokemon on the pokedex")
		print("\n")

		print("2. Display only pokemon names")
		print("\n")

		print("3. Display desired pokemon types")
		print("\n")

		print("4. EXIT")
		print("\n")

		choice = input()

		if choice == "1":
			system("clear")
			pkdatabase.printAll()
		elif choice == "2":
			system("clear")
			pkdatabase.printPokemonName()
		elif choice == "3":
			system("clear")
			print("\the pokemons types are...")
			for i in range(len(pkdatabase.types)):
				print(pkdatabase.types[i])
			choice_type = input("\ttype your choice: ")
			pkdatabase.filtherTypes(choice_type)
		elif choice == "4":
			system("clear")
			print("Have a good day!")
			executing = False
		
		else:
			system("clear")
			print("["+choice+"]", "<- is not a valid choice!")

main()
