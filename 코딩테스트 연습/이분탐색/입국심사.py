def solution(n, times):
    stt, end = 0, max( times )*n + 1
    m = 0
    spvs = [0 for _ in times]
    while stt <= end:
        mid = (stt+end) // 2
        for idx, time in enumerate( times ):
            spvs[idx] = mid // time
        m = sum( spvs )
        if   m > n:
            end = mid - 1
        elif m < n:
            stt = mid + 1
        else:
            break
    if m < n:
        future = [(spv+1)*time for spv, time in zip( spvs, times )]
        for _ in range( n - m ):
            idx = future.index( min( future ) )
            spvs[idx] += 1
            future[idx] += times[idx]
    if m > n:
        past = [(spv-1)*time for spv, time in zip( spvs, times )]
        for _ in range( m - n ):
            idx = past.index( max( past ) )
            spvs[idx] -= 1
            past[idx] -= times[idx]
    answer = 0
    for spv, time in zip( spvs, times ):
        answer = max( answer, spv*time )
    return answer
