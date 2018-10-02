#!/usr/bin/env python3


import math
import os


# Complete the minimumPasses function below.
def minimumPasses(m, w, p, t):
    iter = 0
    coins = 0

    def new_infra(n_items):
        new_machines = m
        new_workers = w
        delta = max(new_machines, new_workers) - min(new_machines, new_workers)
        delta = min(delta, n_items)
        rest = n_items - delta
        a,b = rest // 2, rest // 2
        if rest & 1:
            b += 1
        if new_machines < new_workers:
            new_machines += delta
        else:
            new_workers += delta
        new_machines += a
        new_workers += b
        return new_machines, new_workers

    def items_worth_buying():
        n_items = coins // p
        rest_coins = coins - n_items * p
        new_machines, new_workers = new_infra(n_items)
        rem_days_if_buying = math.ceil(float(t - rest_coins) / (new_machines * new_workers))
        rem_days_if_not_buying = math.ceil(float(t - coins) / (m * w))

        return n_items if rem_days_if_buying <= rem_days_if_not_buying else -1

    while True:
        speed = m * w
        next_improv_iter = int(math.ceil(float(p - coins) / speed))
        rem_iter_till_finish = int(math.ceil(float(t - coins) / speed))
        if next_improv_iter >= rem_iter_till_finish:
            return iter + rem_iter_till_finish
        n_items = items_worth_buying()
        if n_items == -1:
            return iter + rem_iter_till_finish
        coins_prod_till_next_improv_iter = next_improv_iter * speed
        coins += coins_prod_till_next_improv_iter
        m, w = new_infra(n_items)
        coins -= p * n_items
        iter += next_improv_iter


if __name__ == "__main__":
    mwpn = input().split()
    m = int(mwpn[0])
    w = int(mwpn[1])
    p = int(mwpn[2])
    n = int(mwpn[3])
    result = minimumPasses(m, w, p, n)
    print(result)
