import pygame

#define main function
def main():

  #initialize pygame module
  pygame.init()
  # load and set the logo
  logo = pygame.image.load("venv/alien2.png")
  pygame.display.set_icon(logo)
  pygame.display.set_caption("minimal program")

  #create a surface on screen that has the size of 240 x 180
  screen = pygame.display.set_mode((480,360))

  # define a variable to control the main loop
  running = True

  #main loop
  while running:
    #evet handling, gets all event from the event queue
    for event in pygame.event.get():
      #only do something if the event is of type quit
      if event.type == pygame.QUIT:
        # change the value to False, to exit the main loop
        running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
  #call the main function
  main()



