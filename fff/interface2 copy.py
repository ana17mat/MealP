
import pygame
import sys  
import random
import pandas as pd

pygame.font.init()

color1=(248,203,173)

color2=(102,124,38)

white=(255,255,255)

black=(0,0,0)
brown=(45,32,19)

veggie_db=pd.read_csv('veggie_db')

fish_db=pd.read_csv('fish_db')

meat_db=pd.read_csv('meat_db')

aldi_db=pd.read_csv('aldi_db.csv')














myfont = pygame.font.SysFont('Arial', 30)

myfont_1 = pygame.font.SysFont('Arial', 20)

screen=pygame.display.set_mode((1200,650))


botao1=pygame.image.load("Meat.png")
botao1=pygame.transform.scale(botao1, (150,45))

botao2=pygame.image.load("Fish.png")
botao2=pygame.transform.scale(botao2, (150,45))

botao3=pygame.image.load("Veggie.png")
botao3=pygame.transform.scale(botao3, (150,45))

linhah=pygame.image.load("branco.png")
linhah=pygame.transform.scale(linhah, (2000,4))

linhav=pygame.image.load("branco.png")
linhav=pygame.transform.scale(linhav, (4,2000))

down=pygame.image.load("down.png")
down=pygame.transform.scale(down, (150,150))





temp_surface = pygame.Surface((160,270))
temp_surface.fill((color1))




zx=25
zy=150

lunch_list=[]
dinner_list=[]


#######################################################################################

def choose_cats(Mo_l, Tu_l, We_l, Th_l, Fr_l, Mo_d, Tu_d, We_d, Th_d, Fr_d):

    

    pygame.display.set_caption('Plan your Meals')
    screen.fill(color1)

    disp_buttons()
    disp_weekdays()

    while Mo_l==0 or Tu_l==0 or We_l==0 or Th_l==0 or Fr_l==0 or Mo_d==0 or Tu_d==0 or We_d==0 or Th_d==0 or Fr_d==0:
        
        for event in pygame.event.get():
                
            if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
            if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    
                    #print('mouse click')
                    
                    #print([Mo_l, Tu_l, We_l, Th_l, Fr_l])
                    
                    #print([Mo_d, Tu_d, We_d, Th_d, Fr_d])

                    #LUNCH
                    
                    if 175<y<220:
                        if 25<x<175: Mo_l=1, screen.blit(temp_surface, (20,80))
                        if 200<x<350: Tu_l=1, screen.blit(temp_surface, (195,80))
                        if 375<x<525: We_l=1, screen.blit(temp_surface, (370,80))
                        if 550<x<700: Th_l=1, screen.blit(temp_surface, (545,80))
                        if 725<x<875: Fr_l=1, screen.blit(temp_surface, (720,80))
                    if 225<y<270:
                        if 25<x<175: Mo_l=2, screen.blit(temp_surface, (20,80))
                        if 200<x<350: Tu_l=2, screen.blit(temp_surface, (195,80))
                        if 375<x<525: We_l=2, screen.blit(temp_surface, (370,80))
                        if 550<x<700: Th_l=2, screen.blit(temp_surface, (545,80))
                        if 725<x<875: Fr_l=2, screen.blit(temp_surface, (720,80))
                    if 275<y<320:
                        if 25<x<175: Mo_l=3, screen.blit(temp_surface, (20,80))
                        if 200<x<350: Tu_l=3, screen.blit(temp_surface, (195,80))
                        if 375<x<525: We_l=3, screen.blit(temp_surface, (370,80))
                        if 550<x<700: Th_l=3, screen.blit(temp_surface, (545,80))
                        if 725<x<875: Fr_l=3, screen.blit(temp_surface, (720,80))
                        
                    #DINNER
                    
                    if 450<y<495:
                        if 25<x<175: Mo_d=1, screen.blit(temp_surface, (20,355))
                        if 200<x<350: Tu_d=1, screen.blit(temp_surface, (195,355))
                        if 375<x<525: We_d=1, screen.blit(temp_surface, (370,355))
                        if 550<x<700: Th_d=1, screen.blit(temp_surface, (545,355))
                        if 725<x<875: Fr_d=1, screen.blit(temp_surface, (720,355))
                    if 500<y<545:
                        if 25<x<175: Mo_d=2, screen.blit(temp_surface, (20,355))
                        if 200<x<350: Tu_d=2, screen.blit(temp_surface, (195,355))
                        if 375<x<525: We_d=2, screen.blit(temp_surface, (370,355))
                        if 550<x<700: Th_d=2, screen.blit(temp_surface, (545,355))
                        if 725<x<875: Fr_d=2, screen.blit(temp_surface, (720,355))
                    if 550<y<595:
                        if 25<x<175: Mo_d=3, screen.blit(temp_surface, (20,355))
                        if 200<x<350: Tu_d=3, screen.blit(temp_surface, (195,355))
                        if 375<x<525: We_d=3, screen.blit(temp_surface, (370,355))
                        if 550<x<700: Th_d=3, screen.blit(temp_surface, (545,355))
                        if 725<x<875: Fr_d=3, screen.blit(temp_surface, (720,355))
                        
                    pygame.display.flip()

    lunch_list=[Mo_l, Tu_l, We_l, Th_l, Fr_l]
    dinner_list=[Mo_d, Tu_d, We_d, Th_d, Fr_d]
    
    what_recipes(lunch_list, dinner_list)

    #print(lunch_list)

    #print(dinner_list)


    #return lunch_list, dinner_list # manda isto p what_recipes
