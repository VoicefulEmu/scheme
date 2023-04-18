from scheme import *

env = create_global_frame()
eval_all(Pair(2, nil), env)

eval_all(Pair(4, Pair(5, nil)), env)