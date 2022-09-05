logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def highest_bidder(n_dict):
    max_bid = 0
    for key in n_dict:
        if max_bid < n_dict[key] : 
            max_bid = n_dict[key]
            name = key
    print(f"The winner is {name} with highest bid of {max_bid}.")    

print(logo)

ans = "yes"
bid_name_dict = {}

while ans == "yes":
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bid_name_dict[name] = bid
    
    ans = input("Do you want to add more bidders? 'yes' or 'no' ").lower()

highest_bidder(bid_name_dict)
    
    

    
