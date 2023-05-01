from utils import *
from example import example_use_of_gym_env
from planning import *
import glob

MF = 0  # Move Forward
TL = 1  # Turn Left
TR = 2  # Turn Right
PK = 3  # Pickup Key
UD = 4  # Unlock Door


def doorkey_problem(env, info):
    """
    You are required to find the optimal path in
        doorkey-5x5-normal.env
        doorkey-6x6-normal.env
        doorkey-8x8-normal.env

        doorkey-6x6-direct.env
        doorkey-8x8-direct.env

        doorkey-6x6-shortcut.env
        doorkey-8x8-shortcut.env

    Feel Free to modify this fuction
    """
    # optim_act_seq = [TL, MF, PK, TL, UD, MF, MF, MF, MF, TR, MF]
    # return optim_act_seq
    # plot_env(env)
    cost, path = getMinPath(env, info)
    control, control_text = getMotion(env, path, info)
    # print(control_text)
    return control, cost
    

def partA():
    # draw gif for all known env
    fname = glob.glob(os.path.join("envs/known_envs/", '*.env'))
    for i in range(len(fname)):
        env_path = fname[i]
        env, info = load_env(env_path)  # load an environment
        seq, cost = doorkey_problem(env, info)  # find the optimal action sequence
        fn = env_path.split("/")[-1].split(".")[0]
        print(f"Cost: {cost} for {fn}")
        
        gif_path = f"./gif/{fn}.gif"
        draw_gif_from_seq(seq, load_env(env_path)[0], gif_path)  # draw a GIF & save


def partB():
    env_folder = "./envs/random_envs"
    env, info, env_path = load_random_env(env_folder)


if __name__ == "__main__":
    # example_use_of_gym_env()
    partA()
    # partB()
