import requests

def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/ra1.ndom"
    response = requests.get(url).json()
    print("Random Dog Image:", response["message"])

def get_all_breeds():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url).json()
    breeds = response["message"].keys()
    print("Available Breeds:")
    for breed in breeds:
        print(breed)

def get_breed_image(breed_name):
    url = f"https://dog.ceo/api/breed/{breed_name}/images/random"
    response = requests.get(url).json()
    if response["status"] == "success":
        print(f"Random {breed_name.capitalize()} Image: {response['message']}")
    else:
        print("Invalid breed name. Please try again.")

def main():
    while True:
        print("\nDog Image Viewer")
        print("1. Fetch a random dog image")
        print("2. View images of a specific breed")
        print("3. List all available breeds")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            get_random_dog_image()
        elif choice == "2":
            breed = input("Enter breed name: ")
            get_breed_image(breed.lower())
        elif choice == "3":
            get_all_breeds()
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


