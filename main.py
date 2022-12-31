import sys
import json
import requests

sample_data = [
    {'member_name': 'A', 'price_to_get': 14318},
    {'member_name': 'B', 'price_to_get': 1198},
    {'member_name': 'C', 'price_to_get': -4252},
    {'member_name': 'D', 'price_to_get': -11262}
]


def get_total_balance(url):
    if url[-1] != '/':
        url += '/'

    group_id = url.split('/')[-2]
    print(f'Group ID: {group_id}')
    print('-----------------')
    api_url = f'https://manage-expence-api-prod.herokuapp.com/api/group/{group_id}/total_balance'

    try:
        response = requests.get(api_url)
    except requests.exceptions.RequestException as e:
        print('URLが正しくありません。')
        print(e)
        sys.exit(1)

    data = json.loads(response.text)
    return data


def calculation(payment, liquidation=[]):
    # 支払金額が多い順に並べる（受け取る金額多い人が先頭）
    payment = sorted(payment, key=lambda p: p['price_to_get'], reverse=True)

    # 現在の最大債務者と最大債権者を取得
    creditor = payment[0]
    debtor = payment[-1]

    # 清算金額を算出
    amount = min(creditor['price_to_get'], abs(debtor['price_to_get']))

    # 清算金額が0円の場合は終了
    if amount == 0:
        return (payment, liquidation)

    # 債権者と債務者で清算を行い、再帰呼び出しを行う
    creditor['price_to_get'] -= amount
    debtor['price_to_get'] += amount
    liquidation.append({
        'debtor': debtor['member_name'],
        'creditor': creditor['member_name'],
        'amount': amount
    })

    return calculation(payment, liquidation)


def main(url):
    # total_balanceを取得
    if url is None:
        total_balance = sample_data
    else:
        response = get_total_balance(url)
        base_currency_symbol = response['base_currency_symbol']
        total_balance = response['total_balance']

    # 清算前の貸し借り金額を表示
    print('清算前の貸し借り金額')
    for payment in total_balance:
        print(f"{payment['member_name']}: {payment['price_to_get']}")

    # 清算時の送金額を表示
    (payment, liquidation) = calculation(total_balance)

    print('-----------------')
    print('清算時の送金額')
    for l in liquidation:
        print(f"{l['debtor']} -> {l['creditor']}: {int(l['amount'])}")

    # 清算後の残債を表示
    print('-----------------')
    print('清算後の残債')
    for p in payment:
        print(f"{p['member_name']}: {int(p['price_to_get'])}")

    # 相殺金額
    print('-----------------')
    total = 0
    for p in total_balance:
        total += p['price_to_get']
    print(f'相殺金額: {int(total)}')


if __name__ == '__main__':
    # WalicaのURLを取得
    try:
        url = sys.argv[1]
    except IndexError:
        print('URLが入力されていません。')
        print('-----------------')
        url = None

    main(url)
