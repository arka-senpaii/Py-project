#PROJECT MADE BY: Arka Mahajan
#PROJECT NAME: POKEDOX
#EMAIL: arkamahajan@gmail.com 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("1.Pokémon (an abbreviation for Pocket Monsters in Japan) is a Japanese media franchise managed by The Pokémon Company, a company founded by Nintendo, Game Freak, and Creatures.")

print("2.The franchise was created by Satoshi Tajiri in 1996, and is centered on fictional creatures called (Pokémon).")

print("3.In Pokémon, humans, known as Pokémon Trainers, catch and train Pokémon to battle other Pokémon for sport. ")

print("4.All media works within the franchise are set in the Pokémon universe. The English slogan for the franchise is (Gotta Catch ‘Em All!). There are currently 800 Pokémon species.")

df=pd.read_csv("pokemon.csv")
df=df.set_index("#")
print(" "*60)
print("	WELCOME TO POKEDOX")
print("IN THIS POKEDOX 800 POKEMON HAVE BEEN REGISTERED IN THIS POKEDOX")
print("NOW YOU CAN GIVE FOLLOWING NUMBERS TO GET DATA ABOUT POEKMON") 
print("ENTER 1 FOR GET THE TOTAL NUMBER OF POKEMON ACCORDING TO THIER TYPE") 
print("ENTER 2 FOR GETTING AN AGGREGATE OF ALL POKEMON ACCORDING TO THEIR TYPE")
print("ENTER 3 FOR FINDING A POKENMON AND GET THE STATS OF IT.")
print("ENTER 4 TO COMPARE BETWEEN TWO POKEMONS")
x=int(input()) 
if(x==1):
    print("SO THE TOTAL NUMBER OF POKEMON WAS SELECTED BY THE USER ")
    z=df.groupby("Type").agg("count")["Name"] 
    print(z)
    z.plot.bar(color="orange") 
    plt.show()
    print("THANKS FOR USING THE POKEDOX FOR USING IT AGAIN PLEASE SHUTDOWN THE WHOLE PROGRAM")

elif(x==2):
    print("SO THE USER WANTS TOO GET THE AGGREGATE OF THE STATS OF POKEOMON ACCORDING STASTICS")
    print("PLEASE STAND BY TO GET THE DATABASE")
    y=df.groupby("Type").agg("median")[["Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]]
    print(y)
    y.plot.area()
    plt.show()
    print("THANKS FOR USING THE POKEDOX FOR USING IT AGAIN PLEASE SHUTDOWN THE WHOLE PROGRAM")

elif(x==3):
    name=input("ENTER THE NAME OF YOUR POKEMON ")
    name=name.upper() 
    for i in range(1,722):
        dfx=df.iloc[i] 
        if(name==dfx["Name"]):
            print(dfx)
            dfy=dfx.drop(["Name","Type","Legendary"])
            dfy.plot.bar()
            plt.show() 
        else:
            print("BAD INPUT! NAME OF THE POKEMON IS WRONG")

    print("THANKS FOR USING THE POKEDOX FOR USING IT AGAIN PLEASE SHUTDOWN THE WHOLE PROGRAM")

elif(x==4):
    name=input("ENTER THE NAME OF YOUR POKEMON ")
    namex=input("ENTER THE NAME OF YOUR POKEMON YOU WANNA COMPARE ")
    for i in range(1,722):
        dfx=df.iloc[i] 
        if(name==dfx["Name"]):
            dfy=dfx.drop(["Type","Legendary"]) 
        if(namex==dfx["Name"]):
            dfz=dfx.drop(["Type","Legendary"])
            comp=pd.DataFrame([dfy,dfz])
            comp=comp.set_index("Name")
            print(comp)
            comp.plot.bar()
            plt.show()
        print("THANKS FOR USING THE POKEDOX FOR USING IT AGAIN PLEASE SHUTDOWN THE WHOLE PROGRAM")
else:
    print(" 	WRONG INPUT 	"*15)
