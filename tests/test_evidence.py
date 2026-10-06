import unittest
from urbanrag.core import answer,CORPUS
class Tests(unittest.TestCase):
    def test_abstain_unknown(self): self.assertTrue(answer('galaxia supernova')['abstained'])
    def test_citations_are_actual_sources(self):
        r=answer('rede agua cerrado'); self.assertFalse(r['abstained'])
        by_id={d['id']:d for d in CORPUS}
        for c in r['citations']:
            self.assertEqual(c['text'],by_id[c['id']]['text'])
            self.assertIn(f"[{c['id']}]",r['answer'])
