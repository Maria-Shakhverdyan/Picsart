from account import CheckingAccount, SavingsAccount, JointAccount
from customer import Customer
from transfer import Transaction

def main():
    # Example Usage
    cust1 = Customer(name="Maria", contact_info="maria@example.com")
    check_acc = CheckingAccount(account_number=123456, balance=1000.0, overdraft_limit=500.0)
    sav_acc = SavingsAccount(account_number=654321, balance=1500.0, interest_rate=0.03)
    joint_acc = JointAccount(account_number=789012, balance=2000.0, joint_owners=["Maria", "Ann"])

    cust1.add_account(check_acc)
    cust1.add_account(sav_acc)
    cust1.add_account(joint_acc)

    cust1.view_accounts()

    check_acc.deposit(500.0)
    check_acc.show_balance()

    check_acc.withdraw(200.0)
    check_acc.show_balance()

    check_acc.transfer(sav_acc, 100.0)
    check_acc.show_balance()
    sav_acc.show_balance()

    transaction = Transaction(from_account=check_acc, to_account=sav_acc, amount=100.0, transaction_type="Transfer")
    transaction.log()

if __name__ == "__main__":
    main()
