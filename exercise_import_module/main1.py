# import exercise_import_module.module1
# import exercise_import_module.module2
#
# exercise_import_module.module1.greet("sean")
# exercise_import_module.module2.depart("pythonista")

# from exercise_import_module import module1, module2
# module1.greet("sean")
# module2.depart("pythonista")

# from exercise_import_module import module1 as m1, module2 as m2
# m1.greet("john  ")
# m2.depart("pythonista")

from exercise_import_module.module1 import greet
from exercise_import_module.subpackage.module3 import people

for person in people:
    greet(person)