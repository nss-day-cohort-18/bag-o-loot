class Employee():
  def __init__(self, first_name, last_name):
    self.name = "{} {}".format(first_name, last_name)


class FullTime():
  """Describes full-time employees"""

  def __init__(self):
    self.hours_per_week = 40


class PartTime():
  """Describes part-time employees"""

  def __init__(self):
    self.hours_per_week = 24


class HumanResources(Employee, FullTime):
  """Describes human resources employees"""

  def __init__(self, first_name, last_name):
    # Note that we can't use super() any more because there is
    # more than one class being inherited from. Because of that
    # we have to call the constructor of each parent class individually
    Employee.__init__(self, first_name, last_name)
    FullTime.__init__(self)


h = HumanResources('po', 'po')
print(h.name, h.hours_per_week)