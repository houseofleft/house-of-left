with_fx :reverb, mix: 0.9 do
  
  live_loop :tones1 do
    use_synth :hoover
    play choose(chord(:C3, :major)), attack: 6, release: 2
    sleep 8
  end
  
  live_loop :tones2 do
    use_synth :hollow
    play choose(chord(:C3, :major)), attack: 6, release: 4
    sleep 7
  end
  
  live_loop :tones3 do
    use_synth :hoover
    play choose(chord(:A3, :minor)), attack: 3, release: 5
    sleep 10
  end
  
  live_loop :tones4 do
    use_synth :pnoise
    play choose(chord(:C3, :major)), attack: 10, release: 4, amp: 0.2
    sleep 10
  end
      
end