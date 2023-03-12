map_Coaches = {
    "1A": "H",
    "2A": "A",
    "3A": "B",
    "SL": "S"
}

# This function is used to arrange basic train details of a train (like Source - Destination - Distance ) into an
# object and return it
def arrange_basic_train_detail(basic_train_detail):
    basic_train_detail = basic_train_detail.split()

    details = dict()
    details["TrainNumber"] = basic_train_detail[0]
    details["Source"] = basic_train_detail[1][:-2]
    details["Destination"], details["Distance"] = basic_train_detail[2].split('-')
    details["Distance"] = int(details["Distance"])

    return details


# This function is used to arrange Coach details of a train in proper format and return it's object
def arrange_coach_detail(train_coach_detail):
    train_coach_detail = train_coach_detail.split()

    details = dict()
    for coach in train_coach_detail[1:]:
        coach_name, coach_capacity = coach.split('-')
        details[coach_name] = int(coach_capacity)

    return details


# This function is used take reservation for a train as an input
def take_input_for_train_reservation():
    reservation = input().split()

    details = dict()
    details["Source"] = reservation[0]
    details["Destination"] = reservation[1]
    details["Date"] = reservation[2]
    details["Coach"] = reservation[3]
    details["Seats"] = int(reservation[4])

    return details


def check_if_train_available(request):
    for train in reservationSystem.TrainDetails:
        if train["Source"] == request["Source"] and train["Destination"] == request["Destination"]:
            return True
    return False


def check_if_seats_available(request):
    for train in reservationSystem.TrainDetails:
        if train["Source"] == request["Source"] and train["Destination"] == request["Destination"]:
            train.setdefault(request["Date"], train["Coaches"])
            if train["Date"][request["Coach"]] >= request["Seats"]:
                return True
    return False


def check_reservation_is_possible(request):
    if not check_if_train_available(request):
        print("No Trains Available")
        return False
    if not check_if_seats_available(request):
        print("No Seats Available")
        return False
    return True


def calculate_fair(request):
    return []


class TrainReservationSystem:
    def __init__(self):
        self.TotalTrains = 0  # For Counting Total Trains
        self.TrainDetails = []  # List of Objects

    # This is used to print all details of all trains
    def print_all_details(self):
        for train in self.TrainDetails:
            for key, value in train.items():
                print(key, value)

    # This function is used to take train details as an input from user and store it to Data Structure
    def take_input_trains(self):
        t = int(input())
        self.TotalTrains = t

        for _ in range(t):
            basic_train_detail = input()
            train_coach_detail = input()

            basic_detail = arrange_basic_train_detail(basic_train_detail)
            coach_detail = arrange_coach_detail(train_coach_detail)

            # train is used temporarily to store data from both dictionaries.
            train = dict()

            # Adding data of basic_detail to train
            for key, value in basic_detail.items():
                train[key] = value

            # Adding data of coach_detail to train
            train["Coaches"] = coach_detail

            # Adding Remaining Seats to train to keep track of available seats
            # train["AvailableSeatsPerCoach"] = coach_detail

            # Add Train Detail to Data Structure
            self.TrainDetails.append(train)


class Report:
    def __init__(self):
        self.next_PNR = 100000001
        self.log = []  # Contains PNR, Total Fair
        pass

    def add_to_log(self, total_fair):
        curr_PNR = self.next_PNR
        self.next_PNR += 1

        # Calculating Price
        log_record = dict()
        log_record["PNR"] = curr_PNR
        log_record["TotalFair"] = total_fair
        self.log.append(log_record)


if __name__ == "__main__":
    # Create an object of Reservation System
    reservationSystem = TrainReservationSystem()

    # Taking Input for Reservation System
    reservationSystem.take_input_trains()

    reservationSystem.print_all_details()
    # print(reservationSystem.TrainDetails)

    report = Report()

    # while True:
    #     reservation_request = take_input_for_train_reservation()
    #     if check_reservation_is_possible(reservation_request):
    #         total_fair = calculate_fair(reservation_request)
    #         report.add_to_log(total_fair)
    #         pass

    pass