## endf choose_cats


#######################################################################################

def disp_buttons():
    #print('disp_buttons')
    for i in range(5):
        px=zx+(i*175)
        for j in range(2):
            py=zy+(j*275)+25
            #b1
            screen.blit(botao1,(px,py))
            #b2
            screen.blit(botao2,(px,py+50))
            #b3
            screen.blit(botao3,(px,py+100))
    pygame.display.flip()


def disp_weekdays():
    
    wdays=['Monday','Tuesday','Wednesday','Thursday','Friday']
    
    screen.blit(linhah,(0,75))
    screen.blit(linhah,(0,350))
    screen.blit(linhav,(12.5,0))
    

    for i in range(5):
        
        screen.blit(linhav,(187.5+i*175,0))
        
        
        
        px=zx+(i*175)+20
        #DAYS 50
        
        screen.blit(myfont_1.render(wdays[i], False, black),(px,25))
        
        #LUNCH 100
        
        screen.blit(myfont_1.render('Lunch', False, black),(px,125))
        
        #DINNER 400
        screen.blit(myfont_1.render('Dinner', False, black),(px,400))

    pygame.display.flip()
    



    
    

    
#######################################################################################   


def what_recipes(lunch_list, dinner_list):
    #IN lunch list and dinner list with meat fish or veggie (1,2,3)
    #OUT(to show recipes) lunch recipes and dinner recipes, ids of recipes
    total=0
    
    
    prices3=[]
    products3=[]
    
    
    lunch_recipes=[]  #ids das receitas
    
    dinner_recipes=[]  #ids das receitas
    
    set_aldi=[]
    
    veggie_idset=set(veggie_db['id'])

    fish_idset=set(fish_db['id'])
    
    meat_idset=set(meat_db['id'])

    for e in lunch_list:
        #print(e)
        if e[0]==1:

            
         
        
            r=random.choice(list(meat_idset))
            #print(r)
            meat_idset=meat_idset-{r}
            lunch_recipes.append(r)

            index=list(meat_db['id']).index(r)
            set_aldi.append(meat_db['ings'][index])
            
        elif e[0]==2:
          
            r=random.choice(list(fish_idset))
            #print(r)
            fish_idset=fish_idset-{r}
            lunch_recipes.append(r)

            index=list(fish_db['id']).index(r)
            set_aldi.append(fish_db['ings'][index])
                
        elif e[0]==3:
            
            r=random.choice(list(veggie_idset))
            #print(r)
            veggie_idset=veggie_idset-{r}
            lunch_recipes.append(r)
            index=list(veggie_db['id']).index(r)
            set_aldi.append(veggie_db['ings'][index])

            
    for e in dinner_list:
        
        if e[0]==1:
            
            r2=random.choice(list(meat_idset))
            #print(r2)
            meat_idset=meat_idset-{r2}
            dinner_recipes.append(r2)
            index=list(meat_db['id']).index(r2)
            set_aldi.append(meat_db['ings'][index])

            
        elif e[0]==2:
            r2=random.choice(list(fish_idset))
            #print(r2)
            fish_idset=fish_idset-{r2}
            dinner_recipes.append(r2)
            index=list(fish_db['id']).index(r2)
            set_aldi.append(fish_db['ings'][index])
            
        elif e[0]==3:
            r2=random.choice(list(veggie_idset))
            #print(r2)
            veggie_idset=veggie_idset-{r2}
            dinner_recipes.append(r2)
            
            index=list(veggie_db['id']).index(r2)
            set_aldi.append(veggie_db['ings'][index])
 
        
    
    for s in set_aldi:
        
        
    
        list1=s.strip('[').strip(']').split(', ')

   

        for n in list1:
            e=int(n)


        
            if type(e)==int:
                
                products3.append(aldi_db['Ingredient'])
                prices3.append(aldi_db['Price'])

                total=total+aldi_db['Price'][e]
                
                


        






    download_db=pd.DataFrame(zip(prices3, products3), columns=['products:','price:'])
    
    print(download_db)
    
    show_recipes(lunch_recipes, dinner_recipes, total, download_db)






