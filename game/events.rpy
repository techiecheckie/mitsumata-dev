init python:
  event_triggered = False

label run_event(decision, room):
  $event_triggered = False
  
  if room == "riku":
    call riku_event(decision)
  elif room == "susa":
    call susa_event(decision)
  
  return
  
label riku_event(decision):
  #if decision == "1":
    # add drama here
  #  $event_triggered = True
  #elif decision == "3":
    # moar drama here
  #  $event_triggered = True
    
  return
  
label susa_event(decision):
  #if decision == "2":
  #  $event_triggered = True
  #elif decision == "4":
  #  $event_triggered = True
    
  return