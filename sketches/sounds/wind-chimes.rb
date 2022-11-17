with_fx :reverb, room: 1, mix: 0.8 do
  with_fx :echo, mix: 0.8 do
    
    in_thread do
      loop do
        use_synth :dull_bell
        play choose([:C5, :A5, :E5, :G5, :C4, :A4, :E4, :G4]), attack: rrand(0.5, 1.5), release: rrand(0.2, 0.5), decay: rrand(0.5, 1), amp: 0.6
        sleep rrand(4,7)
      end
    end
    
    in_thread do
      loop do
        use_synth :sine
        play choose([:C4, :A4, :E4, :G4, :C3, :A3, :E3, :G3]), attack: rrand(3, 5), release: rrand(2, 4), sustain: rrand(1, 5), decay: rrand(0.5, 1), amp: 0.7
        sleep rrand(5,10)
      end
    end
    
    in_thread do
      loop do
        use_synth :pnoise
        play choose([:C2, :A2, :E2, :G2, :C1, :A1, :E1, :G1]), attack: rrand(6, 7), release: rrand(4, 7), sustain: rrand(6, 9), decay: rrand(2, 3), amp: 0.3
        sleep rrand(10,20)
      end
    end
    
  end
end