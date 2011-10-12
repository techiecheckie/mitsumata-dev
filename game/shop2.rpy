label shop:
      image bg shop = "gfx/backgrounds/shop.png"
      scene bg shop
      
      python:
        def show_shop_ui():     
          ui.frame(xpos=250, ypos= 250)
               
          ui.vbox()
          ui.text("What do you want to buy?")
          ui.textbutton("Sword",clicked=ui.returns("sword"))           
          ui.textbutton("Knife",clicked=ui.returns("knife"))
               
          ui.close()
                     
          return
     
       
        def ask_confirmation():
            ui.frame(xpos=250, ypos=250)
            
            ui.vbox()
            
            ui.text("Are you sure you want to buy this item?")
            ui.textbutton("Yes", clicked=ui.returns("yes"))
            ui.textbutton("No", clicked=ui.returns("no"))
            
            ui.close()
            
            confirmation = ""
            confirmation = ui.interact()
            
            if confirmation == "yes":
                return True
            elif confirmation == "no":
                return False
            return
            
        button = ""
                   
        while(True):
          show_shop_ui()
          
          button = ui.interact()
               
          if button == "sword":

            if ask_confirmation() == True:
                #bought, trigger event
                break
            else:
                continue
                
          elif button == "knife":
            
             if ask_confirmation () == True:
                 #bought, trigger event
                 break
             else:
                 continue
     
      return   
