from datetime import datetime


def main():
    now = datetime.now()
    print("%y", now.strftime("%y"), "- %Y", now.strftime("%Y"))
    print("%a", now.strftime("%a"), "- %A", now.strftime("%A"))
    print("%b", now.strftime("%b"), "- %B", now.strftime("%B"))
    print("%d", now.strftime("%d"))

    print(now.strftime("%A, %d, %B, %y"))

    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))


if __name__ == "__main__":
    main()
