from collections import defaultdict
from util import getlines

day = "9"
# day = "ex"
data = getlines(day)[0]

block_ownership = []
pos = 0

for i in range(0, len(data), 2):
    block_ownership.extend([i // 2] * int(data[i]))
    if i + 1 < len(data):
        block_ownership.extend([None] * int(data[i+1]))

left = 0
right = len(block_ownership) - 1
while left < right:
    if block_ownership[left] != None:
        left += 1
    elif block_ownership[right] == None:
        right -= 1
    else:
        block_ownership[left] = block_ownership[right]
        block_ownership[right] = None
        left += 1
        right -= 1

print(sum([i * block_ownership[i] for i in range(len(block_ownership)) if block_ownership[i] is not None]))


owned_blocks = []
gaps = defaultdict(list)

cursor = 0

for i in range(0, len(data), 2):
    data_size = int(data[i])
    owned_blocks.append((cursor, data_size))
    cursor += int(data[i])
    if i + 1 < len(data):
        gap_size = int(data[i+1])
        gaps[gap_size].append(cursor)
        cursor += gap_size

def maybe_move_block(file_id, owned_blocks, gaps):
    orig_cursor, file_size = owned_blocks[file_id]
    valid_blocks = []
    for gap_size in gaps:
        if gap_size >= file_size:
            valid_blocks.append((gaps[gap_size][0], gap_size))
    if len(valid_blocks) == 0:
        return
    cursor, gap_size = sorted(valid_blocks)[0]
    if cursor >= orig_cursor:
        return
    gaps[gap_size].pop(0)
    if len(gaps[gap_size]) == 0:
        del gaps[gap_size]
    owned_blocks[file_id] = (cursor, file_size)
    gaps[gap_size - file_size].append(cursor + file_size)
    gaps[gap_size - file_size].sort()
        
for file_id in range(len(owned_blocks) - 1, -1, -1):
    orig_cursor, file_size = owned_blocks[file_id]
    valid_blocks = []
    for gap_size in gaps:
        if gap_size >= file_size:
            valid_blocks.append((gaps[gap_size][0], gap_size))

    if len(valid_blocks) == 0:
        continue
    
    cursor, gap_size = sorted(valid_blocks)[0]
    if cursor >= orig_cursor:
        continue

    gaps[gap_size].pop(0)
    if len(gaps[gap_size]) == 0:
        del gaps[gap_size]
    owned_blocks[file_id] = (cursor, file_size)
    if gap_size != file_size:
        gaps[gap_size - file_size].append(cursor + file_size)
        gaps[gap_size - file_size].sort()

ret = 0
for i, blockdata in enumerate(owned_blocks):
    cursor, block_size = blockdata
    first = cursor
    last = cursor + block_size - 1
    ret += i * block_size * (last + first) // 2

print(ret)