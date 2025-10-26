class Bank(object):
    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.bal = balance
        self.n = len(balance)

    def _valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account1) or not self._valid(account2):
            return False
        i = account1 - 1
        j = account2 - 1
        if self.bal[i] < money:
            return False
        self.bal[i] -= money
        self.bal[j] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account):
            return False
        self.bal[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if not self._valid(account):
            return False
        i = account - 1
        if self.bal[i] < money:
            return False
        self.bal[i] -= money
        return True

