\version "2.13.4"

\paper {
    page-top-space = #0.0
    %indent = 0.0
    line-width = 18.0\cm
    ragged-bottom = ##f
    ragged-last-bottom = ##f
}

% #(set-default-paper-size "a4")

#(set-global-staff-size 19)

\header {
        title = "Cello Suite Algorithmica"
        mutopiainstrument = "Cello"
        style = "Baroque"
}

melody = {

	\time 4/4
	\key g \major
	\set Staff.midiInstrument = "cello"
	g,16(d) insert_notes_here 
}


% The score definition

\score {
 	\context Staff << 
        \set Staff.instrumentName = "Cello"
	\set Staff.midiInstrument = "cello"
        { \clef bass \tempo 4=80 \time 4/4 \melody  }
    >>
	\layout { }
 	 \midi { }
}

