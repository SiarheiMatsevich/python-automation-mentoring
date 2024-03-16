import abc
from typing import Optional


# Implement all methods where `NotImplementedError` is raised


class Company(object):
    """
    Represents a company
    """

    def __init__(self, name: str, address: Optional[str] = None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, employee: 'Employee') -> None:
        """
        Adds an employee to 'self.employees' list.
        Checks if the employee is an engineer or manager and not already employed
        """
        # make sure an employee is an instance of Engineer or Manager
        # make sure he is not employed already
        if isinstance(employee, (Engineer, Manager)):
            if employee.is_employed:
                raise ValueError('The employee is already employed')
            else:
                self.employees.append(employee)
                employee.company = self
        else:
            raise ValueError(f'{employee} is not an Engineer or Manager')

    def dismiss_employee(self, employee: 'Employee') -> None:
        """
        Dismisses an employee. Employee must be a company member.
        A company should notify the employee that he/she was dismissed
        """
        if employee in self.employees:
            self.employees.remove(employee)
            employee.notify_dismissed()
        else:
            raise LookupError('The employee is not employed to given company')

    def notify_im_leaving(self, employee: 'Employee') -> None:
        """
        An employee should call this method when leaving a company
        """
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            raise LookupError('The employee is not employed to given company')

    def do_tasks(self, employee: 'Engineer') -> int:
        """
        Engineer should call this method when he is working.
        Company should withdraw 10 money from a personal account and return
        them to engineer. That will be a payment
        """
        # make sure engineer is employed to this company
        if employee in self.employees:
            # check employee is Engineer
            if isinstance(employee, Engineer):
                reward = 10
                if self.__money >= reward:
                    self.__money -= reward
                    if self.is_bankrupt:
                        self.go_bankrupt()
                    return reward
                else:
                    raise ValueError(f'The {self} has not enough money to pay for the work')
            else:
                raise TypeError('Employee must be an engineer')
        else:
            raise LookupError('The employee is not employed to given company')

    def write_reports(self, employee: 'Manager') -> int:
        """
        Manager should call this method when he is working.
        A Company should withdraw 12 money from a personal account and return
        them to manager.
        That will be a payment
        """
        # make sure manager is employed to this company
        if employee in self.employees:
            # check employee is Manager
            if isinstance(employee, Manager):
                reward = 12
                if self.__money >= reward:
                    self.__money -= reward
                    if self.is_bankrupt:
                        self.go_bankrupt()
                    return reward
                else:
                    raise ValueError(f'The {self} has not enough money to pay for the work')
            else:
                raise TypeError('Employee must be a manager')
        else:
            raise LookupError('The employee is not employed to given company')

    def make_a_party(self) -> None:
        """
        Party time! All employees get 5 money
        """
        # make sure a company is not a bankrupt before and after the party
        if not self.is_bankrupt:
            # call employee.bonus_to_salary()
            for employee in self.employees:
                reward = 5
                self.__money -= reward
                employee.bonus_to_salary(company=self, reward=reward)
            if self.is_bankrupt:
                self.go_bankrupt()
        else:
            raise Exception('Party cannot be held. The company is bankrupt')

    def show_money(self) -> int:
        """
        Displays amount of money that company has
        """
        return self.__money

    def go_bankrupt(self) -> None:
        """
        Declare bankruptcy.
        Company money drops to 0.
        All employees become unemployed.
        """
        for employee in self.employees:
            employee.notify_dismissed()
        self.employees.clear()
        self.__money = 0

    @property
    def is_bankrupt(self) -> bool:
        """
        Returns True or False
        """
        return self.__money <= 0

    def __repr__(self) -> str:
        return 'Company (%s)' % self.name


class Person(object):
    """
    Represents any person
    """

    def __init__(self, name: str, age: int, sex: Optional[str] = None, address: Optional[str] = None):
        self.name = name
        self.age = age
        self.sex = sex if sex is not None else '<not specified>'
        self.address = address

    def __repr__(self) -> str:
        return '%s, %s years old' % (self.name, self.age)


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name: str, age: int, sex: Optional[str] = None, address: Optional[str] = None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company: Company) -> None:
        """
        Adds the employee to the company list if it is possible
        """
        # make sure that this person is not employed already
        if not self.is_employed:
            company.add_employee(self)
            self.company = company
        else:
            raise AttributeError(f'The employee {self} is already employed')

    def become_unemployed(self) -> None:
        """
        Leave the current company
        """
        if self.is_employed:
            self.company.notify_im_leaving(self)
            self.company = None
        else:
            raise AttributeError(f'The employee {self} is not employed to any company')

    def notify_dismissed(self) -> None:
        """
        Company should call this method when dismissing an employee
        """
        self.company = None

    def bonus_to_salary(self, company: Company, reward: int = 5) -> None:
        """
        Company should call this method on each employee when having a party
        """
        if company == self.company:
            self.put_money_into_my_wallet(reward)
        else:
            raise AttributeError(f'{self} is not an employee of {company}')

    @property
    def is_employed(self) -> bool:
        """
        Returns True or False
        """
        return self.company is not None

    def put_money_into_my_wallet(self, amount: int) -> None:
        """
        Adds the indicated amount of money to person's budget
        """
        # Engineer and Manager will have to use this method to store their
        # salary, because __money is a private attribute
        self.__money += amount

    def show_money(self) -> int:
        """
        Shows how much money person has earned
        """
        return self.__money

    @abc.abstractmethod
    def do_work(self) -> None:
        """
        This method requires re-implementation
        """
        raise NotImplemented('This method requires re-implementation')

    def __repr__(self) -> str:
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed' % self.name


class Engineer(Employee):
    def do_work(self) -> None:
        """
        Does work and puts money into wallet.
        """
        if self.is_employed:
            self.put_money_into_my_wallet(self.company.do_tasks(self))
        else:
            raise AttributeError(f'{self} cannot do work because they are not employed')


class Manager(Employee):
    def do_work(self) -> None:
        """
        Does work and puts money into wallet.
        """
        if self.is_employed:
            self.put_money_into_my_wallet(self.company.write_reports(self))
        else:
            raise AttributeError(f'{self} cannot do work because they are not employed')


def check_yourself():
    """
    Now let's operate on objects
    """

    # create the first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()

    # add the second company
    doors_company = Company('Windows and doors', address='Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_work()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_work()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()


if __name__ == '__main__':
    check_yourself()
