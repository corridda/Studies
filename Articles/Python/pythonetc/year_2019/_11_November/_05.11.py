"""https://t.me/pythonetc/508"""

"""
If you want objects of a class to have an auto-incremented ID, you can make it happen by tracking current ID
in the class attribute:"""


class Task_1:
    _task_id = 0

    def __init__(self):
        self._id = self._task_id
        type(self)._task_id += 1


"""Mind, that you can't do self._task_id += 1. That creates the _task_id attribute within the instance,
not the class. You should consider using a factory method instead of __init__ to make it look prettier:"""


# This version is also easier to test since any custom ID can be easily provided.
class Task_2:
    _task_id = 0

    def __init__(self, task_id):
        self._id = task_id

    @classmethod
    def create(cls):
        obj = cls(cls._task_id)
        cls._task_id += 1
        return obj


if __name__ == '__main__':
    t1_1 = Task_1()
    t1_2 = Task_1()
    t1_3 = Task_1()
    print(f"Task_1.get_task_id(): {Task_1._task_id}")
    print(f"t1_1._id: {t1_1._id}")

    t2_1 = Task_2.create()
    t2_2 = Task_2.create()
    t2_3 = Task_2.create()
    print(f"Task_2.get_task_id(): {Task_2._task_id}")
    print(f"t2_1._id: {t2_1._id}")
