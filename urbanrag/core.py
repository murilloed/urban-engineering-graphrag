import re,unicodedata
from collections import Counter
import numpy as np

CORPUS=[
  {'id':'D1','asset':'rede-agua','text':'A rede de água do bairro Cerrado conecta o reservatório à escola.','source':'synthetic://water-network'},
  {'id':'D2','asset':'escola','text':'A escola do bairro Cerrado possui 120 alunos e demanda abastecimento de água.','source':'synthetic://school'},
  {'id':'D3','asset':'reservatorio','text':'O reservatório alimenta a rede de água e requer inspeção periódica.','source':'synthetic://reservoir'},
  {'id':'D4','asset':'rede-esgoto','text':'A rede de esgoto atende a praça do bairro Aurora.','source':'synthetic://sewer-network'}]
GRAPH={'rede-agua':['reservatorio','escola'],'reservatorio':['rede-agua'],'escola':['rede-agua'],'rede-esgoto':['praca']}
STOP={'a','o','as','os','de','do','da','e','no','na','em','ao','uma','um','para','com','à'}
def tokens(text):
    s=''.join(c for c in unicodedata.normalize('NFD',text.lower()) if unicodedata.category(c)!='Mn')
    return [t for t in re.findall(r'[a-z0-9]+',s) if t not in STOP]

class Index:
    def __init__(self,docs):
        self.docs=docs; bags=[Counter(tokens(d['text'])) for d in docs]
        self.vocab=sorted({t for b in bags for t in b})
        self.idf=np.array([np.log((1+len(docs))/(1+sum(t in b for b in bags)))+1 for t in self.vocab])
        self.vectors=np.stack([self.encode(d['text']) for d in docs])
    def encode(self,text):
        bag=Counter(tokens(text)); v=np.array([bag[t] for t in self.vocab])*self.idf
        return v/max(1e-12,np.linalg.norm(v))
    def retrieve(self,query,k=2,threshold=.15):
        scores=self.vectors@self.encode(query)
        return [(self.docs[i],float(scores[i])) for i in np.argsort(-scores)[:k] if scores[i]>=threshold]

def answer(query,docs=CORPUS,graph=GRAPH):
    hits=Index(docs).retrieve(query)
    if not hits: return {'answer':'Sem evidência suficiente no corpus.','citations':[],'abstained':True}
    assets={d['asset'] for d,_ in hits}; related={n for a in assets for n in graph.get(a,[])}
    evidence=[{'id':d['id'],'source':d['source'],'text':d['text'],'score':s,'kind':'vector'} for d,s in hits]
    used={e['id'] for e in evidence}
    evidence += [{'id':d['id'],'source':d['source'],'text':d['text'],'score':None,'kind':'graph'}
                 for d in docs if d['asset'] in related and d['id'] not in used]
    return {'answer':' '.join(f"{e['text']} [{e['id']}]" for e in evidence),
            'citations':evidence,'abstained':False,'method':'extractive TF-IDF + one-hop graph'}