#######################################################################################


def show_recipes(lunch_recipes, dinner_recipes, total, download_db):
    
    #IN lunch recipes and dinner recipes, ids of recipes
    
    #OUT to get recipe -> lunch recipes, dinner recipes, string com 'L' ou 'D', dia da semana com 0,1,2,3,4
    
    screen.fill(color1)
    
    disp_weekdays()
    
    #display recipes
    
    #LUNCH
    
    py=zy+25
    
    for i in range(5):
        px=zx+(i*175)
            
        ifood=str(lunch_recipes[i])+'.png'
        food=pygame.image.load(ifood)
        food=pygame.transform.scale(food, (150,150))
        screen.blit(food,(px,py))
    
    #DINNER
    
    py=zy+300
    
    for i in range(5):
        px=zx+(i*175)
        
        ifood=str(dinner_recipes[i])+'.png'
        food=pygame.image.load(ifood)
        food=pygame.transform.scale(food, (150,150))
        screen.blit(food,(px,py))
        
        
    #DISPLAY DO PRICE 
    screen.blit(myfont.render('The total', False, black),(920,90))
    screen.blit(myfont.render('cost of your', False, black),(920,120))
    screen.blit(myfont.render('groceries is:', False, black),(920,150))
    screen.blit(myfont.render('€'+str(round(total,2)), False, black),(920,190))
    
    screen.blit(down,(950,450))

    
    
    pygame.display.flip()
    
    b=True
    while b:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                
                
                #DOWNLOAD AQUI
                
                if 950<x<1100 and 450<y<600:
                    download_db.to_csv('Shopping List.csv', index=False)
                
                
                if 175<y<325:
                    s='L'
                    
                    for i in range(5):
                        px=zx+(i*175)
                        if px<x<px+150:
                            n=i
                            get_recipe(lunch_recipes, dinner_recipes, s, n, total, download_db)
                            b=False
                    

                if 450<y<600:
                    s='D'
                    
                    for i in range(5):
                        px=zx+(i*175)
                        if px<x<px+150:
                            n=i
                            get_recipe(lunch_recipes, dinner_recipes, s, n, total, download_db)
                            b=False



#######################################################################################







    
def get_recipe(lunch_recipes, dinner_recipes, s, n, total, download_db):
    

    screen.fill(brown)
    
    if s=='L':
        r=lunch_recipes
    elif s=='D':
        r=dinner_recipes
    
    idm=r[n]
    
    #display recipe
    ifood='i.'+str(idm)+'.png'
    food=pygame.image.load(ifood)

    h=food.get_height()
    w=food.get_width()

    food=pygame.transform.scale(food, (1000, (h*1000)/w))
    screen.blit(food,(100,0))
    #fake_screen = screen.copy()
    #fake_screen.fill('black')
    #fake_screen.blit(food, (100, 100))
    #screen.blit(pygame.transform.scale(fake_screen, screen.get_rect().size), (0, 0))
    

    
    
    pygame.display.flip()
    
    b=True
    while b:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            elif event.type==pygame.KEYDOWN:    
                        if event.key == pygame.K_BACKSPACE:
                            show_recipes(lunch_recipes, dinner_recipes, total, download_db)
                            b=False
         






#######################################################################################









choose_cats(0,0,0,0,0,0,0,0,0,0)

#b=True
#while b:
 #   
  #  for event in pygame.event.get():
   #     if event.type==pygame.QUIT:
    #        pygame.quit()
     #       sys.exit()







