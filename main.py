#python main.py --start-date 2019-10-10 --end-date 2019-12-23 --output out.csv   (在cmd中輸入格式，日期可自己更改)
#需 install 很多東西，好像是lxml和requests


from crawler import Crawler
from args import get_args
from datetime import datetime


if __name__ == '__main__':
    args = get_args()
    crawler = Crawler()
    contents = crawler.crawl(args.start_date, args.end_date)

    # TODO: write content to file according to spec

    with open(args.output, 'w',encoding="utf-8") as f:
        for content in contents:
            output = (datetime.strftime(content[0], "%Y-%m-%d"), content[1].replace('"', ' '), content[2].replace('"', ' '))

            f.write(f'{output[0]}, "{output[1]}", "{output[2]}"\n')



