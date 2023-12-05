import os
import inspect
import queue

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = f.read().splitlines()


def get_seeds():
    return [int(seed) for seed in lines[0].split(":")[-1].split()]


maps = []
current_map = []

for line in lines[1:]:
    if not line:
        maps.append(current_map)
        current_map = []
    elif line[0].isdigit():
        current_map.append([int(m) for m in line.split()])

# don't forget the last map :)
maps.append(current_map)

# part 1

seeds = get_seeds()
res = 2**32

for seed in seeds:
    for mapping in maps:
        for dest, src, rnge in mapping:
            if seed >= src and seed <= src + rnge:
                seed = dest + abs(seed - src)
                break

    res = min(res, seed)

print(res)

# part 2

seeds = get_seeds()
seeds = list(
    zip(seeds[::2], [src + rnge for src, rnge in zip(seeds[::2], seeds[1::2])])
)

for idx, mapping in enumerate(maps):
    s_new = set()
    q = queue.Queue()

    for seed in seeds:
        q.put(seed)

    while not q.empty():
        seed = q.get()
        s_start, s_end = seed

        # check every map for this seed
        for dest, src, rnge in mapping:
            m_start = src
            m_end = src + rnge

            # if seeds don't overlap, we don't care
            if not max(m_start, s_start) <= min(m_end, s_end):
                continue

            # put remaining seeds in seed list
            if s_start < m_start:
                q.put((s_start, m_start - 1))
                s_start = m_start

            if s_end > m_end:
                q.put((m_end + 1, s_end))
                s_end = m_end

            start_new = dest + abs(s_start - m_start)
            end_new = dest + abs(s_end - m_start)

            s_new.add((start_new, end_new))

            break
        else:
            # we didn't find a map for this seed, so add it to the list
            s_new.add(seed)

    seeds = list(s_new)

print(min(seeds, key=lambda x: x[0])[0])
