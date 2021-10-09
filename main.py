class Task:

    def __init__(self, title, tag=None):
        self.done = False
        self.title = title
        self._priority = 1
        self.tag = tag

    def __str__(self):
        return f'{self.title.capitalize()}'

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        if priority in range(1, 11):
            self._priority = priority
        else:
            return 'Value out of range'


class Dashboard:
    def __init__(self):
        self.task_list = []

    def add_task(self):
        title = input('Task name:\t')
        new_task = Task(title)
        self.task_list.append(new_task)

    def print_all_tasks(self):
        for task in self.task_list:
            print(task)

    def print_tasks_by_priority(self):
        task_priority = []
        inp_priority = int(input('Enter priority:\t'))

        for task in self.task_list:
            print(task)
            print(task.priority)
            if task.priority == inp_priority:
                task_priority.append(task)

        return task_priority

    #title
    def title_search(self, title):
        title_list = []
        for task in self.task_list:
            if task.title == title:
                title_list.append(task)
        return title_list

    #tag
    def tag_search(self, tag):
        tag_list = []
        for task in self.task_list:
            if task.tag == tag:
                tag_list.append(task)
        return tag_list

    #по заданому tag
    def completed_task(self, tag):
        t_list = Dashboard.tag_search(self, tag)

        completed_list = []
        for task in t_list:
            if task.done == True:
                completed_list.append(task)
        return completed_list







if __name__ == '__main__':
    task = Task('My test task')
    task.done = True
    task1 = Task('My test task1', '#task1')
    task1.done = True
    task2 = Task('My test task2', '#task1')
    task3 = Task('My test task3', '#task3')
    task3.done = True
    task4 = Task('My test task4', '#task2')
    dashboard = Dashboard()
    dashboard.task_list.extend([task, task1, task2, task3, task4])
    for task in dashboard.completed_task('#task1'):
        print(task)
