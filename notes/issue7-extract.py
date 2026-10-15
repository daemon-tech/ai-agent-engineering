# Baseline #7 claim extraction. Run from repo root: python3 notes/issue7-extract.py (outputs JSON into notes/, not committed).
import re,glob,random,csv,json
TAG=r'\*\*\[(PR|PP|VC|EE|OP)\]\*\*|\[(PR|PP|VC|EE|OP)\]'
rows=[]
for f in sorted(glob.glob('manuscript/*.md')+['notes/2026-10-frontier-review.md']):
    for i,line in enumerate(open(f),1):
        if line.strip().startswith(('|','#','```')) and '[@' not in line: continue
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*(])',line.strip()):
            cites=re.findall(r'@([\w\-]+)',s) if '[@' in s else []
            tags=re.findall(TAG,s)
            tags=[a or b for a,b in tags]
            if cites or tags:
                rows.append(dict(file=f,line=i,cites=';'.join(cites),tags=';'.join(tags),text=s[:400]))
json.dump(rows,open('notes/issue7-claims.json','w'),indent=0)
print(len(rows), sum(1 for r in rows if r['cites'] and not r['tags']), sum(1 for r in rows if r['tags'] and not r['cites']))
SEED=20261015; random.seed(SEED)
smp=random.sample([r for r in rows if r['cites']],40)
json.dump(smp,open('notes/issue7-sample.json','w'),indent=1)
