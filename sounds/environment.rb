synths = [:sine, :saw, :square]
active_scale = :indian
full_scale = scale(:G2, active_scale, num_octaves: 3)
low = scale(:G2, active_scale)
mid_l = scale(:G3, active_scale)
mid_h = scale(:G3, active_scale)
high = scale(:G4, active_scale)

define :transition do |synth, note_one, note_two, transition_length, buffer_length|
  use_synth synth
  play note_one, amp: 0.2, attack: buffer_length, sustain: buffer_length, release: transition_length
  play note_two, amp: 0.2, attack: transition_length, sustain: buffer_length, release: buffer_length
end

with_fx :reverb, room: 1, mix: 0.8 do
  with_fx :echo, mix: 0.8 do
    
    live_loop 'transitions' do
      transition choose(synths), choose(full_scale), choose(full_scale), rrand_i(60, 180), rrand_i(15, 40)
      sleep rrand_i(10, 3000000000000)
    end
    
    live_loop 'bell_sound' do
      use_synth :dull_bell
      play choose(high), attack: rrand(0.5, 1.5), release: rrand(0.2, 0.5), decay: rrand(0.5, 1), amp: 0.6
      sleep rrand(4,700000000000)
    end
    
    live_loop 'bell_sound' do
      use_synth :dull_bell
      play choose(mid_h), attack: rrand(0.5, 1.5), release: rrand(0.2, 0.5), decay: rrand(0.5, 1), amp: 0.6
      sleep rrand(4,700000)
    end
    
    live_loop 'sine_wave' do
      use_synth :sine
      play choose(mid_l), attack: rrand(3, 5), release: rrand(2, 4), sustain: rrand(1, 5), decay: rrand(0.5, 1), amp: 0.7
      sleep rrand(5,10000000000)
    end
    
    live_loop 'noise' do
      use_synth :pnoise
      play choose(low), attack: rrand(6, 7), release: rrand(4, 7), sustain: rrand(6, 9), decay: rrand(2, 3), amp: 0.3
      sleep rrand(10,2000000000000)
    end
    
  end
end