from environs import Env

env = Env()
env.read_env()  

#TIKR VARIABLES
TIKR_MAIL = env("TIKR_MAIL")
TIKR_PASSWORD = env("TIKR_PASSWORD")