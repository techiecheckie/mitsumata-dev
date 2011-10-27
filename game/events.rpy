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
  #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True
    
  return
  
label soroom_events:
  #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True  
  return
  
label suroom_events:
   #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True
  return
  
label hall1_events:
  #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True  
  return
  
label hall2_events:
  #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True    
  return
  
label kitchen_events:
    if decision == "1":
       call scene15
    
       $event_triggered = True
    #elif decision == "2":
    #    call boobs
    return
  
label bathroom_events:
  #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True    
  return
  
label lib_events:
  #if decision == "X":
    # add drama here, or mayhaps a call to some other label.
    #call dummy_label
    # And set event_triggered to True if an event occurred, so that the search
    # screen knows that it should break the loop and return to the script
    #$event_triggered = True
  #elif decision == "Y":
    #call other_dummy_label
    #$event_triggered = True    
  return
