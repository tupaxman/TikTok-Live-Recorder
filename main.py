import argparse

from enums import Mode, Info
from tiktokbot import TikTok


def banner() -> None:
    print(Info.BANNER)


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-user",
                        dest="user",
                        help="record a live from the username.",
                        action='store')
    parser.add_argument("-room_id",
                        dest="room_id",
                        help="record a live from the room_id.",
                        action='store')
    parser.add_argument("-mode",
                        dest="mode",
                        help="recording mode: (manual,automatic) [Default: manual]\n[manual] => manual live recording\n[automatic] => automatic live recording when the user is in live).",
                        default="manual",
                        action='store')
    parser.add_argument("-output",
                        dest="output",
                        help="output dir",
                        action='store')
    args = parser.parse_args()
    return args


def main():
    banner()

    user = None
    mode = None
    room_id = None

    args = parse_args()
    try:
        if not args.user and not args.room_id:
            raise Exception("[-] Missing user/room_id value")

        if not args.mode:
            raise Exception("[-] Missing mode value")
        if args.mode and args.mode != "manual" and args.mode != "automatic":
            raise Exception("[-] Incorrect -mode value")

        if args.user and args.room_id:
            raise Exception("[-] Enter the username or room_id, not both.")
    except Exception as ex:
        print(ex)
        exit(1)

    user = args.user
    room_id = args.room_id
    if args.mode == "manual":
        mode = Mode.MANUAL
    else:
        mode = Mode.AUTOMATIC

    try:
        bot = TikTok(args.output, mode, user, room_id)
        bot.run()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
