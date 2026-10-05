def get_monty_consts(N, radix=2):
    #Вычисляем константы алгоритма
    #n = L_b(N) — количество бит/цифр модуля N
    L_b_from_N = N.bit_length()
    R = radix ** L_b_from_N
    #R' и N' из линейного разложения R*R' - N*N' = 1
    R_prime = pow(R, -1, N)
    N_prime = (R * R_prime - 1) // N
    #R^2 mod N, для прямого отображения phi_R^{-1}
    R_square_mod_N = (R * R) % N
    return L_b_from_N, N_prime, R_square_mod_N


def phi_R(x, y, N, L_b_from_N, N_prime, radix=2):
    z = 0
    for i in range(L_b_from_N):
        x_i = (x >> i) & 1
        u = (z + x_i * y) % radix
        v = (u * N_prime) % radix
        z = (z + x_i * y + v * N) // radix
    if z >= N:
        return z - N
    else:
        return z


def phi_R_inverse(x, R_sq_mod_N, N, L_b_from_N, N_prime):
    return phi_R(x, R_sq_mod_N, N, L_b_from_N, N_prime)


def monty_pow(x, k, N):
    x = user_input_pow_check(x, k, N)
    if k == 0:
        return 1
    L_b_from_N, N_prime, R_square_mod_N = get_monty_consts(N)
    # y это x в "пространстве" Монтгомери
    y = phi_R_inverse(x, R_square_mod_N, N, L_b_from_N, N_prime)
    accum = phi_R_inverse(1, R_square_mod_N, N, L_b_from_N, N_prime)

    binary_k = bin(k)[2:] # 0b-отбросить
    for bit in binary_k:
        accum = phi_R(accum, accum, N, L_b_from_N, N_prime)
        if bit == '1':
            accum = phi_R(accum, y, N, L_b_from_N, N_prime)
    res = phi_R(accum, 1, N, L_b_from_N, N_prime)
    return res


def monty_multiply(x, y, N):
    x, y = user_input_multiply_check(x, y, N)
    L_b_from_N, N_prime, R_square_mod_N = get_monty_consts(N)
    a = phi_R_inverse(x, R_square_mod_N, N, L_b_from_N, N_prime)
    b = phi_R_inverse(y, R_square_mod_N, N, L_b_from_N, N_prime)
    product_monty = phi_R(a, b, N, L_b_from_N, N_prime)
    res = phi_R(product_monty, 1, N, L_b_from_N, N_prime)
    return res


def user_input_pow_check(x, k, N):
    if not isinstance(N, int) or N <= 1:
        raise ValueError(f"Модуль N должен быть целым числом больше 1. Передано: {N}")
    if N % 2 == 0:
        raise ValueError(f"Модуль N должен быть НЕЧЕТНЫМ, большим 2 (так как базис b=2). Передано: {N}")
    if not isinstance(k, int) or k < 0:
        raise ValueError(f"Степень k должна быть целым неотрицательным числом. Передано: {k}")
    if not isinstance(x, int):
        raise ValueError(f"Основание x должно быть целым числом. Передано: {x}")
    return x % N


def user_input_multiply_check(x, y, N):
    if not isinstance(N, int) or N <= 1:
        raise ValueError(f"Модуль N должен быть целым числом больше 1. Передано: {N}")
    if N % 2 == 0:
        raise ValueError(f"Модуль N должен быть НЕЧЕТНЫМ, большим 2 (так как базис b=2). Передано: {N}")
    if not isinstance(x, int):
        raise ValueError(f"Основание x должно быть целым числом. Передано: {x}")
    if not isinstance(y, int):
        raise ValueError(f"Основание x должно быть целым числом. Передано: {y}")
    return x % N, y % N


# x_test = 12
# k_test = 8
# N_test = 9
# xm_test = 7
# ym_test = 19
#
# print(f"В степень Монтгомери: {monty_pow(x_test, k_test, N_test)}")
# print(f"В степень стандарт: {pow(x_test, k_test, N_test)}")
# print(f"Умножение Монтгомери: {monty_multiply(xm_test, ym_test, N_test)}")
# print(f"Умножение стандарт: {xm_test * ym_test % N_test}")