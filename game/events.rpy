label run_event:
  $event_triggered = False
  
  if room == "riroom":
    call riroom_events
  elif room == "soroom":
    call soroom_events
  elif room == "suroom":
    call suroom_events
  elif room == "roroom":
    call roroom_events
  elif room == "hall1":
    call hall1_events
  elif room == "hall2":
    call hall2_events
  elif room == "kitchen":
    call kitchen_events
  elif room == "bathroom":
    call bathroom_events
  elif room == "lib":
    call lib_events
    
  return
  
label riroom_events:
  if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    $event_triggered = True
  elif decision == "Y":
    call other_dummy_label
    $event_triggered = True
    
  return
  
label soroom_events:
  return
  
label suroom_events:  
  return
  
label hall1_events:
  return
  
label hall2_events:
  return
  
label kitchen_events:
  return
  
label bathroom_events:
  return
  
label lib_events:
  return
