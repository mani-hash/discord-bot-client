import os
import sys
from time import sleep

try:
    import discord
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("You haven't installed the necessary modules")
    print("Please install them before running the script...", end="\n\n")
    print("Modules required (all):")
    print("    1. discord")
    print("    2. dotenv", end="\n\n")
    print("Try the following command in the terminal/cmd (in current directory): ")
    print("      pip install -r requirements.txt ")
    print("              or ")
    print("      pip3 install -r requirements.txt ", end="\n\n")
    print("Closing the program...")
    sleep(2)
    exit()

current_path = os.path.abspath(__file__)
current_head = os.path.split(current_path)
main_path = current_head[0]

env_path = os.path.join(main_path, ".env")

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def in_idle():
    try:
        return sys.stdin.__module__.startswith('idlelib')
    except AttributeError:
        return False

idle_nfo = in_idle()

clear()

if (idle_nfo == True):
    print(" >>>>>> ALERT <<<<<<< ", end="\n\n")
    print("Seems like you ARE running the script in IDLE")
    print("NOTE: The program won't work as expected when run via IDLE", end="\n\n")
    print("Features missing: ")
    print("    1. Coloured interface")
    print("    2. Clear terminal (when switching between menus)")
    print("    3. Loading effects", end="\n\n")
    
else:
    print(" >>>>>> ALERT <<<<<<< ", end="\n\n")
    print("Seems like you are NOT running the script in IDLE")
    print("NOTE: The program won't work as expected when run via IDLE", end="\n\n")
    print("Features missing (if you are running script in a terminal): ")
    print("    1. Coloured interface", end="\n\n")
    print("Other features that might not work:")
    print("    1. Clear terminal (when switching between menus)")
    print("    2. Loading effects", end="\n\n")
    
print("If possible, please try running the script (present in shell folder) on a terminal", end="\n\n")
    
sleep(4)

try:
    delay_user = input("Press enter to continue...")
except:
    exit()



    


client = discord.Client()



def get_envInfo():
    key = ["", ""]
    value = ["", ""]
    s = 0
    fr = open(env_path, "r")
    for line in fr.readlines():
        key[s], value[s] = line.split("=")
        key[s] = key[s].strip()
        value[s] = value[s].strip()
        s += 1
    fr.close()
    return key, value


def create_token(chan_id, token):
    key, value = get_envInfo()
        
    if (chan_id == "" and token == ""):
        print("Default bot token and channel ID are not set")
        print("Please set them here ", end="\n\n")
        try:
            token = input("Enter bot token >> ").strip()
        except KeyboardInterrupt:
            exit()
        p = 20
        while (p < 100):
            try:
                chan_id = int(input("Enter Main channel id >> "))
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print("Only Integer values", end="\n\n")
            else:
                f = open(env_path, "w")
                f.write("DISCORD_TOKEN="+token+"\n")
                f.write("CHANNEL_ID="+str(chan_id)+"\n")
                f.close()
                return token, chan_id
                break
    elif (chan_id == ""):
        print("Default channel ID is not set")
        print("Please enter a valid channel ID here", end="\n\n")
        p = 20
        while (p < 100):
            try:
                chan_id = int(input("Enter prefered default channel id >> "))
                
            except KeyboardInterrupt:
                exit()
            except ValueError:
                print("Only Integer values", end="\n\n")
            else:
                f = open(env_path, "w")
                f.write("DISCORD_TOKEN="+value[0]+"\n")
                f.write("CHANNEL_ID="+str(chan_id)+"\n")
                f.close()
                return value[0], chan_id
                break
    elif (token == ""):
        print("Default bot token is not set")
        print("Please enter a valid bot token here", end="\n\n")
        try:
            token = input("Enter Bot token>> ")
        except KeyboardInterrupt:
            exit()
        else:
            f = open(env_path, "w")
            f.write("DISCORD_TOKEN="+token+"\n")
            f.write("CHANNEL_ID="+value[1]+"\n")
            f.close()
            return token, value[1]

def delete_token():
    key, value = get_envInfo()
    f = open(env_path, "w")
    f.write("DISCORD_TOKEN=\n")
    f.write("CHANNEL_ID="+value[1]+"\n")
    f.close()

def delete_channel():
    key, value = get_envInfo()
    f = open(env_path, "w")
    f.write("DISCORD_TOKEN="+value[0]+"\n")
    f.write("CHANNEL_ID=\n")
    f.close()

