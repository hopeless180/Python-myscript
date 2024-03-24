import sympy as sp

# # 定义符号变量
# V = sp.Symbol('V', positive=True, real=True)  # 正立方体的体积

# # 计算正立方体的表面积
# A = ((V**(1/3))**2) * 6

# # 打印结果
# print("正立方体的表面积：", A)
V, R, S, H, A = sp.Symbols('V R S H A', positive=True, real=True)

# elimination 正圆柱
fn_cylinder_with_SRH = S - 2 * sp.pi * R * H - 2 * sp.pi * R ** 2
fn_cylinder_with_VRH = V - sp.pi * H * R ** 2
# 假设V=1
H_expr = 2 * R
fn_cylinder_with_SR = fn_cylinder_with_SRH.subs(H, H_expr)
fn_cylinder_with_VR = fn_cylinder_with_VRH.subs(H, H_expr)
# 经测验方法1更加耗时
# start_time = time.time()
# S_expr = sp.solve([fn_cylinder_with_SR, fn_cylinder_with_VR], [S, R])
# sp.pprint(S_expr)
# print("方法1用时：", time.time()-start_time)
R_expr = sp.solve(fn_cylinder_with_VR, R)
S_expr = fn_cylinder_with_SR.subs(R, R_expr[0])
sp.pprint(S_expr)

# elimination 正方锥
fn_pyramid_with_SAH = 