"""札幌市家庭ごみ収集日カレンダーのical化.

札幌市家庭ごみ収集日カレンダーをicalにする.
元ファイルは以下を参照.
https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar
"""
from argparse import ArgumentParser, FileType
from datetime import date

import pandas
from icalendar import Calendar, Event, vDate


def main():
    """メイン関数."""
    p = ArgumentParser(description='札幌市家庭ゴミ収集日カレンダーCSVをical化する')
    p.add_argument('-a', '--area', help='地域名')
    p.add_argument(
        'input',
        type=FileType(encoding='utf-8'), help='札幌市家庭ゴミ収集日カレンダーCSV')
    args = p.parse_args()

    df = pandas.read_csv(args.input, dtype='object')

    if args.area is None:
        print('入力可能な地域名:')
        for area in df.columns[2:]:
            print(' ' + area)

        return

    gctypes = {
        '1': '燃やせるゴミ',
        '2': '燃やせないゴミ',
        '8': 'びん・缶・ペット',
        '9': '容器プラ',
        '10': '雑がみ',
        '11': '枝・葉・草'
    }

    ical = Calendar()

    for datestr, gctype in zip(df['日付'], df[args.area]):
        if gctype in gctypes:
            dt = date.fromisoformat(datestr)
            event = Event()
            event.add('SUMMARY', gctypes[gctype])
            event.add('DTSTART', vDate(dt))
            event.add('DTEND', vDate(dt))
            event.add('TRANSP', 'TRANSPARENT')
            ical.add_component(event)

    print(ical.to_ical().decode('utf-8'))


if __name__ == '__main__':
    main()
