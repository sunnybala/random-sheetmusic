#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import re
from pymarkovchain import MarkovChain

class Melody:
	def __init__(self,markov_dict):
		self.markov_dict = markov_dict
		self.lily_string = ""
	
	def addMeasures(self,key_m):
		while len(self.lily_string) < 800:
			self.lily_string += self.markov_dict[key_m].generateString()
		
	def outputFile(self,fileName):
		subprocess.call('cp template-abs.ly '+fileName+'.ly',shell=True)
		#subprocess.call('sed -i "s/PianoMelody/'+self.lily_string+\
		#'/g" '+fileName+'.ly', shell=True)  this is for linux
		subprocess.call('sed -i ".bak" "s/insert_notes_here/'+self.lily_string+\
                '/g" '+fileName+'.ly', shell=True) #this is for macs
		subprocess.call('lilypond '+fileName+'.ly',shell=True)
		subprocess.call('timidity '+fileName+'.midi',shell=True)


def lily_length(lily_notes):
	note_lengths = []
	#print lily_notes
	for note in lily_notes.split():
		note_lengths.append(float(re.sub("\D", "", note)))	
	return sum([1/x for x in note_lengths])

def init_markov():
	mc_Bach = MarkovChain("./mc_Bach")
	mc_Bach.generateDatabase("b a b( d b d) g,(d) b a b( d b d) g,(e) c' b c'( e c' )e g,(e) c' b c'( e c' e) g,(fis) c' b c'( fis c' fis) g,(fis) c' b c'( fis c' fis) g,(g) b a b( g b g) g,(g) b a b( g b fis) g,(e) b a b( g fis g) e( g fis g) b,( d cis b,) cis(g) a g a( g a g) cis(g) a g a( g a g) fis(a) d' cis' d'( a g a) fis( a g a) d( fis e d) e,(b,) g fis g( b, g b,) e,(b,) g fis g( b, g b,) e,(cis d e) d( cis b, a,) g(fis e) d' cis' b a g fis(e d) d' a d' fis a d e fis a g fis e d gis d( f e) f d gis d b d( f e) f d gis d c(e a b) c'( a e d) c(e a b) c'( a fis! e) dis(fis) dis fis a( fis a fis) dis(fis) dis fis a( fis a fis) g(fis e) g fis g a fis g fis e d c b, a, g, fis,( c) d c d( c d c) fis,( c) d c d( c d c) g,( b,) f e f( b, f b,) g,( b,) f e f( b, f b,) g,( c) e d e( c e c) g,( c) e d e( c e c) g,( fis) c' b c'( fis c' fis) g,( fis) c' b c'( fis c' fis) g,( d) b a b( g fis e) d c b, a, g, fis, e, d, cis,( a,) e fis g( e fis g) cis,( a,) e fis g( e fis g) c,!( a,) d e fis( d e fis) c,( a,) d e fis( d e fis) c,( a,) d a, b, c! d e fis g a fis d e fis g a b c' a fis g a b c' d' es'(d' cis' d') d'( c' b c') c' a fis e! d a, b, c d,( a, d) fis a b c' a b( g) d c b,( g, a, b,) d,( g, b, d) g( a) b g cis'( bes a bes) bes( a gis a) a( g! fis g) g( e cis b,) a,( cis e) g a cis' d' cis' d'( a fis) e fis a d fis a, d cis b, a, g, fis, e, d, c'(b a g fis e d c) b(a g fis e d c b,) a(g fis e d c b, a,) g(fis e) fis a d a e a fis a g a e a fis a d a g a e a fis a d a g a e a fis a d a e a fis a g a fis a g a e a fis a d( e) f d fis d g d gis d a d bes d b! d c' d cis' d d' d es' d e' d f' d fis'( d) g'( b) d b g'( b g' b) g'( b) d b g'( b g' b) g'( a) d a g'( a g' a) g'( a) d a g'( a g' a) fis'( c') d c' fis'( c' fis' c') fis'( c') d c' fis'( c' fis' c') ")
	
	#print mc_Bach.generateString()
	return {'Bach':mc_Bach}
			
	
def main():
	markov_dict = init_markov()
	mc_melody = Melody(markov_dict)		
	mc_melody.addMeasures('Bach')
	#print mc_melody.lily_string
	mc_melody.outputFile('Bach-test')
main()
