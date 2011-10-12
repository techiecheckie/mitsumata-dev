label run_event:
  $event_triggered = False
  
  if room == "riroom":
    call riku_event(decision)
  elif room == "suroom":
    call susa_event(decision)
    
  return
  
label riku_event(decision):
  if decision == "1":
    # add drama here
    #$event_triggered = True
    pass
  elif decision == "3":
    show bg redscr with dissolve
    "This triggered while entering Riku's room on decision 3. (events.rpy)"
    hide bg redscr with dissolve
    
    $event_triggered = True
    
  return
  
label susa_event(decision):
  #if decision == "2":
  #  $event_triggered = True
  #elif decision == "4":
  #  $event_triggered = True
    
  return