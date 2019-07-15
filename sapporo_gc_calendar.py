"""札幌市家庭ごみ収集日カレンダーのical化.

札幌市家庭ごみ収集日カレンダーをicalにする.
元ファイルは以下を参照.
https://ckan.pf-sapporo.jp/dataset/garbage_collection_calendar
"""
from argparse import ArgumentParser
from datetime import date

import pandas
from icalendar import Calendar, Event, vDate


def main():
    """メイン関数."""
    p = ArgumentParser()
    p.add_argument('area')
    p.add_argument('input')
    args = p.parse_args()

    df = pandas.read_csv(args.input, dtype='object')

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
