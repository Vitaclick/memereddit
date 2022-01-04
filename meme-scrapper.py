import argparse
from playground.collector import RedditCollector

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A script to collect images/gifs from reddit')
    parser.add_argument('--client_id', action='store', dest='client_id',
                        help='your reddit app client id', required=True)
    parser.add_argument('--client_secret', action='store', dest='client_secret',
                        help='your reddit app client secret', required=True)
    parser.add_argument('--user_agent', action='store', dest='user_agent',
                        help='your reddit app user agent', required=True)
    parser.add_argument('--username', action='store',
                        dest='username', help='your reddit username')
    parser.add_argument('--password', action='store',
                        dest='password', help='your reddit password')
    parser.add_argument('--subreddits', action='store', dest='subreddits_list',
                        nargs='+', help='subreddits to collect memes from', required=True)
    parser.add_argument('--limit', action='store', dest='limit',
                        type=int, help='limit to grab posts', required=True)
    args = parser.parse_args()

    args_data_collector = RedditCollector(client_id=args.client_id,
                                          client_secret=args.client_secret,
                                          user_agent=args.client_secret,
                                          subreddits_list=args.subreddits_list,
                                          limit=args.limit,
                                          username=args.username,
                                          password=args.password)


    data_collector.collect_data()
