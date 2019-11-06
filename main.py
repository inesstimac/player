print("Create a football or basketball player's profile by adding their information!")


class Player:
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight

    def weight_to_lbs(self):
        pounds = self.weight * 2.2
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height, weight, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height=height, weight=weight)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height, weight, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height=height, weight=weight)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


while True:
    start = input("Do you want to enter A) a football player or B) a basketball player? ")

    if start == "A":

        player = FootballPlayer(first_name=input("Enter the player's first name: "),
                                last_name=input("Enter the player's last name: "),
                                height=input("Enter the player's height: "),
                                weight=input("Enter the player's weight: "),
                                goals=input("Enter the number of scored goals: "),
                                yellow_cards=input("Enter the number of yellow cards: "),
                                red_cards=input("Enter the number of red cards: "))

    if start == "B":

        player = BasketballPlayer(first_name=input("Enter the player's first name: "),
                                  last_name=input("Enter the player's last name: "),
                                  height=input("Enter the player's height: "),
                                  weight=input("Enter the player's weight: "),
                                  points=input("Enter the number of scored points: "),
                                  rebounds=input("Enter the number of rebounds: "),
                                  assists=input("Enter the number of assists: "))

    with open("player.txt", "w") as player_file:
        player_file.write(str(player.__dict__))
    break

print("Your player is: " + str(player.__dict__))
