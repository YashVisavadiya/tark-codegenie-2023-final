import collections

map_Coaches = {
    "1A": "H",
    "2A": "A",
    "3A": "B",
    "SL": "S"
}
map_Coaches_with_Price = {
    "1A": 4,
    "2A": 3,
    "3A": 2,
    "SL": 1
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
            train.setdefault(request["Date"], dict(train["Coaches"]))

            # print(request["Date"], train[request["Date"]])

            group = collections.defaultdict(int)
            for coach, seats in train[request["Date"]].items():
                group[coach[0]] += seats

            # print(group)
            req_seats = request["Seats"]
            if len(group) != len(train[request["Date"]].items()):
                for coach, seats in group.items():
                    if coach == map_Coaches[request["Coach"]]:
                        if seats >= req_seats:
                            # Set DS
                            for c, s in train[request["Date"]].items():
                                if c[0] == coach:
                                    if s >= req_seats:
                                        train[request["Date"]][c] -= req_seats
                                        return (True, train["Distance"] * map_Coaches_with_Price[request["Coach"]] * request["Seats"])
                                    else:
                                        req_seats -= train[request["Date"]][c]
                                        train[request["Date"]][c] = 0

                            return (True, train["Distance"] * map_Coaches_with_Price[request["Coach"]] * request["Seats"])

                        return (False, 0)
                pass

            # Check if required coach having required seats
            for coach, seats in train[request["Date"]].items():
                if map_Coaches[request["Coach"]] == coach[0]:
                    if seats >= request["Seats"]:
                        train[request["Date"]][coach] -= request["Seats"]

                        # print(train[request["Date"]][coach], train[request["Date"]])
                        print(train)

                        return (True, train["Distance"] * map_Coaches_with_Price[request["Coach"]] * request["Seats"])

    return (False, 0)


def check_reservation_is_possible(request):
    if not check_if_train_available(request):
        print("No Trains Available")
        return (False, 0)

    # is_possible is true then we have enough seats
    is_possible, total_fair = check_if_seats_available(request)
    if not is_possible:
        print("No Seats Available")
        return (False, 0)
    return (True, total_fair)


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

    # reservationSystem.print_all_details()
    # print(reservationSystem.TrainDetails)

    report = Report()

    while True:
        reservation_request = take_input_for_train_reservation()

        is_possible, total_fair = check_reservation_is_possible(reservation_request)
        if is_possible:
            # Calculate Total Fair
            # total_fair = calculate_fair(reservation_request)

            # Print Output
            print(report.next_PNR, total_fair)

            # Add it to report
            report.add_to_log(total_fair)
            pass

    pass

# 4
# 37393 Ahmedabad-0 Pune-700
# 37393 S1-72 S2-72 B1-72 A1-48 H1-24
# 17726 Rajkot-0 Mumbai-750
# 17726 S1-72 S2-72 B1-72 A1-48 H1-24
# 22548 Ahmedabad-0 Surat-300
# 22548 S1-15 S2-20 B1-36 B2-48
# 72097 Mumbai-0 Jaipur-1000
# 72097 S1-15 S2-20 B1-25 H1-10

# Ahmedabad Pune 2023-03-15 SL 3
# Rajkot Surat 2023-02-21 3A 4
# Ahmedabad Surat 2023-02-23 1A 5
# Ahmedabad Pune 2023-03-23 SL 15
# Ahmedabad Pune 2023-03-23 SL 15
# Ahmedabad Pune 2023-03-23 SL 10
# Ahmedabad Pune 2023-03-23 1A 10
# Ahmedabad Pune 2023-03-23 1A 5
# Ahmedabad Pune 2023-03-23 1A 5
# Mumbai Jaipur 2023-03-23 SL 2
# Mumbai Jaipur 2023-03-23 SL 5
# Mumbai Jaipur 2023-03-23 SL 7
# Mumbai Jaipur 2023-03-23 3A 1
# Mumbai Jaipur 2023-03-23 3A 2
# Mumbai Jaipur 2023-03-23 3A 4
# Ahmedabad Pune 2023-03-26 SL 72
# Ahmedabad Pune 2023-03-26 SL 36
# Ahmedabad Surat 2023-03-18 SL 25
# Ahmedabad Surat 2023-03-18 SL 11
