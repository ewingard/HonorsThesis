import instaloader
#need to use pip install instaloader first to be able to import.
    #instaloader has really good docs too if you need any information about how to use it/defs/etc.

class GetInstagramProfile():

    def __init__(self) -> None:
        self.L = instaloader.Instaloader()
        self.L.login('username', 'password') #put your IG login info into the 'user' and 'pass' options.
        #You can run it without these options to login, but it may bar you from getting scraped images if you
        #scrape images too much without logging in. vice versa with login - sometimes you need to logout to cont.

    def download_hashtag_posts(self, hashtag):
        for post in instaloader.Hashtag.from_name(self.L.context, hashtag).get_posts():
            self.L.download_post(post, target='#'+hashtag) #this means you don't need to put the hashtag in the
            #"" below to download them, it already appended it above!
            #this basically just downloads the images/videos from the hashtags you put in below!
            
if __name__=="__main__":
    cls = GetInstagramProfile()
    # x = input("Type in a hashtag!")
    # cls.download_hastag_posts(x)
    cls.download_hashtag_posts("put_hashtag_contents_here") # when running, type hashtag into the "" to avoid
    #user inputs, skip straight to the scraping!