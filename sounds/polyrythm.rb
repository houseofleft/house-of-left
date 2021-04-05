define :kick_loop do |name, kick_sleep|
  live_loop name do
    sample :bd_haus, rate: rrand(0.3,0.5)
    sleep kick_sleep * 0.1
  end
end

with_fx :bitcrusher, mix: 0.6 do
  with_fx :reverb, mix: 0.5, room: 0.8 do
    with_fx :distortion, distort: 0.3 do
      kick_loop 'kick_1', rrand_i(1, 10)
      kick_loop 'kick_2', rrand_i(1, 10)
      kick_loop 'kick_3', rrand_i(1, 10)
      kick_loop 'kick_4', rrand_i(1, 10)
      kick_loop 'kick_5', rrand_i(1, 10)
      kick_loop 'kick_6', rrand_i(1, 10)
      kick_loop 'kick_7', rrand_i(1, 10)
      kick_loop 'kick_8', rrand_i(1, 10)
    end
  end
end
