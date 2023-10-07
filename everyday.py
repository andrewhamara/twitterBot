from twitter import tweet
import schedule
import time

def main():
    #schedule.every().day.at("23:43").do(tweet)
    schedule.every().hour.at(":00").do(tweet)
    #schedule.every().minute.do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
