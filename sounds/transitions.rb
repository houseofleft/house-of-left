synths = [:sine, :saw, :square]
notes = scale(:B2, :zhi, num_octaves: 3)

define :transition do |synth, note_one, note_two, transition_length, buffer_length|
  use_synth synth
  play note_one, amp: 0.5, attack: buffer_length, sustain: buffer_length, release: transition_length
  play note_two, amp: 0.5, attack: transition_length, sustain: buffer_length, release: buffer_length
end

live_loop 'transitions' do
  transition choose(synths), choose(notes), choose(notes), rrand_i(60, 180), rrand_i(15, 40)
  sleep rrand_i(10, 30)
end
