import youtube
import asyncio
print("Script Loaded")

# loading the YouTube script to run indefinitely
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(youtube.channel_monitor())
    loop.run_forever()
