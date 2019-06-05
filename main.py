import supervised_learning.supervised_learning as sl
import os

def main():
    #storage = r"./storage/"
    workspace_dir = get_workspace()
    my_sl = sl.Supervised_learning(workspace_dir)
    my_sl.run()

def get_workspace():
    workspace_dir = os.getcwd()
    return workspace_dir
main()
