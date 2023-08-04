# DOCTOR LOG KA PROFILE .

doctors = {
    1: {"name": "Dr.CHANDAN", "specialty": " Physician", "available_slots": ["09:00", "10:00", "11:00"]},
    2: {"name": "Dr. MADHUKAR", "specialty": "GASTRO", "available_slots": ["14:00", "15:00", "16:00"]},
    3: {"name": "Dr.KUNDAN", "specialty": " NURO", "available_slots": ["08:00", "09:00", "11:00"]},
    4: {"name": "Dr.KUMAR", "specialty": " GENERAL", "available_slots": ["05:00", "06:00", "08:00"]},
    5: {"name": "Dr.YASH", "specialty": " DENTAL", "available_slots": ["10:00", "11:00", "12:00"]},
    6: {"name": "Dr.RAO", "specialty": " DERMATOLOGIST", "available_slots": ["01:00", "02:00", "04:00"]},
    7: {"name": "Dr.RITWIK", "specialty": " GASTRO", "available_slots": ["04:00", "08:00", "11:00"]},
     

    
    # aur dr. ko add kr skte hai 
}

appointments = {}

# DOCTOR AUR USKE TIME SLOT KE FUNCTION BLOCK
def display_available_doctors():
    print("Available Doctors:")
    print("ID   Doctor Name          Specialty             Available Slots")
    print("*#"*30 )
    for doc_id, doctor in doctors.items():
        doc_info = [doc_id, doctor["name"], doctor["specialty"], ", ".join(doctor["available_slots"])]
        print("{:<4} {:<20} {:<20} {:<20}".format(*doc_info))

# APPOINT. lene  KA  BLOCK

def book_appointment():
    display_available_doctors()
    try:
        doc_id = int(input("Enter the ID of the doctor you want to book an appointment with: "))
        if doc_id not in doctors:
            print("Please Enter Correct Dr. ID")
            return
        doctor = doctors[doc_id]
        print(f"Selected Doctor: {doctor['name']} ({doctor['specialty']})")

        patient_name = input("Enter your name: ")
        appointment_time = input("Enter the desired appointment time (e.g., 09:00): ")

        if appointment_time not in doctor["available_slots"]:
            print("Invalid appointment time or the slot is not available.")
            return

        doctor["available_slots"].remove(appointment_time)
        appointments[patient_name] = {"doctor": doctor["name"], "time": appointment_time}
        print("Appointment booked successfully!")
    except ValueError:
        print("Invalid input. Please enter valid values.")

# BOOKING KA MAIN LOOP
def main():
    print("\U0001F922"*6,"KINDLY BOOK YOUR APPOINTMENT ","\U0001F923"*5)
    
    while True:
        print("\nMENU:",)
        print("1. Available Doctors")
        print("2. Book  Appointment")
        print("0. Exit")

        try:
            choice = int(input("Enter the option number: "))

            if choice == 1:
                display_available_doctors()
            elif choice == 2:
                book_appointment()
            elif choice == 0:
                print("Exiting Hospital Booking System.")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid option number.")

if __name__ == "__main__":
    main()

