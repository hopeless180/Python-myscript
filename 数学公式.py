import sympy as sp

# # 定义符号变量
# V = sp.Symbol('V', positive=True, real=True)  # 正立方体的体积

# # 计算正立方体的表面积
# A = ((V**(1/3))**2) * 6

# # 打印结果
# print("正立方体的表面积：", A)

def elimination_VS():
    # elimination 正圆柱
    V, R, S, H = sp.symbols('V R S H', positive=True, real=True)
    fn_cylinder_with_SRH = S - 2 * sp.pi * R * H - 2 * sp.pi * (R ** 2)
    fn_cylinder_with_VRH = V - sp.pi * H * (R ** 2)
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
    S_expr = sp.solve(S_expr, S)[0]
    sp.pprint(S_expr)


def pyramid_VS():
    #  elimination 正棱锥
    V, R, S, H, A = sp.symbols('V R S H A', positive=True, real=True)
    N = sp.Symbol('N', positive=True, real=True, integer=True)
    fn_pyramid_with_SNARH = S - N * A * sp.sqrt(R ** 2 + (A ** 2) / 4) / 2 - sp.sqrt(R ** 2 + H ** 2) * A * N / 2
    fn_pyramid_with_VNARH = V - N * A * sp.sqrt(R ** 2 + (A ** 2) / 4) / 6
    S_expr = sp.solve([fn_pyramid_with_SNARH, fn_pyramid_with_VNARH], [S, R, A, H, N])[0][0]
    sp.pprint(S_expr)

def cube_VS():
    V, S, H, A = sp.symbols('V S H A', positive=True, real=True)
    fn_cube_with_SAH = S - A ** 2 - 4 * A * H
    fn_cube_with_VAH = V - (A ** 2) * H

    H_expr = A
    fn_cube_with_SA = fn_cube_with_SAH.subs(H, H_expr)
    fn_cube_with_VA = fn_cube_with_VAH.subs(H, H_expr)
    A_expr = sp.solve(fn_cube_with_VA, A)[0]
    S_expr = fn_cube_with_SA.subs(A, A_expr)
    S_expr = sp.solve(S_expr, S)[0]
    sp.pprint(S_expr)

def main():
    return 0

if __name__ == '__main__':
    cube_VS()
    pyramid_VS()
    elimination_VS()
