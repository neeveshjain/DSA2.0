#Custom data structures
class StarCookie:
    milk = '1 lit'
    def __init__(self,color,weight):
        print("Cookie is ready . . .")
        self.color = color
        self.weight = weight

star_cookie1 = StarCookie("Red",16)
print(star_cookie1.color, ' ' , star_cookie1.weight)
star_cookie1.milk = '2 lit'
print(star_cookie1.milk)

print(star_cookie1.__dict__) #important


class Youtuber:
    def __init__(self,usernames, subscribers):
        self.usernames = usernames
        self.subscribers = subscribers
    def subscribe(self,user):
        user.subscribers += 1
        self.subscription += 1

user1 = Youtuber("Neevesh",'onemil')
print(user1.usernames,'',  user1.subscribers)

user2 = Youtuber("Renad",'5')
print(user2.usernames, ' ', user2.subscribers)

