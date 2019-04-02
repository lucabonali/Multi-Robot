from Auction import Auction

def startRouting(path):
    auction = Auction(path)
    auction.step()


startRouting("MapEasy")

