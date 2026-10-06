import argparse,json
from pathlib import Path
from .core import answer
def main():
    p=argparse.ArgumentParser(); p.add_argument('--query',default='rede de água do bairro cerrado'); a=p.parse_args()
    report={'synthetic':True,'query':a.query,**answer(a.query)}
    Path('artifacts').mkdir(exist_ok=True); Path('artifacts/report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=='__main__': main()