def chat_menu_help():
    print(" ", end="\n")
    print(" Type /help for commands")
    print("Some basic commands:")
    print("       1. /prev  - Go back to previous menu")
    print("       2. /clean - Clear the window/terminal/console")
    print("       3. /quit  - exit the program")
    print("       4. /help  - print this help message", end="\n\n")

clear()

print(" ", end="\n")
print("A Simple                                   ")
print("  _______      _______    ____________     ")
print(" |   __  |    |  ___  |  |____    ____|    ")
print(" |  |__| |_   | |   | |       |  |         ")
print(" |   __    |  | |   | |       |  |         ")
print(" |  |__|   |  | |___| |       |  |         ")
print(" |_________|  |_______|       |__|         ")
print("                                    Client ")
print("                           -By Mani        ", end="\n\n")


exitMsg = "Press Ctrl + C to exit..."

k1 = 1
while (k1 < 2):
    if (os.path.isfile(env_path)):
        load_dotenv()
        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN").strip()
        CHANNEL_ID = os.getenv("CHANNEL_ID").strip()
        k1 += 2
    else:
        f = open(env_path, "w")
        f.write("DISCORD_TOKEN=\n")
        f.write("CHANNEL_ID=\n")
        f.close()



if (CHANNEL_ID == "" or DISCORD_TOKEN == ""):
    DISCORD_TOKEN, CHANNEL_ID = create_token(CHANNEL_ID, DISCORD_TOKEN)
    
    print(" ", end="\n")
    print("The bot token and channel ID have been successfully set")
else:
    print("Default bot token and channel ID are already set")

CHANNEL_ID = int(CHANNEL_ID)

    
print("To add new default bot token and channel Id,")
print("you can delete the .env file and run program again", end="\n\n")
print("[NOTE: Refrain from editing the .env file]", end="\n\n")
print("[UPDATE: Changing default channel ID and bot token are still under developement]", end="\n\n")
print("New features will be added in the future!", end="\n\n")




@client.event
async def on_ready():
    global DISCORD_TOKEN
    global CHANNEL_ID
    print('We have logged in as {0.user}'.format(client), end="\n\n")
    i = 15
    n = 20
    while (n < 100):
        print("-"*100)
        print(" >>>>>>>Welcome to discord bot client main menu<<<<<<<", end="\n\n")
        print("Choose your option (Type the number only)", end="\n\n")
        print("Options: ")
        print("   1. Chat in the default channel")
        print("   2. Chat in a different channel (Channel ID is required)")
        print("   3. Exit the program", end="\n\n")
        print("Enter either 1 / 2 / 3 only!!", end="\n\n")

        try:
            en_option = int(input("Choose option >> "))
        except ValueError:
            print(" ", end="\n")
            print("An error occured, please try again", end="\n\n")
        else:
            if (en_option == 1):
                clear()
                print("<<<<< Chat Box >>>>>>>>", end="\n\n")
                chat_menu_help()
                while (i < 100):
                    x = input("Enter message >> ")
                    if (x == "/prev"):
                        clear()
                        break
                    elif (x == ""):
                        pass
                    elif (x == "/clean"):
                        clear()
                    elif (x == "/help"):
                        chat_menu_help()
                    elif (x == "/quit"):
                        clear()
                        print(exitMsg, end="\n\n")
                        return
                    else:
                        try:
                            await client.get_channel(CHANNEL_ID).send(x)
                            print(" ", end="\n")
                            print ("Message has been sent!!", end="\n\n")
                        except discord.errors.HTTPException:
                            print(" ", end="\n")
                            print("You cannot send empty messages!", end="\n\n")
                        except AttributeError:
                            print(" ", end="\n")
                            print("An Error has occured!", end="\n\n")
                            print("Possible Issues: ", end="\n\n")
                            print("1. Channel ID is Invalid")
                            print("2. Access restriction issues (Mainly for unix-like systems; eg:linux/Mac)" )
                            print("3. The .env file got tampered by someone")
                            print("3. Error in code[No quick fixes available]", end="\n\n")
                            print("Identifying and fixing issues....", end="\n\n")
                            dots="."
                            for n2 in range(1, 7):
                                print('\r', "Taking actions"+dots, end=" ", flush=True)
                                dots+="."
                                sleep(1)
                            delete_channel()
                            print(" ", end="\n\n")
                            print("Channel ID has been deleted")
                            print("Re-run the program and enter a valid bot token", end="\n\n")
                            print("Other possible fixes(Attempt only if the above fix didn't work):", end="\n\n")
                            print("a. Make sure necessary permissions are granted to work in the current directory")
                            print("b. Try deleting the .env file and running the program again")
                            print("c. In case of tampering with the code itself, delete and redownload the files", end="\n\n")
                            print(exitMsg, end="\n\n")
                            return
            elif (en_option == 2):
                clear()
                print(" Switch to a different channel here (temporary)", end="\n\n")
                chat_menu_help()
                while (i < 200):
                    try:
                        drop_warn = False
                        temp_channel = input("Enter channel ID >> ").strip()
                        if (temp_channel == "/prev"):
                            print("Going back to previous menu")
                            break
                        elif (temp_channel == "/clean"):
                            drop_warn = True
                            clear()
                        elif (temp_channel == "/help"):
                            chat_menu_help()
                            continue
                        elif (temp_channel == "/quit"):
                            clear()
                            print(exitMsg, end="\n\n")
                            return
                        else:
                            temp_channel = int(temp_channel)
                    except ValueError:
                        print(" ", end="\n")
                        print("Only Integer type values", end="\n\n")
                    except:
                        print(" ", end="\n")
                        print("An unexpected error occured", end="\n\n")
                    else:
                        try:
                            if (drop_warn == True):
                                drop_warn = False
                                raise ValueError
                            else:
                                #try:
                                await client.get_channel(temp_channel).send(".")
                                #except ClientConnectorError:
                                    #print("Unable to connect, check your internet connection..")
                        except ValueError:
                            print(" Switch to a different channel here (temporary)", end="\n\n")
                        except:
                            print(" ", end="\n")
                            print("Cannot send message to this channel", end="\n\n")
                        else:
                            clear()
                            print("<<<<< Chat Box >>>>>>>>", end="\n\n")
                            chat_menu_help()
                            while (i < 100):
                                x = input("Enter message >> ")
                                if (x == "/prev"):
                                    clear()
                                    break
                                elif (x == ""):
                                    pass
                                elif (x == "/clean"):
                                    clear()
                                elif (x == "/help"):
                                    chat_menu_help()
                                elif (x == "/quit"):
                                    clear()
                                    print(exitMsg, end="\n\n")
                                    return
                                else:
                                    try:
                                        await client.get_channel(temp_channel).send(x)
                                    except discord.errors.HTTPException:
                                        print(" ", end="\n")
                                        print("You cannot send empty messages!", end="\n\n")
                                    else:
                                        print(" ", end="\n")
                                        print ("Message has been sent!!", end="\n\n")
            elif (en_option == 3):
                clear()
                print(exitMsg, end="\n\n")
                break

            else:
                print("You have entered an invalid option. ")


