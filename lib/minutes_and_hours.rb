def minutes_to_hours_and_minutes(minutes: )
  h = 0
  min = minutes
  while min >= 60
    h += 1
    min -= 60

  end
  if min >= 10
    "#{h}:#{min}"
  else
    "#{h}:0#{min}"
  end

end


