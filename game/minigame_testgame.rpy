image whack_background = "gfx/backgrounds/whack_a_mole_bg.png"

label testgame:
  # Display the minigame background
  show whack_background at Position(xpos=685, ypos=705) with dissolve

  # Run the minigame
  python:
    # Hide the mouse cursor
    config.mouse = { 'default' : [('gfx/backgrounds/textbox_bg.png',0,0)] }
    
    # Add our new displayable to the ui
    ui.add(Whack())
    # Wait for the return value (read: run the minigame as long as something
    # is returned from the event method
    return_value = ui.interact(suppress_overlay=True, suppress_underlay=True)
    
    # Debug printing
    print "Returned from the minigame, received value(s):", return_value
    
    # Reset the cursor
    config.mouse = None
    
  # Hide the minigame background
  hide whack_background with dissolve
  
  return
  
init python: 
  import pygame

  class Whack(renpy.Displayable): 
    def __init__(self):
      renpy.Displayable.__init__(self) 
      
      self.paddle = Image("gfx/test_cursor.png")
      self.x = 0
      self.y = 0

    # The purpose of this method? Beats me. Might as well follow the demo's
    # example and put everything you want drawn here.
    def visit(self):
      return [self.paddle]

    def render(self, width, height, st, at): 
      # The Render object we'll be drawing into. 
      r = renpy.Render(width, height)
      
      # We have to create the image before we can blit it using the render object
      paddle = renpy.render(self.paddle, 0, 0, st, at)
      # And then blit the image (hard-coded coordinate offsets here for testing purposes only)
      r.blit(paddle, (self.x-41, self.y-37))
      
      # Ask for a screen redraw
      renpy.redraw(self, 0)
      
      return r 

    def event(self, ev, x, y, st): 
      self.x = x
      self.y = y
      
      if ev.type == pygame.MOUSEBUTTONDOWN:
        if ev.button == 1:
          print "Clicked at", x, y
        else:
          # Maybe return the changed HP and MP values here?
          return "Some value or values..."

      # Seems like this ain't really needed, so commented it out for now          
      #raise renpy.IgnoreEvent() 