try:
    client.run(DISCORD_TOKEN)
except discord.errors.LoginFailure:
    #login failure message
    print(" ", end="\n")
    print("An Error has occured!", end="\n\n")
    print("Possible Issues: ", end="\n\n")
    print("1. Bot token is Invalid")
    print("2. Access restriction issues (Mainly for unix-like systems; eg:linux/Mac)" )
    print("3. The .env file got tampered by someone")
    print("3. Error in code[No quick fixes available]", end="\n\n")
    print("Identifying and fixing issues....", end="\n\n")
    dots="."
    for n1 in range(1, 7):
        print('\r', "Taking actions"+dots, end=" ", flush=True)
        dots+="."
        sleep(1)
    delete_token()
    print(" ", end="\n\n")
    print("Bot token has been deleted")
    print("Re-run the program and enter a valid bot token", end="\n\n")
    print("Other possible fixes(Attempt only if the above fix didn't work):", end="\n\n")
    print("a. Make sure necessary permissions are granted to work in the current directory")
    print("b. Try deleting the .env file and running the program again")
    print("c. In case of tampering with the code itself, delete and redownload the files", end="\n\n")
    
except:
    #any other issue message(mostly network connection based issues)
    print(" ")
    print("An Error has occured!", end="\n\n")
    print("Possible Issues: ", end="\n\n")
    print("1. No/slow network connection")
    print("2. Required packages are not installed")
    print("3. Problems related to outdated software")
    print("4. The .env file got tampered by someone")
    print("5. Error in code[No quick fixes available]", end="\n\n")
    print("Fixes available: ", end="\n\n")
    print("a. Reconnect to the network/Try connecting to a different network")
    print("b. Make sure all the required packages are installed")
    print("c. Make sure you aren't using an old version of python")
    print("d. Try deleting the .env file and running the program again")
    print("e. In case of tampering with the code itself, delete and redownload the files", end="\n\n")
    
    
