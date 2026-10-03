import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/userdev/Software_Intro_Task_2026-2027/install/rover_control'
