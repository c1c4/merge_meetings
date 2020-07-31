def main():
    meetings = [
        {'startTime': 0, 'endTime': 1},
        {'startTime': 3, 'endTime': 5},
        {'startTime': 4, 'endTime': 8},
        {'startTime': 10, 'endTime': 12},
        {'startTime': 9, 'endTime': 10},
    ]

    sorted_meetings = sorted(meetings, key=lambda i: i['startTime'])

    new_list_merged_meetings = []
    merged_item = False

    for idx, itm in enumerate(sorted_meetings):
        if idx == len(sorted_meetings) - 1:
            break

        if merged_item:
            merged_item = False
            continue

        merged_itens = {}

        if itm['startTime'] < sorted_meetings[idx+1]['startTime']:
            merged_itens['startTime'] = itm['startTime']
        else:
            merged_itens['startTime'] = sorted_meetings[idx+1]['startTime']
            merged_item = True

        if sorted_meetings[idx+1]['startTime'] > itm['endTime']:
            merged_itens['endTime'] = itm['endTime']
        else:
            merged_itens['endTime'] = sorted_meetings[idx+1]['endTime']
            merged_item = True

        new_list_merged_meetings.append(merged_itens)

    print(new_list_merged_meetings)


if __name__ == '__main__':
    main()
