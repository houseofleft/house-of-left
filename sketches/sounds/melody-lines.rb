define :melody_line do |name, synth, octave|
  
  chords = [(chord :C, :minor7), (chord :Ab, :major7), (chord :Eb, :major7), (chord :Bb, "7")]
  
  chord_one = chords.choose
  chord_two = chords.choose
  chord_three = chords.choose
  chord_four = chords.choose
  
  chord_sequence = [chord_one, chord_two, chord_three, chord_four].ring
  c = chord_sequence[0]
  
  times = [2, 4, 6]
  
  first = times.choose
  second = times.choose
  third = times.choose
  fourth = times.choose
  
  first_wait = times.choose
  second_wait = times.choose
  third_wait = times.choose
  fourth_wait = times.choose
  
  live_loop name do
    use_synth synth
    use_octave octave
    play c[first], attack: 1, release: first_wait, amp: 0.3
    sleep first_wait
    play c[second], attack: 1, release: second_wait, amp: 0.3
    sleep second_wait
    play c[third], attack: 1, release: third_wait, amp: 0.3
    sleep third_wait
    play c[fourth], attack: 1, release: fourth_wait, amp: 0.3
    sleep fourth_wait
    c = chord_sequence.tick
  end
  
end

with_fx :reverb, mix: 0.7, room: 0.8 do
  melody_line 'super-bass', :hoover, -2
  melody_line 'bass', :hoover, -1
  melody_line 'mid', :hoover, 0
  melody_line 'high', :hoover, 1
  melody_line 'super-high', :hoover, 2
end