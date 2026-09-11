# Python List Indexing Cheatsheet

## The basics
- Indexing starts at **0**, not 1.
- **Negative** indexes count from the end, starting at **-1** (the last item).
- `list[-1]` doesn't mean "the third item" or any fixed slot — it means "whatever is last *right now*."

## Your example, explained
```python
friends = ["David", "Victor", "Casper"]

print(friends[-1])      # "Casper" -> last item in the list

friends.append("Omair") # adds "Omair" to the END of the list

print(friends[-1])      # "Omair" -> now the last item, since append() put it there
```

## Index map

```
Positive:    0         1         2
friends = ["David", "Victor", "Casper"]
Negative:   -3        -2        -1
```

So `friends[0]` and `friends[-3]` both point to `"David"`.

## Slicing (`list[start:end:step]`)
`end` is **exclusive** — it stops *before* that index.

| Code | Result | Meaning |
|---|---|---|
| `friends[0:2]` | `['David', 'Victor']` | index 0 up to (not incl.) 2 |
| `friends[:2]` | `['David', 'Victor']` | start defaults to 0 |
| `friends[1:]` | `['Victor', 'Casper']` | end defaults to len(list) |
| `friends[-2:]` | `['Victor', 'Casper']` | last two items |
| `friends[::-1]` | `['Casper', 'Victor', 'David']` | reversed |
| `friends[::2]` | `['David', 'Casper']` | every 2nd item |

## Common gotchas
- **`IndexError`**: accessing an index that doesn't exist (e.g. `friends[10]` on a 3-item list) crashes your program.
- **Off-by-one on slices**: `friends[0:2]` gives 2 items (indexes 0 and 1), not 3.
- **`-1` moves with the list**: after `append()`, `insert()`, or `remove()`, what `-1` points to can change.
- **Empty list**: `friends[-1]` on `[]` raises an `IndexError` — check `len(friends) > 0` first if unsure.

## Quick reference: mutating methods that affect indexes
| Method | Effect |
|---|---|
| `.append(x)` | adds `x` to the end → becomes new `[-1]` |
| `.insert(i, x)` | inserts `x` at position `i`, shifting others right |
| `.pop(i)` | removes and returns item at `i` (default: last item) |
| `.remove(x)` | removes the *first* matching value `x` |
| `.index(x)` | returns the index of the first matching value `x` |
| `len(list)` | total number of items (last valid positive index is `len(list) - 1`) |
