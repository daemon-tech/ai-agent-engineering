#!/usr/bin/env python3
"""Check that every [@key] in manuscript/ is directly followed by ' **[TAG]**', where TAG is the key's
class in references-verification.md. Run from the repo root. --fix inserts missing tags (never changes one)."""
import re, glob, sys
CITE = re.compile(r'\[@(\w+)\]( \*\*\[(\w+)\]\*\*)?')

def classes():
    return {m[1]: m[2] for m in re.finditer(r'\| \d+ \| `([^`]+)` \| (\w+) \|', open('references-verification.md').read())}

def problems(path, text, ver):
    """Yield (location, key, found_tag, expected_class) for each bad citation."""
    for m in CITE.finditer(text):
        k, tag = m[1], m[3]
        if ver.get(k) != tag:
            yield f'{path}:{text.count(chr(10), 0, m.start()) + 1}', k, tag, ver.get(k)

def main(fix=False):
    ver, bad = classes(), []
    for f in sorted(glob.glob('manuscript/*.md')):
        t = open(f).read()
        if fix:
            t2 = CITE.sub(lambda m: m[0] if m[2] or m[1] not in ver else f'{m[0]} **[{ver[m[1]]}]**', t)
            if t2 != t: open(f, 'w').write(t2); t = t2
        bad += problems(f, t, ver)
    for b in bad: print('%s: [@%s] tag=%s expected=%s' % b)
    print(f'{len(bad)} citation problems'); return 1 if bad else 0

if __name__ == '__main__': sys.exit(main('--fix' in sys.argv))
