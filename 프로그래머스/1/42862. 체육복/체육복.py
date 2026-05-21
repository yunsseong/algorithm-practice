def solution(n, lost, reserve):
    
    remove_list = []
    
    lost.sort()
    
    for l in lost:
        if l in reserve:
            remove_list.append(l)
    
    for i in remove_list:
        lost.remove(i)
        reserve.remove(i)
    
    cnt = n - len(lost)
    
    for l in lost:
        if l - 1 in reserve:
            cnt += 1
            reserve.remove(l - 1)
            continue
        
        if l + 1 in reserve:
            reserve.remove(l + 1)
            cnt += 1
    
    return cnt
        
        
    
    answer = 0
    return answer