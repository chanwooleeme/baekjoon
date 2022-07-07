def solution(name):
    answer = 0
    visited = [False] * len(name)
    cnt = 0
    for i, c in enumerate(name):
        if c == 'A':
            visited[i] = True
        else:
            cnt += 1
    cur = 0
    for _ in range(cnt+1):
        visited[cur] = True
        answer += min(ord(name[cur]) - ord('A'), 26 - (ord(name[cur]) - ord('A')))
        next = 1
        if sum(visited) == len(name):
            break
        while len(name):
            if not visited[(cur + next) % len(name)]:
                break
            next += 1
        prev = 1
        while len(name):
            if not visited[(cur - prev) % len(name)]:
                break
            prev += 1
        if next <= prev:
            answer += next
            cur = (cur + next) % len(name)
        else:
            answer += prev
            cur = (cur - prev) % len(name)
    return answer


print(solution("AAAAABBAAAAAAABAAA"))