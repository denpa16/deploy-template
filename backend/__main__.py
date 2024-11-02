from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")

def main():
    print("Hello!")
    print(f"Bot token: {BOT_TOKEN}")

if __name__ == "__main__":
    main()