class Employee:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def displayemp(self):
        print("Emp id {} Emp Name: {} Emp Sal:{}".format(self.eid, self.ename, self.sal))