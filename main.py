from application.domain.model.bank import Bank
from application.domain.service.client_management_service import ClientManagementService
from application.domain.service.transaction_service import TransactionService


def main():
    bank = Bank()
    client_management_svc = ClientManagementService(bank)
    transaction_svc = TransactionService(bank)

    client_names = ["Alice Johnson", "Bob Smith", "Charlie Brown", "David Wilson", "Eva Davis", "Frank Miller",
                    "Grace Lee", "Hannah Clark", "Ian Wright", "Julia Harris"]

    banks_clients_ids = []

    print('adding clients:')
    for client_name in client_names:
        client = client_management_svc.add_client_to_the_bank(client_name)
        banks_clients_ids.append(client.client_id)
        print(client.client_id)

    money_amounts_to_withdraw = [3.14, 82.71, 18.61, 70.577, 49.66, 14.41, 62.23, 30.69, 21.73, 1.30]
    money_amounts_to_deposit = [9.81, 66.62, 12.60, 3159.14, 2828.71, 4211.41, 721.57, 1803.61, 5752.64, 315.69]
    for index, client_id in enumerate(banks_clients_ids):
        deposit_amount = money_amounts_to_deposit[index]
        withdraw_amount = money_amounts_to_withdraw[index]
        try:
            transaction_svc.deposit_money_for_a_client(client_id, deposit_amount)
            transaction_svc.withdraw_money_for_a_client(client_id, withdraw_amount)
        except ValueError as exc:
            print(f'Operation unsuccessful: {exc}')

    bank.show_balance_info_of_all_clients()

    for client_id in banks_clients_ids:
        client = bank.get_client_with_given_id(client_id)
        client.print_statement()

    client_to_remove = banks_clients_ids[::2]
    for client_id in client_to_remove:
        client_management_svc.remove_client_from_the_bank(client_id)


if __name__ == '__main__':
    main()
