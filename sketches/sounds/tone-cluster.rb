short_sleeps = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
long_sleeps = [5, 5, 10, 12.5]
phrase_lengths = [2, 3, 4, 5]

define :tone_loop do |name, f_scale, f_synth|
  phrase_size = phrase_lengths.choose
  note_ring = (f_scale.ring.shuffle.take(phrase_size))
  sleep = short_sleeps.shuffle.take(phrase_size-1) + [long_sleeps.choose]
  sleep_ring = sleep.ring
  # n.b this sleep is outside of a live loop, so delays other function definitions etc
  sleep sleep[-1]
  use_synth f_synth
  live_loop name do
    play note_ring.tick, amp: 0.5, attack: 0.2, sustain: 0.2, release: 0.6
    sleep sleep_ring.look
  end
end

define :ambient_loop do |name, tones, synth, tone_attack, tone_release, tone_sleep|
  live_loop name do
    use_synth synth
    play choose(tones), amp: 0.3, attack: tone_attack, release: tone_release
    sleep tone_sleep
  end
end


with_fx :reverb, mix: 0.7, room: 0.7 do
  ambient_loop 'amb1', chord(:C2, :major), :hollow, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
  tone_loop 'sin1', scale(:A3, :minor), :sine
  tone_loop 'hol2', scale(:A3, :minor), :hollow
  tone_loop 'sin2', scale(:A3, :minor), :sine
  tone_loop 'sin3', scale(:A2, :minor), :sine
  sleep long_sleeps.choose
  tone_loop 'hol4', scale(:C2, :major), :hollow
  tone_loop 'sin4', scale(:C2, :major), :sine
  ambient_loop 'amb2', chord(:A3, :minor), :sine, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
  sleep long_sleeps.choose
  tone_loop 'hol5', scale(:A3, :minor), :hollow
  tone_loop 'hol6', scale(:A2, :minor), :hollow
  ambient_loop 'amb3', chord(:A2, :minor), :sine, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
  sleep long_sleeps.choose
  ambient_loop 'amb4', chord(:C2, :minor), :sine, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
  ambient_loop 'amb5', chord(:A2, :minor), :hollow, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
  sleep long_sleeps.choose
  tone_loop 'sin5', scale(:A3, :minor), :sine
  tone_loop 'hol7', scale(:A3, :minor), :hollow
  tone_loop 'sin6', scale(:A3, :minor), :sine
  ambient_loop 'amb6', chord(:C2, :minor), :sine, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
  sleep long_sleeps.choose
  ambient_loop 'amb7', chord(:A2, :minor), :hollow, rrand_i(3, 9), rrand_i(3, 9), rrand_i(6, 12)
end