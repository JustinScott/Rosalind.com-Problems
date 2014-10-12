def signed_perm(ref, N):
    if len(ref) == N:
        return ''

    s = [i for i in range(-N, N+1)]