mid = (ring :G4, :D4, :B4, :C4, :A4, :G4)
low = (ring :G3, :D3, :B3, :C3, :A3, :G3)

define :tone_loop do |name, sleep, notes|
  live_loop name do
    use_synth :sine
    play notes.tick, release: 0.2
    sleep sleep
  end
end

with_fx :reverb, mix: 0.3, room: 0.2 do
  with_fx :echo, phase: 0.1, decay: 1 do
    tone_loop '9', 0.99, mid
    tone_loop '8', 0.88, mid
    tone_loop '7', 0.77, mid
    tone_loop '3', 0.33, low
    tone_loop '2', 0.22, low
  end
end
