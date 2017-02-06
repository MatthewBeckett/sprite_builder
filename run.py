import subprocess 
import pygame


rows = 1
columns = 4

singles_directory = 'singles'

def get_images():
        cmd = subprocess.Popen(["ls","-m",singles_directory], stdout=subprocess.PIPE)
        (output,err) = cmd.communicate()
        output = output.replace(' ' ,'')
        output = output.replace('\n','')
        output = output.split(",")
	return output	
	
images = []*len(get_images())
for x in get_images():
	images.append(pygame.image.load(singles_directory +'/'+x))
	
pygame.init()

r = images[0].get_rect()

view = pygame.Surface([r.width*columns,r.height*rows],pygame.SRCALPHA,32)


finish = False

x=0
for row in range(0,rows):
	for column in range(0,columns):
		if x > len(images)-1:
			break
		else:
			view.blit(images[x],pygame.Rect(column*r.width,row*r.height,r.width,r.height))		
		x +=1

#pygame.display.update()

pygame.image.save(view,"finished/spritesheet.png")

pygame.quit()

quit()
